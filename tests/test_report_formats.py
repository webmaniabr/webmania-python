"""Report formats, current report downloads, origins and post-send uncertainty (loopback only)."""
import io
import json
import socket
import threading
import time
import unittest
import zipfile

from webmania import (CallOptions, CompanyCredentials, FileAuth, NfeClient, NfeFilesClient,
                      ReportFilesClient, WebmaniaError)
from support import UUID, XML, server, send
from test_sdk import CORPUS

ISSUE = next(c['request'] for c in CORPUS if c['operation'] == 'nfeIssueDocument')
LARGE_XML = XML.replace(b'<!-- synthetic -->', b'<!-- ' + b'synthetic ' * 300 + b'-->')

CREDS = CompanyCredentials('report-key', 'report-secret', 'report-access', 'report-access-secret')
REPORT = '00000000-0000-4000-8000-000000000123'
XLSX = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
CSV = b'numero;destinatario;valor\r\n1;Jo\xe3o;10.00\r\n'  # Latin-1 byte kept unchanged


def workbook():
    ct = ('<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
          '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
    book = ('<?xml version="1.0" encoding="UTF-8"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="R" sheetId="1" r:id="rId1"/></sheets></workbook>')
    book_rels = ('<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
    sheet = '<?xml version="1.0" encoding="UTF-8"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData/></worksheet>'
    raw = io.BytesIO()
    with zipfile.ZipFile(raw, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, text in [('[Content_Types].xml', ct), ('_rels/.rels', rels), ('xl/workbook.xml', book),
                           ('xl/_rels/workbook.xml.rels', book_rels), ('xl/worksheets/sheet1.xml', sheet)]:
            archive.writestr(name, text)
    return raw.getvalue()


class LegacyReportTextXmlTests(unittest.TestCase):
    """FILE-07: only the legacy report operation accepts text/xml, classified by bytes."""

    def download(self, body, media='text/xml'):
        with server(lambda h, r: send(h, body, media=media)) as (base, records, _):
            with NfeFilesClient(base_url=base, trusted_origins=[base]) as client:
                try: return client.download_report(uuid=REPORT, auth=FileAuth('capability')), None, len(records)
                except WebmaniaError as error: return None, error, len(records)

    def test_csv_labeled_text_xml_is_returned_byte_exact(self):
        result, error, count = self.download(CSV)
        self.assertIsNone(error)
        self.assertEqual((result.data, result.media_type, count), (CSV, 'text/csv', 1))

    def test_xlsx_labeled_text_xml_is_identified_by_zip_signature(self):
        book = workbook()
        result, error, count = self.download(book)
        self.assertIsNone(error)
        self.assertEqual((result.data, result.media_type, count), (book, XLSX, 1))

    def test_real_xml_html_and_json_bodies_are_refused_as_reports(self):
        for body in [XML, b'<?xml version="1.0"?><relatorio/>', b'<!doctype html><html><body>x</body></html>',
                     b'  {"error":"x"}', '﻿<html/>'.encode('utf-16')]:
            result, error, count = self.download(body)
            self.assertIsNone(result)
            self.assertEqual((error.kind, error.status, count), ('protocol', 200, 1))
            self.assertEqual(error.outcome, 'unknown')  # the download may have consumed quota

    def test_other_file_operations_gain_no_text_xml_tolerance(self):
        with server(lambda h, r: send(h, CSV, media='text/xml')) as (base, records, _):
            with NfeFilesClient(credentials=CREDS, base_url=base, trusted_origins=[base]) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.download_xml(identifier=UUID, auth=FileAuth('company'))
            self.assertEqual(caught.exception.kind, 'protocol')
            self.assertEqual(len(records), 1)

    def test_declared_csv_still_refuses_markup(self):
        result, error, _ = self.download(b'<html>no</html>', media='text/csv')
        self.assertEqual(error.kind, 'protocol')


class CurrentReportDownloadTests(unittest.TestCase):
    """POLL-04: current report URLs stay on the configured API2 origin and /relatorios/ route."""

    def test_returned_url_on_trusted_origin_downloads_with_explicit_access_mode(self):
        with server(lambda h, r: send(h, CSV, media='text/csv')) as (base, records, _):
            with ReportFilesClient(base_url=base, trusted_origins=[base], credentials=CREDS, issuer_token='report-issuer') as client:
                url = base + '/relatorios/' + REPORT
                self.assertEqual(client.download_url(url, auth=FileAuth('anonymous')).data, CSV)
                self.assertEqual(client.download_url(url, auth=FileAuth('company')).data, CSV)
                self.assertEqual(client.download_report_v2(uuid=REPORT, auth=FileAuth('issuer')).data, CSV)
            self.assertEqual([r['path'] for r in records], ['/relatorios/' + REPORT] * 3)
            first, second, third = [{k.lower(): v for k, v in r['headers'].items()} for r in records]
            self.assertFalse(any(k == 'authorization' or k.startswith(('x-consumer', 'x-access')) for k in first))
            self.assertEqual(second['x-consumer-key'], 'report-key')
            self.assertNotIn('authorization', second)
            self.assertEqual(third['authorization'], 'Bearer report-issuer')
            self.assertFalse(any(k.startswith(('x-consumer', 'x-access')) for k in third))

    def test_foreign_or_malformed_urls_are_refused_before_any_request(self):
        with server(lambda h, r: send(h, CSV, media='text/csv')) as (base, records, _):
            port = base.rsplit(':', 1)[1]
            with ReportFilesClient(base_url=base, trusted_origins=[base], credentials=CREDS) as client:
                for url in ['http://localhost:' + port + '/relatorios/' + REPORT,
                            'https://127.0.0.1:' + port + '/relatorios/' + REPORT,
                            'http://user:pass@127.0.0.1:' + port + '/relatorios/' + REPORT,
                            base + '/relatorio/' + REPORT + '/',
                            base + '/outro/relatorios/' + REPORT,
                            base + '/relatorios/' + REPORT + '#fragment']:
                    with self.assertRaises(WebmaniaError) as caught:
                        client.download_url(url, auth=FileAuth('company'))
                    self.assertEqual(caught.exception.kind, 'validation')
            self.assertEqual(records, [])
        with self.assertRaises(WebmaniaError) as caught:
            ReportFilesClient(base_url='https://api.example.invalid', trusted_origins=['https://other.example.invalid'])
        self.assertEqual(caught.exception.kind, 'configuration')

    def test_json_error_at_200_and_redirects_are_failures_never_files(self):
        state = {'mode': 'json'}
        def handler(h, record):
            if state['mode'] == 'json': send(h, {'error': 'Relatório em processamento'})
            else: send(h, b'', 302, media='text/plain', headers={'Location': 'https://elsewhere.example.invalid/x'})
        with server(handler) as (base, records, _):
            with ReportFilesClient(base_url=base, trusted_origins=[base], credentials=CREDS) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.download_report_v2(uuid=REPORT, auth=FileAuth('company'))
                self.assertEqual((caught.exception.kind, caught.exception.status), ('business', 200))
                state['mode'] = 'redirect'
                with self.assertRaises(WebmaniaError) as caught:
                    client.download_report_v2(uuid=REPORT, auth=FileAuth('company'))
                self.assertEqual(caught.exception.kind, 'redirect')
            self.assertEqual(len(records), 2)

    def test_declared_report_formats_must_match_bytes(self):
        cases = [(workbook(), XLSX, True), (b'%PDF-1.4 not a pdf', 'application/pdf', False),
                 (b'not a zip', 'application/zip', False), (b'<html><body>r</body></html>', 'text/html', True),
                 (b'<relatorio/>', 'application/xml', True), (b'\x01\x02', 'application/octet-stream', True)]
        for body, media, accepted in cases:
            with server(lambda h, r, body=body, media=media: send(h, body, media=media)) as (base, records, _):
                with ReportFilesClient(base_url=base, trusted_origins=[base]) as client:
                    if accepted:
                        result = client.download_report_v2(uuid=REPORT, auth=FileAuth('anonymous'))
                        self.assertEqual((result.data, result.media_type), (body, media))
                    else:
                        with self.assertRaises(WebmaniaError) as caught:
                            client.download_report_v2(uuid=REPORT, auth=FileAuth('anonymous'))
                        self.assertEqual(caught.exception.kind, 'protocol')


class StructuralLocationTests(unittest.TestCase):
    def test_route_segments_in_location_do_not_drop_the_recovery_selector(self):
        request = {'uuid': UUID, 'motivo': 'Synthetic cancellation reason'}
        with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': '/api/1/nfe/cancelar/'})) as (base, records, _):
            with NfeClient(CREDS, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught: client.cancel_document(request)
        error = caught.exception
        self.assertEqual((error.kind, error.outcome), ('redirect', 'unknown'))
        self.assertEqual(error.request_reference.reveal(), {'uuid': UUID})
        self.assertNotIn(UUID, json.dumps(error.to_dict()))
        self.assertEqual(len(records), 1)


class TransportBoundaryTests(unittest.TestCase):
    def test_sent_mutation_whose_2xx_body_never_completes_is_unknown_and_not_replayed(self):
        """CANCEL-05: timeout and explicit cancellation after complete 2xx headers."""
        release = threading.Event()
        headers_sent = threading.Event()
        def handler(h, record):
            h.send_response(200)
            h.send_header('Content-Type', 'application/json')
            h.send_header('Content-Length', '64')
            h.end_headers(); h.wfile.write(b'{"'); h.wfile.flush()
            headers_sent.set()
            release.wait(5)
        try:
            with server(handler) as (base, records, _):
                with NfeClient(CREDS, base_url=base) as client:
                    with self.assertRaises(WebmaniaError) as caught:
                        client.issue_document(ISSUE, options=CallOptions(timeout=0.5))
                    self.assertEqual((caught.exception.kind, caught.exception.outcome), ('timeout', 'unknown'))
                    self.assertEqual(caught.exception.request_reference.reveal(), {'ID': ISSUE['ID']})
                    self.assertEqual(len(records), 1)
                with NfeClient(CREDS, base_url=base) as client:
                    cancel = threading.Event()
                    headers_sent.clear()
                    threading.Thread(target=lambda: (headers_sent.wait(5), time.sleep(0.1), cancel.set()), daemon=True).start()
                    with self.assertRaises(WebmaniaError) as caught:
                        client.issue_document(ISSUE, options=CallOptions(timeout=5, cancel=cancel))
                    self.assertEqual((caught.exception.kind, caught.exception.outcome), ('cancelled', 'unknown'))
                    self.assertEqual(len(records), 2)
        finally:
            release.set()

    def test_many_chunk_size_lines_are_budgeted_per_line(self):
        """HTTP-05: thousands of chunk-size lines beyond one 64 KiB header budget still deliver the body."""
        extension = b';' + b'x' * 30
        def chunked(lines):
            def handler(h, record):
                h.send_response(200)
                h.send_header('Content-Type', 'text/xml')
                h.send_header('Transfer-Encoding', 'chunked')
                h.end_headers()
                h.wfile.write(lines); h.wfile.flush()
            return handler
        body = b''.join(b'1' + extension + b'\r\n' + bytes([c]) + b'\r\n' for c in LARGE_XML) + b'0\r\n\r\n'
        self.assertGreater(len(body), 65536)
        with server(chunked(body)) as (base, records, _):
            with NfeFilesClient(credentials=CREDS, base_url=base, trusted_origins=[base]) as client:
                self.assertEqual(client.download_xml(identifier=UUID, auth=FileAuth('company')).data, LARGE_XML)
            self.assertEqual(len(records), 1)
        oversized = b'1;' + b'x' * 70000 + b'\r\nA\r\n0\r\n\r\n'
        with server(chunked(oversized)) as (base, records, _):
            with NfeFilesClient(credentials=CREDS, base_url=base, trusted_origins=[base]) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.download_xml(identifier=UUID, auth=FileAuth('company'))
                self.assertIn(caught.exception.kind, ['protocol', 'transport'])
            self.assertEqual(len(records), 1)

    def test_explicit_origin_with_path_prefix_and_invalid_origins(self):
        """ENV-04: requests go only to the configured origin and prefix; invalid origins fail first."""
        with server(lambda h, r: send(h, {'status': 'online'})) as (base, records, _):
            with NfeClient(CREDS, base_url=base + '/api1-prefix') as client:
                self.assertEqual(client.get_sefaz_status(), {'status': 'online'})
            self.assertEqual(records[0]['path'], '/api1-prefix/1/nfe/sefaz/')
        for origin in ['http://example.invalid/api', 'https://user@example.invalid/api', 'https://example.invalid/api?x=1',
                       'https://example.invalid/api#f', 'https://example.invalid/a/../api']:
            with self.assertRaises(WebmaniaError) as caught: NfeClient(CREDS, base_url=origin)
            self.assertEqual(caught.exception.kind, 'configuration')


if __name__ == '__main__': unittest.main(verbosity=2)
