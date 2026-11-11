"""Intentionally invalid consumers: every marked line must fail static analysis."""
from webmania.generated.api1_fiscal import NfeCancelRequest, NfeCorrectionRequest, Nfe55Customer, IbsCbs112120Request
from webmania.generated.api2_monitor_documents import MonitorImportRequest
from webmania.generated.api2_mdfe_issuance import MdfeFreightPaymentGroup

cancel_scalar: NfeCancelRequest = 42  # expect-error
correction_scalar: NfeCorrectionRequest = False  # expect-error
customer_scalar: Nfe55Customer = None  # expect-error
event_scalar: IbsCbs112120Request = ['not', 'an', 'event']  # expect-error
import_scalar: MonitorImportRequest = 'not-an-import'  # expect-error
freight_scalar: MdfeFreightPaymentGroup = 19.5  # expect-error
cancel_missing_reason: NfeCancelRequest = {'uuid': 'abcdefab-cdef-4abc-8def-abcdefabcdef'}  # expect-error
cancel_missing_selector: NfeCancelRequest = {'motivo': 'Synthetic reason'}  # expect-error
cancel_wrong_reason: NfeCancelRequest = {'uuid': 'abcdefab-cdef-4abc-8def-abcdefabcdef', 'motivo': 42}  # expect-error
import_missing_company: MonitorImportRequest = {'xml': '<synthetic/>'}  # expect-error

from typing import TYPE_CHECKING
from webmania import EmitterFilesClient, FileAuth
if TYPE_CHECKING:
    files: EmitterFilesClient
    pdf = files.get_nfse_pdf(identifier='abcdefab-cdef-4abc-8def-abcdefabcdef', auth=FileAuth('issuer'))
    unchecked_pdf_bytes: bytes = pdf.data  # expect-error
