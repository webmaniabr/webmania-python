"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api2_emitter_files as m0
from . import api2_emitter_files as m1
from . import api2_emitter_files as m2
from . import api2_emitter_files as m3
from . import api2_emitter_files as m4
from . import api2_emitter_files as m5
from . import api2_emitter_files as m6
from . import api2_emitter_files as m7
from . import api2_emitter_files as m8
from . import api2_emitter_files as m9
from . import api2_emitter_files as m10
from . import api2_emitter_files as m11
from . import api2_emitter_files as m12
from . import api2_emitter_files as m13
from . import api2_emitter_files as m14
from . import api2_emitter_files as m15

class EmitterFilesMethods:
    _execute: Any

    def get_nfse_xml(self, *, identifier: m0.fileGetNfseXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetNfseXml. Contract conditions remain applicable."""
        return self._execute('fileGetNfseXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_nfse_pdf(self, *, identifier: m1.fileGetNfsePdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse | FileRedirectResponse:
        """fileGetNfsePdf. Contract conditions remain applicable."""
        return self._execute('fileGetNfsePdf', UNSET, {'identifier': identifier}, None, options, auth)

    def get_nfse_rps_pdf(self, *, identifier: m2.fileGetNfseRpsPdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetNfseRpsPdf. Contract conditions remain applicable."""
        return self._execute('fileGetNfseRpsPdf', UNSET, {'identifier': identifier}, None, options, auth)

    def get_cte_xml(self, *, identifier: m3.fileGetCteXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetCteXml. Contract conditions remain applicable."""
        return self._execute('fileGetCteXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_cte_cancel_xml(self, *, identifier: m4.fileGetCteCancelXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetCteCancelXml. Contract conditions remain applicable."""
        return self._execute('fileGetCteCancelXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_cte_pdf(self, *, identifier: m5.fileGetCtePdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetCtePdf. Contract conditions remain applicable."""
        return self._execute('fileGetCtePdf', UNSET, {'identifier': identifier}, None, options, auth)

    def get_cte_correction_xml(self, *, identifier: m6.fileGetCteCorrectionXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetCteCorrectionXml. Contract conditions remain applicable."""
        return self._execute('fileGetCteCorrectionXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_cte_correction_pdf(self, *, identifier: m7.fileGetCteCorrectionPdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetCteCorrectionPdf. Contract conditions remain applicable."""
        return self._execute('fileGetCteCorrectionPdf', UNSET, {'identifier': identifier}, None, options, auth)

    def get_mdfe_xml(self, *, identifier: m8.fileGetMdfeXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetMdfeXml. Contract conditions remain applicable."""
        return self._execute('fileGetMdfeXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_mdfe_pdf(self, *, identifier: m9.fileGetMdfePdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetMdfePdf. Contract conditions remain applicable."""
        return self._execute('fileGetMdfePdf', UNSET, {'identifier': identifier}, None, options, auth)

    def get_nfcom_xml(self, *, identifier: m10.fileGetNfcomXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetNfcomXml. Contract conditions remain applicable."""
        return self._execute('fileGetNfcomXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_nfcom_cancel_xml(self, *, identifier: m11.fileGetNfcomCancelXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetNfcomCancelXml. Contract conditions remain applicable."""
        return self._execute('fileGetNfcomCancelXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_nfcom_pdf(self, *, identifier: m12.fileGetNfcomPdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetNfcomPdf. Contract conditions remain applicable."""
        return self._execute('fileGetNfcomPdf', UNSET, {'identifier': identifier}, None, options, auth)

    def get_dce_xml(self, *, identifier: m13.fileGetDceXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetDceXml. Contract conditions remain applicable."""
        return self._execute('fileGetDceXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_dce_cancel_xml(self, *, identifier: m14.fileGetDceCancelXmlIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetDceCancelXml. Contract conditions remain applicable."""
        return self._execute('fileGetDceCancelXml', UNSET, {'identifier': identifier}, None, options, auth)

    def get_dce_pdf(self, *, identifier: m15.fileGetDcePdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """fileGetDcePdf. Contract conditions remain applicable."""
        return self._execute('fileGetDcePdf', UNSET, {'identifier': identifier}, None, options, auth)
