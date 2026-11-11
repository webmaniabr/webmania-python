"""Generated from contracts/api2/dce-issuance.openapi.json; SHA256 c1c8b4e53a31d9f175d0002961915a3b85b320ae9807939ad875b4f724a5f1c5. Do not edit."""
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

CteFiscalResponseLogVariant0 = TypedDict('CteFiscalResponseLogVariant0', {}, total=False)

CteFiscalResponseEventosPagamentoItem = TypedDict('CteFiscalResponseEventosPagamentoItem', {'evento': Union[str, Union[int, float], None], 'codigo': Union[str, Union[int, float], None], 'motivo': Union[str, Union[int, float], None], 'protocolo_evento': Union[str, Union[int, float], None], 'protocolo_cte': Union[str, Union[int, float], None], 'protocolo_vinculacao': Union[str, Union[int, float], None], 'data_evento': Union[str, Union[int, float], None], 'n_seq_evento': Union[str, Union[int, float], None]}, total=False)

CteFiscalResponse = TypedDict('CteFiscalResponse', {'ID': Union[str, Union[int, float]], 'uuid': Required[str], 'chave': Union[str, None], 'serie': Union[str, Union[int, float], None], 'status': Required[str], 'motivo': Union[str, Union[int, float], bool, None], 'modelo': str, 'xml': Union[str, None], 'xml_cancelamento': Union[str, None], 'log': Union['CteFiscalResponseLogVariant0', list[JSONValue], None], 'cte': Union[int, str, None], 'epec': bool, 'dacte': Union[str, None], 'eventos_pagamento': list['CteFiscalResponseEventosPagamentoItem'], 'total_eventos': int, 'consulta_eventos_pagamento': str}, total=False)

MdfeFiscalResponseLogVariant0 = TypedDict('MdfeFiscalResponseLogVariant0', {}, total=False)

MdfeFiscalResponse = TypedDict('MdfeFiscalResponse', {'ID': Union[str, Union[int, float]], 'uuid': Required[str], 'chave': Union[str, None], 'serie': Union[str, Union[int, float], None], 'status': Required[str], 'motivo': Union[str, Union[int, float], bool, None], 'modelo': str, 'xml': Union[str, None], 'xml_cancelamento': Union[str, None], 'log': Union['MdfeFiscalResponseLogVariant0', list[JSONValue], None], 'mdfe': Union[int, str, None], 'damdfe': Union[str, None]}, total=False)

DceFiscalResponseLogVariant0 = TypedDict('DceFiscalResponseLogVariant0', {}, total=False)

DceFiscalResponse = TypedDict('DceFiscalResponse', {'ID': Union[str, Union[int, float]], 'uuid': Required[str], 'chave': Union[str, None], 'serie': Union[str, Union[int, float], None], 'status': Required[str], 'motivo': Union[str, Union[int, float], bool, None], 'modelo': str, 'xml': Union[str, None], 'xml_cancelamento': Union[str, None], 'log': Union['DceFiscalResponseLogVariant0', list[JSONValue], None], 'numero': Union[int, str, None], 'dace': str}, total=False)

FiscalEventResponseLogVariant0 = TypedDict('FiscalEventResponseLogVariant0', {}, total=False)

FiscalEventResponse = TypedDict('FiscalEventResponse', {'uuid': str, 'chave': str, 'evento': Union[Union[int, float], str], 'status': Required[str], 'motivo': Union[str, None], 'xml': Union[str, None], 'xml_cancelamento': Union[str, None], 'dacce': str, 'log': Union['FiscalEventResponseLogVariant0', list[JSONValue], None], 'codigo': Union[Union[int, float], str], 'protocolo_evento': str, 'data_evento': str}, total=False)

CtePaymentEventsEventosPagamentoItem = TypedDict('CtePaymentEventsEventosPagamentoItem', {'evento': Union[str, Union[int, float], None], 'codigo': Union[str, Union[int, float], None], 'motivo': Union[str, Union[int, float], None], 'protocolo_evento': Union[str, Union[int, float], None], 'protocolo_cte': Union[str, Union[int, float], None], 'protocolo_vinculacao': Union[str, Union[int, float], None], 'data_evento': Union[str, Union[int, float], None], 'n_seq_evento': Union[str, Union[int, float], None]}, total=False)

CtePaymentEvents = TypedDict('CtePaymentEvents', {'uuid': Required[str], 'chave': str, 'status': Required[str], 'eventos_pagamento': Required[list['CtePaymentEventsEventosPagamentoItem']], 'total_eventos': Required[int]}, total=False)

EmitterIssueDcePayloadItensItem = TypedDict('EmitterIssueDcePayloadItensItem', {'descricao': Required[str], 'informacoes_adicionais': Union[str, None], 'ncm': Required[str], 'quantidade': Required[Union[Union[int, float], str]], 'valor_unitario': Required[Union[Union[int, float], str]]}, total=False)

EmitterIssueDcePayloadObservacoesVariant0Item = TypedDict('EmitterIssueDcePayloadObservacoesVariant0Item', {'campo': str, 'texto': str}, total=False)

EmitterIssueDcePayloadObservacoesEmitenteVariant0Item = TypedDict('EmitterIssueDcePayloadObservacoesEmitenteVariant0Item', {'campo': str, 'texto': str}, total=False)

EmitterIssueDcePayloadCliente = TypedDict('EmitterIssueDcePayloadCliente', {'bairro': str, 'cep': str, 'cnpj': str, 'codigo_municipio': str, 'codigo_pais': str, 'complemento': Union[str, None], 'cpf': str, 'email': Union[str, None], 'endereco': list[JSONValue], 'identificacao_alternativa': str, 'logradouro': str, 'municipio': str, 'nome_completo': str, 'numero': str, 'pais': str, 'razao_social': str, 'telefone': Union[str, None], 'uf': str}, total=False)

EmitterIssueDcePayloadEmitente = TypedDict('EmitterIssueDcePayloadEmitente', {'bairro': str, 'cep': str, 'cnpj': str, 'codigo_municipio': str, 'complemento': Union[str, None], 'cpf': str, 'endereco': list[JSONValue], 'identificacao_alternativa': str, 'logradouro': str, 'municipio': str, 'nome_completo': str, 'numero': str, 'razao_social': str, 'telefone': Union[str, None], 'uf': str}, total=False)

EmitterIssueDcePayloadTransporte = TypedDict('EmitterIssueDcePayloadTransporte', {'cnpj_transportadora': Union[str, None], 'modalidade': Required[Literal['0', '1', '2']]}, total=False)

EmitterIssueDcePayload = TypedDict('EmitterIssueDcePayload', {'ID': Union[str, None], 'ambiente': Required[Literal['1', 1, '2', 2]], 'informacoes_adicionais': Union[str, None], 'informacoes_adicionais_emitente': Union[str, None], 'itens': Required[list['EmitterIssueDcePayloadItensItem']], 'observacoes': Union[list['EmitterIssueDcePayloadObservacoesVariant0Item'], None], 'observacoes_emitente': Union[list['EmitterIssueDcePayloadObservacoesEmitenteVariant0Item'], None], 'origem': Union[Literal['api', 'webmaniabr', 'woocommerce', 'prestashop', 'opencart', 'magento'], None], 'solicitacao': Union[str, None], 'url_notificacao': Union[str, None], 'cliente': 'EmitterIssueDcePayloadCliente', 'emitente': 'EmitterIssueDcePayloadEmitente', 'transporte': 'EmitterIssueDcePayloadTransporte'}, total=False)

EmitterCancelDcePayload = TypedDict('EmitterCancelDcePayload', {'chave': str, 'justificativa': Required[str], 'uuid': str}, total=False)

DceDocumentedGroup282 = TypedDict('DceDocumentedGroup282', {'ID': str, 'uuid': str, 'chave': str, 'serie': Union[Union[int, float], str], 'numero': Union[Union[int, float], str], 'status': str, 'motivo': str, 'modelo': str, 'xml': str, 'xml_cancelamento': str, 'dace': str, 'log': list[JSONValue]}, total=False)

DceDocumentedGroup1106 = TypedDict('DceDocumentedGroup1106', {'uuid': str, 'chave': str, 'justificativa': str}, total=False)

DceItemGroup = TypedDict('DceItemGroup', {'descricao': Required[str], 'informacoes_adicionais': Union[str, None], 'ncm': Required[str], 'quantidade': Required[Union[Union[int, float], str]], 'valor_unitario': Required[Union[Union[int, float], str]]}, total=False)

emitterIssueDceResponse: TypeAlias = Union['DceFiscalResponse']

emitterCancelDceResponse: TypeAlias = Union['FiscalEventResponse']

emitterGetDceResponse: TypeAlias = Union['DceFiscalResponse']

emitterGetDceIdentifierParameter: TypeAlias = str

_bind_types(globals(), __name__, ['EmitterError', 'NfseServiceCodeAliquotaSugerida', 'NfseServiceCode', 'NfseParameterRequirements', 'NfseProviderStatus', 'NfcomServiceStatus', 'NfseFiscalResponseNfseSubstituida', 'NfseFiscalResponseInfoNfseItem', 'NfseFiscalResponseLogVariant0', 'NfseFiscalResponse', 'NfcomPaymentEventPagamentoVariant0', 'NfcomPaymentEvent', 'NfcomFiscalResponseLogVariant0Variant0', 'NfcomFiscalResponse', 'NfcomPaymentEvents', 'NfseManifestationRequest', 'CteFiscalResponseLogVariant0', 'CteFiscalResponseEventosPagamentoItem', 'CteFiscalResponse', 'MdfeFiscalResponseLogVariant0', 'MdfeFiscalResponse', 'DceFiscalResponseLogVariant0', 'DceFiscalResponse', 'FiscalEventResponseLogVariant0', 'FiscalEventResponse', 'CtePaymentEventsEventosPagamentoItem', 'CtePaymentEvents', 'EmitterIssueDcePayloadItensItem', 'EmitterIssueDcePayloadObservacoesVariant0Item', 'EmitterIssueDcePayloadObservacoesEmitenteVariant0Item', 'EmitterIssueDcePayloadCliente', 'EmitterIssueDcePayloadEmitente', 'EmitterIssueDcePayloadTransporte', 'EmitterIssueDcePayload', 'EmitterCancelDcePayload', 'DceDocumentedGroup282', 'DceDocumentedGroup1106', 'DceItemGroup', 'emitterIssueDceResponse', 'emitterCancelDceResponse', 'emitterGetDceResponse', 'emitterGetDceIdentifierParameter'])
