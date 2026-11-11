"""Private stdlib HTTP worker. All resolver and socket work is owned by its process."""
import http.client
import email.message
import os
import ipaddress
import pickle
import socket
import ssl
import struct
import sys
import time

IN = sys.stdin.buffer
OUT = sys.stdout.buffer
MAX_COMMAND = 9 * 1024 * 1024


def emit(value):
    payload = pickle.dumps(value, protocol=4)
    OUT.write(struct.pack('!I', len(payload)) + payload)
    OUT.flush()


def receive():
    size = IN.read(4)
    if not size: return None
    if len(size) != 4: raise EOFError
    length = struct.unpack('!I', size)[0]
    if length > MAX_COMMAND: raise ValueError
    payload = IN.read(length)
    if len(payload) != length: raise EOFError
    return pickle.loads(payload)


class Response(http.client.HTTPResponse):
    def _read_status(self):
        # http.client normally skips only 100. Skip every legal informational
        # response, recording its metadata before the final response begins.
        for _ in range(17):
            version, status, reason = super()._read_status()
            if not 100 <= status < 200: return version, status, reason
            emit(('status', status))
            emit(('unsafe_headers', True))
            fields = self._fields()
            emit(('unsafe_headers', False))
            emit(('headers', fields))
            if status == 101: raise http.client.HTTPException('Unsupported upgrade.')
        raise http.client.HTTPException('Too many informational responses.')

    def _fields(self, maximum=65536):
        lines = []
        budget = 0
        while True:
            line = self.fp.readline(65537)
            budget += len(line)
            if len(line) > 65536 or budget > maximum or len(lines) >= 100:
                raise http.client.HTTPException('Header budget.')
            if line == b'\r\n': break
            if not line or not line.endswith(b'\r\n') or b':' not in line:
                raise http.client.HTTPException('Incomplete fields.')
            name, value = line[:-2].split(b':', 1)
            if not name or any(c not in b"!#$%&'*+-.^_`|~0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" for c in name):
                raise http.client.HTTPException('Invalid field name.')
            if any(c < 32 and c != 9 or c == 127 for c in value):
                raise http.client.HTTPException('Invalid field value.')
            fields = (name.decode('ascii'), value.decode('latin-1').strip(' \t'))
            lines.append(fields)
            emit(('headers', [fields]))
        return lines

    def begin(self):
        if self.headers is not None: return
        version, status, reason = self._read_status()
        emit(('status', status))
        self.code = self.status = status
        self.reason = reason.strip()
        if version in ('HTTP/1.0', 'HTTP/0.9'): self.version = 10
        elif version.startswith('HTTP/1.'): self.version = 11
        else: raise http.client.UnknownProtocol(version)
        emit(('unsafe_headers', True))
        fields = self._fields()
        self.headers = self.msg = email.message.Message()
        for key, value in fields: self.headers[key] = value
        emit(('unsafe_headers', False))
        self.chunked = self.headers.get('transfer-encoding', '').lower() == 'chunked'
        self.chunk_left = None if self.chunked else 'UNKNOWN'
        self.will_close = self._check_close()
        self.length = None
        length = self.headers.get('content-length')
        if length is not None and not self.chunked:
            if not length.isascii() or not length.isdecimal(): raise http.client.HTTPException('Invalid content length.')
            self.length = int(length)
        if status in (204, 304) or 100 <= status < 200 or self._method == 'HEAD': self.length = 0
        if not self.will_close and not self.chunked and self.length is None: self.will_close = True

    def _read_and_discard_trailer(self):
        emit(('unsafe_headers', True))
        self._fields(2048)
        emit(('unsafe_headers', False))


class Connection(http.client.HTTPConnection):
    response_class = Response
    def send(self, data):
        if self.sock is None: self.connect()
        emit(('sent', True))
        return http.client.HTTPConnection.send(self, data)


class SecureConnection(http.client.HTTPSConnection):
    response_class = Response
    send = Connection.send


def run():
    # Linux: terminate owned resolver/socket work if the parent dies.
    if sys.platform == 'linux':
        import ctypes
        import signal
        parent = os.getppid()
        if ctypes.CDLL(None).prctl(1, signal.SIGKILL) != 0 or os.getppid() != parent: return
    cfg = receive()
    context = ssl.create_default_context(cafile=cfg['ca_file'])
    cls = SecureConnection if cfg['scheme'] == 'https' else Connection
    kw = {'context': context} if cfg['scheme'] == 'https' else {}
    conn = cls(cfg['host'], cfg['port'], **kw)
    def connect(address, timeout=None, source_address=None, **_):
        answers = socket.getaddrinfo(address[0], address[1], 0, socket.SOCK_STREAM)
        for family, kind, proto, _, sockaddr in answers:
            if cfg['scheme'] == 'http' and not ipaddress.ip_address(sockaddr[0]).is_loopback: continue
            sock = socket.socket(family, kind, proto)
            sock.settimeout(timeout)
            try:
                if source_address: sock.bind(source_address)
                sock.connect(sockaddr)
                return sock
            except OSError: sock.close()
        raise OSError('Connection failed.')
    conn._create_connection = connect
    emit(('ready', True))
    while True:
        request = receive()
        if request is None: break
        verb, path, body, headers, timeout, limit = request
        response = None
        try:
            conn.timeout = timeout
            if conn.sock is not None: conn.sock.settimeout(timeout)
            conn.request(verb, path, body=body, headers=headers)
            response = conn.getresponse()
            fields = response.getheaders()
            emit(('headers', fields))
            names = [k.lower() for k, _ in fields]
            if any(names.count(k) > 1 for k in ['content-length', 'content-type', 'transfer-encoding', 'content-encoding', 'location']) or ('content-length' in names and 'transfer-encoding' in names):
                raise http.client.HTTPException('Ambiguous headers.')
            lengths = [v for k, v in fields if k.lower() == 'content-length']
            if lengths and not lengths[0].isascii() or lengths and not lengths[0].isdigit():
                raise http.client.HTTPException('Invalid content length.')
            transfers = [v.lower() for k, v in fields if k.lower() == 'transfer-encoding']
            if transfers and transfers != ['chunked']: raise http.client.HTTPException('Unsupported transfer coding.')
            chunks = bytearray()
            while not response.isclosed() and response.length != 0:
                block = response.read1(min(65536, limit + 1 - len(chunks)))
                if not block: break
                chunks.extend(block)
                if len(chunks) > limit:
                    emit(('error', 'response_limit')); conn.close(); break
            else: block = None
            if len(chunks) > limit: continue
            if response.length not in (None, 0): raise http.client.HTTPException('Truncated body.')
            emit(('result', (response.status, dict(fields), bytes(chunks))))
        except (socket.timeout, TimeoutError):
            emit(('error', 'timeout')); conn.close()
        except http.client.HTTPException:
            emit(('error', 'protocol')); conn.close()
        except (OSError, ValueError, UnicodeError):
            emit(('error', 'transport')); conn.close()
        finally:
            if response is not None: response.close()
    conn.close()


if __name__ == '__main__':
    try: run()
    except (EOFError, OSError, ValueError, pickle.UnpicklingError): pass
