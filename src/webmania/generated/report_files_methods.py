"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api2_reports as m0

class ReportFilesMethods:
    _execute: Any

    def download_report_v2(self, *, uuid: m0.fiscalDownloadReportV2UuidParameter, auth: FileAuth, options: CallOptions | None = None) -> FileResponse:
        """Exported fiscal report (current report service). Contract conditions remain applicable."""
        return self._execute('fiscalDownloadReportV2', UNSET, {'uuid': uuid}, None, options, auth)
