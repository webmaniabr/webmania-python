"""Generated from contracts/api2/emitter-files.openapi.json; SHA256 51ceb9bdfc4b76d0728ee315245686fbb2c4af7a70482b50ff27b28098fbe731. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

FiscalFileUuid: TypeAlias = str

FiscalFileIdentifier: TypeAlias = Union[str]

FiscalFileError = TypedDict('FiscalFileError', {'error': JSONValue, 'message': str, 'msg': str}, total=False)

NfsePdfPending = TypedDict('NfsePdfPending', {'msg': Required[str]}, total=False)

fileGetNfseXmlIdentifierParameter: TypeAlias = 'FiscalFileUuid'

fileGetNfsePdfIdentifierParameter: TypeAlias = 'FiscalFileUuid'

fileGetNfseRpsPdfIdentifierParameter: TypeAlias = 'FiscalFileUuid'

fileGetCteXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetCteCancelXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetCtePdfIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetCteCorrectionXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetCteCorrectionPdfIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetMdfeXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetMdfePdfIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetNfcomXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetNfcomCancelXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetNfcomPdfIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetDceXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetDceCancelXmlIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

fileGetDcePdfIdentifierParameter: TypeAlias = 'FiscalFileIdentifier'

_bind_types(globals(), __name__, ['FiscalFileUuid', 'FiscalFileIdentifier', 'FiscalFileError', 'NfsePdfPending', 'fileGetNfseXmlIdentifierParameter', 'fileGetNfsePdfIdentifierParameter', 'fileGetNfseRpsPdfIdentifierParameter', 'fileGetCteXmlIdentifierParameter', 'fileGetCteCancelXmlIdentifierParameter', 'fileGetCtePdfIdentifierParameter', 'fileGetCteCorrectionXmlIdentifierParameter', 'fileGetCteCorrectionPdfIdentifierParameter', 'fileGetMdfeXmlIdentifierParameter', 'fileGetMdfePdfIdentifierParameter', 'fileGetNfcomXmlIdentifierParameter', 'fileGetNfcomCancelXmlIdentifierParameter', 'fileGetNfcomPdfIdentifierParameter', 'fileGetDceXmlIdentifierParameter', 'fileGetDceCancelXmlIdentifierParameter', 'fileGetDcePdfIdentifierParameter'])
