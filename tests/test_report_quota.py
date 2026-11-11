"""Normal one-request quota-effect regressions for the pinned API1 report GET."""
import hashlib
import json
import os
from pathlib import Path
import socket
import threading
import unittest

import webmania
from webmania import CallOptions, CompanyCredentials, FileAuth, NfeClient, NfeFilesClient, WebmaniaError
from support import ZIP, server, send

UUID = '00000000-0000-4000-8000-000000000097'
CREDS = CompanyCredentials('quota-key', 'quota-secret', 'quota-access', 'quota-access-secret')
ROWS = []


class ReportQuotaTests(unittest.TestCase):
    def run_case(self, case, operation, reply, outcome, precancel=False):
        def handler(h, record):
            if reply == 'drop':
                h.close_connection = True
                h.connection.shutdown(socket.SHUT_WR)
            elif reply == 'partial':
                h.send_response(200)
                h.send_header('Content-Type', 'application/zip')
                h.send_header('Content-Length', str(len(ZIP) + 10))
                h.end_headers()
                h.wfile.write(ZIP[:5]); h.wfile.flush()
                h.close_connection = True
                h.connection.shutdown(socket.SHUT_WR)
            elif reply == '422': send(h, {'error': 'Synthetic known rejection'}, status=422)
            elif reply == 'invalid': send(h, b'invalid zip', media='application/zip')
            else: send(h, ZIP, media='application/zip')
        error = None
        with server(handler) as (base, records, _):
            cancelled = threading.Event()
            if precancel: cancelled.set()
            options = CallOptions(timeout=2, cancel=cancelled)
            if operation == 'report':
                client = NfeFilesClient(credentials=CREDS, base_url=base, trusted_origins=[base])
                call = lambda: client.download_report(uuid=UUID, auth=FileAuth('capability'), options=options)
            else:
                client = NfeClient(CREDS, base_url=base)
                call = (lambda: client.get_sefaz_status(options=options)) if operation == 'passive' else (lambda: client.update_company({'cnae': None}, options=options))
            try:
                if reply == 'success' and not precancel:
                    self.assertEqual(call().data, ZIP)
                else:
                    with self.assertRaises(WebmaniaError) as caught: call()
                    error = caught.exception
                    self.assertEqual(error.outcome, outcome)
                    if precancel: self.assertEqual(error.kind, 'cancelled')
                    elif reply == '422': self.assertEqual((error.kind, error.status), ('http', 422))
                    elif reply == 'invalid': self.assertEqual((error.kind, error.status), ('protocol', 200))
                    else: self.assertIn(error.kind, ['protocol', 'transport'])
                    if operation == 'report':
                        self.assertIsNone(error.request_reference)
                        self.assertNotIn(UUID, json.dumps(error.to_dict()))
                        self.assertNotIn(base, json.dumps(error.to_dict()))
            finally: client.close()
            self.assertEqual(len(records), 0 if precancel else 1)
            for record in records:
                headers = {k.lower(): v for k, v in record['headers'].items()}
                if operation == 'post':
                    self.assertEqual((record['method'], record['path']), ('POST', '/1/nfe/empresa/'))
                    self.assertEqual(json.loads(record['raw']), {'cnae': None})
                if operation == 'report':
                    self.assertEqual(record['method'], 'GET')
                    self.assertEqual(record['path'], '/relatorio/' + UUID + '/')
                    self.assertEqual(record['raw'], b'')
                    self.assertFalse(any(k == 'authorization' or k.startswith(('x-consumer', 'x-access')) for k in headers))
            ROWS.append({'case': case, 'operation': operation, 'reply': reply, 'expected_outcome': outcome, 'observed_outcome': error.outcome if error else None, 'kind': error.kind if error else None, 'status': error.status if error else 200, 'HTTP_requests': len(records), 'report_recovery_reference': bool(error.request_reference) if error and operation == 'report' else None, 'assertions': 'matched'})

    def test_report_capture_drop(self): self.run_case('report-drop', 'report', 'drop', 'unknown')
    def test_passive_capture_drop(self): self.run_case('passive-drop', 'passive', 'drop', None)
    def test_post_capture_drop(self): self.run_case('post-drop', 'post', 'drop', 'unknown')
    def test_complete_known_422(self): self.run_case('report-known422', 'report', '422', None)
    def test_report_precancel(self): self.run_case('report-precancel', 'report', 'drop', None, precancel=True)
    def test_report_valid_success(self): self.run_case('report-valid', 'report', 'success', None)
    def test_report_invalid_200(self): self.run_case('report-protocol200', 'report', 'invalid', 'unknown')
    def test_report_partial_body(self): self.run_case('report-partial', 'report', 'partial', 'unknown')

    @classmethod
    def tearDownClass(cls):
        if os.environ.get('WEBMANIA_QUOTA_RECEIPT'):
            origin = Path(webmania.__file__).resolve()
            Path(os.environ['WEBMANIA_QUOTA_RECEIPT']).write_text(json.dumps({'version': webmania.__version__, 'origin': str(origin), 'origin_sha256': hashlib.sha256(origin.read_bytes()).hexdigest(), 'rows': ROWS, 'HTTP_requests': sum(x['HTTP_requests'] for x in ROWS), 'real_API': False, 'source_fallback': False}, indent=2) + '\n')


if __name__ == '__main__': unittest.main(verbosity=2)
