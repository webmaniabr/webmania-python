"""Original-text overlap regressions and controls; loopback fixtures only."""
import json
import unicodedata
import unittest
from urllib.parse import quote, quote_plus

from webmania import CompanyCredentials, NfeClient, WebmaniaError
from webmania.errors import Redactor, mutation_reference
from support import UUID, server, send


class RedactionOverlapTests(unittest.TestCase):
    def test_overlapping_credentials_and_contextual_uuid_http_tls(self):
        for tls in (False, True):
            for reverse in (False, True):
                for pair, echo in [(['ABCD-1234', '1234-WXYZ'], 'ABCD-1234-WXYZ'),
                                   ([UUID, UUID[-12:] + '-opaque-suffix'], UUID + '-opaque-suffix')]:
                    if reverse: pair = list(reversed(pair))
                    with self.subTest(tls=tls, reverse=reverse, echo=echo):
                        sentence = 'Public rejection: ' + echo + '; inspection complete.'
                        def handler(h, r):
                            send(h, {'error': sentence, echo: sentence,
                                     'public_notice': 'Provider rejected input.',
                                     'code': 539, 'retryable': False}, 500,
                                 headers={'X-Request-ID': echo})
                        with server(handler, tls=tls) as (base, records, ca):
                            credentials = CompanyCredentials(*pair, 'unrelated-access-key', 'unrelated-access-secret')
                            with NfeClient(credentials, base_url=base, ca_file=ca) as client:
                                with self.assertRaises(WebmaniaError) as caught:
                                    client.cancel_document({'uuid': UUID, 'motivo': 'Synthetic cancellation reason for controlled testing'})
                            error = caught.exception
                            self.assertEqual(error.kind, 'http')
                            self.assertEqual(error.outcome, 'unknown')
                            self.assertEqual(error.correlation_id, '[redacted]')
                            expected = 'Public rejection: [redacted]; inspection complete.'
                            self.assertEqual(error.response['error'], expected)
                            self.assertEqual(error.response['[redacted]'], expected)
                            self.assertEqual(error.response['public_notice'], 'Provider rejected input.')
                            self.assertEqual(error.response['code'], 539)
                            self.assertIs(error.response['retryable'], False)
                            public = json.dumps(error.to_dict()) + repr(error) + str(error) + repr(error.args) + str(error.__dict__)
                            for secret in pair: self.assertNotIn(secret, public)
                            self.assertNotIn('-WXYZ', public)
                            self.assertNotIn('-opaque-suffix', public)
                            self.assertIsNone(error.__cause__)
                            self.assertIsNone(error.__context__)
                            self.assertEqual(len(records), 1)

    def test_self_overlap_chains_containment_and_order(self):
        for secrets, echo in [(['ABA'], 'ABABA'),
                              (['ABC', 'BCD', 'CDE'], 'ABCDE'),
                              (['ABCD', 'BC', 'DEFG'], 'ABCDEFG'),
                              (['ABCD-1234', '1234-WXYZ'], 'ABCD-1234-WXYZ')]:
            for ordered in (secrets, list(reversed(secrets))):
                with self.subTest(secrets=ordered):
                    self.assertEqual(Redactor(ordered).text('Public: ' + echo + '; done.'), 'Public: [redacted]; done.')
        self.assertEqual(Redactor(['secret', 'redacted']).text('secret'), '[redacted]')
        self.assertEqual(Redactor(['ABCD', 'WXYZ']).text('ABCD WXYZ'), '[redacted] [redacted]')

    def test_normalized_json_and_percent_forms_overlap(self):
        secrets = ['café ALPHA', 'ALPHA OMEGA']
        echo = 'café ALPHA OMEGA'
        forms = {echo, unicodedata.normalize('NFD', echo), json.dumps(echo, ensure_ascii=True)[1:-1]}
        for normalized in (echo, unicodedata.normalize('NFD', echo)):
            for encoder in (quote, quote_plus):
                encoded = encoder(normalized, safe='')
                forms.update((encoded, encoded.replace('%C3%A9', '%c3%a9').replace('%CC%81', '%cc%81')))
        for form in forms:
            with self.subTest(form=form):
                self.assertEqual(Redactor(secrets).text('Public: ' + form + '; done.'), 'Public: [redacted]; done.')

    def test_numeric_and_url_intervals_join_original_literal_matches(self):
        self.assertEqual(Redactor(['1000', '3-opaque']).text('Public: 1e3-opaque; done.'), 'Public: [redacted]; done.')
        value = 'PRIVATE https://example.invalid/opaque'
        self.assertEqual(Redactor([value]).text('Public: ' + value + ' done.'), 'Public: [redacted-url] done.')
        self.assertEqual(Redactor(['PRIVATE https://']).text('Public: PRIVATE https://example.invalid/opaque done.'), 'Public: [redacted-url] done.')

    def test_case_numeric_recovery_and_output_policy_controls(self):
        upper = 'ABCDEFAB-CDEF-4ABC-8DEF-ABCDEFABCDEF'
        lower = upper.lower()
        redactor = Redactor([upper, 'ArbitraryToken'])
        self.assertEqual(redactor.text(lower + ' arbitrarytoken'), lower + ' arbitrarytoken')
        contextual = Redactor(['abcdefabcdef-opaque'], uuid_secrets=[upper])
        self.assertEqual(contextual.text(lower + '-opaque'), '[redacted]')
        self.assertEqual(contextual.text(upper + '-opaque'), '[redacted]-opaque')
        self.assertEqual(Redactor(['private']).clean({'public': True, 'code': 539, 'marker': '[redacted]'}),
                         {'public': True, 'code': 539, 'marker': '[redacted]'})
        # Existing opaque-secret policy is literal substring matching at every
        # length; REDACT-02 boundary behavior remains a separate policy question.
        self.assertEqual(Redactor(['xy']).text('xy (xy) zxyword XY'), '[redacted] ([redacted]) z[redacted]word XY')
        for selector in ('ABCD-1234-WXYZ', '9e2'):
            self.assertIsNone(mutation_reference({'ID': selector}, {}, ['1234-WXYZ', '900']))
        reference = mutation_reference({'ID': 'public-recovery-selector'}, {}, ['private'])
        self.assertEqual(reference.reveal(), {'ID': 'public-recovery-selector'})
        self.assertEqual(Redactor(['ABA']).text('ABABA' * 819), '[redacted]')
        self.assertEqual(Redactor(['ABA']).text('ABABA' * 820), '[truncated]')
        self.assertLessEqual(len(Redactor(['private']).text('x' * 4096)), 1024)


if __name__ == '__main__': unittest.main()
