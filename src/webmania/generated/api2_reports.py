"""Generated from contracts/api2/reports.openapi.json; SHA256 3c6b4938a0b44bc2b8dfef7d5b5e98dd5d5c939c2c5ec3227cf43759ba2a6191. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

ReportUuid: TypeAlias = str

ReportError = TypedDict('ReportError', {'error': Required[str]}, total=False)

ReportHttpError = TypedDict('ReportHttpError', {}, total=False)

fiscalDownloadReportV2UuidParameter: TypeAlias = 'ReportUuid'

_bind_types(globals(), __name__, ['ReportUuid', 'ReportError', 'ReportHttpError', 'fiscalDownloadReportV2UuidParameter'])
