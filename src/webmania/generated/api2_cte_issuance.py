"""Generated from contracts/api2/cte-issuance.openapi.json; SHA256 57f5baee26677dcb139f2cb10cbe91e7bc7f0f3178a1a91481f469b7fe6811b8. Do not edit."""
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

EmitterIssueCtePayloadAereoNaturezaCarga = TypedDict('EmitterIssueCtePayloadAereoNaturezaCarga', {'dimensoes': str, 'informacoes_manuseio': list[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '99']]}, total=False)

EmitterIssueCtePayloadAereoProdutosPerigososItem = TypedDict('EmitterIssueCtePayloadAereoProdutosPerigososItem', {'descricao_volumes': Required[str], 'numero_onu': Required[str], 'quantidade_total': Required[Union[Union[int, float], str]], 'unidade_medida': Required[Literal['1', '2', '3', '4', '5']]}, total=False)

EmitterIssueCtePayloadAereoTarifa = TypedDict('EmitterIssueCtePayloadAereoTarifa', {'classe': Literal['M', 'G', 'E'], 'codigo': str, 'valor': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadAereo = TypedDict('EmitterIssueCtePayloadAereo', {'natureza_carga': 'EmitterIssueCtePayloadAereoNaturezaCarga', 'numero_minuta': str, 'numero_oca': str, 'previsao_entrega': str, 'produtos_perigosos': list['EmitterIssueCtePayloadAereoProdutosPerigososItem'], 'tarifa': 'EmitterIssueCtePayloadAereoTarifa'}, total=False)

EmitterIssueCtePayloadAquaviarioContainersItemDocumentosItem = TypedDict('EmitterIssueCtePayloadAquaviarioContainersItemDocumentosItem', {'chave': str, 'medida_rateada': Union[Union[int, float], str], 'numero': str, 'serie': str}, total=False)

EmitterIssueCtePayloadAquaviarioContainersItem = TypedDict('EmitterIssueCtePayloadAquaviarioContainersItem', {'documentos': list['EmitterIssueCtePayloadAquaviarioContainersItemDocumentosItem'], 'identificacao': Required[str], 'lacres': list[str]}, total=False)

EmitterIssueCtePayloadAquaviario = TypedDict('EmitterIssueCtePayloadAquaviario', {'adicional_frete': Union[Union[int, float], str], 'balsas': list[str], 'containers': list['EmitterIssueCtePayloadAquaviarioContainersItem'], 'direcao': Literal['N', 'L', 'S', 'O'], 'identificacao_navio': str, 'irin_navio': str, 'numero_viagem': str, 'tipo_navegacao': Literal['0', '1'], 'valor_prestacao': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadCargaFluxo = TypedDict('EmitterIssueCtePayloadCargaFluxo', {'destino': str, 'origem': str, 'passagens': list[str], 'rota': str}, total=False)

EmitterIssueCtePayloadCargaQuantidadesItem = TypedDict('EmitterIssueCtePayloadCargaQuantidadesItem', {'quantidade': Required[Union[Union[int, float], str]], 'tipo_medida': str, 'unidade_medida': Literal['0', '1', '2', '3', '4', '5']}, total=False)

EmitterIssueCtePayloadCargaSeguro = TypedDict('EmitterIssueCtePayloadCargaSeguro', {'nome_razao_seguradora': str, 'numero_apolice': str, 'responsavel': Literal['4', '5']}, total=False)

EmitterIssueCtePayloadCarga = TypedDict('EmitterIssueCtePayloadCarga', {'caracteristicas': str, 'fluxo': 'EmitterIssueCtePayloadCargaFluxo', 'produto_predominante': Required[str], 'quantidades': Required[list['EmitterIssueCtePayloadCargaQuantidadesItem']], 'seguro': 'EmitterIssueCtePayloadCargaSeguro', 'valor_averbacao': Union[Union[int, float], str], 'valor_total': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadCobrancaDuplicatasItem = TypedDict('EmitterIssueCtePayloadCobrancaDuplicatasItem', {'data_vencimento': str, 'numero': str, 'valor': Required[Union[Union[int, float], str]]}, total=False)

EmitterIssueCtePayloadCobrancaFatura = TypedDict('EmitterIssueCtePayloadCobrancaFatura', {'numero': str, 'valor_desconto': Union[Union[int, float], str], 'valor_liquido': Union[Union[int, float], str], 'valor_original': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadCobranca = TypedDict('EmitterIssueCtePayloadCobranca', {'duplicatas': list['EmitterIssueCtePayloadCobrancaDuplicatasItem'], 'fatura': 'EmitterIssueCtePayloadCobrancaFatura'}, total=False)

EmitterIssueCtePayloadDestinatario = TypedDict('EmitterIssueCtePayloadDestinatario', {'bairro': str, 'cep': str, 'cidade': str, 'cnpj': str, 'codigo_pais': str, 'complemento': str, 'cpf': str, 'email': str, 'endereco': str, 'ie': str, 'isuf': str, 'nome_razao': str, 'numero': str, 'telefone': str, 'uf': str, 'nome_fantasia': str}, total=False)

EmitterIssueCtePayloadDocumentosAnterioresItemDocumentosItem = TypedDict('EmitterIssueCtePayloadDocumentosAnterioresItemDocumentosItem', {'chave': str, 'data_emissao': str, 'numero': str, 'serie': str, 'tipo': Literal['7', 7, '8', 8, '9', 9, '10', 10, '11', 11, '12', 12, '13', 13]}, total=False)

EmitterIssueCtePayloadDocumentosAnterioresItemEmissor = TypedDict('EmitterIssueCtePayloadDocumentosAnterioresItemEmissor', {'cnpj': str, 'cpf': str, 'ie': str, 'nome_razao': str, 'uf': str}, total=False)

EmitterIssueCtePayloadDocumentosAnterioresItem = TypedDict('EmitterIssueCtePayloadDocumentosAnterioresItem', {'documentos': list['EmitterIssueCtePayloadDocumentosAnterioresItemDocumentosItem'], 'emissor': 'EmitterIssueCtePayloadDocumentosAnterioresItemEmissor'}, total=False)

EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesCargaItem = TypedDict('EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesCargaItem', {'identificacao': Required[str], 'lacres': list[str], 'quantidade_rateada': Union[Union[int, float], str], 'tipo': Required[Literal['1', '2', '3', '4']]}, total=False)

EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItemUnidadesCargaItem = TypedDict('EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItemUnidadesCargaItem', {'identificacao': Required[str], 'lacres': list[str], 'quantidade_rateada': Union[Union[int, float], str], 'tipo': Required[Literal['1', '2', '3', '4']]}, total=False)

EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItem = TypedDict('EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItem', {'identificacao': Required[str], 'lacres': list[str], 'quantidade_rateada': Union[Union[int, float], str], 'tipo': Required[Literal['1', '2', '3', '4', '5', '6', '7']], 'unidades_carga': list['EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItemUnidadesCargaItem']}, total=False)

EmitterIssueCtePayloadDocumentosFiscaisItem = TypedDict('EmitterIssueCtePayloadDocumentosFiscaisItem', {'base_calculo': Union[Union[int, float], str], 'base_calculo_st': Union[Union[int, float], str], 'cfop': str, 'chave': str, 'data_emissao': str, 'descricao': str, 'icms': Union[Union[int, float], str], 'icms_st': Union[Union[int, float], str], 'modelo': Literal['1', '4'], 'numero': str, 'numero_pedido': str, 'numero_romaneio': str, 'peso': Union[Union[int, float], str], 'pin': str, 'previsao_entrega': str, 'serie': str, 'tipo': Literal['1', '2', '3', '4', '5', '6', '9'], 'unidades_carga': list['EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesCargaItem'], 'unidades_transporte': list['EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItem'], 'valor_produtos': Union[Union[int, float], str], 'valor_total': Union[Union[int, float], str], 'CFOP': str, 'subserie': str}, total=False)

EmitterIssueCtePayloadDutoviario = TypedDict('EmitterIssueCtePayloadDutoviario', {'data_inicio_prestacao': str, 'data_termino_prestacao': str, 'valor_tarifa': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadEntrega = TypedDict('EmitterIssueCtePayloadEntrega', {'data': str, 'data_final': str, 'data_inicial': str}, total=False)

EmitterIssueCtePayloadExpedidor = TypedDict('EmitterIssueCtePayloadExpedidor', {'bairro': str, 'cep': str, 'cidade': str, 'cnpj': str, 'codigo_pais': str, 'complemento': str, 'cpf': str, 'email': str, 'endereco': str, 'ie': str, 'nome_razao': str, 'numero': str, 'telefone': str, 'uf': str, 'nome_fantasia': str}, total=False)

EmitterIssueCtePayloadFerroviarioFerroviasItem = TypedDict('EmitterIssueCtePayloadFerroviarioFerroviasItem', {'bairro': str, 'cep': str, 'cidade': Required[str], 'cnpj': Required[str], 'complemento': str, 'endereco': Required[str], 'ie': str, 'nome_razao': Required[str], 'numero': str, 'uf': str}, total=False)

EmitterIssueCtePayloadFerroviario = TypedDict('EmitterIssueCtePayloadFerroviario', {'cte_origem': str, 'ferrovias': list['EmitterIssueCtePayloadFerroviarioFerroviasItem'], 'fluxo': str, 'responsavel_emissao': Literal['1', '2'], 'responsavel_faturamento': Literal['1', '2'], 'tipo_trafego': Literal['0', '1', '2', '3'], 'valor_frete': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadImpostosIcmsPartilha = TypedDict('EmitterIssueCtePayloadImpostosIcmsPartilha', {'aliquota_fcp_uf_destino': Union[Union[int, float], str], 'aliquota_icms_interestadual': Union[Union[int, float], str], 'aliquota_icms_uf_destino': Union[Union[int, float], str], 'aliquota_icms_uf_origem': Union[Union[int, float], str], 'base_calculo': Union[Union[int, float], str], 'valor_icms_uf_remetente': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadImpostosIcms = TypedDict('EmitterIssueCtePayloadImpostosIcms', {'aliquota': Union[Union[int, float], str], 'aliquota_st_retido': Union[Union[int, float], str], 'bc_st_retido': Union[Union[int, float], str], 'credito_outorgado': Union[Union[int, float], str], 'devido_origem': Literal[True, False, 0, 1, '0', '1'], 'partilha': 'EmitterIssueCtePayloadImpostosIcmsPartilha', 'percentual_reducao': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadImpostosIbsCbsCompraGovernamentalVariant0 = TypedDict('EmitterIssueCtePayloadImpostosIbsCbsCompraGovernamentalVariant0', {'aliquota_reducao': Union[Union[int, float], str], 'ente': Literal['1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6], 'referencias_dfe': Union[list[str], None], 'tipo_operacao': Literal['1', 1, '2', 2, '3', 3, '4', 4]}, total=False)

EmitterIssueCtePayloadImpostosIbsCbsEstornoCredito = TypedDict('EmitterIssueCtePayloadImpostosIbsCbsEstornoCredito', {'valor_cbs': Union[Union[int, float], str], 'valor_ibs': Union[Union[int, float], str]}, total=False)

EmitterIssueCtePayloadImpostosIbsCbsIbsEstadual = TypedDict('EmitterIssueCtePayloadImpostosIbsCbsIbsEstadual', {'valor_devolvido': str}, total=False)

EmitterIssueCtePayloadImpostosIbsCbsIbsMunicipal = TypedDict('EmitterIssueCtePayloadImpostosIbsCbsIbsMunicipal', {'valor_devolvido': str}, total=False)

EmitterIssueCtePayloadImpostosIbsCbsCbs = TypedDict('EmitterIssueCtePayloadImpostosIbsCbsCbs', {'valor_devolvido': str}, total=False)

EmitterIssueCtePayloadImpostosIbsCbsCreditoPresumido = TypedDict('EmitterIssueCtePayloadImpostosIbsCbsCreditoPresumido', {'classificacao': str, 'aliquota_ibs': str, 'aliquota_cbs': str}, total=False)

EmitterIssueCtePayloadImpostosIbsCbs = TypedDict('EmitterIssueCtePayloadImpostosIbsCbs', {'compra_governamental': Union['EmitterIssueCtePayloadImpostosIbsCbsCompraGovernamentalVariant0', None], 'estorno_credito': 'EmitterIssueCtePayloadImpostosIbsCbsEstornoCredito', 'indicador_doacao': Literal[True, False, 0, 1, '0', '1'], 'situacao_tributaria': str, 'classificacao_tributaria': str, 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'EmitterIssueCtePayloadImpostosIbsCbsIbsEstadual', 'ibs_municipal': 'EmitterIssueCtePayloadImpostosIbsCbsIbsMunicipal', 'cbs': 'EmitterIssueCtePayloadImpostosIbsCbsCbs', 'credito_presumido': 'EmitterIssueCtePayloadImpostosIbsCbsCreditoPresumido'}, total=False)

EmitterIssueCtePayloadImpostos = TypedDict('EmitterIssueCtePayloadImpostos', {'beneficio_fiscal': str, 'cfop': Required[str], 'classificacao_tributaria': Required[Literal['00', '20', '40', '41', '51', '60', '90', 'SN']], 'cofins': Union[Union[int, float], str], 'csll': Union[Union[int, float], str], 'icms': 'EmitterIssueCtePayloadImpostosIcms', 'inss': Union[Union[int, float], str], 'ir': Union[Union[int, float], str], 'pis': Union[Union[int, float], str], 'ibs_cbs': 'EmitterIssueCtePayloadImpostosIbsCbs'}, total=False)

EmitterIssueCtePayloadLocalInicioPrestacao = TypedDict('EmitterIssueCtePayloadLocalInicioPrestacao', {'cidade': str, 'cod_ibge': str, 'codigo_municipio': Union[str, None], 'uf': str}, total=False)

EmitterIssueCtePayloadLocalTerminoPrestacao = TypedDict('EmitterIssueCtePayloadLocalTerminoPrestacao', {'cidade': str, 'cod_ibge': str, 'codigo_municipio': Union[str, None], 'uf': str}, total=False)

EmitterIssueCtePayloadMultimodalSeguro = TypedDict('EmitterIssueCtePayloadMultimodalSeguro', {'cnpj_seguradora': str, 'nome_razao_seguradora': str, 'numero_apolice': str, 'numero_averbacao': str}, total=False)

EmitterIssueCtePayloadMultimodal = TypedDict('EmitterIssueCtePayloadMultimodal', {'cotm': str, 'negociavel': Literal[True, False, 0, 1, '0', '1'], 'seguro': 'EmitterIssueCtePayloadMultimodalSeguro'}, total=False)

EmitterIssueCtePayloadObservacoesContribuinteItem = TypedDict('EmitterIssueCtePayloadObservacoesContribuinteItem', {'descricao': Required[str], 'identificacao': Required[str]}, total=False)

EmitterIssueCtePayloadObservacoesFiscoItem = TypedDict('EmitterIssueCtePayloadObservacoesFiscoItem', {'descricao': Required[str], 'identificacao': Required[str]}, total=False)

EmitterIssueCtePayloadPagamentosVinculadosItem = TypedDict('EmitterIssueCtePayloadPagamentosVinculadosItem', {'cnpj_base_psp': Required[str], 'cnpj_recebedor': Required[str], 'id_transacao': Required[str], 'n_pag': Required[Union[int, str]], 'tp_meio_pagamento': Required[str]}, total=False)

EmitterIssueCtePayloadRecebedor = TypedDict('EmitterIssueCtePayloadRecebedor', {'bairro': str, 'cep': str, 'cidade': str, 'cnpj': str, 'codigo_pais': str, 'complemento': str, 'cpf': str, 'email': str, 'endereco': str, 'ie': str, 'nome_razao': str, 'numero': str, 'telefone': str, 'uf': str, 'nome_fantasia': str}, total=False)

EmitterIssueCtePayloadRemetente = TypedDict('EmitterIssueCtePayloadRemetente', {'bairro': str, 'cep': str, 'cidade': str, 'cnpj': str, 'codigo_pais': str, 'complemento': str, 'cpf': str, 'email': str, 'endereco': str, 'ie': str, 'nome_fantasia': str, 'nome_razao': str, 'numero': str, 'telefone': str, 'uf': str}, total=False)

EmitterIssueCtePayloadRodoviarioOrdensColetaItemEmissor = TypedDict('EmitterIssueCtePayloadRodoviarioOrdensColetaItemEmissor', {'cnpj': str, 'ie': str, 'telefone': str, 'uf': str}, total=False)

EmitterIssueCtePayloadRodoviarioOrdensColetaItem = TypedDict('EmitterIssueCtePayloadRodoviarioOrdensColetaItem', {'data_emissao': str, 'emissor': 'EmitterIssueCtePayloadRodoviarioOrdensColetaItemEmissor', 'numero': str, 'serie': str}, total=False)

EmitterIssueCtePayloadRodoviarioVeiculoProprietario = TypedDict('EmitterIssueCtePayloadRodoviarioVeiculoProprietario', {'cnpj': str, 'cpf': str, 'ie': str, 'nome_razao': str, 'registro_estadual': str, 'taf': str, 'tipo': Literal['0', '1', '2'], 'uf': str}, total=False)

EmitterIssueCtePayloadRodoviarioVeiculo = TypedDict('EmitterIssueCtePayloadRodoviarioVeiculo', {'placa': str, 'proprietario': 'EmitterIssueCtePayloadRodoviarioVeiculoProprietario', 'renavam': str, 'uf_licenciamento': str}, total=False)

EmitterIssueCtePayloadRodoviario = TypedDict('EmitterIssueCtePayloadRodoviario', {'data_viagem': str, 'ordens_coleta': list['EmitterIssueCtePayloadRodoviarioOrdensColetaItem'], 'registro_estadual_cte_os': str, 'rntrc': str, 'taf_cte_os': str, 'tipo_fretamento': Literal['1', '2'], 'veiculo': 'EmitterIssueCtePayloadRodoviarioVeiculo'}, total=False)

EmitterIssueCtePayloadServico = TypedDict('EmitterIssueCtePayloadServico', {'componentes': list[JSONValue], 'descricao': str, 'tipo': Union[Literal['0', 0, '1', 1, '2', 2, '3', 3, '4', 4], Literal['6', 6, '7', 7, '8', 8]], 'valor_recebido': Required[Union[Union[int, float], str]], 'valor_total': Required[Union[Union[int, float], str]]}, total=False)

EmitterIssueCtePayloadTomador = TypedDict('EmitterIssueCtePayloadTomador', {'bairro': str, 'cep': str, 'cidade': str, 'cnpj': str, 'codigo_pais': str, 'complemento': str, 'cpf': str, 'email': str, 'endereco': str, 'ie': str, 'nome_fantasia': str, 'nome_razao': str, 'numero': str, 'telefone': str, 'uf': str}, total=False)

EmitterIssueCtePayloadVeiculosNovosItem = TypedDict('EmitterIssueCtePayloadVeiculosNovosItem', {'chassi': Required[str], 'cor': Required[str], 'cor_descricao': Required[str], 'marca_modelo': Required[str], 'valor_frete_unitario': Required[Union[Union[int, float], str]], 'valor_unitario': Required[Union[Union[int, float], str]]}, total=False)

EmitterIssueCtePayload = TypedDict('EmitterIssueCtePayload', {'aereo': 'EmitterIssueCtePayloadAereo', 'alteracao_tomador': Literal[True, False, 0, 1, '0', '1'], 'ambiente': Required[Literal['1', 1, '2', 2]], 'aquaviario': 'EmitterIssueCtePayloadAquaviario', 'caracteristica_servico': str, 'caracteristica_transporte': str, 'carga': Required['EmitterIssueCtePayloadCarga'], 'cobranca': 'EmitterIssueCtePayloadCobranca', 'contribuicao_tomador': Required[Literal['1', 1, '2', 2, '9', 9]], 'cte_referenciado': str, 'data_emissao': Union[str, None], 'destinatario': 'EmitterIssueCtePayloadDestinatario', 'detalhes_retirada': str, 'documentos_anteriores': list['EmitterIssueCtePayloadDocumentosAnterioresItem'], 'documentos_fiscais': list['EmitterIssueCtePayloadDocumentosFiscaisItem'], 'dutoviario': 'EmitterIssueCtePayloadDutoviario', 'entrega': 'EmitterIssueCtePayloadEntrega', 'expedidor': 'EmitterIssueCtePayloadExpedidor', 'ferroviario': 'EmitterIssueCtePayloadFerroviario', 'finalidade': Required[Literal['0', '1', '3']], 'globalizado': Literal[True, False, 0, 1, '0', '1'], 'impostos': Required['EmitterIssueCtePayloadImpostos'], 'indicador_tomador': Required[Literal['0', 0, '1', 1, '2', 2, '3', 3, '4', 4]], 'informacao_globalizado': str, 'local_inicio_prestacao': Required['EmitterIssueCtePayloadLocalInicioPrestacao'], 'local_termino_prestacao': Required['EmitterIssueCtePayloadLocalTerminoPrestacao'], 'modalidade': Required[Literal['1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '6', 6]], 'modelo': Required[Literal['cte', 'cte_os']], 'multimodal': 'EmitterIssueCtePayloadMultimodal', 'natureza_operacao': Required[str], 'observacoes_contribuinte': list['EmitterIssueCtePayloadObservacoesContribuinteItem'], 'observacoes_fisco': list['EmitterIssueCtePayloadObservacoesFiscoItem'], 'observacoes_gerais': str, 'origem': str, 'pagamentos_vinculados': list['EmitterIssueCtePayloadPagamentosVinculadosItem'], 'recebedor': 'EmitterIssueCtePayloadRecebedor', 'remetente': 'EmitterIssueCtePayloadRemetente', 'rodoviario': 'EmitterIssueCtePayloadRodoviario', 'servico': Required['EmitterIssueCtePayloadServico'], 'tomador': 'EmitterIssueCtePayloadTomador', 'veiculos_novos': list['EmitterIssueCtePayloadVeiculosNovosItem'], 'url_notificacao': str, 'nfe_xml': str}, total=False)

EmitterIssueSimplifiedCtePayload = TypedDict('EmitterIssueSimplifiedCtePayload', {'ambiente': Required[Literal['1', 1, '2', 2]], 'modelo': Required[Literal['cte']], 'nfe_xml': Required[str], 'origem': str}, total=False)

EmitterCancelCtePayload = TypedDict('EmitterCancelCtePayload', {'chave': str, 'justificativa': Required[str], 'uuid': str}, total=False)

EmitterCorrectCtePayloadAlteracoesItem = TypedDict('EmitterCorrectCtePayloadAlteracoesItem', {'campo': Required[str], 'grupo': Required[str], 'item': Union[int, str], 'valor': Required[str]}, total=False)

EmitterCorrectCtePayload = TypedDict('EmitterCorrectCtePayload', {'alteracoes': Required[list['EmitterCorrectCtePayloadAlteracoesItem']], 'ambiente': Literal['1', 1, '2', 2], 'chave': JSONValue, 'origem': str, 'sequencia': Union[int, str], 'uuid': str}, total=False)

EmitterConfirmCteDeliveryPayload = TypedDict('EmitterConfirmCteDeliveryPayload', {'chave': str, 'comprovante': Required[str], 'data_hora': str, 'documento_recebedor': str, 'informacoes': str, 'latitude': str, 'longitude': str, 'nome_recebedor': str, 'notas_fiscais': list[str], 'uuid': str}, total=False)

EmitterCancelCteDeliveryPayload = TypedDict('EmitterCancelCteDeliveryPayload', {'chave': str, 'protocolo': str, 'sequencia': str, 'uuid': str}, total=False)

EmitterLinkCtePaymentPayloadPagamento = TypedDict('EmitterLinkCtePaymentPayloadPagamento', {'cnpj_base_psp': Required[str], 'cnpj_recebedor': Required[str], 'id_transacao': Required[str], 'n_pag': Required[Union[int, str]], 'tp_meio_pagamento': Required[str]}, total=False)

EmitterLinkCtePaymentPayload = TypedDict('EmitterLinkCtePaymentPayload', {'chave': str, 'pagamento': Required['EmitterLinkCtePaymentPayloadPagamento'], 'protocolo': Union[str, None], 'sequencia': Union[Union[int, str], None], 'uuid': str}, total=False)

EmitterCancelCtePaymentLinkPayload = TypedDict('EmitterCancelCtePaymentLinkPayload', {'chave': str, 'protocolo': Union[str, None], 'protocolo_vinculacao': str, 'sequencia': Union[Union[int, str], None], 'sequencia_vinculacao': Union[int, str], 'uuid': str}, total=False)

CteDocumentedGroup654 = TypedDict('CteDocumentedGroup654', {'uuid': str, 'chave': str, 'serie': Union[Union[int, float], str], 'numero': Union[Union[int, float], str], 'status': str, 'motivo': str, 'epec': bool, 'xml': str, 'xml_cancelamento': str, 'dacte': str, 'log': list[JSONValue]}, total=False)

CteDocumentedGroup5669 = TypedDict('CteDocumentedGroup5669', {'uuid': str, 'justificativa': str}, total=False)

CteDocumentedGroup5730 = TypedDict('CteDocumentedGroup5730', {'uuid': str, 'comprovante': str, 'nome_recebedor': str, 'documento_recebedor': str, 'notas_fiscais': str, 'data_hora': str, 'informacoes': str, 'longitude': str, 'latitude': str}, total=False)

CteDocumentedGroup5835 = TypedDict('CteDocumentedGroup5835', {'uuid': str, 'sequencia': str}, total=False)

CteDocumentedGroup5904 = TypedDict('CteDocumentedGroup5904', {'uuid': str, 'alteracoes': list[JSONValue], 'ambiente': Union[int, str], 'sequencia': Union[int, str]}, total=False)

CteDocumentedGroup5949 = TypedDict('CteDocumentedGroup5949', {'grupo': str, 'campo': str, 'valor': str, 'item': Union[int, str]}, total=False)

CteDocumentedGroup6032Pagamento = TypedDict('CteDocumentedGroup6032Pagamento', {}, total=False)

CteDocumentedGroup6032 = TypedDict('CteDocumentedGroup6032', {'uuid': str, 'protocolo': str, 'sequencia': Union[int, str], 'pagamento': 'CteDocumentedGroup6032Pagamento'}, total=False)

CteDocumentedGroup6120 = TypedDict('CteDocumentedGroup6120', {'uuid': str, 'protocolo': str, 'protocolo_vinculacao': str, 'sequencia': Union[int, str]}, total=False)

CteServiceGroup = TypedDict('CteServiceGroup', {'componentes': list[JSONValue], 'descricao': str, 'tipo': Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4'], 'valor_recebido': Required[Union[Union[int, float], str]], 'valor_total': Required[Union[Union[int, float], str]]}, total=False)

CteOsServiceGroup = TypedDict('CteOsServiceGroup', {'componentes': list[JSONValue], 'descricao': Required[str], 'tipo': Required[Literal[6, 7, 8, '6', '7', '8']], 'valor_recebido': Required[Union[Union[int, float], str]], 'valor_total': Required[Union[Union[int, float], str]]}, total=False)

emitterIssueCteResponse: TypeAlias = Union['CteFiscalResponse']

emitterIssueSimplifiedCteResponse: TypeAlias = Union['CteFiscalResponse']

emitterCancelCteResponse: TypeAlias = Union['FiscalEventResponse']

emitterCorrectCteResponse: TypeAlias = Union['FiscalEventResponse']

emitterConfirmCteDeliveryResponse: TypeAlias = Union['FiscalEventResponse']

emitterCancelCteDeliveryResponse: TypeAlias = Union['FiscalEventResponse']

emitterLinkCtePaymentResponse: TypeAlias = Union['FiscalEventResponse']

emitterCancelCtePaymentLinkResponse: TypeAlias = Union['FiscalEventResponse']

emitterGetCteResponse: TypeAlias = Union['CteFiscalResponse']

emitterGetCteIdentifierParameter: TypeAlias = str

emitterGetCtePaymentEventsResponse: TypeAlias = Union['CtePaymentEvents']

emitterGetCtePaymentEventsIdentifierParameter: TypeAlias = str

_bind_types(globals(), __name__, ['EmitterError', 'NfseServiceCodeAliquotaSugerida', 'NfseServiceCode', 'NfseParameterRequirements', 'NfseProviderStatus', 'NfcomServiceStatus', 'NfseFiscalResponseNfseSubstituida', 'NfseFiscalResponseInfoNfseItem', 'NfseFiscalResponseLogVariant0', 'NfseFiscalResponse', 'NfcomPaymentEventPagamentoVariant0', 'NfcomPaymentEvent', 'NfcomFiscalResponseLogVariant0Variant0', 'NfcomFiscalResponse', 'NfcomPaymentEvents', 'NfseManifestationRequest', 'CteFiscalResponseLogVariant0', 'CteFiscalResponseEventosPagamentoItem', 'CteFiscalResponse', 'MdfeFiscalResponseLogVariant0', 'MdfeFiscalResponse', 'DceFiscalResponseLogVariant0', 'DceFiscalResponse', 'FiscalEventResponseLogVariant0', 'FiscalEventResponse', 'CtePaymentEventsEventosPagamentoItem', 'CtePaymentEvents', 'EmitterIssueCtePayloadAereoNaturezaCarga', 'EmitterIssueCtePayloadAereoProdutosPerigososItem', 'EmitterIssueCtePayloadAereoTarifa', 'EmitterIssueCtePayloadAereo', 'EmitterIssueCtePayloadAquaviarioContainersItemDocumentosItem', 'EmitterIssueCtePayloadAquaviarioContainersItem', 'EmitterIssueCtePayloadAquaviario', 'EmitterIssueCtePayloadCargaFluxo', 'EmitterIssueCtePayloadCargaQuantidadesItem', 'EmitterIssueCtePayloadCargaSeguro', 'EmitterIssueCtePayloadCarga', 'EmitterIssueCtePayloadCobrancaDuplicatasItem', 'EmitterIssueCtePayloadCobrancaFatura', 'EmitterIssueCtePayloadCobranca', 'EmitterIssueCtePayloadDestinatario', 'EmitterIssueCtePayloadDocumentosAnterioresItemDocumentosItem', 'EmitterIssueCtePayloadDocumentosAnterioresItemEmissor', 'EmitterIssueCtePayloadDocumentosAnterioresItem', 'EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesCargaItem', 'EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItemUnidadesCargaItem', 'EmitterIssueCtePayloadDocumentosFiscaisItemUnidadesTransporteItem', 'EmitterIssueCtePayloadDocumentosFiscaisItem', 'EmitterIssueCtePayloadDutoviario', 'EmitterIssueCtePayloadEntrega', 'EmitterIssueCtePayloadExpedidor', 'EmitterIssueCtePayloadFerroviarioFerroviasItem', 'EmitterIssueCtePayloadFerroviario', 'EmitterIssueCtePayloadImpostosIcmsPartilha', 'EmitterIssueCtePayloadImpostosIcms', 'EmitterIssueCtePayloadImpostosIbsCbsCompraGovernamentalVariant0', 'EmitterIssueCtePayloadImpostosIbsCbsEstornoCredito', 'EmitterIssueCtePayloadImpostosIbsCbsIbsEstadual', 'EmitterIssueCtePayloadImpostosIbsCbsIbsMunicipal', 'EmitterIssueCtePayloadImpostosIbsCbsCbs', 'EmitterIssueCtePayloadImpostosIbsCbsCreditoPresumido', 'EmitterIssueCtePayloadImpostosIbsCbs', 'EmitterIssueCtePayloadImpostos', 'EmitterIssueCtePayloadLocalInicioPrestacao', 'EmitterIssueCtePayloadLocalTerminoPrestacao', 'EmitterIssueCtePayloadMultimodalSeguro', 'EmitterIssueCtePayloadMultimodal', 'EmitterIssueCtePayloadObservacoesContribuinteItem', 'EmitterIssueCtePayloadObservacoesFiscoItem', 'EmitterIssueCtePayloadPagamentosVinculadosItem', 'EmitterIssueCtePayloadRecebedor', 'EmitterIssueCtePayloadRemetente', 'EmitterIssueCtePayloadRodoviarioOrdensColetaItemEmissor', 'EmitterIssueCtePayloadRodoviarioOrdensColetaItem', 'EmitterIssueCtePayloadRodoviarioVeiculoProprietario', 'EmitterIssueCtePayloadRodoviarioVeiculo', 'EmitterIssueCtePayloadRodoviario', 'EmitterIssueCtePayloadServico', 'EmitterIssueCtePayloadTomador', 'EmitterIssueCtePayloadVeiculosNovosItem', 'EmitterIssueCtePayload', 'EmitterIssueSimplifiedCtePayload', 'EmitterCancelCtePayload', 'EmitterCorrectCtePayloadAlteracoesItem', 'EmitterCorrectCtePayload', 'EmitterConfirmCteDeliveryPayload', 'EmitterCancelCteDeliveryPayload', 'EmitterLinkCtePaymentPayloadPagamento', 'EmitterLinkCtePaymentPayload', 'EmitterCancelCtePaymentLinkPayload', 'CteDocumentedGroup654', 'CteDocumentedGroup5669', 'CteDocumentedGroup5730', 'CteDocumentedGroup5835', 'CteDocumentedGroup5904', 'CteDocumentedGroup5949', 'CteDocumentedGroup6032Pagamento', 'CteDocumentedGroup6032', 'CteDocumentedGroup6120', 'CteServiceGroup', 'CteOsServiceGroup', 'emitterIssueCteResponse', 'emitterIssueSimplifiedCteResponse', 'emitterCancelCteResponse', 'emitterCorrectCteResponse', 'emitterConfirmCteDeliveryResponse', 'emitterCancelCteDeliveryResponse', 'emitterLinkCtePaymentResponse', 'emitterCancelCtePaymentLinkResponse', 'emitterGetCteResponse', 'emitterGetCteIdentifierParameter', 'emitterGetCtePaymentEventsResponse', 'emitterGetCtePaymentEventsIdentifierParameter'])
