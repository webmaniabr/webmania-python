"""One-attempt synchronous HTTP transport with process-owned DNS and sockets."""
from __future__ import annotations
import ipaddress
import math
import os
import pickle
import selectors
import ssl
import struct
import subprocess
import sys
import threading
import time
from pathlib import Path
from urllib.parse import unquote, urlsplit
from .errors import WebmaniaError
from .types import CallOptions


def positive(value, integer=False):
    if isinstance(value, bool): return False
    if isinstance(value, int): return value > 0
    return not integer and isinstance(value, float) and value > 0 and math.isfinite(value)


def checked_url(url, origin_only=False):
    invalid = False
    parts = None
    try:
        if not isinstance(url, str) or any(ord(c) < 33 or ord(c) == 127 for c in url) or '\\' in url:
            invalid = True
        else:
            parts = urlsplit(url)
            if parts.username is not None or parts.password is not None or parts.fragment or parts.query or not parts.hostname: invalid = True
            if parts.scheme not in ['http', 'https'] or (origin_only and parts.path not in ['', '/']): invalid = True
            if any(segment in ['.', '..'] for segment in unquote(parts.path).split('/')): invalid = True
            if parts.scheme == 'http':
                try: loopback = ipaddress.ip_address(parts.hostname).is_loopback
                except ValueError: loopback = parts.hostname == 'localhost'
                if not loopback: invalid = True
            _ = parts.port
            url.encode('utf-8')
    except (ValueError, TypeError, UnicodeError): invalid = True
    if invalid or parts is None:
        raise WebmaniaError('configuration', 'Expected an HTTPS origin/base URL or HTTP loopback test URL.')
    return parts


class Transport:
    def __init__(self, base_url, *, timeout=30.0, max_response_bytes=2 * 1024 * 1024,
                 max_request_bytes=8 * 1024 * 1024, ca_file=None):
        self.base = checked_url(base_url)
        if not positive(timeout) or timeout > sys.float_info.max or not positive(max_response_bytes, True) or not positive(max_request_bytes, True) or max_request_bytes > 8 * 1024 * 1024:
            raise WebmaniaError('configuration', 'Timeout and byte limits must be finite positive bounded values.')
        self.timeout = float(timeout)
        self.max_response_bytes = max_response_bytes
        self.max_request_bytes = max_request_bytes
        failed = False
        try: ssl.create_default_context(cafile=ca_file)
        except (OSError, ssl.SSLError, TypeError): failed = True
        if failed: raise WebmaniaError('configuration', 'Unable to initialize the verified TLS context.')
        self.ca_file = ca_file
        self.lock = threading.Lock()
        self.closed = False
        self.worker = None
        self.buffer = bytearray()
        # Start a network-idle worker so process startup is outside call deadlines.
        self._start()

    def __del__(self):
        try: self._stop()
        except (AttributeError, OSError): pass

    def _start(self, deadline=None, cancel=None):
        self.worker = subprocess.Popen([sys.executable, '-I', str(Path(__file__).with_name('_transport_worker.py'))],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            env={'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8'}, close_fds=True)
        self.buffer.clear()
        for stream in [self.worker.stdin, self.worker.stdout]: os.set_blocking(stream.fileno(), False)
        config = {'scheme': self.base.scheme, 'host': self.base.hostname, 'port': self.base.port, 'ca_file': self.ca_file}
        self._exchange(config, deadline if deadline is not None else time.monotonic() + 5, cancel, 131072, startup=True)

    def _stop(self):
        worker, self.worker = self.worker, None
        if worker is not None:
            if worker.poll() is None: worker.kill()
            worker.wait()
            worker.stdin.close(); worker.stdout.close()
        self.buffer.clear()

    def close(self):
        self.closed = True
        # An active call observes closed within 20 ms and reaps its own worker.
        if self.lock.acquire(blocking=False):
            try: self._stop()
            finally: self.lock.release()

    def _exchange(self, command, deadline, cancel, bound, startup=False):
        payload = pickle.dumps(command, protocol=4)
        pending = memoryview(struct.pack('!I', len(payload)) + payload)
        observed = []
        sent = False
        unsafe = False
        status = None
        kind = None
        result = None
        with selectors.DefaultSelector() as select:
            select.register(self.worker.stdout, selectors.EVENT_READ)
            select.register(self.worker.stdin, selectors.EVENT_WRITE)
            while kind is None and result is None:
                if self.closed: kind = 'cancelled'; break
                if cancel is not None and cancel.is_set(): kind = 'cancelled'; break
                if time.monotonic() >= deadline: kind = 'timeout'; break
                for key, _ in select.select(min(0.02, max(0, deadline - time.monotonic()))):
                    if key.fileobj is self.worker.stdin:
                        try: count = os.write(key.fd, pending)
                        except (BrokenPipeError, OSError): kind = 'transport'; break
                        pending = pending[count:]
                        if not pending: select.unregister(self.worker.stdin)
                    else:
                        chunk = os.read(key.fd, 65536)
                        if not chunk: kind = 'transport'; break
                        self.buffer.extend(chunk)
                        while len(self.buffer) >= 4:
                            length = struct.unpack('!I', self.buffer[:4])[0]
                            if length > bound: kind = 'protocol'; break
                            if len(self.buffer) < length + 4: break
                            frame = pickle.loads(self.buffer[4:length + 4]); del self.buffer[:length + 4]
                            tag, value = frame
                            if tag == 'status': status = value
                            elif tag == 'sent': sent = True
                            elif tag == 'headers':
                                observed.extend(value)
                                if len(observed) > 512: kind = 'protocol'; break
                            elif tag == 'unsafe_headers': unsafe = value
                            elif tag == 'error': kind = value
                            elif tag == 'ready' and startup: return None
                            elif tag == 'result': result = value
        if kind is not None:
            # Stop possible HTTP writes first, then consume already-emitted
            # dispatch/header observations. Cancellation may race a readable IPC
            # frame; throwing that frame away could lose mutation uncertainty.
            if self.worker.poll() is None: self.worker.kill()
            self.worker.wait()
            drained = 0
            while drained < 262144:
                chunk = os.read(self.worker.stdout.fileno(), min(65536, 262144 - drained))
                if not chunk: break
                drained += len(chunk); self.buffer.extend(chunk)
            if drained >= 262144: unsafe = True
            while len(self.buffer) >= 4:
                length = struct.unpack('!I', self.buffer[:4])[0]
                if length > bound or len(self.buffer) < length + 4: break
                tag, value = pickle.loads(self.buffer[4:length + 4]); del self.buffer[:length + 4]
                if tag == 'sent': sent = True
                elif tag == 'status': status = value
                elif tag == 'headers':
                    if len(observed) + len(value) <= 512: observed.extend(value)
                    else: unsafe = True
                elif tag == 'unsafe_headers' and drained < 262144: unsafe = unsafe or value
            self._stop()
            error = WebmaniaError(kind, {'timeout': 'Absolute request deadline expired.', 'cancelled': 'Request cancelled.', 'response_limit': 'Response exceeds the configured byte limit.'}.get(kind, 'Request transport failed.'))
            error.status = status
            error._request_sent = sent
            error._observed_headers = observed
            error._unsafe_headers = unsafe
            raise error
        return result, observed

    def request(self, verb, path, body, headers, options=None):
        options = options or CallOptions()
        if not isinstance(options, CallOptions): raise WebmaniaError('configuration', 'Expected CallOptions.')
        timeout = self.timeout if options.timeout is None else options.timeout
        limit = self.max_response_bytes if options.max_response_bytes is None else options.max_response_bytes
        if not positive(timeout) or timeout > sys.float_info.max or not positive(limit, True) or (options.cancel is not None and not isinstance(options.cancel, threading.Event)):
            raise WebmaniaError('configuration', 'Invalid per-call timeout, byte limit, or cancellation event.')
        if body is not None and len(body) > self.max_request_bytes: raise WebmaniaError('request_limit', 'Request exceeds the configured byte limit.')
        if options.cancel is not None and options.cancel.is_set(): raise WebmaniaError('cancelled', 'Request cancelled before network access.')
        deadline = time.monotonic() + timeout
        while not self.lock.acquire(timeout=min(0.02, max(0, deadline - time.monotonic()))):
            if options.cancel is not None and options.cancel.is_set(): raise WebmaniaError('cancelled', 'Request cancelled while waiting for the client.')
            if time.monotonic() >= deadline: raise WebmaniaError('timeout', 'Request deadline expired while waiting for the client.')
        pending = None
        result = None
        try:
            if self.closed: raise WebmaniaError('configuration', 'Client is closed.')
            if self.worker is None: self._start(deadline, options.cancel)
            result, observed = self._exchange((verb, path, body, headers, max(0.001, deadline - time.monotonic()), limit), deadline, options.cancel, limit + 262144)
            status, fields, data = result
            # Private metadata never enters user-visible HTTP headers.
            fields = dict(fields)
            return status, fields, data, observed
        except WebmaniaError as exc: pending = exc
        finally: self.lock.release()
        raise pending
