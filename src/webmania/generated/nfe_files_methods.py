"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api1_files as m0
from . import api1_files as m1
from . import api1_files as m2
from . import api1_files as m3
from . import api1_files as m4
from . import api1_files as m5
from . import api1_files as m6
from . import api1_files as m7
from . import api1_files as m8
from . import api1_files as m9
from . import api1_files as m10
from . import api1_files as m11
from . import api1_files as m12
from . import api1_files as m13

class NfeFilesMethods:
    _execute: Any

    def download_danfe(self, *, identifier: m0.nfeDownloadDanfeIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """NF-e/NFC-e DANFE. Contract conditions remain applicable."""
        return self._execute('nfeDownloadDanfe', UNSET, {'identifier': identifier}, None, options, auth)

    def download_simple_danfe(self, *, identifier: m1.nfeDownloadSimpleDanfeIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """NF-e simple DANFE. Contract conditions remain applicable."""
        return self._execute('nfeDownloadSimpleDanfe', UNSET, {'identifier': identifier}, None, options, auth)

    def download_label_danfe(self, *, identifier: m2.nfeDownloadLabelDanfeIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """NF-e label DANFE. Contract conditions remain applicable."""
        return self._execute('nfeDownloadLabelDanfe', UNSET, {'identifier': identifier}, None, options, auth)

    def download_correction_pdf(self, *, identifier: m3.nfeDownloadCorrectionPdfIdentifierParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """CC-e PDF by event UUID or first event. Contract conditions remain applicable."""
        return self._execute('nfeDownloadCorrectionPdf', UNSET, {'identifier': identifier}, None, options, auth)

    def download_correction_pdf_sequence(self, *, identifier: m4.nfeDownloadCorrectionPdfSequenceIdentifierParameter, event: m4.nfeDownloadCorrectionPdfSequenceEventParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """CC-e PDF with sequence. Contract conditions remain applicable."""
        return self._execute('nfeDownloadCorrectionPdfSequence', UNSET, {'identifier': identifier, 'event': event}, None, options, auth)

    def download_xml(self, *, identifier: m5.nfeDownloadXmlIdentifierParameter, query: m5.nfeDownloadXmlQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """NF-e/NFC-e XML. Contract conditions remain applicable."""
        return self._execute('nfeDownloadXml', UNSET, {'identifier': identifier}, query, options, auth)

    def download_cancellation_xml(self, *, identifier: m6.nfeDownloadCancellationXmlIdentifierParameter, query: m6.nfeDownloadCancellationXmlQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """Cancellation XML. Contract conditions remain applicable."""
        return self._execute('nfeDownloadCancellationXml', UNSET, {'identifier': identifier}, query, options, auth)

    def download_correction_xml(self, *, identifier: m7.nfeDownloadCorrectionXmlIdentifierParameter, query: m7.nfeDownloadCorrectionXmlQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """CC-e XML by event UUID. Contract conditions remain applicable."""
        return self._execute('nfeDownloadCorrectionXml', UNSET, {'identifier': identifier}, query, options, auth)

    def download_correction_xml_sequence(self, *, identifier: m8.nfeDownloadCorrectionXmlSequenceIdentifierParameter, event: m8.nfeDownloadCorrectionXmlSequenceEventParameter, query: m8.nfeDownloadCorrectionXmlSequenceQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """CC-e XML with sequence. Contract conditions remain applicable."""
        return self._execute('nfeDownloadCorrectionXmlSequence', UNSET, {'identifier': identifier, 'event': event}, query, options, auth)

    def download_manifestation_xml(self, *, uuid: m9.nfeDownloadManifestationXmlUuidParameter, query: m9.nfeDownloadManifestationXmlQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """Recipient manifestation XML. Contract conditions remain applicable."""
        return self._execute('nfeDownloadManifestationXml', UNSET, {'uuid': uuid}, query, options, auth)

    def download_payment_event_xml(self, *, identifier: m10.nfeDownloadPaymentEventXmlIdentifierParameter, query: m10.nfeDownloadPaymentEventXmlQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """ECONF XML by event UUID. Contract conditions remain applicable."""
        return self._execute('nfeDownloadPaymentEventXml', UNSET, {'identifier': identifier}, query, options, auth)

    def download_payment_event_xml_sequence(self, *, identifier: m11.nfeDownloadPaymentEventXmlSequenceIdentifierParameter, event: m11.nfeDownloadPaymentEventXmlSequenceEventParameter, query: m11.nfeDownloadPaymentEventXmlSequenceQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """ECONF XML with sequence. Contract conditions remain applicable."""
        return self._execute('nfeDownloadPaymentEventXmlSequence', UNSET, {'identifier': identifier, 'event': event}, query, options, auth)

    def download_ibs_cbs_event_xml(self, *, uuid: m12.nfeDownloadIbsCbsEventXmlUuidParameter, query: m12.nfeDownloadIbsCbsEventXmlQuery | None = None, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """IBS/CBS event XML. Contract conditions remain applicable."""
        return self._execute('nfeDownloadIbsCbsEventXml', UNSET, {'uuid': uuid}, query, options, auth)

    def download_report(self, *, uuid: m13.fiscalDownloadReportUuidParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """Exported fiscal report. Contract conditions remain applicable."""
        return self._execute('fiscalDownloadReport', UNSET, {'uuid': uuid}, None, options, auth)
