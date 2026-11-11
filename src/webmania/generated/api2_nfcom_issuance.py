"""Generated from contracts/api2/nfcom-issuance.openapi.json; SHA256 37e97ae269b8a4bcde524fd83e4e4403020050c8a8eb24aef21f247170818a65. Do not edit."""
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

EmitterIssueNfcomPayloadAssinanteVariant0ContratoVariant0 = TypedDict('EmitterIssueNfcomPayloadAssinanteVariant0ContratoVariant0', {'data_fim': Union[str, None], 'data_inicio': Union[str, None], 'numero': Union[str, None]}, total=False)

EmitterIssueNfcomPayloadAssinanteVariant0 = TypedDict('EmitterIssueNfcomPayloadAssinanteVariant0', {'codigo': Union[str, None], 'contrato': Union['EmitterIssueNfcomPayloadAssinanteVariant0ContratoVariant0', None], 'tipo': Union[Union[int, str], None], 'tipo_servico': Union[Union[int, str], None]}, total=False)

EmitterIssueNfcomPayloadClienteEndereco = TypedDict('EmitterIssueNfcomPayloadClienteEndereco', {'bairro': Required[str], 'cep': Required[str], 'codigo_municipio': Required[str], 'codigo_pais': Union[str, None], 'complemento': Union[str, None], 'logradouro': Required[str], 'municipio': Required[str], 'numero': Required[str], 'pais': Union[str, None], 'telefone': Union[str, None], 'uf': Required[Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'EX']]}, total=False)

EmitterIssueNfcomPayloadCliente = TypedDict('EmitterIssueNfcomPayloadCliente', {'cnpj': Union[str, None], 'cpf': Union[str, None], 'email': Union[Union[list[str], None], str], 'endereco': Required['EmitterIssueNfcomPayloadClienteEndereco'], 'exterior': Union[Literal[True, False, 0, 1, '0', '1'], None], 'indicador_ie': Union[Literal['1', 1, '2', 2, '9', 9], None], 'inscricao_estadual': Union[str, None], 'nome_completo': Union[str, None], 'razao_social': Union[str, None], 'inscricao_municipal': str}, total=False)

EmitterIssueNfcomPayloadCofaturamentoVariant0NfReferenciadaVariant0 = TypedDict('EmitterIssueNfcomPayloadCofaturamentoVariant0NfReferenciadaVariant0', {'cnpj': str, 'competencia': str, 'hash115': Union[str, None], 'modelo': Literal['21', '22'], 'numero': Union[int, str], 'serie': str}, total=False)

EmitterIssueNfcomPayloadCofaturamentoVariant0 = TypedDict('EmitterIssueNfcomPayloadCofaturamentoVariant0', {'chave_nfcom_local': Union[str, None], 'nf_referenciada': Union['EmitterIssueNfcomPayloadCofaturamentoVariant0NfReferenciadaVariant0', None]}, total=False)

EmitterIssueNfcomPayloadFaturaVariant0 = TypedDict('EmitterIssueNfcomPayloadFaturaVariant0', {'codigo_barras_fatura': str, 'competencia_fatura': str, 'data_periodo_final': str, 'data_periodo_inicial': str, 'data_vencimento': str, 'numero_debito_automatico': str}, total=False)

EmitterIssueNfcomPayloadFaturamentoCentralizadoVariant0 = TypedDict('EmitterIssueNfcomPayloadFaturamentoCentralizadoVariant0', {'cnpj': str, 'codigo_uf': Literal['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53']}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CompraGovernamentalVariant0 = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CompraGovernamentalVariant0', {'aliquota_reducao': Union[Union[int, float], str], 'documentos_referenciados': Union[list[Union[str, Union[int, float]]], None], 'ente': Literal['1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6], 'referencias_dfe': Union[list[str], None], 'tipo_operacao': Literal['1', 1, '2', 2, '3', 3, '4', 4]}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CreditoPresumido = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CreditoPresumido', {'aliquota_cbs': Union[Union[int, float], str], 'aliquota_ibs': Union[Union[int, float], str], 'base_calculo': Union[Union[int, float], str], 'classificacao': str}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0EstornoCredito = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0EstornoCredito', {'valor_cbs': Union[Union[int, float], str], 'valor_ibs': Union[Union[int, float], str]}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0Cbs = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0Cbs', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsEstadual = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsEstadual', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsMunicipal = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsMunicipal', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0 = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0', {'classificacao_tributaria': str, 'classificacao_tributaria_regular': str, 'compra_governamental': Union['EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CompraGovernamentalVariant0', None], 'credito_presumido': 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CreditoPresumido', 'estorno_credito': 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0EstornoCredito', 'indicador_doacao': Literal[True, False, 0, 1, '0', '1'], 'situacao_tributaria': str, 'situacao_tributaria_regular': str, 'cbs': 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0Cbs', 'ibs_estadual': 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsEstadual', 'ibs_municipal': 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsMunicipal'}, total=False)

EmitterIssueNfcomPayloadImpostosVariant0 = TypedDict('EmitterIssueNfcomPayloadImpostosVariant0', {'ibs_cbs': Union['EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0', None]}, total=False)

EmitterIssueNfcomPayloadPgtoVincVariant0PagamentosItem = TypedDict('EmitterIssueNfcomPayloadPgtoVincVariant0PagamentosItem', {'cnpj_base_psp': Required[str], 'cnpj_receb': Required[str], 'id_transacao': Required[str], 'n_pag': Required[Union[int, str]], 'tp_meio_pgto': Required[str]}, total=False)

EmitterIssueNfcomPayloadPgtoVincVariant0 = TypedDict('EmitterIssueNfcomPayloadPgtoVincVariant0', {'pagamentos': list['EmitterIssueNfcomPayloadPgtoVincVariant0PagamentosItem']}, total=False)

EmitterIssueNfcomPayloadSubstituicaoVariant0NfReferenciadaVariant0 = TypedDict('EmitterIssueNfcomPayloadSubstituicaoVariant0NfReferenciadaVariant0', {'cnpj': str, 'competencia': str, 'hash115': Union[str, None], 'modelo': Literal['21', '22'], 'numero': Union[int, str], 'serie': str}, total=False)

EmitterIssueNfcomPayloadSubstituicaoVariant0 = TypedDict('EmitterIssueNfcomPayloadSubstituicaoVariant0', {'chave_nfcom_substituida': Union[str, None], 'motivo': Literal['01', '02', '03', '04', '05'], 'nf_referenciada': Union['EmitterIssueNfcomPayloadSubstituicaoVariant0NfReferenciadaVariant0', None]}, total=False)

EmitterIssueNfcomPayload = TypedDict('EmitterIssueNfcomPayload', {'ambiente': Required[Literal['1', 1, '2', 2]], 'assinante': Union['EmitterIssueNfcomPayloadAssinanteVariant0', None], 'autorizar_download': Union[list[str], None], 'cliente': Required['EmitterIssueNfcomPayloadCliente'], 'cofaturamento': Union['EmitterIssueNfcomPayloadCofaturamentoVariant0', None], 'consumidor_final': Union[Literal['0', 0, '1', 1], None], 'fatura': Union['EmitterIssueNfcomPayloadFaturaVariant0', None], 'faturamento_centralizado': Union['EmitterIssueNfcomPayloadFaturamentoCentralizadoVariant0', None], 'finalidade': Required[Literal['1', 1, '2', 2, '3', 3, '4', 4]], 'impostos': Union['EmitterIssueNfcomPayloadImpostosVariant0', None], 'indicador_cessao_meios_rede': Union[Literal['1', 1], None], 'indicador_nota_entrada': Union[Literal['1', 1], None], 'indicador_pre_pago': Union[Literal['1', 1], None], 'informacoes_complementares': Union[str, None], 'itens': Required[list['NfcomItemGroup']], 'municipio_fato_gerador': Union[str, None], 'natureza_operacao': Required[str], 'origem': Union[str, None], 'pgto_vinc': Union['EmitterIssueNfcomPayloadPgtoVincVariant0', None], 'presenca_comprador': Union[Literal['1', 1, '2', 2, '3', 3, '4', 4, '9', 9], None], 'previa_danfecom': Union[Literal[True, False, 0, 1, '0', '1'], None], 'processo_emissao': Union[Literal['0', 0, '3', 3], None], 'substituicao': Union['EmitterIssueNfcomPayloadSubstituicaoVariant0', None], 'tipo_faturamento': Union[Literal['0', 0, '1', 1, '2', 2], None], 'tipo_operacao': Required[Literal['0', 0, '1', 1]], 'url_notificacao': Union[str, None], 'ID': str}, total=False)

EmitterCancelNfcomPayload = TypedDict('EmitterCancelNfcomPayload', {'chave': Required[str], 'justificativa': Required[str]}, total=False)

NfcomDocumentedGroup1906 = TypedDict('NfcomDocumentedGroup1906', {'autorizar_download': list[JSONValue]}, total=False)

NfcomDocumentedGroup1953 = TypedDict('NfcomDocumentedGroup1953', {'indicador_pre_pago': Union[int, str], 'indicador_cessao_meios_rede': Union[int, str], 'indicador_nota_entrada': Union[int, str]}, total=False)

NfcomDocumentedGroup2114Substituicao = TypedDict('NfcomDocumentedGroup2114Substituicao', {}, total=False)

NfcomDocumentedGroup2114SubstituicaoNfReferenciada = TypedDict('NfcomDocumentedGroup2114SubstituicaoNfReferenciada', {}, total=False)

NfcomDocumentedGroup2114 = TypedDict('NfcomDocumentedGroup2114', {'substituicao': 'NfcomDocumentedGroup2114Substituicao', 'substituicao.chave_nfcom_substituida': str, 'substituicao.motivo': str, 'substituicao.nf_referenciada.*': 'NfcomDocumentedGroup2114SubstituicaoNfReferenciada'}, total=False)

NfcomDocumentedGroup2382 = TypedDict('NfcomDocumentedGroup2382', {'chave': str, 'justificativa': str}, total=False)

NfcomItemGroupVariant0ImpostosCofinsVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosCofinsVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'situacao_tributaria': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '49', '50', '51', '52', '53', '54', '55', '56', '60', '61', '62', '63', '64', '65', '66', '67', '70', '71', '72', '73', '74', '75', '98', '99'], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant0ImpostosFunttelVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosFunttelVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant0ImpostosFustVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosFustVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0CompraGovernamentalVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0CompraGovernamentalVariant0', {'aliquota_reducao': Union[Union[int, float], str], 'documentos_referenciados': Union[list[Union[str, Union[int, float]]], None], 'ente': Literal['1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6], 'tipo_operacao': Literal['1', 1, '2', 2, '3', 3, '4', 4], 'referencias_dfe': str}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0CreditoPresumido = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0CreditoPresumido', {'aliquota_cbs': Union[Union[int, float], str], 'aliquota_ibs': Union[Union[int, float], str], 'base_calculo': Union[Union[int, float], str], 'classificacao': str}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0EstornoCredito = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0EstornoCredito', {'valor_cbs': Union[Union[int, float], str], 'valor_ibs': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0Cbs = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0Cbs', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsEstadual = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsEstadual', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsMunicipal = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsMunicipal', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant0ImpostosIbsCbsVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosIbsCbsVariant0', {'classificacao_tributaria': str, 'classificacao_tributaria_regular': str, 'compra_governamental': Union['NfcomItemGroupVariant0ImpostosIbsCbsVariant0CompraGovernamentalVariant0', None], 'credito_presumido': 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0CreditoPresumido', 'estorno_credito': 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0EstornoCredito', 'indicador_doacao': Literal[True, False, 0, 1, '0', '1'], 'situacao_tributaria': str, 'situacao_tributaria_regular': str, 'cbs': 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0Cbs', 'ibs_estadual': 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsEstadual', 'ibs_municipal': 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsMunicipal'}, total=False)

NfcomItemGroupVariant0ImpostosIcmsVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosIcmsVariant0', {'aliquota_icms': Union[Union[Union[int, float], str], None], 'codigo_cfop': Union[str, None], 'origem': Literal['0', 0, '1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6, '7', 7, '8', 8], 'situacao_tributaria': Literal['00', '10', '20', '30', '40', '41', '45', '50', '51', '60', '70', '90'], 'valor_base_calculo': Union[Union[Union[int, float], str], None], 'valor_icms': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant0ImpostosPisVariant0 = TypedDict('NfcomItemGroupVariant0ImpostosPisVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'situacao_tributaria': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '49', '50', '51', '52', '53', '54', '55', '56', '60', '61', '62', '63', '64', '65', '66', '67', '70', '71', '72', '73', '74', '75', '98', '99'], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant0Impostos = TypedDict('NfcomItemGroupVariant0Impostos', {'codigo_classificacao': Union[str, None], 'cofins': Union['NfcomItemGroupVariant0ImpostosCofinsVariant0', None], 'funttel': Union['NfcomItemGroupVariant0ImpostosFunttelVariant0', None], 'fust': Union['NfcomItemGroupVariant0ImpostosFustVariant0', None], 'ibs_cbs': Union['NfcomItemGroupVariant0ImpostosIbsCbsVariant0', None], 'icms': Union['NfcomItemGroupVariant0ImpostosIcmsVariant0', None], 'pis': Union['NfcomItemGroupVariant0ImpostosPisVariant0', None]}, total=False)

NfcomItemGroupVariant0 = TypedDict('NfcomItemGroupVariant0', {'classe_imposto': Union[str, None], 'codigo': Union[str, None], 'codigo_classificacao': Required[Union[str, None]], 'descricao': Required[str], 'impostos': 'NfcomItemGroupVariant0Impostos', 'indicador_total': Required[Literal['0', 0, '1', 1]], 'quantidade': Required[Union[Union[int, float], str]], 'unidade': Required[str], 'valor_total': Required[Union[Union[int, float], str]], 'valor_unitario': Required[Union[Union[int, float], str]], 'valor_desconto': Union[Union[int, float], str], 'outras_despesas': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant1ImpostosCofinsVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosCofinsVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'situacao_tributaria': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '49', '50', '51', '52', '53', '54', '55', '56', '60', '61', '62', '63', '64', '65', '66', '67', '70', '71', '72', '73', '74', '75', '98', '99'], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant1ImpostosFunttelVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosFunttelVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant1ImpostosFustVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosFustVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0CompraGovernamentalVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0CompraGovernamentalVariant0', {'aliquota_reducao': Union[Union[int, float], str], 'documentos_referenciados': Union[list[Union[str, Union[int, float]]], None], 'ente': Literal['1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6], 'tipo_operacao': Literal['1', 1, '2', 2, '3', 3, '4', 4], 'referencias_dfe': str}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0CreditoPresumido = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0CreditoPresumido', {'aliquota_cbs': Union[Union[int, float], str], 'aliquota_ibs': Union[Union[int, float], str], 'base_calculo': Union[Union[int, float], str], 'classificacao': str}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0EstornoCredito = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0EstornoCredito', {'valor_cbs': Union[Union[int, float], str], 'valor_ibs': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0Cbs = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0Cbs', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsEstadual = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsEstadual', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsMunicipal = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsMunicipal', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant1ImpostosIbsCbsVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosIbsCbsVariant0', {'classificacao_tributaria': str, 'classificacao_tributaria_regular': str, 'compra_governamental': Union['NfcomItemGroupVariant1ImpostosIbsCbsVariant0CompraGovernamentalVariant0', None], 'credito_presumido': 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0CreditoPresumido', 'estorno_credito': 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0EstornoCredito', 'indicador_doacao': Literal[True, False, 0, 1, '0', '1'], 'situacao_tributaria': str, 'situacao_tributaria_regular': str, 'cbs': 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0Cbs', 'ibs_estadual': 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsEstadual', 'ibs_municipal': 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsMunicipal'}, total=False)

NfcomItemGroupVariant1ImpostosIcmsVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosIcmsVariant0', {'aliquota_icms': Union[Union[Union[int, float], str], None], 'codigo_cfop': Union[str, None], 'origem': Literal['0', 0, '1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6, '7', 7, '8', 8], 'situacao_tributaria': Literal['00', '10', '20', '30', '40', '41', '45', '50', '51', '60', '70', '90'], 'valor_base_calculo': Union[Union[Union[int, float], str], None], 'valor_icms': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant1ImpostosPisVariant0 = TypedDict('NfcomItemGroupVariant1ImpostosPisVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'situacao_tributaria': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '49', '50', '51', '52', '53', '54', '55', '56', '60', '61', '62', '63', '64', '65', '66', '67', '70', '71', '72', '73', '74', '75', '98', '99'], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant1Impostos = TypedDict('NfcomItemGroupVariant1Impostos', {'codigo_classificacao': Union[str, None], 'cofins': Union['NfcomItemGroupVariant1ImpostosCofinsVariant0', None], 'funttel': Union['NfcomItemGroupVariant1ImpostosFunttelVariant0', None], 'fust': Union['NfcomItemGroupVariant1ImpostosFustVariant0', None], 'ibs_cbs': Union['NfcomItemGroupVariant1ImpostosIbsCbsVariant0', None], 'icms': Union['NfcomItemGroupVariant1ImpostosIcmsVariant0', None], 'pis': Union['NfcomItemGroupVariant1ImpostosPisVariant0', None]}, total=False)

NfcomItemGroupVariant1 = TypedDict('NfcomItemGroupVariant1', {'classe_imposto': Required[Union[str, None]], 'codigo': Union[str, None], 'codigo_classificacao': Union[str, None], 'descricao': Required[str], 'impostos': 'NfcomItemGroupVariant1Impostos', 'indicador_total': Required[Literal['0', 0, '1', 1]], 'quantidade': Required[Union[Union[int, float], str]], 'unidade': Required[str], 'valor_total': Required[Union[Union[int, float], str]], 'valor_unitario': Required[Union[Union[int, float], str]], 'valor_desconto': Union[Union[int, float], str], 'outras_despesas': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant2ImpostosCofinsVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosCofinsVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'situacao_tributaria': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '49', '50', '51', '52', '53', '54', '55', '56', '60', '61', '62', '63', '64', '65', '66', '67', '70', '71', '72', '73', '74', '75', '98', '99'], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant2ImpostosFunttelVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosFunttelVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant2ImpostosFustVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosFustVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0CompraGovernamentalVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0CompraGovernamentalVariant0', {'aliquota_reducao': Union[Union[int, float], str], 'documentos_referenciados': Union[list[Union[str, Union[int, float]]], None], 'ente': Literal['1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6], 'tipo_operacao': Literal['1', 1, '2', 2, '3', 3, '4', 4], 'referencias_dfe': str}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0CreditoPresumido = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0CreditoPresumido', {'aliquota_cbs': Union[Union[int, float], str], 'aliquota_ibs': Union[Union[int, float], str], 'base_calculo': Union[Union[int, float], str], 'classificacao': str}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0EstornoCredito = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0EstornoCredito', {'valor_cbs': Union[Union[int, float], str], 'valor_ibs': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0Cbs = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0Cbs', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsEstadual = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsEstadual', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsMunicipal = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsMunicipal', {'aliquota_diferimento': Union[Union[int, float], str], 'valor_devolvido': Union[Union[int, float], str]}, total=False)

NfcomItemGroupVariant2ImpostosIbsCbsVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosIbsCbsVariant0', {'classificacao_tributaria': str, 'classificacao_tributaria_regular': str, 'compra_governamental': Union['NfcomItemGroupVariant2ImpostosIbsCbsVariant0CompraGovernamentalVariant0', None], 'credito_presumido': 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0CreditoPresumido', 'estorno_credito': 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0EstornoCredito', 'indicador_doacao': Literal[True, False, 0, 1, '0', '1'], 'situacao_tributaria': str, 'situacao_tributaria_regular': str, 'cbs': 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0Cbs', 'ibs_estadual': 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsEstadual', 'ibs_municipal': 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsMunicipal'}, total=False)

NfcomItemGroupVariant2ImpostosIcmsVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosIcmsVariant0', {'aliquota_icms': Union[Union[Union[int, float], str], None], 'codigo_cfop': Union[str, None], 'origem': Literal['0', 0, '1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6, '7', 7, '8', 8], 'situacao_tributaria': Literal['00', '10', '20', '30', '40', '41', '45', '50', '51', '60', '70', '90'], 'valor_base_calculo': Union[Union[Union[int, float], str], None], 'valor_icms': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant2ImpostosPisVariant0 = TypedDict('NfcomItemGroupVariant2ImpostosPisVariant0', {'aliquota': Union[Union[Union[int, float], str], None], 'situacao_tributaria': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '49', '50', '51', '52', '53', '54', '55', '56', '60', '61', '62', '63', '64', '65', '66', '67', '70', '71', '72', '73', '74', '75', '98', '99'], 'valor': Union[Union[Union[int, float], str], None], 'valor_base_calculo': Union[Union[Union[int, float], str], None]}, total=False)

NfcomItemGroupVariant2Impostos = TypedDict('NfcomItemGroupVariant2Impostos', {'codigo_classificacao': Required[Union[str, None]], 'cofins': Union['NfcomItemGroupVariant2ImpostosCofinsVariant0', None], 'funttel': Union['NfcomItemGroupVariant2ImpostosFunttelVariant0', None], 'fust': Union['NfcomItemGroupVariant2ImpostosFustVariant0', None], 'ibs_cbs': Union['NfcomItemGroupVariant2ImpostosIbsCbsVariant0', None], 'icms': Union['NfcomItemGroupVariant2ImpostosIcmsVariant0', None], 'pis': Union['NfcomItemGroupVariant2ImpostosPisVariant0', None]}, total=False)

NfcomItemGroupVariant2 = TypedDict('NfcomItemGroupVariant2', {'classe_imposto': Union[str, None], 'codigo': Union[str, None], 'codigo_classificacao': Union[str, None], 'descricao': Required[str], 'impostos': Required['NfcomItemGroupVariant2Impostos'], 'indicador_total': Required[Literal['0', 0, '1', 1]], 'quantidade': Required[Union[Union[int, float], str]], 'unidade': Required[str], 'valor_total': Required[Union[Union[int, float], str]], 'valor_unitario': Required[Union[Union[int, float], str]], 'valor_desconto': Union[Union[int, float], str], 'outras_despesas': Union[Union[int, float], str]}, total=False)

NfcomItemGroup: TypeAlias = Union['NfcomItemGroupVariant0', 'NfcomItemGroupVariant1', 'NfcomItemGroupVariant2']

emitterIssueNfcomResponse: TypeAlias = Union['NfcomFiscalResponse']

emitterCancelNfcomResponse: TypeAlias = Union['FiscalEventResponse']

_bind_types(globals(), __name__, ['EmitterError', 'NfseServiceCodeAliquotaSugerida', 'NfseServiceCode', 'NfseParameterRequirements', 'NfseProviderStatus', 'NfcomServiceStatus', 'NfseFiscalResponseNfseSubstituida', 'NfseFiscalResponseInfoNfseItem', 'NfseFiscalResponseLogVariant0', 'NfseFiscalResponse', 'NfcomPaymentEventPagamentoVariant0', 'NfcomPaymentEvent', 'NfcomFiscalResponseLogVariant0Variant0', 'NfcomFiscalResponse', 'NfcomPaymentEvents', 'NfseManifestationRequest', 'CteFiscalResponseLogVariant0', 'CteFiscalResponseEventosPagamentoItem', 'CteFiscalResponse', 'MdfeFiscalResponseLogVariant0', 'MdfeFiscalResponse', 'DceFiscalResponseLogVariant0', 'DceFiscalResponse', 'FiscalEventResponseLogVariant0', 'FiscalEventResponse', 'CtePaymentEventsEventosPagamentoItem', 'CtePaymentEvents', 'EmitterIssueNfcomPayloadAssinanteVariant0ContratoVariant0', 'EmitterIssueNfcomPayloadAssinanteVariant0', 'EmitterIssueNfcomPayloadClienteEndereco', 'EmitterIssueNfcomPayloadCliente', 'EmitterIssueNfcomPayloadCofaturamentoVariant0NfReferenciadaVariant0', 'EmitterIssueNfcomPayloadCofaturamentoVariant0', 'EmitterIssueNfcomPayloadFaturaVariant0', 'EmitterIssueNfcomPayloadFaturamentoCentralizadoVariant0', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CompraGovernamentalVariant0', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0CreditoPresumido', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0EstornoCredito', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0Cbs', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsEstadual', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0IbsMunicipal', 'EmitterIssueNfcomPayloadImpostosVariant0IbsCbsVariant0', 'EmitterIssueNfcomPayloadImpostosVariant0', 'EmitterIssueNfcomPayloadPgtoVincVariant0PagamentosItem', 'EmitterIssueNfcomPayloadPgtoVincVariant0', 'EmitterIssueNfcomPayloadSubstituicaoVariant0NfReferenciadaVariant0', 'EmitterIssueNfcomPayloadSubstituicaoVariant0', 'EmitterIssueNfcomPayload', 'EmitterCancelNfcomPayload', 'NfcomDocumentedGroup1906', 'NfcomDocumentedGroup1953', 'NfcomDocumentedGroup2114Substituicao', 'NfcomDocumentedGroup2114SubstituicaoNfReferenciada', 'NfcomDocumentedGroup2114', 'NfcomDocumentedGroup2382', 'NfcomItemGroupVariant0ImpostosCofinsVariant0', 'NfcomItemGroupVariant0ImpostosFunttelVariant0', 'NfcomItemGroupVariant0ImpostosFustVariant0', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0CompraGovernamentalVariant0', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0CreditoPresumido', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0EstornoCredito', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0Cbs', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsEstadual', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0IbsMunicipal', 'NfcomItemGroupVariant0ImpostosIbsCbsVariant0', 'NfcomItemGroupVariant0ImpostosIcmsVariant0', 'NfcomItemGroupVariant0ImpostosPisVariant0', 'NfcomItemGroupVariant0Impostos', 'NfcomItemGroupVariant0', 'NfcomItemGroupVariant1ImpostosCofinsVariant0', 'NfcomItemGroupVariant1ImpostosFunttelVariant0', 'NfcomItemGroupVariant1ImpostosFustVariant0', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0CompraGovernamentalVariant0', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0CreditoPresumido', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0EstornoCredito', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0Cbs', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsEstadual', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0IbsMunicipal', 'NfcomItemGroupVariant1ImpostosIbsCbsVariant0', 'NfcomItemGroupVariant1ImpostosIcmsVariant0', 'NfcomItemGroupVariant1ImpostosPisVariant0', 'NfcomItemGroupVariant1Impostos', 'NfcomItemGroupVariant1', 'NfcomItemGroupVariant2ImpostosCofinsVariant0', 'NfcomItemGroupVariant2ImpostosFunttelVariant0', 'NfcomItemGroupVariant2ImpostosFustVariant0', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0CompraGovernamentalVariant0', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0CreditoPresumido', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0EstornoCredito', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0Cbs', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsEstadual', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0IbsMunicipal', 'NfcomItemGroupVariant2ImpostosIbsCbsVariant0', 'NfcomItemGroupVariant2ImpostosIcmsVariant0', 'NfcomItemGroupVariant2ImpostosPisVariant0', 'NfcomItemGroupVariant2Impostos', 'NfcomItemGroupVariant2', 'NfcomItemGroup', 'emitterIssueNfcomResponse', 'emitterCancelNfcomResponse'])
