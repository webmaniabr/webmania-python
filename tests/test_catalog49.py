"""Catalog49 causal regressions, executed against normally installed artifacts."""
import copy
from dataclasses import replace
import io
import json
import os
import struct
import threading
import time
import unittest
from unittest import mock
import zipfile
from urllib.parse import parse_qs, urlsplit
from webmania import CallOptions, CompanyCredentials, MonitorClient, NfeClient, WebmaniaError, with_additional_fields
from webmania.errors import Redactor
from webmania.file_inspection import xml_document, zip_parts, xlsx_package
from webmania.pdf_structure import pdf_document
from support import PDF, UUID, HERE, send, server

CREDS = CompanyCredentials('catalog-key', 'catalog-secret', 'catalog-access', 'catalog-access-secret')


class Catalog49Tests(unittest.TestCase):
    def test_short_capabilities_preserve_words_and_literal_credentials(self):
        r = Redactor(['1234'], contextual_values=['z', 'ab', '7'])
        self.assertEqual(r.text('(z), ab; 7 size label abc 17 912345'), '([redacted]), [redacted]; [redacted] size label abc 17 9[redacted]5')
        self.assertEqual(Redactor(['xy']).text('zxyword'), 'z[redacted]word')

    def test_finite_snapshots_surrogates_cycles_and_additional_depth(self):
        deep = 'private'
        for _ in range(512): deep = {'layer': deep}
        cycle = {}; cycle['cycle'] = cycle
        with server(lambda h,r:send(h, {'status':'online','extension':float('inf')})) as (base, records, _):
            with NfeClient(CREDS, base_url=base) as client:
                for value in [deep, cycle, '\ud800', float('nan')]:
                    with self.assertRaises(WebmaniaError) as error: with_additional_fields({}, {'future':value})
                    self.assertEqual(error.exception.kind, 'validation')
                with self.assertRaises(WebmaniaError) as error: client.get_document(query={'ID':'\ud800'})
                self.assertEqual(error.exception.kind, 'validation'); self.assertEqual(records, [])
                # Overflow via a finite JSON lexeme must be refused as well as NaN.
        with server(lambda h,r:send(h, b'{"status":"online","extension":1e999}')) as (base, records, _):
            with NfeClient(CREDS, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as error: client.get_sefaz_status()
                self.assertEqual(error.exception.kind, 'protocol')
            self.assertEqual(len(records), 1)

        for text in ['1e-400','7.0000000000000001','1e10000000']:
            raw=('{"status":"online","extension":'+text+'}').encode()
            with server(lambda h,r,raw=raw:send(h,raw)) as (base,records,_):
                with NfeClient(CREDS,base_url=base) as client:
                    with self.assertRaises(WebmaniaError) as error: client.get_sefaz_status()
                    self.assertEqual(error.exception.kind,'protocol')
                self.assertEqual(len(records),1)

    def test_continuation75_resume_without_duplicates_or_hidden_io(self):
        template = next(x['response'] for x in json.loads((HERE/'fixtures/operations.json').read_text(encoding='utf-8'))['cases'] if x['operation']=='monitorCreateCompany')
        items = [{**copy.deepcopy(template), 'uuid':f'00000000-0000-4000-8000-{i:012x}'} for i in range(100)]
        def handler(h,r):
            query=parse_qs(urlsplit(r['path']).query); page=int(query['page'][0]); data=items[(page-1)*50:page*50]
            send(h, {'data':data,'meta':{'current_page':page,'last_page':2,'per_page':50,'total':100}})
        with server(handler) as (base, records, _):
            with MonitorClient('catalog-monitor',base_url=base) as client:
                first=client.iter_companies({'per_page':50},max_items=75)
                got=list(first); self.assertEqual(len(got),75); self.assertEqual(len(records),2)
                token=first.continuation; self.assertIsNotNone(token)
                with self.assertRaises(WebmaniaError): client.iter_companies({'per_page':25},continuation=token)
                self.assertEqual(len(records),2)
                with self.assertRaises(WebmaniaError): client.iter_companies({'per_page':50},continuation=replace(token,_offset=-1))
                self.assertEqual(len(records),2)
                second=client.iter_companies({'per_page':50},continuation=token,max_items=25)
                got+=list(second); self.assertEqual(len(records),3); self.assertIsNone(second.continuation)
                self.assertEqual([x['uuid'] for x in got],[x['uuid'] for x in items])

    def test_classic_pdf_graph_offsets_generations_and_opaque_tokens(self):
        pdf_document(PDF)
        for bad in [PDF.replace(b'/Count 1', b'/Count 2'), PDF.replace(b'/Catalog',b'/Notalog'), PDF.replace(b'/Parent 2',b'/Parent 1'), PDF.replace(b'/Root 1 0 R',b'/Root 1 7 R'), b'%PDF-1.4\ntrailer << /Root 1 0 R >>\n%%EOF\n']:
            with self.subTest(bad=bad[:40]), self.assertRaises(ValueError): pdf_document(bad)
        # Same-width generation change must agree in object, xref and Root.
        xref_line=b'%010d 00000 n' % PDF.find(b'1 0 obj')
        revised=PDF.replace(b'1 0 obj',b'1 7 obj').replace(b'/Root 1 0 R',b'/Root 1 7 R').replace(xref_line,xref_line.replace(b'00000 n',b'00007 n'))
        pdf_document(revised)

    def test_xml_duplicate_expanded_attributes_dtd_utf16_and_bounds(self):
        xml_document('<nfeProc a="1"><NFe/></nfeProc>'.encode('utf-16'))
        for data in [b'<nfeProc a="1" a="2"/>',b'<nfeProc xmlns:x="urn:a" xmlns:y="urn:a" x:a="1" y:a="2"/>',b'<!DOCTYPE nfeProc [<!ENTITY x "x">]><nfeProc>&x;</nfeProc>', b'<nfeProc>'+b'<x>'*65+b'</x>'*65+b'</nfeProc>']:
            with self.subTest(data=data[:60]), self.assertRaises(ValueError): xml_document(data)

    def test_zip_local_central_crc_size_and_expansion_consistency(self):
        raw=io.BytesIO()
        with zipfile.ZipFile(raw,'w',compression=zipfile.ZIP_DEFLATED) as archive: archive.writestr('part.txt',b'bounded-data')
        data=raw.getvalue(); self.assertEqual(zip_parts(data)['part.txt'],b'bounded-data')
        for field in [6,8,14,18,22]:
            bad=bytearray(data); bad[field]^=1
            with self.subTest(field=field), self.assertRaises(ValueError): zip_parts(bytes(bad))

    def test_terminal_invalid_import_keeps_error_state_and_stops(self):
        value={'uuid':UUID,'status':'invalido','erro':'fiscal import refused'}
        # Use the exact required fields from the pinned positive fixture.
        fixture=next(x['response'] for x in json.loads((HERE/'fixtures/operations.json').read_text(encoding='utf-8'))['cases'] if x['operation']=='monitorGetImportStatus'); value={**fixture,**value}
        with server(lambda h,r:send(h,value)) as (base,records,_):
            with MonitorClient('catalog-monitor',base_url=base) as client:
                for invalid in [dict(options=CallOptions(timeout=0)),dict(deadline=10**400),dict(interval=10**400)]:
                    with self.assertRaises(WebmaniaError) as error: client.wait_import(UUID,**invalid)
                    self.assertEqual(error.exception.kind,'configuration')
                self.assertEqual(client.wait_import(UUID,max_attempts=2),value)
            self.assertEqual(len(records),1)

    def test_owned_worker_close_and_after_send_uncertainty(self):
        accepted=threading.Event()
        def handler(h,r): accepted.set(); time.sleep(.2); send(h,{'uuid':UUID,'status':'cancelado'})
        with server(handler) as (base,records,_):
            client=NfeClient(CREDS,base_url=base)
            worker=client._transport.worker
            event=threading.Event(); result=[]
            def call():
                try: client.cancel_document({'uuid':UUID,'motivo':'Synthetic cancellation reason'},options=CallOptions(timeout=1,cancel=event))
                except WebmaniaError as error: result.append(error)
            real_write=os.write
            def delay_after_request(fd, data):
                count=real_write(fd,data); time.sleep(.12); return count
            # Dispatch can complete while the parent has not consumed its IPC
            # frame. Abort must reap then drain that already-written observation.
            with mock.patch('webmania.transport.os.write',side_effect=delay_after_request):
                thread=threading.Thread(target=call);thread.start();self.assertTrue(accepted.wait(1));event.set();thread.join(1)
            self.assertFalse(thread.is_alive());self.assertEqual(result[0].kind,'cancelled');self.assertEqual(result[0].outcome,'unknown')
            self.assertIsNotNone(worker.poll());self.assertEqual(len(records),1);client.close()

    def test_aborted_observation_budget_cannot_reenable_recovery(self):
        prefix=(b'HTTP/1.1 100 Continue\r\n'+b'X-Public: bounded\r\n'*90+b'\r\n')*3
        frame=prefix+b'HTTP/1.1 500 Controlled\r\nLocation: /private/'+UUID.encode()+b'\r\nContent-Length: 2\r\nContent-Type: application/json\r\n\r\n{}'
        with server(lambda h,r:(h.wfile.write(frame),h.wfile.flush())) as (base,records,_):
            with NfeClient(CREDS,base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught: client.cancel_document({'uuid':UUID,'motivo':'Synthetic cancellation reason'})
                self.assertEqual(caught.exception.kind,'protocol')
                self.assertEqual(caught.exception.outcome,'unknown')
                self.assertIsNone(caught.exception.request_reference)
            self.assertEqual(len(records),1)
        frame=b'HTTP/1.1 500 Controlled\r\nTransfer-Encoding: chunked\r\nContent-Type: application/json\r\n\r\n2\r\n{}\r\n0\r\nLocation: /private/'+UUID.encode()+b'?token='+b'X'*2100+b'\r\n\r\n'
        with server(lambda h,r:(h.wfile.write(frame),h.wfile.flush())) as (base,records,_):
            with NfeClient(CREDS,base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught: client.cancel_document({'uuid':UUID,'motivo':'Synthetic cancellation reason'})
                self.assertEqual(caught.exception.kind,'protocol')
                self.assertEqual(caught.exception.outcome,'unknown')
                self.assertIsNone(caught.exception.request_reference)
            self.assertEqual(len(records),1)
