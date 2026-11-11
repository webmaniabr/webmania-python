"""Installed-package static typing smoke checks (not a network script)."""
from typing import TYPE_CHECKING, assert_type
from webmania import CompanyCredentials, NfeClient, MonitorClient, with_additional_fields, EmitterFilesClient, FileAuth, FileResponse, FileRedirectResponse
from webmania.generated.api1_fiscal import NfeProduct, FiscalCompanyUpdateRequest, NfeCertificateValidity, Api1Error
from webmania.generated.api2_monitor_reads import MonitorCompanyPage

if TYPE_CHECKING:
    credentials = CompanyCredentials('synthetic', 'synthetic', 'synthetic', 'synthetic')
    product: NfeProduct = {'nome': 'Synthetic', 'codigo': '01', 'ncm': '00000000', 'quantidade': '1.0000', 'unidade': 'UN', 'subtotal': '0.10', 'total': '0.10', 'origem': 0}
    update: FiscalCompanyUpdateRequest = {'cnae': None, 'email': 'synthetic@example.invalid'}
    client = NfeClient(credentials)
    assert_type(client.get_certificate_validity(), NfeCertificateValidity | Api1Error)
    monitor = MonitorClient('synthetic')
    assert_type(monitor.list_companies(), MonitorCompanyPage)

    assert_type(with_additional_fields(update, {'future_option': False}), FiscalCompanyUpdateRequest)

if TYPE_CHECKING:
    files: EmitterFilesClient
    pdf = files.get_nfse_pdf(identifier='abcdefab-cdef-4abc-8def-abcdefabcdef', auth=FileAuth('issuer'))
    assert_type(pdf, FileResponse | FileRedirectResponse)
    if isinstance(pdf, FileRedirectResponse):
        assert_type(pdf.location.reveal(), str)
    else:
        assert_type(pdf.data, bytes)
    assert_type(files.get_nfse_xml(identifier='abcdefab-cdef-4abc-8def-abcdefabcdef', auth=FileAuth('issuer')), FileResponse)
