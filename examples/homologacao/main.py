#!/usr/bin/env python3
"""Exemplo neutro de homologação (ambiente 2) com o SDK Python.

Lê a configuração somente de variáveis WEBMANIA_*, imprime uma linha JSON mascarada por passo
e nunca repete uma mutação. Sem WEBMANIA_LIVE=1 não faz nenhuma requisição (saída 77).
"""
import hashlib
import json
import os
import sys
import time
from urllib.parse import urlsplit

from webmania import (CompanyCredentials, EmitterClient, EmitterFilesClient, FileAuth, FileRedirectResponse,
                      NfeClient, NfeFilesClient, WebmaniaError)

BLOCKED = 77
SCOPES = ('readonly', 'nfe', 'nfse', 'all')
TERMINAL_NFE = ('aprovado', 'reprovado', 'denegado', 'cancelado')
POLL_ATTEMPTS, POLL_INTERVAL = 24, 5.0
FAILED = []


def ref(value):
    return hashlib.sha256(str(value).encode('utf-8')).hexdigest()[:12] if value not in (None, '') else None


def emit(step, operation, ok, *, status=None, outcome=None, kind=None, reference=None, **extra):
    line = {'step': step, 'operation': operation, 'ok': ok, 'http_status': status, 'outcome': outcome,
            'kind': kind, 'ref': reference, **extra}
    if not ok:
        FAILED.append(step)
    print(json.dumps(line, sort_keys=True), flush=True)


def ledger(model, identifier, status, operation):
    path = os.environ.get('WEBMANIA_LIVE_LEDGER')
    if not path or identifier in (None, ''):
        return
    with open(path, 'a', encoding='utf-8') as handle:
        handle.write(json.dumps({'model': model, 'identifier': str(identifier), 'status': status, 'operation': operation}) + '\n')


def file_summary(result):
    if isinstance(result, FileRedirectResponse):
        return {'file': {'redirect': True}}
    data = result.data
    fmt = 'pdf' if data.startswith(b'%PDF-') else 'zip' if data.startswith(b'PK') else \
        'xml' if data.lstrip(b'\xef\xbb\xbf \t\r\n')[:1] == b'<' else 'other'
    return {'file': {'size': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'format': fmt}}


class Unknown(Exception):
    """A sent mutation whose result is unknown: stop, never repeat."""


def call(step, operation, function, *, reference=None, mutation=False, files=False):
    try:
        result = function()
    except WebmaniaError as error:
        emit(step, operation, False, status=error.status, outcome=error.outcome, kind=error.kind, reference=reference)
        if mutation and error.outcome == 'unknown':
            raise Unknown(step) from None
        return None
    extra = file_summary(result) if files else {}
    status = getattr(result, 'status', 200) if files else 200
    emit(step, operation, True, status=status, reference=reference, **extra)
    return result


def blocked(reason):
    print(json.dumps({'result': 'blocked', 'reason': reason}), flush=True)
    return BLOCKED


def origin(url):
    parts = urlsplit(url)
    return parts.scheme + '://' + parts.netloc


def poll(step, operation, fetch, done, reference):
    result = None
    for attempt in range(POLL_ATTEMPTS):
        result = call(step, operation, fetch, reference=reference)
        if isinstance(result, dict) and done(str(result.get('status', ''))):
            return result
        if attempt < POLL_ATTEMPTS - 1:
            time.sleep(POLL_INTERVAL)
    return result


def payload(name):
    path = os.environ.get(name)
    if not path:
        return None
    with open(path, encoding='utf-8') as handle:
        value = json.load(handle)
    return value if isinstance(value, dict) and value.get('ambiente') == 2 and type(value.get('ambiente')) is int else None


def issue(step, operation, function, model, document):
    try:
        return call(step, operation, function, mutation=True, reference=ref(document.get('ID')))
    except Unknown:
        ledger(model, document.get('ID') or 'unidentified', 'unknown', operation)
        raise


def cancel(step, operation, function, model, uuid, reference):
    try:
        return call(step, operation, function, mutation=True, reference=reference)
    except Unknown:
        ledger(model, uuid, 'unknown', operation)
        raise


def nfe_cycle(nfe, files, document):
    issued = issue('nfe.issue', 'nfeIssueDocument', lambda: nfe.issue_document(document), 'nfe', document)
    if not isinstance(issued, dict) or not issued.get('uuid'):
        return
    uuid = issued['uuid']
    reference = ref(uuid)
    ledger('nfe', uuid, str(issued.get('status', 'processando')), 'nfeIssueDocument')
    current = poll('nfe.consult', 'nfeGetDocument', lambda: nfe.get_document(query={'uuid': uuid}),
                   lambda s: s in TERMINAL_NFE, reference)
    status = str(current.get('status', '')) if isinstance(current, dict) else ''
    if status != 'aprovado':
        ledger('nfe', uuid, status or 'unknown', 'nfeGetDocument')
        return
    try:
        auth = FileAuth('company')
        call('nfe.query', 'nfeQueryDocument', lambda: nfe.query_document({'uuid': uuid}), reference=reference)
        call('nfe.danfe', 'nfeDownloadDanfe', lambda: files.download_danfe(identifier=uuid, auth=auth), reference=reference, files=True)
        call('nfe.danfe_simple', 'nfeDownloadSimpleDanfe', lambda: files.download_simple_danfe(identifier=uuid, auth=auth), reference=reference, files=True)
        call('nfe.xml', 'nfeDownloadXml', lambda: files.download_xml(identifier=uuid, auth=auth), reference=reference, files=True)
    finally:
        # An approved document is always cancelled, even after a failed step above.
        cancelled = cancel('nfe.cancel', 'nfeCancelDocument',
                           lambda: nfe.cancel_document({'uuid': uuid, 'motivo': 'Cancelamento de teste em homologacao.'}),
                           'nfe', uuid, reference)
    if cancelled is None:
        ledger('nfe', uuid, 'aprovado', 'nfeCancelDocument')
        return
    final = poll('nfe.consult_cancelled', 'nfeGetDocument', lambda: nfe.get_document(query={'uuid': uuid}),
                 lambda s: s == 'cancelado', reference)
    status = str(final.get('status', '')) if isinstance(final, dict) else 'unknown'
    ledger('nfe', uuid, status, 'nfeCancelDocument')
    if status != 'cancelado':
        # Only a consult that shows the cancellation counts as success.
        emit('nfe.consult_cancelled', 'nfeGetDocument', False, kind='not_cancelled', reference=reference)
        return
    call('nfe.cancellation_xml', 'nfeDownloadCancellationXml',
         lambda: files.download_cancellation_xml(identifier=uuid, auth=FileAuth('company')), reference=reference, files=True)


def nfse_identifier(result):
    if not isinstance(result, dict):
        return None
    if result.get('uuid'):
        return result['uuid']
    items = result.get('info_nfse')
    return items[0].get('uuid') if isinstance(items, list) and items and isinstance(items[0], dict) else None


def nfse_cycle(emitter, files, document):
    issued = issue('nfse.issue', 'emitterIssueNfse', lambda: emitter.issue_nfse(document), 'nfse', document)
    uuid = nfse_identifier(issued)
    if not uuid:
        return
    reference = ref(uuid)
    ledger('nfse', uuid, str(issued.get('status', 'processando')), 'emitterIssueNfse')
    current = poll('nfse.consult', 'emitterGetNfse', lambda: emitter.get_nfse(identifier=uuid),
                   lambda s: s not in ('', 'processando', 'pendente'), reference)
    status = str(current.get('status', '')) if isinstance(current, dict) else ''
    if status != 'aprovado':
        ledger('nfse', uuid, status or 'unknown', 'emitterGetNfse')
        return
    try:
        auth = FileAuth('issuer')
        call('nfse.xml', 'fileGetNfseXml', lambda: files.get_nfse_xml(identifier=uuid, auth=auth), reference=reference, files=True)
        for step, operation, field, method in [('nfse.pdf', 'fileGetNfsePdf', 'pdf_nfse', files.get_nfse_pdf),
                                               ('nfse.rps_pdf', 'fileGetNfseRpsPdf', 'pdf_rps', files.get_nfse_rps_pdf)]:
            if current.get(field):
                call(step, operation, lambda method=method: method(identifier=uuid, auth=auth), reference=reference, files=True)
            else:
                emit(step, operation, True, kind='not_offered', reference=reference)
    finally:
        cancelled = cancel('nfse.cancel', 'emitterCancelNfse',
                           lambda: emitter.cancel_nfse({'uuid': uuid, 'motivo': '1', 'justificativa': 'Cancelamento de teste em homologacao.'}),
                           'nfse', uuid, reference)
    if cancelled is None:
        ledger('nfse', uuid, 'aprovado', 'emitterCancelNfse')
        return
    final = poll('nfse.consult_cancelled', 'emitterGetNfse', lambda: emitter.get_nfse(identifier=uuid),
                 lambda s: s == 'cancelado', reference)
    status = str(final.get('status', 'unknown')) if isinstance(final, dict) else 'unknown'
    ledger('nfse', uuid, status, 'emitterCancelNfse')
    if status != 'cancelado':
        emit('nfse.consult_cancelled', 'emitterGetNfse', False, kind='not_cancelled', reference=reference)


def main():
    env = os.environ
    if env.get('WEBMANIA_LIVE') != '1':
        print(json.dumps({'result': 'blocked'}), flush=True)
        return BLOCKED
    api1 = env.get('WEBMANIA_API1_BASE_URL', 'https://webmania.com.br/api')
    files_base = env.get('WEBMANIA_FILES_BASE_URL', 'https://nfe.webmania.com.br')
    api2 = env.get('WEBMANIA_API2_BASE_URL', 'https://api.webmania.com.br')
    scope = env.get('WEBMANIA_LIVE_SCOPE', 'readonly')
    if scope not in SCOPES:
        return blocked('scope')
    # The allow list is required: without it no origin is trusted (fail closed, before any credential).
    allowed = {h.strip().lower() for h in env.get('WEBMANIA_LIVE_ALLOWED_HOSTS', '').split(',') if h.strip()}
    if not allowed:
        return blocked('allowed_hosts')
    if any((urlsplit(u).hostname or '').lower() not in allowed for u in (api1, files_base, api2)):
        return blocked('origin_not_allowed')
    names = ['WEBMANIA_CONSUMER_KEY', 'WEBMANIA_CONSUMER_SECRET', 'WEBMANIA_ACCESS_TOKEN', 'WEBMANIA_ACCESS_TOKEN_SECRET', 'WEBMANIA_ISSUER_TOKEN']
    if any(not env.get(n) for n in names):
        return blocked('credentials')
    nfe_document = payload('WEBMANIA_LIVE_NFE_PAYLOAD') if scope in ('nfe', 'all') else None
    nfse_document = payload('WEBMANIA_LIVE_NFSE_PAYLOAD') if scope in ('nfse', 'all') else None
    if scope in ('nfe', 'all') and nfe_document is None or scope in ('nfse', 'all') and nfse_document is None:
        return blocked('payload')
    if scope != 'readonly':
        # The ledger must be writable before the first mutation; existing content is preserved.
        path = env.get('WEBMANIA_LIVE_LEDGER')
        if not path:
            return blocked('ledger')
        try:
            os.close(os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o600))
        except OSError:
            return blocked('ledger')
    company = CompanyCredentials(env['WEBMANIA_CONSUMER_KEY'], env['WEBMANIA_CONSUMER_SECRET'],
                                 env['WEBMANIA_ACCESS_TOKEN'], env['WEBMANIA_ACCESS_TOKEN_SECRET'])
    issuer = env['WEBMANIA_ISSUER_TOKEN']
    try:
        with NfeClient(company, base_url=api1) as nfe, EmitterClient(issuer, base_url=api2) as emitter, \
                NfeFilesClient(credentials=company, base_url=files_base, trusted_origins=[origin(files_base)]) as nfe_files, \
                EmitterFilesClient(issuer_token=issuer, base_url=api2, trusted_origins=[origin(api2)]) as emitter_files:
            call('readonly.sefaz', 'nfeGetSefazStatus', nfe.get_sefaz_status)
            call('readonly.certificate', 'nfeGetCertificateValidity', nfe.get_certificate_validity)
            call('readonly.tax_classes', 'nfeListTaxClasses', nfe.list_tax_classes)
            call('readonly.nfse_provider', 'emitterGetNfseProviderStatus', emitter.get_nfse_provider_status)
            if nfe_document is not None:
                nfe_cycle(nfe, nfe_files, nfe_document)
            if nfse_document is not None:
                nfse_cycle(emitter, emitter_files, nfse_document)
    except Unknown:
        return 1
    except WebmaniaError as error:
        emit('configuration', None, False, kind=error.kind)
        return 1
    return 1 if FAILED else 0


if __name__ == '__main__':
    sys.exit(main())
