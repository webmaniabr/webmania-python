"""The neutral homologation example against a loopback fixture: masked lines, ledger, no replay."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from support import PDF, XML, server, send
from test_sdk import CORPUS

CASE = {c['operation']: c for c in CORPUS}

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / 'examples' / 'homologacao' / 'run.sh'
NFE = '00000000-0000-4000-8000-0000000000a1'
NFSE = '00000000-0000-4000-8000-0000000000b2'
SECRETS = {'WEBMANIA_CONSUMER_KEY': 'example-key-value', 'WEBMANIA_CONSUMER_SECRET': 'example-secret-value',
           'WEBMANIA_ACCESS_TOKEN': 'example-access-value', 'WEBMANIA_ACCESS_TOKEN_SECRET': 'example-access-secret-value',
           'WEBMANIA_ISSUER_TOKEN': 'example-issuer-value'}


def environment(**extra):
    env = {k: v for k, v in os.environ.items() if not k.startswith('WEBMANIA_')}
    env['PATH'] = os.path.dirname(sys.executable) + os.pathsep + env.get('PATH', '')
    env.update(extra)
    return env


class HomologationExampleTests(unittest.TestCase):
    def test_without_opt_in_the_example_is_blocked_before_any_request(self):
        result = subprocess.run(['sh', str(RUN)], env=environment(**SECRETS), capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 77)
        self.assertEqual(json.loads(result.stdout), {'result': 'blocked'})

    def test_full_cycle_prints_masked_steps_and_records_the_ledger(self):
        state = {'nfe': 'aprovado', 'nfse': 'aprovado'}
        def handler(h, record):
            path, method = record['path'].split('?', 1)[0], record['method']
            if path == '/1/nfe/sefaz/': send(h, {'status': 'online'})
            elif path == '/1/nfe/certificado/': send(h, {'expiration': 30})
            elif path == '/1/nfe/classe-imposto/': send(h, [])
            elif path == '/2/nfse/status': send(h, CASE['emitterGetNfseProviderStatus']['response'])
            elif path == '/1/nfe/emissao/': send(h, {'uuid': NFE, 'status': 'processando'})
            elif path == '/1/nfe/consulta/': send(h, {'uuid': NFE, 'status': state['nfe']})
            elif path == '/1/nfe/cancelar/': state.update(nfe='cancelado'); send(h, {'status': 'cancelado'})
            elif path.startswith('/danfe/'): send(h, PDF, media='application/pdf')
            elif path.startswith('/xmlnfe/'): send(h, XML, media='application/xml')
            elif path == '/2/nfse/emissao': send(h, dict(CASE['emitterIssueNfse']['response'], uuid=NFSE, status='processando'))
            elif path == '/2/nfse/consulta/' + NFSE:
                send(h, dict(CASE['emitterGetNfse']['response'], uuid=NFSE, status=state['nfse'], pdf_nfse='ok'))
            elif path == '/2/nfse/cancelar':
                state.update(nfse='cancelado'); send(h, dict(CASE['emitterCancelNfse']['response'], uuid=NFSE, status='cancelado'))
            elif path == '/xmlnfse/' + NFSE: send(h, b'<?xml version="1.0"?><CompNfse/>', media='text/xml')
            elif path == '/nfse/' + NFSE: send(h, PDF, media='application/pdf')
            else: send(h, {'error': 'unexpected ' + method}, status=404)
        with server(handler) as (base, records, _), tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / 'nfe.json').write_text(json.dumps(dict(CASE['nfeIssueDocument']['request'], ambiente=2)))
            (folder / 'nfse.json').write_text(json.dumps(dict(CASE['emitterIssueNfse']['request'], ambiente=2)))
            ledger = folder / 'ledger.jsonl'
            env = environment(WEBMANIA_LIVE='1', WEBMANIA_LIVE_SCOPE='all', WEBMANIA_API1_BASE_URL=base,
                              WEBMANIA_FILES_BASE_URL=base, WEBMANIA_API2_BASE_URL=base,
                              WEBMANIA_LIVE_ALLOWED_HOSTS='127.0.0.1', WEBMANIA_LIVE_LEDGER=str(ledger),
                              WEBMANIA_LIVE_NFE_PAYLOAD=str(folder / 'nfe.json'),
                              WEBMANIA_LIVE_NFSE_PAYLOAD=str(folder / 'nfse.json'), **SECRETS)
            result = subprocess.run(['sh', str(RUN)], env=env, capture_output=True, text=True, timeout=120)
            lines = [json.loads(line) for line in result.stdout.splitlines()]
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(all(line['ok'] for line in lines))
            self.assertEqual([line['step'] for line in lines][:4],
                             ['readonly.sefaz', 'readonly.certificate', 'readonly.tax_classes', 'readonly.nfse_provider'])
            for step in ['nfe.issue', 'nfe.cancel', 'nfe.cancellation_xml', 'nfse.issue', 'nfse.cancel', 'nfse.pdf']:
                self.assertIn(step, [line['step'] for line in lines])
            for value in [*SECRETS.values(), NFE, NFSE, base]:
                self.assertNotIn(value, result.stdout + result.stderr)
            entries = [json.loads(line) for line in ledger.read_text().splitlines()]
            self.assertEqual({(e['model'], e['identifier']) for e in entries}, {('nfe', NFE), ('nfse', NFSE)})
            self.assertEqual([e['status'] for e in entries if e['operation'] in ['nfeCancelDocument', 'emitterCancelNfse']],
                             ['cancelado', 'cancelado'])
            issued = [r for r in records if r['method'] == 'POST' and r['path'] in ['/1/nfe/emissao/', '/2/nfse/emissao']]
            self.assertEqual(len(issued), 2)

    def test_unknown_cancellation_is_recorded_and_never_repeated(self):
        def handler(h, record):
            path = record['path'].split('?', 1)[0]
            if path == '/1/nfe/sefaz/': send(h, {'status': 'online'})
            elif path == '/1/nfe/certificado/': send(h, {'expiration': 30})
            elif path == '/1/nfe/classe-imposto/': send(h, [])
            elif path == '/2/nfse/status': send(h, CASE['emitterGetNfseProviderStatus']['response'])
            elif path == '/1/nfe/emissao/': send(h, {'uuid': NFE, 'status': 'processando'})
            elif path == '/1/nfe/consulta/': send(h, {'uuid': NFE, 'status': 'aprovado'})
            elif path == '/1/nfe/cancelar/': send(h, {'error': 'indisponivel'}, status=503)
            elif path.startswith('/danfe/'): send(h, PDF, media='application/pdf')
            elif path.startswith('/xmlnfe/'): send(h, XML, media='application/xml')
            else: send(h, {'error': 'unexpected'}, status=404)
        with server(handler) as (base, records, _), tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / 'nfe.json').write_text(json.dumps(dict(CASE['nfeIssueDocument']['request'], ambiente=2)))
            ledger = folder / 'ledger.jsonl'
            env = environment(WEBMANIA_LIVE='1', WEBMANIA_LIVE_SCOPE='nfe', WEBMANIA_API1_BASE_URL=base,
                              WEBMANIA_FILES_BASE_URL=base, WEBMANIA_API2_BASE_URL=base,
                              WEBMANIA_LIVE_ALLOWED_HOSTS='127.0.0.1', WEBMANIA_LIVE_LEDGER=str(ledger),
                              WEBMANIA_LIVE_NFE_PAYLOAD=str(folder / 'nfe.json'), **SECRETS)
            result = subprocess.run(['sh', str(RUN)], env=env, capture_output=True, text=True, timeout=120)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            entries = [json.loads(line) for line in ledger.read_text().splitlines()]
            self.assertIn({'model': 'nfe', 'identifier': NFE, 'status': 'unknown', 'operation': 'nfeCancelDocument'}, entries)
            cancels = [r for r in records if r['method'] == 'PUT' and r['path'].split('?', 1)[0] == '/1/nfe/cancelar/']
            self.assertEqual(len(cancels), 1)

    def test_without_allowed_hosts_the_example_is_blocked_before_any_request(self):
        with server(lambda h, record: send(h, {}, status=500)) as (base, records, _):
            for hosts in [None, ' , ']:
                extra = {} if hosts is None else {'WEBMANIA_LIVE_ALLOWED_HOSTS': hosts}
                env = environment(WEBMANIA_LIVE='1', WEBMANIA_API1_BASE_URL=base, WEBMANIA_FILES_BASE_URL=base,
                                  WEBMANIA_API2_BASE_URL=base, **extra, **SECRETS)
                result = subprocess.run(['sh', str(RUN)], env=env, capture_output=True, text=True, timeout=60)
                self.assertEqual(result.returncode, 77, result.stdout + result.stderr)
                self.assertEqual(json.loads(result.stdout), {'result': 'blocked', 'reason': 'allowed_hosts'})
            self.assertEqual(records, [])

    def test_post_cancel_consult_succeeds_only_with_status_cancelado(self):
        # The fixture accepts each cancellation, but the documents never show 'cancelado'.
        def handler(h, record):
            path = record['path'].split('?', 1)[0]
            if path == '/1/nfe/sefaz/': send(h, {'status': 'online'})
            elif path == '/1/nfe/certificado/': send(h, {'expiration': 30})
            elif path == '/1/nfe/classe-imposto/': send(h, [])
            elif path == '/2/nfse/status': send(h, CASE['emitterGetNfseProviderStatus']['response'])
            elif path == '/1/nfe/emissao/': send(h, {'uuid': NFE, 'status': 'processando'})
            elif path == '/1/nfe/consulta/': send(h, {'uuid': NFE, 'status': 'aprovado'})
            elif path == '/1/nfe/cancelar/': send(h, {'status': 'cancelado'})
            elif path.startswith('/danfe/'): send(h, PDF, media='application/pdf')
            elif path.startswith('/xmlnfe/'): send(h, XML, media='application/xml')
            elif path == '/2/nfse/emissao': send(h, dict(CASE['emitterIssueNfse']['response'], uuid=NFSE, status='processando'))
            elif path == '/2/nfse/consulta/' + NFSE:
                send(h, dict(CASE['emitterGetNfse']['response'], uuid=NFSE, status='aprovado', pdf_nfse='ok'))
            elif path == '/2/nfse/cancelar': send(h, dict(CASE['emitterCancelNfse']['response'], uuid=NFSE, status='cancelado'))
            elif path == '/xmlnfse/' + NFSE: send(h, b'<?xml version="1.0"?><CompNfse/>', media='text/xml')
            elif path == '/nfse/' + NFSE: send(h, PDF, media='application/pdf')
            else: send(h, {'error': 'unexpected'}, status=404)
        with server(handler) as (base, records, _), tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / 'nfe.json').write_text(json.dumps(dict(CASE['nfeIssueDocument']['request'], ambiente=2)))
            (folder / 'nfse.json').write_text(json.dumps(dict(CASE['emitterIssueNfse']['request'], ambiente=2)))
            ledger = folder / 'ledger.jsonl'
            env = environment(WEBMANIA_LIVE='1', WEBMANIA_LIVE_SCOPE='all', WEBMANIA_API1_BASE_URL=base,
                              WEBMANIA_FILES_BASE_URL=base, WEBMANIA_API2_BASE_URL=base,
                              WEBMANIA_LIVE_ALLOWED_HOSTS='127.0.0.1', WEBMANIA_LIVE_LEDGER=str(ledger),
                              WEBMANIA_LIVE_NFE_PAYLOAD=str(folder / 'nfe.json'),
                              WEBMANIA_LIVE_NFSE_PAYLOAD=str(folder / 'nfse.json'),
                              PYTHONPATH=str(ROOT / 'src'), PYTHONDONTWRITEBYTECODE='1', **SECRETS)
            # Same example, with the wait between consults skipped so every attempt runs at once.
            script = ROOT / 'examples' / 'homologacao' / 'main.py'
            fast = 'import runpy, sys, time; time.sleep = lambda seconds: None; runpy.run_path(sys.argv[1], run_name="__main__")'
            result = subprocess.run([sys.executable, '-c', fast, str(script)], env=env, capture_output=True, text=True, timeout=120)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            lines = [json.loads(line) for line in result.stdout.splitlines()]
            for model, operation in [('nfe', 'nfeGetDocument'), ('nfse', 'emitterGetNfse')]:
                verdict = [line for line in lines if line['step'] == model + '.consult_cancelled' and not line['ok']]
                self.assertEqual(len(verdict), 1, result.stdout)
                self.assertEqual((verdict[0]['operation'], verdict[0]['kind']), (operation, 'not_cancelled'))
            self.assertNotIn('nfe.cancellation_xml', [line['step'] for line in lines])
            cancels = [r['path'].split('?', 1)[0] for r in records if r['path'].split('?', 1)[0] in ['/1/nfe/cancelar/', '/2/nfse/cancelar']]
            self.assertEqual(sorted(cancels), ['/1/nfe/cancelar/', '/2/nfse/cancelar'])
            entries = [json.loads(line) for line in ledger.read_text().splitlines()]
            self.assertEqual([e['status'] for e in entries if e['operation'] in ['nfeCancelDocument', 'emitterCancelNfse']],
                             ['aprovado', 'aprovado'])

    def test_mutation_scope_without_a_writable_ledger_is_blocked_before_any_request(self):
        with server(lambda h, record: send(h, {}, status=500)) as (base, records, _), tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            (folder / 'nfe.json').write_text(json.dumps(dict(CASE['nfeIssueDocument']['request'], ambiente=2)))
            for ledger in [None, str(folder)]:
                extra = {} if ledger is None else {'WEBMANIA_LIVE_LEDGER': ledger}
                env = environment(WEBMANIA_LIVE='1', WEBMANIA_LIVE_SCOPE='nfe', WEBMANIA_API1_BASE_URL=base,
                                  WEBMANIA_FILES_BASE_URL=base, WEBMANIA_API2_BASE_URL=base,
                                  WEBMANIA_LIVE_ALLOWED_HOSTS='127.0.0.1', WEBMANIA_LIVE_NFE_PAYLOAD=str(folder / 'nfe.json'),
                                  **extra, **SECRETS)
                result = subprocess.run(['sh', str(RUN)], env=env, capture_output=True, text=True, timeout=60)
                self.assertEqual(result.returncode, 77, result.stdout + result.stderr)
                self.assertEqual(json.loads(result.stdout), {'result': 'blocked', 'reason': 'ledger'})
            self.assertEqual(records, [])

    def test_origin_outside_the_allowed_hosts_is_blocked(self):
        env = environment(WEBMANIA_LIVE='1', WEBMANIA_API1_BASE_URL='https://other.example.invalid/api',
                          WEBMANIA_LIVE_ALLOWED_HOSTS='127.0.0.1', **SECRETS)
        result = subprocess.run(['sh', str(RUN)], env=env, capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 77)
        self.assertEqual(json.loads(result.stdout)['reason'], 'origin_not_allowed')


if __name__ == '__main__': unittest.main(verbosity=2)
