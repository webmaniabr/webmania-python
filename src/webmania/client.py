"""Service-isolated synchronous clients for the pinned public fiscal contracts."""
from __future__ import annotations
from dataclasses import replace
from decimal import Decimal, InvalidOperation
from copy import deepcopy
import json
import math
import re
import sys
import time
from urllib.parse import quote, urlencode, urlsplit, parse_qsl
from uuid import uuid4
from .binary import file_result
from .pagination import PageIterator
from .errors import WebmaniaError, Redactor, mutation_reference
from .transport import Transport, checked_url, positive
from .types import CompanyCredentials, ResellerCredentials, CallOptions, FileAuth, FileRedirectResponse, UNSET
from .redirects import ProtectedLocation, location_diagnostic_values, location_path_uuids
from .validation import OPERATIONS, operation, validate
from .generated.nfe_methods import NfeMethods
from .generated.emitter_methods import EmitterMethods
from .generated.monitor_methods import MonitorMethods
from .generated.reseller_methods import ResellerMethods
from .generated.nfe_files_methods import NfeFilesMethods
from .generated.emitter_files_methods import EmitterFilesMethods
from .generated.report_files_methods import ReportFilesMethods

HEADER_NAMES = ['X-Consumer-Key', 'X-Consumer-Secret', 'X-Access-Token', 'X-Access-Token-Secret']
# Literal segments of the pinned routes are public structure, never private Location values.
ROUTE_SEGMENTS = frozenset(segment for record in OPERATIONS.values() for segment in record['path'].split('/')
                           if segment and not segment.startswith('{'))


def credential(value):
    return isinstance(value, str) and 0 < len(value) <= 8192 and all(33 <= ord(c) <= 126 for c in value)


def credential_headers(value, kind):
    if type(value) is not kind:
        raise WebmaniaError('configuration', 'Expected credentials for this service scope.')
    vals = [value.consumer_key, value.consumer_secret, value.access_token, value.access_token_secret]
    if not all(credential(v) for v in vals):
        raise WebmaniaError('configuration', 'All four credentials must be nonempty ASCII header values.')
    return dict(zip(HEADER_NAMES, vals))


def bearer_headers(token):
    if not credential(token):
        raise WebmaniaError('configuration', 'A nonempty ASCII Bearer token is required for this service.')
    return {'Authorization': 'Bearer ' + token}


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result: raise ValueError('Duplicate JSON key.')
        result[key] = value
    return result


def depth_limit(value, depth=0):
    pending = [(value, depth, frozenset())]
    while pending:
        node, level, parents = pending.pop()
        if level > 64: raise ValueError('Maximum JSON depth exceeded.')
        if isinstance(node, (dict, list)):
            if id(node) in parents: raise ValueError('Cyclic JSON value.')
            ancestors = parents | {id(node)}
            if isinstance(node, dict):
                if any(not isinstance(k, str) for k in node): raise ValueError('JSON keys must be strings.')
                for key in node: key.encode('utf-8')
                children = node.values()
            else: children = node
            pending.extend((child, level + 1, ancestors) for child in children)
        elif isinstance(node, str): node.encode('utf-8')
        elif node is None or isinstance(node, (bool, int)): pass
        elif isinstance(node, float) and math.isfinite(node): pass
        else: raise ValueError('Expected finite JSON values.')


def finite_float(text):
    try: exact = Decimal(text)
    except InvalidOperation: raise ValueError('Unsupported decimal exponent.') from None
    _, digits, exponent = exact.as_tuple()
    # Check the compact lexical representation before conversion or expansion.
    # 4096 digits remain below the supported runtimes' default JSON int limit.
    if not exact.is_finite() or not isinstance(exponent, int) or len(digits) > 4096 or abs(exponent) > 4096 or not -4096 <= exact.adjusted() <= 4095:
        raise ValueError('Decimal response number exceeds the supported bound.')
    value = float(text)
    if not math.isfinite(value): raise ValueError('Nonfinite number.')
    # Preserve semantic integers exactly, including exponent/decimal notation.
    # A fractional lexeme must not become an integer or zero by float rounding.
    if exact == exact.to_integral_value(): return int(exact)
    if value == 0 or value.is_integer(): raise ValueError('Fractional number loses its lexical semantics.')
    return value


def error_payload(value):
    return isinstance(value, dict) and ('error' in value or any(value.get(k) not in (None, False, '', [], {}) for k in ['erro', 'errors']) or value.get('success') is False)


class BaseClient:
    _scope = ''
    def __init__(self, base_url, headers, **transport_options):
        self._transport = Transport(base_url, **transport_options)
        self._headers = headers.copy()
        self._secrets = list(headers.values())
        self._secrets += [v.removeprefix('Bearer ') for v in headers.values() if v.startswith('Bearer ')]

    def __repr__(self):
        return type(self).__name__ + '([private configuration])'

    def close(self):
        self._transport.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()

    def _execute(self, oid, request=UNSET, path_params=None, query=None, options=None, auth=None):
        record, doc, spec = operation(oid)
        if record['client'] != self._scope:
            raise WebmaniaError('configuration', 'Operation is not in this client service scope.')
        if spec.get('x-sdk-generation-enabled') is False:
            raise WebmaniaError('capability', 'This operation is not available in this SDK release; no request was sent.')
        module = record['module']
        params = spec.get('parameters', [])
        path_params = dict(path_params or {})
        query = {} if query is None else dict(query)
        invalid_query = False
        try: depth_limit(query); depth_limit(path_params)
        except (ValueError, UnicodeError, TypeError): invalid_query = True
        if invalid_query: raise WebmaniaError('validation', 'Expected finite Unicode query and path values.')
        validate(module, record['query_schema'], query)
        if oid == 'nfeGetDocument':
            validate(module, {'$ref': '#/components/schemas/NfeLookupRequest'}, query)
        if oid == 'monitorGetDownloadStatistics':
            year, month = query.get('ano'), query.get('mes')
            if (year is None) != (month is None):
                raise WebmaniaError('validation', 'Statistics require a year/month pair; the provider validates its calendar.')
        route = record['path']
        for p in params:
            if p['in'] == 'path':
                value = path_params.get(p['name'], UNSET)
                validate(module, p['schema'], value)
                if isinstance(value, str) and (value in ['.', '..'] or any(ord(c) < 32 or c in '/\\%?#' for c in value)):
                    raise WebmaniaError('validation', 'Unsafe path identifier.')
                route = route.replace('{' + p['name'] + '}', quote(str(value), safe=''))
        request_schema = spec.get('requestBody', {}).get('content', {}).get('application/json', {}).get('schema')
        body = None
        request_snapshot = None
        invalid_json = False
        try:
            if request_schema is not None:
                depth_limit(request)
                body = json.dumps(request, ensure_ascii=False, allow_nan=False, separators=(',', ':')).encode('utf-8')
                request_snapshot = json.loads(body, object_pairs_hook=strict_object)
                depth_limit(request_snapshot)
        except (TypeError, ValueError, UnicodeError, OverflowError, RecursionError):
            invalid_json = True
        if invalid_json:
            raise WebmaniaError('validation', 'Expected finite JSON values with string keys and bounded depth.')
        if request_schema is not None:
            validate(module, request_schema, request_snapshot)
        elif request is not UNSET:
            raise WebmaniaError('validation', 'This operation does not accept a JSON body.')
        headers = self._headers.copy()
        extra_secrets = []
        if self._scope.endswith('Files'):
            headers, extra_secrets = self._file_auth(spec, auth, query)
            if options is None: options = CallOptions(max_response_bytes=32 * 1024 * 1024)
            elif options.max_response_bytes is None: options = replace(options, max_response_bytes=32 * 1024 * 1024)
        elif auth is not None:
            raise WebmaniaError('configuration', 'File authorization is not valid for a JSON operation.')
        headers.update({'User-Agent': 'Webmania-Python/0.1.0a8', 'Accept': 'application/json', 'Accept-Encoding': 'identity'})
        if body is not None: headers['Content-Type'] = 'application/json'
        binary = any(v.get('schema', {}).get('format') == 'binary' for k, r in spec['responses'].items() if k.startswith('2') for v in r.get('content', {}).values())
        if binary: headers['Accept'] = ', '.join(dict.fromkeys(t for k, r in spec['responses'].items() if k.startswith('2') for t in r.get('content', {}) if t != 'text/html'))
        prefix = self._transport.base.path.rstrip('/')
        path = prefix + route
        if query:
            path += '?' + urlencode({k: ('true' if v else 'false') if isinstance(v, bool) else v for k, v in query.items()}, doseq=False)
        diagnostic_secrets = self._secrets + extra_secrets + list(path_params.values())
        diagnostic_request = {'body': request_snapshot, 'query': dict(parse_qsl(urlsplit(path).query, keep_blank_values=True))}
        diagnostic_uuids = list(path_params.values()) + list(options._known_uuid_capabilities if options else ())
        redactor = Redactor(diagnostic_secrets, diagnostic_request, uuid_secrets=diagnostic_uuids, contextual_values=options._known_capabilities if options else ())
        effects = spec.get('x-operation-effects', {}).get('business_mutation', record['verb'] not in ['GET', 'HEAD'])
        # Pinned API1 files x-retry-policy: this GET can consume report quota.
        if oid == 'fiscalDownloadReport': effects = True
        mutation = (query.get('atualizar_status') == 1 if effects == 'provider_status_refresh_when_atualizar_status_is_1' else bool(isinstance(request_snapshot, dict) and request_snapshot.get('relatorio') is not None) if effects == 'only_when_relatorio_is_present' else effects is not False)
        request_id = str(uuid4())
        reference = mutation_reference(request_snapshot, path_params,
                                       self._secrets + extra_secrets + list(options._known_capabilities if options else ()),
                                       options._known_uuid_capabilities if options else (),
                                       capability_access=self._scope.endswith('Files') and auth.mode in ['capability', 'document_token', 'anonymous'])
        result = None
        pending = None
        try:
            result = self._transport.request(record['verb'], path, body, headers, options)
        except WebmaniaError as exc:
            pending = exc
        def observed_context(observed):
            values, uuids = [], []
            for key, val in observed:
                if key.lower() == 'location':
                    values.extend(location_diagnostic_values(val))
                    uuids.extend(location_path_uuids(val))
            masker = Redactor(diagnostic_secrets, diagnostic_request, uuid_secrets=diagnostic_uuids + uuids, contextual_values=values + list(options._known_capabilities if options else ()))
            # Diagnostics stay fully masked; only the recovery filter ignores proven route structure
            # (pinned route literals and the configured base path), so a selector is not dropped
            # because it contains a segment such as "1" or "nfe".
            structural = ROUTE_SEGMENTS | {s for s in self._transport.base.path.split('/') if s}
            private_values = [v for v in values if v not in structural]
            recovery = mutation_reference(request_snapshot, path_params,
                self._secrets + extra_secrets + list(options._known_capabilities if options else ()) + private_values,
                list(options._known_uuid_capabilities if options else ()) + uuids,
                capability_access=self._scope.endswith('Files') and auth.mode in ['capability', 'document_token', 'anonymous'])
            return masker, recovery
        if pending is not None:
            sent = getattr(pending, '_request_sent', False)
            _, reference = observed_context(getattr(pending, '_observed_headers', ()))
            if getattr(pending, '_unsafe_headers', False): reference = None
            # Transport metadata is private call-local state, never an error field.
            for attr in ['_observed_headers', '_unsafe_headers']:
                if hasattr(pending, attr): delattr(pending, attr)
            if mutation and sent: pending.outcome = 'unknown'; pending.request_reference = reference
            pending.request_id = request_id
            raise pending
        status, raw_headers, raw, observed = result
        safe_headers = {k.lower(): v for k, v in raw_headers.items()}
        protected_location = None
        redactor, reference = observed_context(observed)
        correlation = next((safe_headers[k] for k in ['x-correlation-id', 'x-request-id', 'request-id'] if k in safe_headers), None)
        correlation = redactor.text(correlation) if correlation else None
        def failure(kind, message, value=None):
            uncertain = mutation and (status >= 500 or kind in ['protocol', 'response_schema', 'business', 'protected_file', 'redirect'])
            return WebmaniaError(kind, message, status=status, response=redactor.clean(value) if value is not None else None,
                                 correlation_id=correlation, outcome='unknown' if uncertain else None,
                                 request_reference=reference if uncertain else None, request_id=request_id, location=protected_location)
        if 300 <= status < 400:
            documented = binary and status == 302 and spec['responses'].get('302', {}).get('headers', {}).get('Location', {}).get('required') is True
            if 'location' in safe_headers:
                location_error = None
                try: protected_location = ProtectedLocation(safe_headers['location'])
                except WebmaniaError as exc: location_error = exc
                if location_error is not None:
                    raise failure('protocol', 'Invalid or ambiguous HTTP redirect Location.')
            if documented:
                if protected_location is None:
                    raise failure('protocol', 'Documented redirect requires one valid Location header.')
                return FileRedirectResponse(protected_location)
            raise failure('redirect', 'Unexpected HTTP redirect refused.')
        media = safe_headers.get('content-type', '').split(';', 1)[0].strip().lower()
        value = None
        json_failed = False
        if media == 'application/json' or media.endswith('+json'):
            try:
                value = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=strict_object,
                                   parse_float=finite_float, parse_constant=lambda _: (_ for _ in ()).throw(ValueError('Nonfinite number.')))
                depth_limit(value)
            except (ValueError, UnicodeError, RecursionError): json_failed = True
        if not 200 <= status < 300:
            raise failure('http', 'HTTP request failed.', value)
        terminal_import = oid == 'monitorGetImportStatus' and status == 200 and isinstance(value, dict) and value.get('status') == 'invalido'
        if error_payload(value) and not terminal_import:
            raise failure('business', 'Provider returned a functional error.', value)
        if binary:
            if value is not None:
                raise failure('business', 'Provider returned JSON instead of a completed fiscal file.', value)
            allowed = {t for k, r in spec['responses'].items() if k == str(status) for t, v in r.get('content', {}).items() if v.get('schema', {}).get('format') == 'binary'}
            binary_error = None
            try: response = file_result(status, safe_headers, raw, allowed, oid)
            except WebmaniaError as exc: binary_error = exc
            if binary_error is not None: raise failure(binary_error.kind, str(binary_error))
            return response
        if json_failed or value is None:
            raise failure('protocol', 'Expected a finite JSON response with unique keys.')
        schema = spec['responses'].get(str(status), {}).get('content', {}).get('application/json', {}).get('schema')
        if schema is None: raise failure('protocol', 'Unexpected successful HTTP status.')
        schema_error = None
        try: validate(module, schema, value, response=True)
        except WebmaniaError as exc: schema_error = exc
        if schema_error is not None:
            raise failure('response_schema', 'Response does not match the pinned contract.', value)
        return value


class NfeClient(NfeMethods, BaseClient):
    _scope = 'Nfe'
    def __init__(self, credentials: CompanyCredentials, *, base_url='https://webmania.com.br/api', **options):
        super().__init__(base_url, credential_headers(credentials, CompanyCredentials), **options)

    def issue_nfe(self, request, *, options=None):
        validate('api1_fiscal', {'$ref': '#/components/schemas/Nfe55IssueRequest'}, request)
        return self.issue_document(request, options=options)

    def issue_nfce(self, request, *, options=None):
        validate('api1_fiscal', {'$ref': '#/components/schemas/Nfce65IssueRequest'}, request)
        return self.issue_document(request, options=options)

    def wait_report(self, request, *, max_attempts=20, interval=5.0, deadline=120.0, options=None):
        invalid = False
        try:
            depth_limit(request)
            request = deepcopy(request)
        except (ValueError, TypeError, RecursionError): invalid = True
        if invalid: raise WebmaniaError('validation', 'Expected a finite bounded polling request.')
        return _poll(lambda opts: self.create_or_poll_report(request, options=opts), lambda r: r.get('status') == 'concluido', max_attempts, interval, deadline, options, report_capability=True)


class EmitterClient(EmitterMethods, BaseClient):
    _scope = 'Emitter'
    def __init__(self, issuer_token: str, *, base_url='https://api.webmania.com.br', **options):
        super().__init__(base_url, bearer_headers(issuer_token), **options)


class ResellerClient(ResellerMethods, BaseClient):
    _scope = 'Reseller'
    def __init__(self, credentials: ResellerCredentials, *, base_url='https://webmania.com.br', **options):
        super().__init__(base_url, credential_headers(credentials, ResellerCredentials), **options)


class MonitorClient(MonitorMethods, BaseClient):
    _scope = 'Monitor'
    def __init__(self, monitor_token: str, *, base_url='https://api.webmania.com.br', **options):
        super().__init__(base_url, bearer_headers(monitor_token), **options)

    def iter_companies(self, query=None, *, max_pages=100, max_items=None, continuation=None, options=None):
        return PageIterator(self.list_companies, query, max_pages, max_items, continuation, options, 'companies')

    def iter_reports(self, query=None, *, max_pages=100, max_items=None, continuation=None, options=None):
        return PageIterator(self.list_reports, query, max_pages, max_items, continuation, options, 'reports')

    def iter_company_municipalities(self, company, query=None, *, max_pages=100, max_items=None, continuation=None, options=None):
        return PageIterator(lambda **kw: self.list_company_municipalities(company=company, **kw), query, max_pages, max_items, continuation, options, ['municipalities', company])

    def wait_import(self, uuid, *, max_attempts=20, interval=5.0, deadline=120.0, options=None):
        return _poll(lambda opts: self.get_import_status(uuid=uuid, options=opts), lambda r: r.get('status') in ['concluido', 'invalido'], max_attempts, interval, deadline, options)


class FilesBase(BaseClient):
    def __init__(self, base_url, headers, trusted_origins, **options):
        selected = checked_url(base_url)
        origin = (selected.scheme, selected.hostname, selected.port or (443 if selected.scheme == 'https' else 80))
        approved = set()
        for value in trusted_origins:
            p = checked_url(value, origin_only=True)
            approved.add((p.scheme, p.hostname, p.port or (443 if p.scheme == 'https' else 80)))
        if origin not in approved:
            raise WebmaniaError('configuration', 'File origin requires explicit trust before any transfer.')
        self._trusted = approved
        super().__init__(base_url, headers, **options)

    def _file_auth(self, spec, auth, query):
        if not isinstance(auth, FileAuth):
            raise WebmaniaError('configuration', 'Choose one explicit FileAuth mode for this transfer.')
        policies = spec.get('security', [])
        if auth.mode == 'company' and self._scope == 'NfeFiles' and any('ConsumerKey' in p for p in policies):
            if not self._headers or auth.token is not None: raise WebmaniaError('configuration', 'Company file credentials are required without a token.')
            return self._headers.copy(), []
        if auth.mode == 'issuer' and self._scope == 'EmitterFiles' and any('FiscalFileCompanyBearer' in p for p in policies):
            if not self._headers or auth.token is not None: raise WebmaniaError('configuration', 'Issuer file Bearer is required without a token.')
            return self._headers.copy(), []
        if auth.mode == 'company' and self._scope == 'ReportFiles' and any('ConsumerKey' in p for p in policies):
            if not self._company or auth.token is not None: raise WebmaniaError('configuration', 'Company report credentials are required without a token.')
            return self._company.copy(), []
        if auth.mode == 'issuer' and self._scope == 'ReportFiles' and any('ReportCompanyBearer' in p for p in policies):
            if not self._bearer or auth.token is not None: raise WebmaniaError('configuration', 'The company API2 Bearer is required without a token.')
            return self._bearer.copy(), []
        if auth.mode == 'document_token' and any('DocumentToken' in p or 'FiscalDocumentLinkToken' in p for p in policies):
            if not credential(auth.token): raise WebmaniaError('configuration', 'An existing document capability token is required.')
            query['token'] = auth.token
            return {}, [auth.token]
        if auth.mode == 'anonymous' and {} in policies and auth.token is None:
            return {}, []
        if auth.mode == 'capability' and policies == [] and auth.token is None:
            return {}, []
        raise WebmaniaError('capability', 'This explicit file access mode is not supported by the route.')

    def download_url(self, url, *, auth: FileAuth, options=None):
        # URLs do not create new trust. Only the configured origin/prefix and
        # exactly one pinned route can be consumed by this isolated client.
        if not isinstance(auth, FileAuth): raise WebmaniaError('configuration', 'Choose an explicit FileAuth mode.')
        invalid = False
        try:
            p = urlsplit(url)
            target = self._transport.base
            if p.scheme != target.scheme or p.hostname != target.hostname or p.port != target.port or p.username or p.password or p.fragment:
                invalid = True
            pairs = parse_qsl(p.query, keep_blank_values=True, strict_parsing=True)
            if len({k for k, _ in pairs}) != len(pairs): invalid = True
        except (ValueError, TypeError): invalid = True
        if invalid: raise WebmaniaError('validation', 'File URL must match the configured trusted origin without credentials or fragments.')
        query = dict(pairs)
        token = query.pop('token', None)
        if token is not None and (auth.mode != 'document_token' or token != auth.token):
            raise WebmaniaError('validation', 'A URL token must match the one explicit document token mode.')
        prefix = self._transport.base.path.rstrip('/')
        if prefix and not p.path.startswith(prefix + '/'):
            raise WebmaniaError('validation', 'File URL does not match the configured path prefix.')
        route = p.path[len(prefix):]
        for oid, record in OPERATIONS.items():
            if record['client'] != self._scope: continue
            pattern = re.escape(record['path'])
            names = re.findall(r'\{([^}]+)\}', record['path'])
            for name in names: pattern = pattern.replace(re.escape('{' + name + '}'), r'([^/%?#]+)')
            match = re.fullmatch(pattern, route)
            if match:
                if 'download' in query:
                    hint = record['query_schema'].get('properties', {}).get('download')
                    if not isinstance(hint, dict) or hint.get('type') != 'integer' or hint.get('const') != 1 or query['download'] != '1':
                        raise WebmaniaError('validation', 'The download URL hint must be the canonical value 1 on a supported route.')
                    query['download'] = 1
                params = dict(zip(names, match.groups()))
                for name in ['event']:
                    if name in params:
                        if not params[name].isdigit(): raise WebmaniaError('validation', 'Invalid event sequence.')
                        params[name] = int(params[name])
                return self._execute(oid, UNSET, params, query, options, auth)
        raise WebmaniaError('validation', 'File URL does not match a pinned fiscal route.')


class NfeFilesClient(NfeFilesMethods, FilesBase):
    _scope = 'NfeFiles'
    def __init__(self, *, trusted_origins, credentials=None, base_url='https://nfe.webmania.com.br', **options):
        headers = credential_headers(credentials, CompanyCredentials) if credentials is not None else {}
        super().__init__(base_url, headers, trusted_origins, **options)


class EmitterFilesClient(EmitterFilesMethods, FilesBase):
    _scope = 'EmitterFiles'
    def __init__(self, *, trusted_origins, issuer_token=None, base_url='https://api.webmania.com.br', **options):
        headers = bearer_headers(issuer_token) if issuer_token is not None else {}
        super().__init__(base_url, headers, trusted_origins, **options)


class ReportFilesClient(ReportFilesMethods, FilesBase):
    """Current report exports (fiscalDownloadReportV2) on one explicitly trusted API2 origin.

    The report URL returned by create_or_poll_report is a sensitive capability. Use
    ``download_url`` with the returned URL: only the configured origin and the pinned
    ``/relatorios/{uuid}`` route are accepted, and credentials are attached only for the
    explicit FileAuth mode (``anonymous``, ``company`` or ``issuer``).
    """
    _scope = 'ReportFiles'
    def __init__(self, *, trusted_origins, credentials=None, issuer_token=None, base_url='https://api.webmania.com.br', **options):
        self._company = credential_headers(credentials, CompanyCredentials) if credentials is not None else {}
        self._bearer = bearer_headers(issuer_token) if issuer_token is not None else {}
        super().__init__(base_url, {}, trusted_origins, **options)
        self._secrets += list(self._company.values()) + list(self._bearer.values())
        self._secrets += [v.removeprefix('Bearer ') for v in self._bearer.values()]


def _poll(fetch, completed, attempts, interval, deadline, options, *, report_capability=False):
    if not positive(attempts, True) or not positive(interval) or interval < 5 or not positive(deadline) or interval > sys.float_info.max or deadline > sys.float_info.max:
        raise WebmaniaError('configuration', 'Polling needs finite limits, positive attempts, and an interval of at least five seconds.')
    options = options or CallOptions()
    if not isinstance(options, CallOptions) or options.timeout is not None and (not positive(options.timeout) or options.timeout > sys.float_info.max):
        raise WebmaniaError('configuration', 'Expected valid finite CallOptions.')
    end = time.monotonic() + deadline
    for index in range(attempts):
        remaining = end - time.monotonic()
        if remaining <= 0: raise WebmaniaError('polling_timeout', 'Polling deadline expired.')
        result = fetch(replace(options, timeout=min(remaining, options.timeout or 30.0)))
        if completed(result): return result
        if report_capability and isinstance(result, dict):
            values = tuple(str(result[k]) for k in ['uuid', 'url', 'token'] if result.get(k) is not None)
            if isinstance(result.get('url'), str): values += tuple(location_diagnostic_values(result['url']))
            uuids = (str(result['uuid']),) if isinstance(result.get('uuid'), str) else ()
            options = replace(options, _known_capabilities=options._known_capabilities + values, _known_uuid_capabilities=options._known_uuid_capabilities + uuids)
        if index == attempts - 1: break
        wait = min(interval, max(0, end - time.monotonic()))
        if options.cancel is not None:
            if options.cancel.wait(wait): raise WebmaniaError('cancelled', 'Polling cancelled.')
        else: time.sleep(wait)
    raise WebmaniaError('polling_timeout', 'Polling attempt limit reached; no mutation was replayed.')
