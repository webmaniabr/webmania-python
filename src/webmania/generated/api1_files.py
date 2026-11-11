"""Generated from contracts/api1/files.openapi.json; SHA256 4c2a0297f607c115d4fde5528cf25d194ea10ed59d566c5d52880340d1a8cdc1. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

Uuid: TypeAlias = str

AccessKey: TypeAlias = str

Api1ErrorLogVariant1 = TypedDict('Api1ErrorLogVariant1', {'cStat': Union[str, int], 'xMotivo': str}, total=False)

Api1Error = TypedDict('Api1Error', {'error': Required[Union[str, list[str]]], 'message': str, 'code': Union[str, int], 'status': str, 'log': Union[str, 'Api1ErrorLogVariant1']}, total=False)

nfeDownloadDanfeIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadSimpleDanfeIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadLabelDanfeIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCorrectionPdfIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCorrectionPdfSequenceIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCorrectionPdfSequenceEventParameter: TypeAlias = int

nfeDownloadXmlQuery = TypedDict('nfeDownloadXmlQuery', {'download': Literal[1]}, total=False)

nfeDownloadXmlIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCancellationXmlQuery = TypedDict('nfeDownloadCancellationXmlQuery', {'download': Literal[1]}, total=False)

nfeDownloadCancellationXmlIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCorrectionXmlQuery = TypedDict('nfeDownloadCorrectionXmlQuery', {'download': Literal[1]}, total=False)

nfeDownloadCorrectionXmlIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCorrectionXmlSequenceQuery = TypedDict('nfeDownloadCorrectionXmlSequenceQuery', {'download': Literal[1]}, total=False)

nfeDownloadCorrectionXmlSequenceIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadCorrectionXmlSequenceEventParameter: TypeAlias = int

nfeDownloadManifestationXmlQuery = TypedDict('nfeDownloadManifestationXmlQuery', {'download': Literal[1]}, total=False)

nfeDownloadManifestationXmlUuidParameter: TypeAlias = 'Uuid'

nfeDownloadPaymentEventXmlQuery = TypedDict('nfeDownloadPaymentEventXmlQuery', {'download': Literal[1]}, total=False)

nfeDownloadPaymentEventXmlIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadPaymentEventXmlSequenceQuery = TypedDict('nfeDownloadPaymentEventXmlSequenceQuery', {'download': Literal[1]}, total=False)

nfeDownloadPaymentEventXmlSequenceIdentifierParameter: TypeAlias = Union['Uuid', 'AccessKey']

nfeDownloadPaymentEventXmlSequenceEventParameter: TypeAlias = int

nfeDownloadIbsCbsEventXmlQuery = TypedDict('nfeDownloadIbsCbsEventXmlQuery', {'download': Literal[1]}, total=False)

nfeDownloadIbsCbsEventXmlUuidParameter: TypeAlias = 'Uuid'

fiscalDownloadReportUuidParameter: TypeAlias = 'Uuid'

_bind_types(globals(), __name__, ['Uuid', 'AccessKey', 'Api1ErrorLogVariant1', 'Api1Error', 'nfeDownloadDanfeIdentifierParameter', 'nfeDownloadSimpleDanfeIdentifierParameter', 'nfeDownloadLabelDanfeIdentifierParameter', 'nfeDownloadCorrectionPdfIdentifierParameter', 'nfeDownloadCorrectionPdfSequenceIdentifierParameter', 'nfeDownloadCorrectionPdfSequenceEventParameter', 'nfeDownloadXmlQuery', 'nfeDownloadXmlIdentifierParameter', 'nfeDownloadCancellationXmlQuery', 'nfeDownloadCancellationXmlIdentifierParameter', 'nfeDownloadCorrectionXmlQuery', 'nfeDownloadCorrectionXmlIdentifierParameter', 'nfeDownloadCorrectionXmlSequenceQuery', 'nfeDownloadCorrectionXmlSequenceIdentifierParameter', 'nfeDownloadCorrectionXmlSequenceEventParameter', 'nfeDownloadManifestationXmlQuery', 'nfeDownloadManifestationXmlUuidParameter', 'nfeDownloadPaymentEventXmlQuery', 'nfeDownloadPaymentEventXmlIdentifierParameter', 'nfeDownloadPaymentEventXmlSequenceQuery', 'nfeDownloadPaymentEventXmlSequenceIdentifierParameter', 'nfeDownloadPaymentEventXmlSequenceEventParameter', 'nfeDownloadIbsCbsEventXmlQuery', 'nfeDownloadIbsCbsEventXmlUuidParameter', 'fiscalDownloadReportUuidParameter'])
