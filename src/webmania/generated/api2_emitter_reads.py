"""Generated from contracts/api2/emitter-reads.openapi.json; SHA256 43cc01352085f9af97cb68e337dced4022b8beca6b8359642516d9aaa9ed3fda. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

EmitterError = TypedDict('EmitterError', {'error': str, 'message': str, 'status': bool, 'configured': bool}, total=False)

NfseServiceCodeAliquotaSugerida = TypedDict('NfseServiceCodeAliquotaSugerida', {'iss': Union[Union[int, float], str]}, total=False)

NfseServiceCode = TypedDict('NfseServiceCode', {'codigo': Required[Union[str, Union[int, float]]], 'descricao': Required[str], 'id_cnae': Union[str, Union[int, float]], 'codigo_tributacao': Union[str, Union[int, float]], 'aliquota_sugerida': 'NfseServiceCodeAliquotaSugerida'}, total=False)

NfseParameterRequirements = TypedDict('NfseParameterRequirements', {}, total=False)

NfseProviderStatus = TypedDict('NfseProviderStatus', {'status': Required[Literal[True]], 'modelo': str, 'versao': str, 'ambientes': Required[list[Literal[1, 2]]], 'autenticacao': Required[list[str]], 'emissao': Required[list[str]], 'funcoes': Required[list[str]], 'pdf_nfse': Required[bool], 'pdf_sincrono': Required[bool], 'codigo_servico': list['NfseServiceCode'], 'parametros_disponiveis': 'NfseParameterRequirements'}, total=False)

NfcomServiceStatus = TypedDict('NfcomServiceStatus', {'operacional': Required[bool], 'mensagem': Required[str]}, total=False)

NfseFiscalResponseNfseSubstituida = TypedDict('NfseFiscalResponseNfseSubstituida', {'uuid': str, 'numero': str, 'codigo_verificacao': str}, total=False)

NfseFiscalResponseInfoNfseItem = TypedDict('NfseFiscalResponseInfoNfseItem', {'uuid': str, 'modelo': str, 'status': str, 'motivo': Union[str, Union[int, float], bool, None], 'numero': str, 'codigo_verificacao': str, 'xml': str, 'pdf_nfse': str, 'pdf_nfse_status': str, 'pdf_rps': str}, total=False)

NfseFiscalResponseLogVariant0 = TypedDict('NfseFiscalResponseLogVariant0', {}, total=False)

NfseFiscalResponse = TypedDict('NfseFiscalResponse', {'ID': str, 'uuid': Required[str], 'modelo': Required[str], 'status': Required[str], 'chave': str, 'numero_lote': Union[str, Union[int, float]], 'serie_lote': Union[str, Union[int, float]], 'protocolo': str, 'numero': str, 'codigo_verificacao': str, 'serie_rps': Union[str, Union[int, float]], 'numero_rps': Union[str, Union[int, float]], 'xml': str, 'xml_cancelamento': str, 'pdf_nfse': str, 'pdf_nfse_status': str, 'pdf_rps': str, 'atualizado_em': str, 'motivo': Union[str, Union[int, float], bool, None], 'quantidade_rps': Union[int, str], 'nfse_substituida': 'NfseFiscalResponseNfseSubstituida', 'info_nfse': list['NfseFiscalResponseInfoNfseItem'], 'log': Union['NfseFiscalResponseLogVariant0', list[JSONValue]]}, total=False)

NfcomPaymentEventPagamentoVariant0 = TypedDict('NfcomPaymentEventPagamentoVariant0', {'nPag': Union[str, Union[int, float], bool, None], 'idTransacao': Union[str, Union[int, float], bool, None], 'tpMeioPgto': Union[str, Union[int, float], bool, None], 'CNPJReceb': Union[str, Union[int, float], bool, None], 'CNPJBasePSP': Union[str, Union[int, float], bool, None]}, total=False)

NfcomPaymentEvent = TypedDict('NfcomPaymentEvent', {'evento': Union[str, None], 'codigo': Union[str, None], 'motivo': Union[str, None], 'protocolo_evento': Union[str, None], 'protocolo_nfcom': Union[str, None], 'protocolo_vinculacao': Union[str, None], 'data_evento': Union[str, None], 'n_seq_evento': Union[Union[int, str], None], 'pagamento': Union['NfcomPaymentEventPagamentoVariant0', None]}, total=False)

NfcomFiscalResponseLogVariant0Variant0 = TypedDict('NfcomFiscalResponseLogVariant0Variant0', {}, total=False)

NfcomFiscalResponse = TypedDict('NfcomFiscalResponse', {'uuid': Required[str], 'chave': Union[str, None], 'serie': Union[int, str, None], 'nfcom': Union[int, str, None], 'status': Required[str], 'motivo': str, 'modelo': Required[Literal['nfcom']], 'contingencia': bool, 'xml': str, 'danfecom': str, 'xml_cancelamento': Union[str, None], 'protocolo': str, 'data_autorizacao': Union[str, None], 'eventos_pagamento': list['NfcomPaymentEvent'], 'total_eventos': int, 'consulta_eventos_pagamento': str, 'log': Union[Union['NfcomFiscalResponseLogVariant0Variant0', list[JSONValue]], None]}, total=False)

NfcomPaymentEvents = TypedDict('NfcomPaymentEvents', {'uuid': Required[str], 'chave': Union[str, None], 'status': Required[str], 'eventos_pagamento': Required[list['NfcomPaymentEvent']], 'total_eventos': Required[int]}, total=False)

NfseManifestationRequest = TypedDict('NfseManifestationRequest', {'ambiente': Required[Literal[1, 2, '1', '2']], 'chave': Required[str], 'manifestador': Required[Literal[1, 2, '1', '2']], 'evento': Required[Literal[1, 2, '1', '2']], 'motivo_rejeicao': Literal[1, 2, 3, 4, 5, 9, '1', '2', '3', '4', '5', '9'], 'justificativa_rejeicao': str}, total=False)

EmitterFunctionalError = TypedDict('EmitterFunctionalError', {'error': Required[str], 'message': str, 'status': bool, 'configured': bool}, total=False)

emitterGetNfseProviderStatusQuery = TypedDict('emitterGetNfseProviderStatusQuery', {'todos_servicos': bool}, total=False)

emitterGetNfseProviderStatusResponse: TypeAlias = Union[Union['NfseProviderStatus', 'EmitterFunctionalError']]

emitterGetNfcomServiceStatusResponse: TypeAlias = Union[Union['NfcomServiceStatus', 'EmitterFunctionalError']]

emitterGetNfseResponse: TypeAlias = Union[Union['NfseFiscalResponse', 'EmitterFunctionalError']]

emitterGetNfseIdentifierParameter: TypeAlias = str

emitterGetNfcomResponse: TypeAlias = Union[Union['NfcomFiscalResponse', 'EmitterFunctionalError']]

emitterGetNfcomIdentifierParameter: TypeAlias = str

emitterGetNfcomPaymentEventsResponse: TypeAlias = Union[Union['NfcomPaymentEvents', 'EmitterFunctionalError']]

emitterGetNfcomPaymentEventsIdentifierParameter: TypeAlias = str

emitterManifestNfseResponse: TypeAlias = Union[Union['NfseFiscalResponse', 'EmitterFunctionalError']]

_bind_types(globals(), __name__, ['EmitterError', 'NfseServiceCodeAliquotaSugerida', 'NfseServiceCode', 'NfseParameterRequirements', 'NfseProviderStatus', 'NfcomServiceStatus', 'NfseFiscalResponseNfseSubstituida', 'NfseFiscalResponseInfoNfseItem', 'NfseFiscalResponseLogVariant0', 'NfseFiscalResponse', 'NfcomPaymentEventPagamentoVariant0', 'NfcomPaymentEvent', 'NfcomFiscalResponseLogVariant0Variant0', 'NfcomFiscalResponse', 'NfcomPaymentEvents', 'NfseManifestationRequest', 'EmitterFunctionalError', 'emitterGetNfseProviderStatusQuery', 'emitterGetNfseProviderStatusResponse', 'emitterGetNfcomServiceStatusResponse', 'emitterGetNfseResponse', 'emitterGetNfseIdentifierParameter', 'emitterGetNfcomResponse', 'emitterGetNfcomIdentifierParameter', 'emitterGetNfcomPaymentEventsResponse', 'emitterGetNfcomPaymentEventsIdentifierParameter', 'emitterManifestNfseResponse'])
