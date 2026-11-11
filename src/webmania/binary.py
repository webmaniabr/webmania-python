"""Conservative file envelope checks, without executing XML or unpacking archives."""
import re
from .errors import WebmaniaError
from .types import FileResponse
from .pdf_inspection import encryption_entry
from .pdf_structure import pdf_document
from .file_inspection import xml_document, zip_parts, xlsx_package


ZIP_SIGNATURES = (b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08')
XLSX = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
REPORT_OPERATIONS = frozenset({'fiscalDownloadReport', 'fiscalDownloadReportV2'})


def xml_root(data):
    return xml_document(data).tag.rsplit('}', 1)[-1]


def _markup_or_json(data):
    """True when a body starts like XML, HTML or JSON (after a BOM and whitespace)."""
    head = data[:1024]
    for bom, codec in [(b'\xef\xbb\xbf', 'utf-8'), (b'\xff\xfe', 'utf-16-le'), (b'\xfe\xff', 'utf-16-be')]:
        if head.startswith(bom):
            head = head[len(bom):].decode(codec, 'ignore').encode('utf-8', 'ignore')
            break
    return head.lstrip(b' \t\r\n').startswith((b'<', b'{'))


def _check_pdf(status, data):
    if not data.startswith(b'%PDF-') or b'%%EOF' not in data[-4096:]:
        raise WebmaniaError('protocol', 'Expected a PDF envelope.', status=status)
    if encryption_entry(data):
        raise WebmaniaError('protected_file', 'A PDF encryption entry was detected.', status=status)
    invalid_pdf = False
    try: pdf_document(data)
    except (ValueError, OverflowError, RecursionError, TypeError): invalid_pdf = True
    if invalid_pdf: raise WebmaniaError('protocol', 'Malformed or unsupported classic PDF structure.', status=status)


def report_result(operation_id, status, headers, data, allowed):
    """Report files: the declared media type and the bytes must agree.

    Only the legacy report operation accepts ``text/xml``: a ZIP local-file signature is XLSX,
    any other report body is CSV returned byte-exact (never decoded). An XML document, an HTML
    page or a JSON body is refused as a report. ``FileResponse.media_type`` carries the detected
    format in that case.
    """
    media = headers.get('content-type', '').split(';', 1)[0].strip().lower()
    if not allowed: raise WebmaniaError('protocol', 'Unexpected successful fiscal file status.', status=status)
    if media not in allowed:
        raise WebmaniaError('protocol', 'Unexpected fiscal file media type.', status=status)
    if not data:
        raise WebmaniaError('protocol', 'Empty fiscal file response.', status=status)
    detected = media
    invalid = False
    try:
        if media == 'text/xml' and operation_id == 'fiscalDownloadReport':
            if data.startswith(b'PK\x03\x04'):
                xlsx_package(zip_parts(data)); detected = XLSX
            elif b'\x00' in data or _markup_or_json(data):
                raise WebmaniaError('protocol', 'A report labeled text/xml must be CSV or XLSX; XML, HTML and JSON bodies are refused.', status=status)
            else:
                detected = 'text/csv'
        elif media in ['application/zip', 'application/x-zip-compressed']:
            if not data.startswith(ZIP_SIGNATURES): raise ValueError('signature')
            zip_parts(data)
        elif media == XLSX:
            if not data.startswith(b'PK\x03\x04'): raise ValueError('signature')
            xlsx_package(zip_parts(data))
        elif media == 'application/pdf':
            _check_pdf(status, data)
        elif media == 'text/csv':
            if data.startswith(ZIP_SIGNATURES) or b'\x00' in data or _markup_or_json(data): raise ValueError('csv')
        elif media in ['text/html', 'application/xml', 'text/xml']:
            # Declared text renderings of a report; never executed or parsed as fiscal XML.
            if data.startswith(ZIP_SIGNATURES) or b'\x00' in data: raise ValueError('text')
            if media != 'text/html': xml_document(data)
        elif media != 'application/octet-stream':
            raise ValueError('media')
    except (ValueError, OverflowError, RecursionError, TypeError): invalid = True
    if invalid: raise WebmaniaError('protocol', 'Malformed or unsupported fiscal file structure.', status=status)
    return FileResponse(data, detected, status, headers.get('content-disposition'))


def file_result(status, headers, data, allowed, operation_id=None):
    if operation_id in REPORT_OPERATIONS:
        return report_result(operation_id, status, headers, data, allowed)
    media = headers.get('content-type', '').split(';', 1)[0].strip().lower()
    if not allowed: raise WebmaniaError('protocol', 'Unexpected successful fiscal file status.', status=status)
    if data[:128].lstrip().lower().startswith((b'<html', b'<!doctype html')):
        raise WebmaniaError('protocol', 'HTML cannot be promoted to a fiscal file.', status=status)
    if media not in allowed:
        raise WebmaniaError('protocol', 'Unexpected fiscal file media type.', status=status)
    if media in ['application/zip', 'application/x-zip-compressed'] and any(m in allowed for m in ['application/xml', 'text/xml']):
        raise WebmaniaError('protected_file', 'XML was returned as an archive; the plaintext XML was not delivered.', status=status)
    if media in ['application/xml', 'text/xml'] and data.startswith((b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08')):
        raise WebmaniaError('protected_file', 'XML was returned as an archive; the plaintext XML was not delivered.', status=status)
    invalid_structure = False
    try:
        if media in ['application/xml', 'text/xml']: xml_document(data)
        elif media in ['application/zip', 'application/x-zip-compressed']: zip_parts(data)
        elif media == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': xlsx_package(zip_parts(data))
    except (ValueError, OverflowError, RecursionError): invalid_structure = True
    if invalid_structure: raise WebmaniaError('protocol', 'Malformed or unsupported fiscal file structure.', status=status)
    if media in ['application/xml', 'text/xml']:
        if data.startswith((b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08')):
            raise WebmaniaError('protected_file', 'XML was returned as an archive; the plaintext XML was not delivered.', status=status)
        if xml_root(data) not in {'nfeProc', 'NFe', 'procEventoNFe', 'evento', 'retEvento', 'cteProc', 'CTe', 'procEventoCTe', 'mdfeProc', 'MDFe', 'procEventoMDFe', 'nfcomProc', 'NFCom', 'procEventoNFCom', 'dceProc', 'DCe', 'procEventoDCe', 'CompNfse', 'Nfse', 'NFSe', 'ConsultarNfseResposta', 'nfseProc', 'procEventoNFSe', 'DPS', 'nfse', 'retConsSitNFe', 'procCancNFe'}:
            raise WebmaniaError('protocol', 'Expected a recognizable fiscal XML envelope.', status=status)
    elif media == 'application/pdf':
        _check_pdf(status, data)
        # Cryptographic password/decryption absence remains unestablished.
    elif media in ['application/zip', 'application/x-zip-compressed']:
        if not data.startswith((b'PK\x03\x04', b'PK\x05\x06', b'PK\x07\x08')):
            raise WebmaniaError('protocol', 'Expected a ZIP envelope.', status=status)
    elif not data:
        raise WebmaniaError('protocol', 'Empty fiscal file response.', status=status)
    return FileResponse(data, media, status, headers.get('content-disposition'))
