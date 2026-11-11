"""Loopback-only socket fixtures. No remote fiscal service is used."""
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import ssl
import subprocess
import tempfile
import threading

HERE = Path(__file__).resolve().parent
UUID = '00000000-0000-4000-8000-000000000001'
PDF = b'%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 72 72] /Resources << >> >>\nendobj\nxref\n0 4\n0000000000 65535 f \n0000000009 00000 n \n0000000058 00000 n \n0000000115 00000 n \ntrailer\n<< /Size 4 /Root 1 0 R >>\nstartxref\n201\n%%EOF\n'
XML = b'\xef\xbb\xbf<?xml version="1.0" encoding="UTF-8"?>\n<!-- synthetic -->\n<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe"><NFe/></nfeProc>\n'
ZIP = b'PK\x05\x06' + b'\0' * 18


@contextmanager
def server(handler, tls=False, wrong_hostname=False):
    records = []
    class Handler(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'
        def log_message(self, *_): pass
        def handle_request(self):
            raw = self.rfile.read(int(self.headers.get('Content-Length', 0)))
            record = {'method': self.command, 'path': self.path, 'headers': dict(self.headers), 'raw': raw, 'peer_port': self.client_address[1]}
            records.append(record)
            try: handler(self, record)
            except (BrokenPipeError, ConnectionResetError, ssl.SSLError): pass
        do_GET = do_POST = do_PUT = do_DELETE = handle_request
    class Server(ThreadingHTTPServer):
        daemon_threads = True
        def handle_error(self, *_): pass
    fixture = Server(('127.0.0.1', 0), Handler)
    with tempfile.TemporaryDirectory() as directory:
        ca = None
        if tls:
            path = Path(directory)
            ca = path / 'cert.pem'
            key = path / 'key.pem'
            san = 'DNS:wrong.invalid' if wrong_hostname else 'IP:127.0.0.1,DNS:localhost'
            subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-nodes', '-days', '1', '-subj', '/CN=controlled-fixture', '-addext', 'subjectAltName=' + san, '-keyout', str(key), '-out', str(ca)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(ca, key)
            fixture.socket = context.wrap_socket(fixture.socket, server_side=True)
        thread = threading.Thread(target=fixture.serve_forever, daemon=True)
        thread.start()
        try: yield ('https' if tls else 'http') + '://127.0.0.1:' + str(fixture.server_port), records, str(ca) if ca else None
        finally:
            fixture.shutdown(); fixture.server_close(); thread.join(timeout=2)


def send(handler, value, status=200, media='application/json', headers=None):
    data = json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode() if media == 'application/json' and not isinstance(value, bytes) else value
    handler.send_response(status)
    handler.send_header('Content-Type', media)
    handler.send_header('Content-Length', str(len(data)))
    for k, v in (headers or {}).items(): handler.send_header(k, v)
    handler.end_headers(); handler.wfile.write(data); handler.wfile.flush()
