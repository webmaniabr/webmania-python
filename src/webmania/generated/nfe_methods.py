"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api1_fiscal as m0
from . import api1_fiscal as m1
from . import api1_fiscal as m2
from . import api1_fiscal as m3
from . import api1_fiscal as m4
from . import api1_fiscal as m5
from . import api1_fiscal as m6
from . import api1_fiscal as m7
from . import api1_fiscal as m8
from . import api1_fiscal as m9
from . import api1_fiscal as m10
from . import api1_fiscal as m11
from . import api1_fiscal as m12
from . import api1_fiscal as m13
from . import api1_fiscal as m14
from . import api1_fiscal as m15
from . import api1_fiscal as m16
from . import api1_fiscal as m17
from . import api1_fiscal as m18
from . import api1_fiscal as m19
from . import api1_fiscal as m20

class NfeMethods:
    _execute: Any

    def get_certificate_validity(self, *, options: CallOptions | None = None) -> m0.nfeGetCertificateValidityResponse:
        """Read remaining A1 certificate validity. Contract conditions remain applicable."""
        return self._execute('nfeGetCertificateValidity', UNSET, {}, None, options, None)

    def get_sefaz_status(self, *, options: CallOptions | None = None) -> m1.nfeGetSefazStatusResponse:
        """Read SEFAZ availability. Contract conditions remain applicable."""
        return self._execute('nfeGetSefazStatus', UNSET, {}, None, options, None)

    def get_document(self, *, query: m2.nfeGetDocumentQuery | None = None, options: CallOptions | None = None) -> m2.nfeGetDocumentResponse:
        """Query own document by access key, UUID or customer ID. Contract conditions remain applicable."""
        return self._execute('nfeGetDocument', UNSET, {}, query, options, None)

    def query_document(self, request: m3.NfeLookupRequest, *, options: CallOptions | None = None) -> m3.nfeQueryDocumentResponse:
        """Query own document with JSON body (legacy compatibility). Contract conditions remain applicable."""
        return self._execute('nfeQueryDocument', request, {}, None, options, None)

    def create_correction(self, request: m4.NfeCorrectionRequest, *, options: CallOptions | None = None) -> m4.nfeCreateCorrectionResponse:
        """Register correction letter. Contract conditions remain applicable."""
        return self._execute('nfeCreateCorrection', request, {}, None, options, None)

    def create_manifestation(self, request: m5.NfeManifestationRequest, *, options: CallOptions | None = None) -> m5.nfeCreateManifestationResponse:
        """Register recipient manifestation. Contract conditions remain applicable."""
        return self._execute('nfeCreateManifestation', request, {}, None, options, None)

    def cancel_document(self, request: m6.NfeCancelRequest, *, options: CallOptions | None = None) -> m6.nfeCancelDocumentResponse:
        """Cancel NF-e/NFC-e; optional NFC-e replacement. Contract conditions remain applicable."""
        return self._execute('nfeCancelDocument', request, {}, None, options, None)

    def void_numbering(self, request: m7.NfeVoidRequest, *, options: CallOptions | None = None) -> m7.nfeVoidNumberingResponse:
        """Void unused NF-e/NFC-e numbering. Contract conditions remain applicable."""
        return self._execute('nfeVoidNumbering', request, {}, None, options, None)

    def create_payment_event(self, request: m8.NfePaymentEventRequest, *, options: CallOptions | None = None) -> m8.nfeCreatePaymentEventResponse:
        """Register financial reconciliation ECONF. Contract conditions remain applicable."""
        return self._execute('nfeCreatePaymentEvent', request, {}, None, options, None)

    def cancel_payment_event(self, request: m9.NfePaymentEventCancelRequest, *, options: CallOptions | None = None) -> m9.nfeCancelPaymentEventResponse:
        """Cancel ECONF using its event UUID. Contract conditions remain applicable."""
        return self._execute('nfeCancelPaymentEvent', request, {}, None, options, None)

    def cancel_ibs_cbs_event(self, request: m10.NfeIbsCbsEventCancelRequest, *, options: CallOptions | None = None) -> m10.nfeCancelIbsCbsEventResponse:
        """Cancel authorized IBS/CBS event by UUID. Contract conditions remain applicable."""
        return self._execute('nfeCancelIbsCbsEvent', request, {}, None, options, None)

    def list_tax_classes(self, *, options: CallOptions | None = None) -> m11.nfeListTaxClassesResponse:
        """List configured fiscal tax classes. Contract conditions remain applicable."""
        return self._execute('nfeListTaxClasses', UNSET, {}, None, options, None)

    def delete_tax_classes(self, request: m12.TaxClassDeleteRequest, *, options: CallOptions | None = None) -> m12.nfeDeleteTaxClassesResponse:
        """Delete one or more fiscal tax classes. Contract conditions remain applicable."""
        return self._execute('nfeDeleteTaxClasses', request, {}, None, options, None)

    def save_tax_classes(self, request: m13.FiscalTaxClassRequest, *, options: CallOptions | None = None) -> m13.nfeSaveTaxClassesResponse:
        """Create/update fiscal tax class(es). Contract conditions remain applicable."""
        return self._execute('nfeSaveTaxClasses', request, {}, None, options, None)

    def issue_document(self, request: m14.NfeIssueRequest, *, options: CallOptions | None = None) -> m14.nfeIssueDocumentResponse:
        """Issue NF-e or NFC-e. Contract conditions remain applicable."""
        return self._execute('nfeIssueDocument', request, {}, None, options, None)

    def issue_return(self, request: m15.NfeReturnRequest, *, options: CallOptions | None = None) -> m15.nfeIssueReturnResponse:
        """Issue return or reversal NF-e. Contract conditions remain applicable."""
        return self._execute('nfeIssueReturn', request, {}, None, options, None)

    def issue_adjustment(self, request: m16.NfeAdjustmentRequest, *, options: CallOptions | None = None) -> m16.nfeIssueAdjustmentResponse:
        """Issue adjustment NF-e. Contract conditions remain applicable."""
        return self._execute('nfeIssueAdjustment', request, {}, None, options, None)

    def issue_complement(self, request: m17.NfeComplementRequest, *, options: CallOptions | None = None) -> m17.nfeIssueComplementResponse:
        """Issue complementary NF-e. Contract conditions remain applicable."""
        return self._execute('nfeIssueComplement', request, {}, None, options, None)

    def update_company(self, request: m18.FiscalCompanyUpdateRequest, *, options: CallOptions | None = None) -> m18.fiscalUpdateCompanyResponse:
        """Update issuer company/address/model configuration/certificate. Contract conditions remain applicable."""
        return self._execute('fiscalUpdateCompany', request, {}, None, options, None)

    def create_or_poll_report(self, request: m19.FiscalReportRequest, *, options: CallOptions | None = None) -> m19.fiscalCreateOrPollReportResponse:
        """Request or inspect asynchronous fiscal report. Contract conditions remain applicable."""
        return self._execute('fiscalCreateOrPollReport', request, {}, None, options, None)

    def create_ibs_cbs_event(self, request: m20.NfeIbsCbsEventRequest, *, options: CallOptions | None = None) -> m20.nfeCreateIbsCbsEventResponse:
        """Register one of eleven IBS/CBS event variants. Contract conditions remain applicable."""
        return self._execute('nfeCreateIbsCbsEvent', request, {}, None, options, None)
