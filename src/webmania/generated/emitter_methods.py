"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api2_cte_issuance as m0
from . import api2_cte_issuance as m1
from . import api2_cte_issuance as m2
from . import api2_cte_issuance as m3
from . import api2_cte_issuance as m4
from . import api2_cte_issuance as m5
from . import api2_cte_issuance as m6
from . import api2_cte_issuance as m7
from . import api2_cte_issuance as m8
from . import api2_cte_issuance as m9
from . import api2_dce_issuance as m10
from . import api2_dce_issuance as m11
from . import api2_dce_issuance as m12
from . import api2_emitter_reads as m13
from . import api2_emitter_reads as m14
from . import api2_emitter_reads as m15
from . import api2_emitter_reads as m16
from . import api2_emitter_reads as m17
from . import api2_emitter_reads as m18
from . import api2_mdfe_issuance as m19
from . import api2_mdfe_issuance as m20
from . import api2_mdfe_issuance as m21
from . import api2_mdfe_issuance as m22
from . import api2_mdfe_issuance as m23
from . import api2_nfcom_issuance as m24
from . import api2_nfcom_issuance as m25
from . import api2_nfse_issuance as m26
from . import api2_nfse_issuance as m27
from . import api2_nfse_issuance as m28

class EmitterMethods:
    _execute: Any

    def issue_cte(self, request: m0.EmitterIssueCtePayload, *, options: CallOptions | None = None) -> m0.emitterIssueCteResponse:
        """emitterIssueCte. Contract conditions remain applicable."""
        return self._execute('emitterIssueCte', request, {}, None, options, None)

    def issue_simplified_cte(self, request: m1.EmitterIssueSimplifiedCtePayload, *, options: CallOptions | None = None) -> m1.emitterIssueSimplifiedCteResponse:
        """emitterIssueSimplifiedCte. Contract conditions remain applicable."""
        return self._execute('emitterIssueSimplifiedCte', request, {}, None, options, None)

    def cancel_cte(self, request: m2.EmitterCancelCtePayload, *, options: CallOptions | None = None) -> m2.emitterCancelCteResponse:
        """emitterCancelCte. Contract conditions remain applicable."""
        return self._execute('emitterCancelCte', request, {}, None, options, None)

    def correct_cte(self, request: m3.EmitterCorrectCtePayload, *, options: CallOptions | None = None) -> m3.emitterCorrectCteResponse:
        """emitterCorrectCte. Contract conditions remain applicable."""
        return self._execute('emitterCorrectCte', request, {}, None, options, None)

    def confirm_cte_delivery(self, request: m4.EmitterConfirmCteDeliveryPayload, *, options: CallOptions | None = None) -> m4.emitterConfirmCteDeliveryResponse:
        """emitterConfirmCteDelivery. Contract conditions remain applicable."""
        return self._execute('emitterConfirmCteDelivery', request, {}, None, options, None)

    def cancel_cte_delivery(self, request: m5.EmitterCancelCteDeliveryPayload, *, options: CallOptions | None = None) -> m5.emitterCancelCteDeliveryResponse:
        """emitterCancelCteDelivery. Contract conditions remain applicable."""
        return self._execute('emitterCancelCteDelivery', request, {}, None, options, None)

    def link_cte_payment(self, request: m6.EmitterLinkCtePaymentPayload, *, options: CallOptions | None = None) -> m6.emitterLinkCtePaymentResponse:
        """emitterLinkCtePayment. Contract conditions remain applicable."""
        return self._execute('emitterLinkCtePayment', request, {}, None, options, None)

    def cancel_cte_payment_link(self, request: m7.EmitterCancelCtePaymentLinkPayload, *, options: CallOptions | None = None) -> m7.emitterCancelCtePaymentLinkResponse:
        """emitterCancelCtePaymentLink. Contract conditions remain applicable."""
        return self._execute('emitterCancelCtePaymentLink', request, {}, None, options, None)

    def get_cte(self, *, identifier: m8.emitterGetCteIdentifierParameter, options: CallOptions | None = None) -> m8.emitterGetCteResponse:
        """emitterGetCte. Contract conditions remain applicable."""
        return self._execute('emitterGetCte', UNSET, {'identifier': identifier}, None, options, None)

    def get_cte_payment_events(self, *, identifier: m9.emitterGetCtePaymentEventsIdentifierParameter, options: CallOptions | None = None) -> m9.emitterGetCtePaymentEventsResponse:
        """emitterGetCtePaymentEvents. Contract conditions remain applicable."""
        return self._execute('emitterGetCtePaymentEvents', UNSET, {'identifier': identifier}, None, options, None)

    def issue_dce(self, request: m10.EmitterIssueDcePayload, *, options: CallOptions | None = None) -> m10.emitterIssueDceResponse:
        """emitterIssueDce. Contract conditions remain applicable."""
        return self._execute('emitterIssueDce', request, {}, None, options, None)

    def cancel_dce(self, request: m11.EmitterCancelDcePayload, *, options: CallOptions | None = None) -> m11.emitterCancelDceResponse:
        """emitterCancelDce. Contract conditions remain applicable."""
        return self._execute('emitterCancelDce', request, {}, None, options, None)

    def get_dce(self, *, identifier: m12.emitterGetDceIdentifierParameter, options: CallOptions | None = None) -> m12.emitterGetDceResponse:
        """emitterGetDce. Contract conditions remain applicable."""
        return self._execute('emitterGetDce', UNSET, {'identifier': identifier}, None, options, None)

    def get_nfse_provider_status(self, *, query: m13.emitterGetNfseProviderStatusQuery | None = None, options: CallOptions | None = None) -> m13.emitterGetNfseProviderStatusResponse:
        """Read the company NFSe provider capabilities. Contract conditions remain applicable."""
        return self._execute('emitterGetNfseProviderStatus', UNSET, {}, query, options, None)

    def get_nfcom_service_status(self, *, options: CallOptions | None = None) -> m14.emitterGetNfcomServiceStatusResponse:
        """Read production SEFAZ NFCom service availability. Contract conditions remain applicable."""
        return self._execute('emitterGetNfcomServiceStatus', UNSET, {}, None, options, None)

    def get_nfse(self, *, identifier: m15.emitterGetNfseIdentifierParameter, options: CallOptions | None = None) -> m15.emitterGetNfseResponse:
        """Consult a company-owned NFSe or RPS batch. Contract conditions remain applicable."""
        return self._execute('emitterGetNfse', UNSET, {'identifier': identifier}, None, options, None)

    def get_nfcom(self, *, identifier: m16.emitterGetNfcomIdentifierParameter, options: CallOptions | None = None) -> m16.emitterGetNfcomResponse:
        """Get a company-owned NFCom16. Contract conditions remain applicable."""
        return self._execute('emitterGetNfcom', UNSET, {'identifier': identifier}, None, options, None)

    def get_nfcom_payment_events(self, *, identifier: m17.emitterGetNfcomPaymentEventsIdentifierParameter, options: CallOptions | None = None) -> m17.emitterGetNfcomPaymentEventsResponse:
        """Read NFCom payment-event metadata. Contract conditions remain applicable."""
        return self._execute('emitterGetNfcomPaymentEvents', UNSET, {'identifier': identifier}, None, options, None)

    def manifest_nfse(self, request: m18.NfseManifestationRequest, *, options: CallOptions | None = None) -> m18.emitterManifestNfseResponse:
        """Manifest participation in a national NFSe. Contract conditions remain applicable."""
        return self._execute('emitterManifestNfse', request, {}, None, options, None)

    def issue_mdfe(self, request: m19.EmitterIssueMdfePayload, *, options: CallOptions | None = None) -> m19.emitterIssueMdfeResponse:
        """emitterIssueMdfe. Contract conditions remain applicable."""
        return self._execute('emitterIssueMdfe', request, {}, None, options, None)

    def close_mdfe(self, request: m20.EmitterCloseMdfePayload, *, options: CallOptions | None = None) -> m20.emitterCloseMdfeResponse:
        """emitterCloseMdfe. Contract conditions remain applicable."""
        return self._execute('emitterCloseMdfe', request, {}, None, options, None)

    def cancel_mdfe(self, request: m21.EmitterCancelMdfePayload, *, options: CallOptions | None = None) -> m21.emitterCancelMdfeResponse:
        """emitterCancelMdfe. Contract conditions remain applicable."""
        return self._execute('emitterCancelMdfe', request, {}, None, options, None)

    def add_mdfe_conductor(self, request: m22.EmitterAddMdfeConductorPayload, *, options: CallOptions | None = None) -> m22.emitterAddMdfeConductorResponse:
        """emitterAddMdfeConductor. Contract conditions remain applicable."""
        return self._execute('emitterAddMdfeConductor', request, {}, None, options, None)

    def get_mdfe(self, *, key: m23.emitterGetMdfeKeyParameter, options: CallOptions | None = None) -> m23.emitterGetMdfeResponse:
        """emitterGetMdfe. Contract conditions remain applicable."""
        return self._execute('emitterGetMdfe', UNSET, {'key': key}, None, options, None)

    def issue_nfcom(self, request: m24.EmitterIssueNfcomPayload, *, options: CallOptions | None = None) -> m24.emitterIssueNfcomResponse:
        """emitterIssueNfcom24. Contract conditions remain applicable."""
        return self._execute('emitterIssueNfcom', request, {}, None, options, None)

    def cancel_nfcom(self, request: m25.EmitterCancelNfcomPayload, *, options: CallOptions | None = None) -> m25.emitterCancelNfcomResponse:
        """emitterCancelNfcom25. Contract conditions remain applicable."""
        return self._execute('emitterCancelNfcom', request, {}, None, options, None)

    def issue_nfse(self, request: m26.EmitterIssueNfsePayload, *, options: CallOptions | None = None) -> m26.emitterIssueNfseResponse:
        """emitterIssueNfse. Contract conditions remain applicable."""
        return self._execute('emitterIssueNfse', request, {}, None, options, None)

    def cancel_nfse(self, request: m27.EmitterCancelNfsePayload, *, options: CallOptions | None = None) -> m27.emitterCancelNfseResponse:
        """emitterCancelNfse. Contract conditions remain applicable."""
        return self._execute('emitterCancelNfse', request, {}, None, options, None)

    def replace_nfse(self, request: m28.EmitterReplaceNfsePayload, *, options: CallOptions | None = None) -> m28.emitterReplaceNfseResponse:
        """emitterReplaceNfse. Contract conditions remain applicable."""
        return self._execute('emitterReplaceNfse', request, {}, None, options, None)
