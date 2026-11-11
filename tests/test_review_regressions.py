"""Decisive regressions from independent review, using loopback only."""
import copy
from datetime import date
import importlib
import json
import typing
import threading
import time
import unittest
from urllib.parse import parse_qs, quote, urlsplit

from webmania import (CallOptions, CompanyCredentials, EmitterFilesClient, FileAuth,
                      MonitorClient, MutationReference, NfeClient, NfeFilesClient,
                      WebmaniaError)
from webmania.validation import DOCUMENTS
from support import HERE, UUID, XML, server, send
from test_sdk import COMPANY, CORPUS


def typed_variants(value):
    if hasattr(value, '__required_keys__'):
        return [value]
    return [variant for arg in typing.get_args(value) for variant in typed_variants(arg)]


class ReviewTransportTests(unittest.TestCase):
    def test_complete_content_length_close_http10_http11_and_tls(self):
        for version, tls in [('HTTP/1.0', False), ('HTTP/1.1', False), ('HTTP/1.1', True)]:
            with self.subTest(version=version, tls=tls):
                def handler(h, r):
                    h.protocol_version = version
                    send(h, {'status': 'online'}, headers={'Connection': 'close'})
                    h.close_connection = True
                with server(handler, tls=tls) as (base, records, ca):
                    with NfeClient(COMPANY, base_url=base, ca_file=ca) as client:
                        self.assertEqual(client.get_sefaz_status()['status'], 'online')
                        self.assertEqual(client.get_sefaz_status()['status'], 'online')
                    self.assertEqual(len(records), 2)
                    self.assertNotEqual(records[0]['peer_port'], records[1]['peer_port'])

    def test_error_presence_is_failure_even_when_value_is_empty(self):
        selected = [None]
        with server(lambda h, r: send(h, {'status': 'online', **selected[0]})) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                for value in [False, None, '', [], {}]:
                    selected[0] = {'error': value}
                    with self.assertRaises(WebmaniaError) as caught:
                        client.get_sefaz_status()
                    self.assertEqual(caught.exception.kind, 'business')
                for control in [{}, {'erro': None}, {'errors': []}]:
                    selected[0] = control
                    self.assertEqual(client.get_sefaz_status()['status'], 'online')
            self.assertEqual(len(records), 8)

    def test_mutation_reference_can_explicitly_query_the_prior_attempt(self):
        original = 'abcdefab-cdef-4abc-8def-abcdefabcdef'
        request = {'uuid': original, 'motivo': 'Synthetic cancellation review reason.'}
        def handler(h, record):
            if record['method'] == 'PUT':
                request['uuid'] = 'changed-after-serialization'
                send(h, {'error': 'Synthetic upstream failure'}, 503)
            else:
                send(h, {'uuid': original, 'status': 'processando'})
        with server(handler) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.cancel_document(request)
                error = caught.exception
                self.assertEqual(error.outcome, 'unknown')
                self.assertIsInstance(error.request_reference, MutationReference)
                self.assertNotIn(original, str(error.__dict__) + json.dumps(error.to_dict()))
                recovered = error.request_reference.reveal()
                self.assertEqual(recovered, {'uuid': original})
                recovered['uuid'] = 'local-copy-change'
                self.assertEqual(error.request_reference.reveal(), {'uuid': original})
                self.assertEqual(client.get_document(query=error.request_reference.reveal())['uuid'], original)
            self.assertEqual([r['method'] for r in records], ['PUT', 'GET'])
            self.assertEqual(parse_qs(urlsplit(records[1]['path']).query), {'uuid': [original]})

    def test_mutation_timeout_and_cancel_keep_the_actual_recovery_selector(self):
        for mode in ['timeout', 'cancelled']:
            with self.subTest(mode=mode):
                def handler(h, record):
                    if record['method'] == 'PUT':
                        time.sleep(0.25)
                        send(h, {'uuid': UUID, 'status': 'cancelado'})
                    else: send(h, {'uuid': UUID, 'status': 'processando'})
                with server(handler) as (base, records, _):
                    with NfeClient(COMPANY, base_url=base) as client:
                        event = threading.Event()
                        timer = threading.Timer(0.04, event.set) if mode == 'cancelled' else None
                        if timer: timer.start()
                        options = CallOptions(timeout=0.08) if mode == 'timeout' else CallOptions(timeout=1, cancel=event)
                        with self.assertRaises(WebmaniaError) as caught:
                            client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'}, options=options)
                        error = caught.exception
                        self.assertEqual(error.kind, mode)
                        self.assertEqual(error.outcome, 'unknown')
                        self.assertEqual(error.request_reference.reveal(), {'uuid': UUID})
                        self.assertNotIn(UUID, json.dumps(error.to_dict()))
                        client.get_document(query=error.request_reference.reveal())
                        if timer: timer.join()
                    self.assertEqual([r['method'] for r in records], ['PUT', 'GET'])

    def test_recovery_reference_excludes_credentials_sensitive_fields_and_capabilities(self):
        credentials = CompanyCredentials(UUID, 'synthetic-secret', 'synthetic-access', 'synthetic-access-secret')
        with server(lambda h, r: send(h, {'error': 'Synthetic failure'}, 503)) as (base, records, _):
            with NfeClient(credentials, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'})
                self.assertIsNone(caught.exception.request_reference)
                self.assertNotIn(UUID, json.dumps(caught.exception.to_dict()))
            with NfeClient(COMPANY, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.update_company({'uuid': UUID, 'certificado': 'Zml4dHVyZQ==', 'certificado_senha': UUID})
                self.assertIsNone(caught.exception.request_reference)
                with self.assertRaises(WebmaniaError) as caught:
                    client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'},
                                           options=CallOptions(_known_capabilities=(UUID,), _known_uuid_capabilities=(UUID,)))
                self.assertIsNone(caught.exception.request_reference)
            marker_credentials = CompanyCredentials('[redacted]', 'synthetic-secret', 'synthetic-access', 'synthetic-access-secret')
            with NfeClient(marker_credentials, base_url=base) as client:
                issue = copy.deepcopy(next(c['request'] for c in CORPUS if c['operation'] == 'nfeIssueDocument'))
                issue['ID'] = '[redacted]'
                with self.assertRaises(WebmaniaError) as caught: client.issue_document(issue)
                self.assertIsNone(caught.exception.request_reference)
            with EmitterFilesClient(base_url=base, trusted_origins=[base], issuer_token='synthetic-issuer') as files:
                with self.assertRaises(WebmaniaError) as caught:
                    files.get_nfse_xml(identifier=UUID, auth=FileAuth('issuer'))
                self.assertEqual(caught.exception.request_reference.reveal(), {'identifier': UUID})
                self.assertNotIn(UUID, json.dumps(caught.exception.to_dict()))
                with self.assertRaises(WebmaniaError) as caught:
                    files.get_nfse_xml(identifier=UUID, auth=FileAuth('anonymous'))
                self.assertIsNone(caught.exception.request_reference)
            self.assertEqual(len(records), 6)

    def test_monitor_path_selectors_are_recoverable_without_becoming_capabilities(self):
        for operation_id, query_id, parameter in [('monitorUpdateCompany', 'monitorGetCompany', 'company'),
                                                   ('monitorManifestDocument', 'monitorGetDocument', 'fd')]:
            case = copy.deepcopy(next(c for c in CORPUS if c['operation'] == operation_id))
            query = copy.deepcopy(next(c for c in CORPUS if c['operation'] == query_id))
            selector = case['path_params'][parameter]
            def handler(h, record):
                send(h, query['response'] if record['method'] == 'GET' else {'error': 'Synthetic failure'},
                     200 if record['method'] == 'GET' else 503)
            with server(handler) as (base, records, _):
                with MonitorClient('synthetic-monitor', base_url=base) as client:
                    with self.assertRaises(WebmaniaError) as caught:
                        getattr(client, case['method'])(case['request'], **case['path_params'])
                    error = caught.exception
                    self.assertEqual(error.outcome, 'unknown')
                    self.assertEqual(error.request_reference.reveal(), {parameter: selector})
                    self.assertNotIn(selector, json.dumps(error.to_dict()))
                    getattr(client, query['method'])(**error.request_reference.reveal())
                self.assertEqual(len(records), 2)
                self.assertIn(selector, records[1]['path'])

    def test_statistics_uses_provider_calendar_and_keeps_structural_pair_validation(self):
        result = copy.deepcopy(next(c['response'] for c in CORPUS if c['operation'] == 'monitorGetDownloadStatistics'))
        # A month after the local clock: the SDK must not apply its own calendar.
        year = date.today().year + 1
        with server(lambda h, r: send(h, result)) as (base, records, _):
            with MonitorClient('synthetic-monitor', base_url=base) as client:
                self.assertEqual(client.get_download_statistics(query={'ano': year, 'mes': 10}), result)
                for query in [{'ano': year}, {'mes': 10}, {'ano': year, 'mes': 0}, {'ano': year, 'mes': 13}]:
                    with self.assertRaises(WebmaniaError): client.get_download_statistics(query=query)
            self.assertEqual(len(records), 1)
            self.assertEqual(parse_qs(urlsplit(records[0]['path']).query), {'ano': [str(year)], 'mes': ['10']})


class ReviewSerializationTests(unittest.TestCase):
    def test_all_declared_root_fields_and_required_keys_survive_composition(self):
        audited = 0
        composed = 0
        for module, document in DOCUMENTS.items():
            models = importlib.import_module('webmania.generated.' + module)
            for name, schema in document['components']['schemas'].items():
                if not schema.get('properties'): continue
                variants = typed_variants(getattr(models, name))
                self.assertTrue(variants, (module, name))
                for variant in variants:
                    fields = typing.get_type_hints(variant, include_extras=True)
                    self.assertFalse(set(schema['properties']) - fields.keys(), (module, name, variant))
                    self.assertFalse(set(schema.get('required', [])) - variant.__required_keys__, (module, name, variant))
                audited += 1
                if 'anyOf' in schema or 'oneOf' in schema: composed += 1
        self.assertGreater(audited, 400)
        self.assertGreaterEqual(composed, 23)

    def test_download_url_normalizes_only_the_supported_canonical_hint(self):
        token = 'synthetic+document-token'
        with server(lambda h, r: send(h, XML, media='text/xml')) as (base, records, _):
            with NfeFilesClient(base_url=base, trusted_origins=[base], credentials=COMPANY) as client:
                for query, auth in [('download=1', FileAuth('company')),
                                    ('download=1&token=' + quote(token, safe=''), FileAuth('document_token', token))]:
                    self.assertEqual(client.download_url(base + '/xmlnfe/' + UUID + '/?' + query, auth=auth).data, XML)
                self.assertEqual(parse_qs(urlsplit(records[0]['path']).query), {'download': ['1']})
                self.assertEqual(parse_qs(urlsplit(records[1]['path']).query), {'download': ['1'], 'token': [token]})
                self.assertIn('X-Consumer-Key', records[0]['headers'])
                self.assertNotIn('X-Consumer-Key', records[1]['headers'])
                for query in ['download=0', 'download=false', 'download=01', 'download=1.0', 'download=',
                              'download=+1', 'download=1&download=1', 'download=1&future=1', 'token=a&token=b']:
                    with self.assertRaises(WebmaniaError):
                        client.download_url(base + '/xmlnfe/' + UUID + '/?' + query, auth=FileAuth('company'))
                with self.assertRaises(WebmaniaError):
                    client.download_url(base + '/danfe/' + UUID + '/?download=1', auth=FileAuth('company'))
                with self.assertRaises(WebmaniaError):
                    client.download_url(base + '/xmlnfe/' + UUID + '/?download=1&token=' + token, auth=FileAuth('company'))
            self.assertEqual(len(records), 2)

    def test_deepest_accepted_serialized_values_are_redacted_from_shallow_echoes(self):
        private = 'synthetic-private-leaf-value'
        with server(lambda h, r: send(h, {'error': private, private: private}, 422,
                                     headers={'X-Request-ID': private})) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                for levels in [0, 30, 31, 32, 33, 40, 62, 63]:
                    nested = private
                    for _ in range(levels): nested = {'level': nested}
                    with self.subTest(levels=levels), self.assertRaises(WebmaniaError) as caught:
                        client.update_company({'future_option': nested})
                    self.assertNotIn(private, json.dumps(caught.exception.to_dict()))
                    self.assertEqual(caught.exception.correlation_id, '[redacted]')
                too_deep = private
                for _ in range(64): too_deep = {'level': too_deep}
                with self.assertRaises(WebmaniaError) as caught: client.update_company({'future_option': too_deep})
                self.assertEqual(caught.exception.kind, 'validation')
            self.assertEqual(len(records), 8)
            self.assertIn(private, records[-1]['raw'].decode())

    def test_snapshot_uses_json_bytes_and_collects_deep_uuid_capabilities(self):
        actual = 'synthetic-wire-secret'
        class MisleadingString(str):
            def __str__(self): return 'not-the-serialized-value'
        selected = [actual]
        with server(lambda h, r: send(h, {'error': selected[0], selected[0]: selected[0]}, 422,
                                     headers={'X-Request-ID': selected[0]})) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.update_company({'future_option': MisleadingString(actual)})
                self.assertIn(actual, records[0]['raw'].decode())
                self.assertNotIn(actual, json.dumps(caught.exception.to_dict()))
                upper = 'ABCDEFAB-CDEF-4ABC-8DEF-ABCDEFABCDEF'
                nested = {'uuid': upper}
                for _ in range(62): nested = {'level': nested}
                selected[0] = upper.lower()
                with self.assertRaises(WebmaniaError) as caught:
                    client.update_company({'future_option': nested})
                self.assertNotIn(upper.lower(), json.dumps(caught.exception.to_dict()))
                self.assertEqual(caught.exception.correlation_id, '[redacted]')
            self.assertEqual(len(records), 2)
