"""Documented and unexpected redirects: protected metadata, never followed."""
from dataclasses import asdict
import json
import typing
import unittest
from urllib.parse import parse_qs, urlsplit

from webmania import (CompanyCredentials, EmitterFilesClient, FileAuth, FileRedirectResponse,
                      FileResponse, NfeClient, ProtectedLocation, WebmaniaError)
from support import PDF, UUID, server, send
from test_sdk import COMPANY


class RedirectTests(unittest.TestCase):
    def test_documented_external_location_is_protected_and_never_trusted_or_followed(self):
        token = 'synthetic-private-location-token'
        with server(lambda h, r: send(h, PDF, media='application/pdf')) as (target, target_records, _):
            location = target + '/private/' + UUID + '?token=' + token
            with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': location})) as (base, records, _):
                with EmitterFilesClient(base_url=base, trusted_origins=[base], issuer_token='synthetic-issuer') as client:
                    result = client.get_nfse_pdf(identifier=UUID, auth=FileAuth('issuer'))
                    self.assertIsInstance(result, FileRedirectResponse)
                    self.assertEqual(result.status, 302)
                    self.assertEqual(result.location.reveal(), location)
                    self.assertFalse(result.location.is_relative)
                    diagnostic = str(result) + repr(result) + str(result.location) + repr(result.location)
                    diagnostic += json.dumps(result.to_dict()) + json.dumps(asdict(result), default=str)
                    diagnostic += json.dumps(vars(result), default=str)
                    for private in [location, token, UUID]: self.assertNotIn(private, diagnostic)
                    with self.assertRaises(WebmaniaError) as caught:
                        client.download_url(result.location.reveal(), auth=FileAuth('issuer'))
                    self.assertEqual(caught.exception.kind, 'validation')
                self.assertEqual(len(records), 1)
                self.assertEqual(records[0]['headers']['Authorization'], 'Bearer synthetic-issuer')
            self.assertEqual(target_records, [])

    def test_relative_and_network_path_references_stay_unresolved(self):
        state = ['/darps/' + UUID + '?token=synthetic-relative-token']
        with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': state[0]})) as (base, records, _):
            with EmitterFilesClient(base_url=base, trusted_origins=[base], issuer_token='synthetic-issuer') as client:
                for location in ['/darps/' + UUID + '?token=synthetic-relative-token',
                                 '../darps/' + UUID, '?download=synthetic-capability',
                                 '//other.example.invalid/darps/' + UUID, '#page=2']:
                    state[0] = location
                    result = client.get_nfse_pdf(identifier=UUID, auth=FileAuth('issuer'))
                    self.assertIsInstance(result, FileRedirectResponse)
                    self.assertEqual(result.location.reveal(), location)
                    self.assertTrue(result.location.is_relative)
                self.assertEqual(len(records), 5)
                self.assertTrue(all('/nfse/' in r['path'] for r in records))

    def test_redirect_metadata_preserves_original_authentication_separation(self):
        location = '/darps/' + UUID + '?token=synthetic-output-capability'
        with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': location})) as (base, records, _):
            with EmitterFilesClient(base_url=base, trusted_origins=[base], issuer_token='synthetic-issuer') as client:
                for auth in [FileAuth('issuer'), FileAuth('document_token', 'synthetic+document-token'), FileAuth('anonymous')]:
                    self.assertIsInstance(client.get_nfse_pdf(identifier=UUID, auth=auth), FileRedirectResponse)
            self.assertEqual(len(records), 3)
            self.assertEqual(records[0]['headers']['Authorization'], 'Bearer synthetic-issuer')
            for record in records[1:]: self.assertNotIn('Authorization', record['headers'])
            self.assertEqual(parse_qs(urlsplit(records[1]['path']).query), {'token': ['synthetic+document-token']})
            self.assertEqual(parse_qs(urlsplit(records[2]['path']).query), {})
            for record in records:
                self.assertFalse(any(k.lower().startswith('x-consumer') or k.lower().startswith('x-access') for k in record['headers']))

    def test_two_xx_file_response_and_other_download_types_remain_compatible(self):
        with server(lambda h, r: send(h, PDF, media='application/pdf')) as (base, records, _):
            with EmitterFilesClient(base_url=base, trusted_origins=[base], issuer_token='synthetic-issuer') as client:
                result = client.get_nfse_pdf(identifier=UUID, auth=FileAuth('issuer'))
                self.assertIsInstance(result, FileResponse)
                self.assertEqual(result.data, PDF)
                self.assertEqual(result.status, 200)
                self.assertFalse(hasattr(result, 'location'))
            self.assertEqual(len(records), 1)
        self.assertEqual(typing.get_type_hints(EmitterFilesClient.get_nfse_pdf)['return'], FileResponse | FileRedirectResponse)
        self.assertIs(typing.get_type_hints(EmitterFilesClient.get_nfse_xml)['return'], FileResponse)

    def test_missing_duplicate_folded_and_malformed_locations_are_refused(self):
        selected = [None]
        def handler(h, r):
            if selected[0] == 'duplicate':
                h.send_response(302)
                h.send_header('Location', '/darps/one?token=synthetic-one')
                h.send_header('location', '/darps/two?token=synthetic-two')
                h.send_header('Content-Length', '0'); h.end_headers()
            else:
                headers = {} if selected[0] is None else {'Location': selected[0]}
                send(h, b'', 302, media='text/plain', headers=headers)
        with server(handler) as (base, records, _):
            with EmitterFilesClient(base_url=base, trusted_origins=[base], issuer_token='synthetic-issuer') as client:
                for invalid in [None, '', '   ', 'duplicate', 'javascript:alert(1)', 'data:application/pdf,synthetic',
                                'https://', 'https://user:password@example.invalid/private',
                                'https://example.invalid:99999/private', '//', '///other.invalid/path',
                                '/bad\\path', '/bad%zz', '/bad%0d%0aHeader', '/bad%00path',
                                '/first,https://other.invalid/second', '/folded\r\n continuation']:
                    with self.subTest(location=invalid):
                        selected[0] = invalid
                        with self.assertRaises(WebmaniaError) as caught:
                            client.get_nfse_pdf(identifier=UUID, auth=FileAuth('issuer'))
                        error = caught.exception
                        self.assertEqual(error.kind, 'protocol')
                        self.assertEqual(error.status, 302)
                        self.assertIsNone(error.location)
                        self.assertNotIn('synthetic-one', json.dumps(error.to_dict()))
            self.assertEqual(len(records), 17)
        for invalid in ['/literal\r\nHeader', '/literal\nHeader', '/literal\x00path', '/space inside', 'https:relative', 'ftp://example.invalid/file']:
            with self.subTest(invalid=invalid), self.assertRaises(WebmaniaError): ProtectedLocation(invalid)

    def test_unexpected_mutation_redirect_is_unknown_and_recoverable_without_replay(self):
        state = [302]
        location = '/private/' + UUID + '?token=synthetic-redirect-token'
        request = {'uuid': UUID, 'motivo': 'Synthetic cancellation reason'}
        def handler(h, record):
            send(h, b'', state[0], media='text/plain', headers={'Location': location, 'X-Request-ID': 'synthetic-redirect-token'})
        with server(handler) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                for status in [301, 302, 303, 307, 308]:
                    state[0] = status
                    with self.assertRaises(WebmaniaError) as caught: client.cancel_document(request)
                    error = caught.exception
                    self.assertEqual(error.kind, 'redirect')
                    self.assertEqual(error.status, status)
                    self.assertEqual(error.outcome, 'unknown')
                    # Location now establishes the same UUID as a capability.
                    self.assertIsNone(error.request_reference)
                    self.assertEqual(error.location.reveal(), location)
                    diagnostic = json.dumps(error.to_dict()) + repr(error) + str(error.__dict__)
                    for private in [UUID, location, 'synthetic-redirect-token']: self.assertNotIn(private, diagnostic)
                    self.assertEqual(json.loads(records[-1]['raw']), request)
                self.assertEqual(len(records), 5)
                self.assertTrue(all(r['method'] == 'PUT' for r in records))

    def test_passive_unexpected_redirect_does_not_invent_mutation_uncertainty(self):
        location = 'https://untrusted.example.invalid/private?token=synthetic-passive-capability'
        with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': location})) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught: client.get_sefaz_status()
                error = caught.exception
                self.assertEqual(error.kind, 'redirect')
                self.assertIsNone(error.outcome)
                self.assertIsNone(error.request_reference)
                self.assertEqual(error.location.reveal(), location)
                self.assertNotIn(location, json.dumps(error.to_dict()))
            self.assertEqual(len(records), 1)

    def test_location_path_uuid_case_is_redacted_without_folding_opaque_query_tokens(self):
        capability = 'ABCDEFAB-ABCD-4ABC-8ABC-ABCDEFABCDEF'
        mixed = 'aBcDeFaB-aBcD-4aBc-8aBc-aBcDeFaBcDeF'
        opaque = 'FEDCBAFE-FEDC-4FED-8FED-FEDCBAFEDCBA'
        state = ['/darps/' + capability + '?token=synthetic-link-token', capability]
        with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': state[0], 'X-Request-ID': state[1]})) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                for path, echo in [('/darps/' + capability, capability),
                                   ('/darps/' + capability, capability.lower()),
                                   ('/darps/' + capability, mixed),
                                   ('/darps/%41' + capability[1:], capability.lower())]:
                    state[:] = [path + '?token=synthetic-link-token', echo]
                    with self.assertRaises(WebmaniaError) as caught:
                        client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'})
                    error = caught.exception
                    self.assertEqual(error.kind, 'redirect')
                    self.assertEqual(error.outcome, 'unknown')
                    self.assertEqual(error.correlation_id, '[redacted]')
                    self.assertEqual(error.request_reference.reveal(), {'uuid': UUID})
                    self.assertEqual(error.location.reveal(), state[0])
                    for spelling in [capability, capability.lower(), mixed]:
                        self.assertNotIn(spelling, json.dumps(error.to_dict()) + str(error.__dict__))
                # A UUID-shaped query token has no inferred UUID semantics.
                state[0] = '/darps/plain?token=' + opaque
                for echo, expected in [(opaque, '[redacted]'), (opaque.lower(), opaque.lower())]:
                    state[1] = echo
                    with self.assertRaises(WebmaniaError) as caught:
                        client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'})
                    self.assertEqual(caught.exception.correlation_id, expected)
            self.assertEqual(len(records), 6)

    def test_malformed_authority_keeps_path_redaction_without_folding_other_components(self):
        capability = 'FEDCBAFE-ABCD-4ABC-8ABC-FEDCBAFEDCBA'
        opaque = 'ABCDEFAB-ABCD-4ABC-8ABC-ABCDEFABCDEF'
        state = ['', '']
        def handler(h, record):
            if state[0] == 'duplicate':
                h.send_response(302)
                h.send_header('Location', 'https://[invalid/private/' + capability)
                h.send_header('location', '/private/' + opaque)
                h.send_header('X-Request-ID', capability.lower())
                h.send_header('Connection', 'close'); h.send_header('Content-Length', '0'); h.end_headers()
            else:
                send(h, b'', 302, media='text/plain', headers={'Location': state[0], 'X-Request-ID': state[1], 'Connection': 'close'})
        with server(handler) as (base, records, _):
            cases = [
                ('/private/' + capability + '?token=c-opaque-link', capability.lower(), 'redirect', '[redacted]', True),
                (base + '/private/' + capability, capability.lower(), 'redirect', '[redacted]', True),
                ('https://[invalid/private/' + capability + '?token=c-opaque-link', capability.lower(), 'protocol', '[redacted]', False),
                ('//[invalid/private/' + capability + '?token=c-opaque-link', capability.lower(), 'protocol', '[redacted]', False),
                ('HTTPS://[invalid/private/%46' + capability[1:] + '?token=c-opaque-link', capability.lower(), 'protocol', '[redacted]', False),
                ('https://[invalid/private/' + capability + '#fragment?token=' + opaque, capability.lower(), 'protocol', '[redacted]', False),
                ('https://[invalid/private/plain?token=' + opaque, opaque, 'protocol', '[redacted]', False),
                ('https://[invalid/private/plain?token=' + opaque, opaque.lower(), 'protocol', opaque.lower(), False),
                ('https://' + opaque + '@[invalid/private/plain?token=c-opaque-link', opaque.lower(), 'protocol', opaque.lower(), False),
                ('https://prefix%2F' + opaque + '@[invalid/private/plain?token=c-opaque-link', opaque.lower(), 'protocol', opaque.lower(), False),
                ('https://[' + opaque + '/private/plain?token=c-opaque-link', opaque.lower(), 'protocol', opaque.lower(), False),
                ('/private/plain?token=c-opaque-link', opaque.lower(), 'redirect', opaque.lower(), True),
                ('duplicate', capability.lower(), 'protocol', None, False),
            ]
            with NfeClient(COMPANY, base_url=base) as client:
                for location, echo, kind, correlation, recoverable in cases:
                    with self.subTest(location=location, echo=echo):
                        state[:] = [location, echo]
                        with self.assertRaises(WebmaniaError) as caught:
                            client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'})
                        error = caught.exception
                        self.assertEqual(error.kind, kind)
                        self.assertEqual(error.status, 302)
                        self.assertEqual(error.outcome, 'unknown')
                        self.assertEqual(error.request_reference.reveal(), {'uuid': UUID})
                        self.assertEqual(error.correlation_id, correlation)
                        self.assertEqual(error.location is not None, recoverable)
                        if recoverable: self.assertEqual(error.location.reveal(), location)
                        self.assertNotIn(capability.lower(), json.dumps(error.to_dict()).lower())
                        self.assertEqual(len(records), cases.index((location, echo, kind, correlation, recoverable)) + 1)
            self.assertEqual(len(records), len(cases))
            self.assertTrue(all(record['method'] == 'PUT' and record['path'] == '/1/nfe/cancelar/' for record in records))

    def test_refused_location_userinfo_is_redacted_literally_from_diagnostics(self):
        secret = 'synthetic-userinfo-secret'
        location = 'https://synthetic-user:' + secret + '@example.invalid/private'
        with server(lambda h, r: send(h, b'', 302, media='text/plain', headers={'Location': location, 'X-Request-ID': secret})) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                with self.assertRaises(WebmaniaError) as caught:
                    client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'})
                error = caught.exception
                self.assertEqual(error.kind, 'protocol')
                self.assertEqual(error.outcome, 'unknown')
                self.assertEqual(error.correlation_id, '[redacted]')
                self.assertIsNone(error.location)
                self.assertNotIn(secret, json.dumps(error.to_dict()))
            self.assertEqual(len(records), 1)

    def test_invalid_or_duplicate_mutation_redirect_retains_uncertain_selector(self):
        state = ['bad']
        def handler(h, r):
            h.send_response(302)
            h.send_header('Location', '/bad%0aLocation' if state[0] == 'bad' else '/one')
            if state[0] == 'duplicate': h.send_header('Location', '/two')
            h.send_header('Content-Length', '0'); h.end_headers()
        with server(handler) as (base, records, _):
            with NfeClient(COMPANY, base_url=base) as client:
                for kind in ['bad', 'duplicate']:
                    state[0] = kind
                    with self.assertRaises(WebmaniaError) as caught:
                        client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason'})
                    error = caught.exception
                    self.assertEqual(error.kind, 'protocol')
                    self.assertEqual(error.status, 302)
                    self.assertEqual(error.outcome, 'unknown')
                    self.assertEqual(error.request_reference.reveal(), {'uuid': UUID})
                    self.assertIsNone(error.location)
            self.assertEqual(len(records), 2)
