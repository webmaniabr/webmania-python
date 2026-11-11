import copy
import dataclasses
import hashlib
import importlib
import json
import math
from pathlib import Path
import threading
import time
import typing
import unittest
from unittest import mock
import socket
import subprocess
from urllib.parse import parse_qs, urlsplit, quote

from webmania import *
from webmania.errors import Redactor
from webmania.validation import DOCUMENTS, OPERATIONS, validate
from support import HERE, PDF, XML, ZIP, UUID, server, send

COMPANY = CompanyCredentials('synthetic-company-key', 'synthetic-company-secret', 'synthetic-company-access', 'synthetic-company-access-secret')
RESELLER = ResellerCredentials('synthetic-reseller-key', 'synthetic-reseller-secret', 'synthetic-reseller-access', 'synthetic-reseller-access-secret')
CORPUS = json.loads((HERE/'fixtures/operations.json').read_text())['cases']


def clients(base, ca=None):
    options = {'base_url':base, 'timeout':2, 'ca_file':ca}
    return {'Nfe':NfeClient(COMPANY,**options), 'Emitter':EmitterClient('synthetic-issuer',**options),
            'Monitor':MonitorClient('synthetic-monitor',**options), 'Reseller':ResellerClient(RESELLER,**options),
            'NfeFiles':NfeFilesClient(credentials=COMPANY,trusted_origins=[base],**options),
            'EmitterFiles':EmitterFilesClient(issuer_token='synthetic-issuer-files',trusted_origins=[base],**options)}


class ContractTests(unittest.TestCase):
    def test_wire_corpus_all_102_named_operations(self):
        selected = [None]
        def handler(h, record):
            c = selected[0]
            if c['binary']:
                data = PDF if c['media_type']=='application/pdf' else XML if c['media_type'] in ['application/xml','text/xml'] else ZIP
            else: data = c['response']
            send(h,data,c['status'],c['media_type'])
        with server(handler) as (base, records, _):
            pool=clients(base)
            try:
                self.assertEqual(len(CORPUS),102)
                for case in CORPUS:
                    with self.subTest(operation=case['operation']):
                        selected[0]=case
                        client=pool[case['client']]
                        method=getattr(client,case['method'])
                        kwargs={**case['path_params']}
                        if case['query']: kwargs['query']=case['query']
                        if case['client'].endswith('Files'):
                            kwargs['auth']=FileAuth('capability' if case['operation']=='fiscalDownloadReport' else 'company' if case['client']=='NfeFiles' else 'issuer')
                        args=[case['request']] if case['has_request'] else []
                        before=len(records)
                        if not case['enabled']:
                            with self.assertRaises(WebmaniaError) as caught: method(*args,**kwargs)
                            self.assertEqual(caught.exception.kind,'capability');self.assertEqual(len(records),before);continue
                        result=method(*args,**kwargs)
                        self.assertEqual(len(records),before+1)
                        record=records[-1]
                        expected=case['path']
                        for k,v in case['path_params'].items():expected=expected.replace('{'+k+'}',quote(str(v),safe=''))
                        self.assertEqual(record['method'],case['http_method']);self.assertEqual(urlsplit(record['path']).path,expected)
                        self.assertEqual(parse_qs(urlsplit(record['path']).query),{k:[str(v)] for k,v in case['query'].items()})
                        self.assertEqual(json.loads(record['raw']) if record['raw'] else None,case['request'])
                        headers={k.lower():v for k,v in record['headers'].items()}
                        if case['client'] in ['Nfe','NfeFiles','Reseller'] and case['operation']!='fiscalDownloadReport':
                            self.assertEqual(headers['x-consumer-key'], 'synthetic-reseller-key' if case['client']=='Reseller' else 'synthetic-company-key')
                            self.assertNotIn('authorization',headers)
                        elif case['operation']=='fiscalDownloadReport':
                            self.assertNotIn('authorization',headers);self.assertNotIn('x-consumer-key',headers)
                        else:
                            expected_token='synthetic-monitor' if case['client']=='Monitor' else 'synthetic-issuer-files' if case['client']=='EmitterFiles' else 'synthetic-issuer'
                            self.assertEqual(headers['authorization'],'Bearer '+expected_token);self.assertNotIn('x-consumer-key',headers)
                        if case['binary']:self.assertIsInstance(result,FileResponse)
                        else:self.assertEqual(result,case['response'])
            finally:
                for c in pool.values():c.close()
        self.assertEqual(len(records),101)

    def test_public_semantic_corpus(self):
        corpus=json.loads((HERE/'fixtures/semantic_cases.json').read_text())['cases']
        self.assertGreater(len(corpus),150)
        for c in corpus:
            with self.subTest(case=c.get('name',c.get('id'))):
                passed=True
                try:validate(c['module'],{'$ref':'#/components/schemas/'+c['schema']},c['instance'])
                except WebmaniaError:passed=False
                self.assertEqual(passed,c['valid'])

    def test_generated_types_support_runtime_introspection(self):
        checked=0
        for module in DOCUMENTS:
            model=importlib.import_module('webmania.generated.'+module)
            for value in vars(model).values():
                if isinstance(value,type) and hasattr(value,'__required_keys__'):
                    typing.get_type_hints(value,include_extras=True);checked+=1
        self.assertGreater(checked,500)
        for client in [NfeClient,EmitterClient,MonitorClient,ResellerClient,NfeFilesClient,EmitterFilesClient]:
            for record in OPERATIONS.values():
                if record['client']==client._scope:
                    hints=typing.get_type_hints(getattr(client,record['method']))
                    self.assertIn('return',hints)

    def test_ipi_and_payment_identifier_variants_are_preserved_on_wire(self):
        base_request=copy.deepcopy(next(c['request'] for c in CORPUS if c['operation']=='nfeIssueDocument'))
        fields=['cnpj_transacional_pag','cnpj_credenciadora','cnpj_beneficiario']
        with server(lambda h,r:send(h,{'uuid':UUID,'status':'processando'})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                for ipi in ['001',1,'0','999',999]:
                    for value in ['00000000000000',['00000000000000','00.000.000/0000-00']]:
                        request=copy.deepcopy(base_request)
                        request['produtos'][0]['impostos']['ipi']={'situacao_tributaria':'99','codigo_enquadramento':ipi,'aliquota':'0.00'}
                        for field in fields:request['pedido'][field]=value
                        client.issue_document(request)
                        wire=json.loads(records[-1]['raw'])
                        self.assertEqual(wire['produtos'][0]['impostos']['ipi']['codigo_enquadramento'],ipi)
                        for field in fields:self.assertEqual(wire['pedido'][field],value)
                self.assertEqual(len(records),10)
                for invalid in [True,-1,1000,1.5,'','1000','9.9','1e2',' 999 ',{},[],None]:
                    with self.subTest(invalid_ipi=invalid):
                        request=copy.deepcopy(base_request)
                        request['produtos'][0]['impostos']['ipi']={'situacao_tributaria':'99','codigo_enquadramento':invalid,'aliquota':'0.00'}
                        with self.assertRaises(WebmaniaError):client.issue_document(request)
                for field in fields:
                    for invalid in [0,[0],[],'',['invalid'],['123'],['00000000000000',0],None,{},'0'*15]:
                        request=copy.deepcopy(base_request);request['pedido'][field]=invalid
                        with self.assertRaises(WebmaniaError):client.issue_document(request)
                self.assertEqual(len(records),10)

    def test_decimal_text_exact_extensions(self):
        schema=DOCUMENTS['api2_nfcom_issuance']['components']['schemas']['NfcomItemGroup']['properties']['quantidade']
        for value,validity in [('0.0001',True),('1e-4',True),('1e-5',False),('-1',False),('99999999999.9999',True),('100000000000.0000',False),('NaN',False)]:
            with self.subTest(value=value):
                if validity:validate('api2_nfcom_issuance',schema,value)
                else:
                    with self.assertRaises(WebmaniaError):validate('api2_nfcom_issuance',schema,value)

    def test_omission_null_false_zero_extra_and_exact_decimal(self):
        payload={'cnae':None,'informacoes_fisco':'synthetic','future':{'amount':'9007199254740999.9900','flag':False,'number':0,'nullable':None}}
        with server(lambda h,r:send(h,{'success':'Updated','future':payload['future']})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:result=client.update_company(payload)
            self.assertEqual(json.loads(records[0]['raw']),payload);self.assertNotIn('certificado',json.loads(records[0]['raw']))
            self.assertEqual(result['future'],payload['future'])


class TransportTests(unittest.TestCase):
    def assert_error(self,kind,call):
        with self.assertRaises(WebmaniaError) as caught:call()
        self.assertEqual(caught.exception.kind,kind)
        self.assertIsNone(caught.exception.__cause__)
        self.assertIsNone(caught.exception.__context__)
        return caught.exception

    def test_reuses_connection_and_dns_and_tls_deadlines(self):
        with server(lambda h,r:send(h,{'status':'online'})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                client.get_sefaz_status();client.get_sefaz_status()
            self.assertEqual(records[0]['peer_port'],records[1]['peer_port'])
        # The resolver now lives in the owned worker. Inject the same slow
        # resolver there; a parent-thread monkeypatch cannot affect a subprocess.
        real_popen = subprocess.Popen
        def slow_worker(args, **kwargs):
            program = 'import socket,time,runpy; socket.getaddrinfo=lambda *a,**k: (time.sleep(0.3) or []); runpy.run_path(' + repr(args[-1]) + ',run_name="__main__")'
            return real_popen([args[0], '-I', '-c', program], **kwargs)
        with mock.patch('webmania.transport.subprocess.Popen',slow_worker):
            with NfeClient(COMPANY,base_url='https://synthetic.invalid',timeout=0.08) as client:
                start=time.monotonic();self.assert_error('timeout',client.get_sefaz_status);self.assertLess(time.monotonic()-start,0.3)
        # A TLS handshake deadline is controlled without accepting HTTP data.
        listener=socket.socket();listener.bind(('127.0.0.1',0));listener.listen(1)
        finished=threading.Event()
        def accept_stalled_tls():
            conn,_=listener.accept()
            try:finished.wait(1)
            finally:conn.close()
        thread=threading.Thread(target=accept_stalled_tls,daemon=True);thread.start()
        try:
            with NfeClient(COMPANY,base_url='https://127.0.0.1:'+str(listener.getsockname()[1]),timeout=0.1) as client:
                start=time.monotonic();self.assert_error('timeout',client.get_sefaz_status);self.assertLess(time.monotonic()-start,0.4)
        finally:finished.set();listener.close();thread.join(timeout=1)

    def test_http_loopback_is_enforced_after_dns_resolution(self):
        # The resolver and the connection probe run inside the worker process that performs DNS.
        import os, tempfile
        real_popen=subprocess.Popen
        with tempfile.TemporaryDirectory() as directory:
            marker=os.path.join(directory,'connected')
            def public_dns_worker(args,**kwargs):
                program=('import socket,runpy\n'
                         "socket.getaddrinfo=lambda *a,**k: [(socket.AF_INET,socket.SOCK_STREAM,6,'',('203.0.113.1',80))]\n"
                         'def _connect(*a,**k):\n'
                         '    open('+repr(marker)+",'w').close()\n"
                         "    raise OSError('blocked by test')\n"
                         'socket.socket.connect=_connect\n'
                         'socket.socket.connect_ex=_connect\n'
                         'runpy.run_path('+repr(str(args[-1]))+',run_name="__main__")')
                return real_popen([args[0],'-I','-c',program],**kwargs)
            with mock.patch('webmania.transport.subprocess.Popen',public_dns_worker):
                with NfeClient(COMPANY,base_url='http://localhost') as client:self.assert_error('transport',client.get_sefaz_status)
            self.assertFalse(os.path.exists(marker))

    def test_ambiguous_http_headers_are_rejected(self):
        def handler(h,r):
            h.wfile.write(b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: 19\r\nContent-Length: 19\r\n\r\n{"status":"online"}');h.wfile.flush()
        with server(handler) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:self.assert_error('protocol',client.get_sefaz_status)
            self.assertEqual(len(records),1)

    def test_waiting_for_connection_can_be_cancelled(self):
        started=threading.Event()
        def handler(h,r):
            started.set();time.sleep(0.25);send(h,{'status':'online'})
        with server(handler) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                first=threading.Thread(target=client.get_sefaz_status);first.start();self.assertTrue(started.wait(1))
                cancel=threading.Event();timer=threading.Timer(0.04,cancel.set);timer.start()
                self.assert_error('cancelled',lambda:client.get_sefaz_status(options=CallOptions(cancel=cancel)))
                first.join(timeout=1);timer.join();self.assertEqual(len(records),1)

    def test_http_failures_business_schema_and_protocol_no_replay(self):
        state=[200,{'status':'online'},'application/json']
        with server(lambda h,r:send(h,state[1],state[0],state[2])) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                self.assertEqual(client.get_sefaz_status()['status'],'online')
                for status,data,media,kind in [(401,{'error':'Invalid account'},'application/json','http'),(503,{'error':'Upstream busy'},'application/json','http'),(200,{'error':'Rejection 539'},'application/json','business'),(200,{},'application/json','response_schema'),(200,b'{bad','application/json-bad','protocol'),(302,b'','text/html','redirect')]:
                    state[:]=status,data,media;self.assert_error(kind,client.get_sefaz_status)
                self.assertEqual(len(records),7)

    def test_validation_rejects_locally(self):
        with server(lambda h,r:send(h,{})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                for payload in [{'motivo':'short'},{'uuid':UUID,'motivo':'A valid synthetic reason','bad':float('nan')}]:
                    self.assert_error('validation',lambda:client.cancel_document(payload))
                self.assert_error('validation',lambda:client.get_document())
            self.assertEqual(records,[])

    def test_tls_default_rejects_untrusted_and_explicit_ca_accepts(self):
        with server(lambda h,r:send(h,{'status':'online'}),tls=True) as (base,records,ca):
            with NfeClient(COMPANY,base_url=base) as bad:self.assert_error('transport',bad.get_sefaz_status)
            self.assertEqual(records,[])
            with NfeClient(COMPANY,base_url=base,ca_file=ca) as good:self.assertEqual(good.get_sefaz_status()['status'],'online')
        with server(lambda h,r:send(h,{'status':'online'}),tls=True,wrong_hostname=True) as (base,records,ca):
            with NfeClient(COMPANY,base_url=base,ca_file=ca) as bad:self.assert_error('transport',bad.get_sefaz_status)
            self.assertEqual(records,[])

    def test_deadline_slow_headers_and_close_delimited_drip(self):
        def slow_header(h,r):
            h.wfile.write(b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n')
            h.wfile.flush();time.sleep(0.8);h.wfile.write(b'Content-Length: 19\r\n\r\n{"status":"online"}');h.wfile.flush()
        def drip(h,r):
            h.send_response(200);h.send_header('Content-Type','application/json');h.send_header('Connection','close');h.end_headers();h.close_connection=True
            for b in b'{"status":"online"}':h.wfile.write(bytes([b]));h.wfile.flush();time.sleep(0.04)
        for handler in [slow_header,drip]:
            with server(handler) as (base,records,_):
                with NfeClient(COMPANY,base_url=base,timeout=0.15) as client:
                    start=time.monotonic();self.assert_error('timeout',client.get_sefaz_status);self.assertLess(time.monotonic()-start,0.6)
                self.assertEqual(len(records),1)

    def test_cancel_during_body_and_before_network(self):
        cancel=threading.Event()
        def stalled(h,r):
            h.send_response(200);h.send_header('Content-Type','application/json');h.send_header('Content-Length','100');h.end_headers();h.wfile.write(b'{');h.wfile.flush();time.sleep(1)
        with server(stalled) as (base,records,_):
            with NfeClient(COMPANY,base_url=base,timeout=3) as client:
                timer=threading.Timer(0.08,cancel.set);timer.start();start=time.monotonic()
                self.assert_error('cancelled',lambda:client.get_sefaz_status(options=CallOptions(cancel=cancel)))
                self.assertLess(time.monotonic()-start,0.6);timer.join()
                self.assert_error('cancelled',lambda:client.get_sefaz_status(options=CallOptions(cancel=cancel)))
            self.assertEqual(len(records),1)

    def test_bounds_truncation_duplicate_json_and_nonfinite(self):
        state=[b'x'*200, 'text/plain']
        with server(lambda h,r:send(h,state[0],media=state[1])) as (base,records,_):
            with NfeClient(COMPANY,base_url=base,max_response_bytes=100) as client:
                self.assert_error('response_limit',client.get_sefaz_status)
                for data in [b'{"status":"online","status":"offline"}',b'{"x":NaN}']:
                    state[:]=data,'application/json';self.assert_error('protocol',client.get_sefaz_status)
        def truncated(h,r):
            h.send_response(200);h.send_header('Content-Type','application/json');h.send_header('Content-Length','200');h.send_header('Connection','close');h.end_headers();h.wfile.write(b'{"status":"online"}');h.wfile.flush();h.close_connection=True
        with server(truncated) as (base,_,_):
            with NfeClient(COMPANY,base_url=base) as client:self.assert_error('protocol',client.get_sefaz_status)
        with self.assertRaises(WebmaniaError):NfeClient(COMPANY,base_url='http://example.invalid')
        with self.assertRaises(WebmaniaError):NfeClient(COMPANY,timeout=float('inf'))
        with self.assertRaises(WebmaniaError):NfeClient(RESELLER)
        with self.assertRaises(WebmaniaError):ResellerClient(COMPANY)

    def test_mutation_uncertain_reference_redacted_timeout_5xx_business_protocol(self):
        state=[500,{'error':'Synthetic failure'},'application/json']
        payload={'uuid':UUID,'motivo':'Synthetic cancellation reason'}
        with server(lambda h,r:send(h,state[1],state[0],state[2])) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                for status,data,media,kind in [(500,{'error':'Busy'},'application/json','http'),(200,{'error':'Unknown acceptance'},'application/json','business'),(200,b'bad','text/plain','protocol'),(200,{},'application/json','response_schema')]:
                    state[:]=status,data,media;e=self.assert_error(kind,lambda:client.cancel_document(payload))
                    self.assertEqual(e.outcome,'unknown');self.assertEqual(e.request_reference.redacted,{'uuid':'[redacted]'});self.assertEqual(e.request_reference.reveal(),{'uuid':UUID})
                    self.assertNotIn(UUID,str(e.__dict__))
                self.assertEqual(len(records),4)

    def test_uuid_capability_case_equivalence_preserves_path_success_and_token_case(self):
        upper='ABCDEFAB-CDEF-4ABC-8DEF-ABCDEFABCDEF';lower=upper.lower();mixed='aBcDeFaB-cDeF-4aBc-8dEf-aBcDeFaBcDeF'
        state=[True]
        def handler(h,r):
            if state[0]:send(h,{'error':'Report '+lower+' '+mixed,lower:{mixed:lower}},400,headers={'X-Request-ID':mixed})
            else:send(h,ZIP,media='application/zip')
        with server(handler) as (base,records,_):
            with NfeFilesClient(base_url=base,trusted_origins=[base]) as client:
                error=self.assert_error('http',lambda:client.download_report(uuid=upper,auth=FileAuth('capability')))
                for spelling in [upper,lower,mixed]:self.assertNotIn(spelling,str(error.__dict__))
                self.assertEqual(error.correlation_id,'[redacted]');self.assertIn(upper,records[0]['path'])
                state[0]=False;self.assertEqual(client.download_report(uuid=upper,auth=FileAuth('capability')).data,ZIP)
        # Arbitrary credentials/passwords are not made case-insensitive, even
        # when their literal bytes happen to look like a UUID.
        r=Redactor(secrets=[upper,'ArbitraryToken'],request={'password':upper})
        self.assertEqual(r.clean({'message':lower+' arbitrarytoken'})['message'],lower+' arbitrarytoken')
        with server(lambda h,r:send(h,{'uuid':lower,'status':'processando'})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                self.assertEqual(client.query_document({'uuid':upper})['uuid'],lower)
                self.assertEqual(json.loads(records[0]['raw'])['uuid'],upper)

    def test_redaction_numeric_equivalence_and_query_values(self):
        for original, echo in [('9007199254740993',9007199254740992),('000123',123),('1e3',1000)]:
            r=Redactor(request={'private_number':original})
            cleaned=r.clean({'echo':echo,str(echo):str(echo),'message':'value '+str(echo)})
            self.assertNotIn(str(echo),json.dumps(cleaned));self.assertEqual(cleaned['echo'],'[redacted]')
        with server(lambda h,r:send(h,{'error':'Failed lookup '+UUID,'uuid':UUID},400,headers={'X-Request-ID':UUID})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                error=self.assert_error('http',lambda:client.get_document(query={'uuid':UUID}))
                self.assertNotIn(UUID,str(error.__dict__));self.assertEqual(error.correlation_id,'[redacted]')

    def test_redaction_generic_echo_keys_numbers_unicode_urls_and_correlation(self):
        payload={'informacoes_fisco':'Café fiscal privado','certificado_senha':'synthetic-password','certificado':'Zml4dHVyZQ==','future':{'zero':0,'value':12345,'nullable':None}}
        secret='synthetic-company-secret'
        response={'error':'Rejection 539: '+payload['informacoes_fisco']+' '+secret,'code':'539','detail':{'12345':12345,'Café fiscal privado':'Cafe\u0301 fiscal privado'},'url':'https://example.invalid/capability?token=private','token':'unknown-private-token','safe':'Use a valid CFOP'}
        with server(lambda h,r:send(h,response,400,headers={'X-Request-ID':quote(payload['informacoes_fisco'])})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:e=self.assert_error('http',lambda:client.update_company(payload))
            diagnostic=json.dumps(e.__dict__,ensure_ascii=False)+repr(e)+str(e)+repr(e.args)
            for private in [secret,payload['informacoes_fisco'],'Cafe\u0301 fiscal privado','12345','unknown-private-token','example.invalid']:self.assertNotIn(private,diagnostic)
            self.assertEqual(e.response['code'],'539');self.assertEqual(e.response['safe'],'Use a valid CFOP');self.assertIn('[redacted]',e.correlation_id)
        r=Redactor(['secret','redacted'],{'x':'e\u0301'})
        clean=r.clean({'secret':1,'redacted':2,'message':'é secret https://example.invalid/secret'})
        self.assertEqual(len(clean),3);self.assertNotIn('secret',json.dumps(clean))


class FileTests(unittest.TestCase):
    assert_error = TransportTests.assert_error
    def test_explicit_auth_modes_no_fallback_and_mixed_url_rejected(self):
        with server(lambda h,r:send(h,XML,media='text/xml')) as (base,records,_):
            with EmitterFilesClient(base_url=base,trusted_origins=[base],issuer_token='synthetic-file-issuer') as client:
                client.get_nfse_xml(identifier=UUID,auth=FileAuth('issuer'))
                client.get_nfse_xml(identifier=UUID,auth=FileAuth('document_token','synthetic-document-token'))
                client.get_nfse_xml(identifier=UUID,auth=FileAuth('anonymous'))
                self.assertEqual(records[0]['headers']['Authorization'],'Bearer synthetic-file-issuer')
                for r in records[1:]:self.assertNotIn('Authorization',r['headers'])
                self.assertEqual(parse_qs(urlsplit(records[1]['path']).query),{'token':['synthetic-document-token']})
                self.assert_error('capability',lambda:client.get_mdfe_xml(identifier=UUID,auth=FileAuth('anonymous')))
                self.assert_error('validation',lambda:client.download_url(base+'/xmlnfse/'+UUID+'?token=synthetic-document-token',auth=FileAuth('issuer')))
                self.assert_error('validation',lambda:client.download_url('https://other.invalid/xmlnfse/'+UUID,auth=FileAuth('issuer')))
                self.assertEqual(len(records),3)
        with self.assertRaises(WebmaniaError):EmitterFilesClient(trusted_origins=[])
        with server(lambda h,r:send(h,{'error':'Denied'},401)) as (base,records,_):
            with EmitterFilesClient(base_url=base,trusted_origins=[base],issuer_token='synthetic-file-issuer') as client:
                self.assert_error('http',lambda:client.get_nfse_xml(identifier=UUID,auth=FileAuth('issuer')))
            self.assertEqual(len(records),1)

    def test_api2_xml_zip_and_pdf_encryption_are_distinct_failures(self):
        state=[ZIP,'application/zip']
        with server(lambda h,r:send(h,state[0],media=state[1])) as (base,records,_):
            with EmitterFilesClient(base_url=base,trusted_origins=[base],issuer_token='synthetic-file-issuer') as client:
                self.assert_error('protected_file',lambda:client.get_nfse_xml(identifier=UUID,auth=FileAuth('issuer')))
                state[:]=b'%PDF-1.4\ntrailer << /Encrypt 5 0 R >>\n%%EOF','application/pdf'
                self.assert_error('protected_file',lambda:client.get_nfse_pdf(identifier=UUID,auth=FileAuth('issuer')))
                state[:]=b'<!DOCTYPE html><html>synthetic</html>','application/pdf'
                self.assert_error('protocol',lambda:client.get_nfse_pdf(identifier=UUID,auth=FileAuth('issuer')))
                self.assertEqual(len(records),3)

    def test_binary_preservation_limits_capability_gate_and_protection(self):
        state=[XML,'text/xml']
        with server(lambda h,r:send(h,state[0],media=state[1],headers={'Content-Disposition':'attachment; filename="synthetic.xml"'})) as (base,records,_):
            with NfeFilesClient(base_url=base,trusted_origins=[base],credentials=COMPANY) as client:
                result=client.download_xml(identifier=UUID,auth=FileAuth('company'))
                self.assertEqual(result.data,XML);self.assertEqual(result.protection,'not_established');self.assertIn('synthetic.xml',result.content_disposition)
                self.assert_error('capability',lambda:client.download_ibs_cbs_event_xml(uuid=UUID,auth=FileAuth('company')))
                self.assertEqual(len(records),1)
                state[:]=ZIP,'text/xml';self.assert_error('protected_file',lambda:client.download_xml(identifier=UUID,auth=FileAuth('company')))
                state[:]=b'<html>untrusted</html>','text/xml';self.assert_error('protocol',lambda:client.download_xml(identifier=UUID,auth=FileAuth('company')))
                state[:]=PDF,'application/pdf';self.assertEqual(client.download_danfe(identifier=UUID,auth=FileAuth('company')).data,PDF)
                self.assert_error('response_limit',lambda:client.download_danfe(identifier=UUID,auth=FileAuth('company'),options=CallOptions(max_response_bytes=10)))
                state[:]=ZIP,'application/zip';client.download_report(uuid=UUID,auth=FileAuth('capability'))
                self.assertNotIn('X-Consumer-Key',records[-1]['headers'])


class PdfInspectionTests(unittest.TestCase):
    def test_encryption_entries_strings_streams_and_xref(self):
        from webmania.pdf_inspection import encryption_entry
        for data, expected in [
            (b'%PDF-1.4\ntrailer << /Encrypt 5 0 R >>\n%%EOF', True),
            (b'%PDF-1.5\n1 0 obj << /Type /XRef /Encrypt 5 0 R >> endobj\n%%EOF', True),
            (b'%PDF-1.4\ntrailer << /Encr#79pt 5 0 R >>\n%%EOF', True),
            (b'%PDF-1.4\n1 0 obj << /Text (trailer << /Encrypt 5 0 R >>) >> endobj\n%%EOF', False),
            (b'%PDF-1.4\n% trailer << /Encrypt 5 0 R >>\ntrailer << /Root 1 0 R >>\n%%EOF', False),
            (b'%PDF-1.4\n1 0 obj << /Length 28 >>\nstream\ntrailer << /Encrypt 5 0 R >>\nendstream\nendobj\n%%EOF', False),
            (b'%PDF-1.4\n1 0 obj << /Length 2 0 R >>\nstream\ntrailer << /Encrypt 5 0 R >>\nendstream\n%%EOF', False),
        ]:
            with self.subTest(data=data):self.assertEqual(encryption_entry(data),expected)


class PollingTests(unittest.TestCase):
    def test_pages_advance_and_bound(self):
        def handler(h,r):
            page=int(parse_qs(urlsplit(r['path']).query).get('page',['1'])[0])
            send(h,{'data':[],'meta':{'current_page':page,'last_page':2,'per_page':10,'total':0}})
        with server(handler) as (base,records,_):
            with MonitorClient('synthetic-monitor',base_url=base) as client:
                self.assertEqual(list(client.iter_companies({'per_page':10})),[]);self.assertEqual(len(records),2)
                with self.assertRaises(WebmaniaError) as e:list(client.iter_companies(max_pages=1))
                self.assertEqual(e.exception.kind,'pagination')

    def test_pending_capability_is_redacted_in_later_poll_errors(self):
        calls=[0]
        capability='ABCDEFAB-CDEF-4ABC-8DEF-ABCDEFABCDEF'
        def handler(h,r):
            calls[0]+=1
            send(h,{'uuid':capability,'status':'processando'} if calls[0]==1 else {'error':'Failed report '+capability.lower(),'uuid':capability.lower()},200 if calls[0]==1 else 500,headers={'X-Request-ID':capability.lower()})
        with server(handler) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client, mock.patch('webmania.client.time.sleep',return_value=None):
                req={'modelo':'nfe','relatorio':'xml','status':'emitidas','data_inicio':'2026-10-01','data_final':'2026-10-25'}
                with self.assertRaises(WebmaniaError) as caught:client.wait_report(req,max_attempts=2)
                self.assertNotIn(capability,str(caught.exception.__dict__));self.assertNotIn(capability.lower(),str(caught.exception.__dict__))
                self.assertEqual(caught.exception.correlation_id,'[redacted]')
                self.assertEqual(len(records),2)

    def test_report_polling_complete_pending_bounds_and_cancel(self):
        state=['concluido']
        with server(lambda h,r:send(h,{'uuid':UUID,'status':state[0],'url':'https://example.invalid/capability'})) as (base,records,_):
            with NfeClient(COMPANY,base_url=base) as client:
                req={'modelo':'nfe','relatorio':'xml','status':'emitidas','data_inicio':'2026-10-01','data_final':'2026-10-25'}
                self.assertEqual(client.wait_report(req)['status'],'concluido')
                state[0]='processando'
                with self.assertRaises(WebmaniaError) as e:client.wait_report(req,max_attempts=1)
                self.assertEqual(e.exception.kind,'polling_timeout')
                cancel=threading.Event();timer=threading.Timer(0.08,cancel.set);timer.start()
                with self.assertRaises(WebmaniaError) as e:client.wait_report(req,options=CallOptions(cancel=cancel))
                self.assertEqual(e.exception.kind,'cancelled');timer.join()
                with self.assertRaises(WebmaniaError):client.wait_report(req,interval=0.1)
                self.assertEqual(len(records),3)


if __name__=='__main__':unittest.main()
