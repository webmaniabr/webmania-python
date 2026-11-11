"""Generated from contracts/api2/mdfe-issuance.openapi.json; SHA256 ba9f4259c1828cd0b8246c633cf5ad818f266e08c08010faa583de91be849d9a. Do not edit."""
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

EmitterIssueMdfePayloadAereo = TypedDict('EmitterIssueMdfePayloadAereo', {'aerodromo_destino': str, 'aerodromo_embarque': str, 'data_voo': str, 'matricula_aeronave': str, 'nacionalidade_aeronave': str, 'numero_voo': str}, total=False)

EmitterIssueMdfePayloadAquaviarioCargaVaziaItem = TypedDict('EmitterIssueMdfePayloadAquaviarioCargaVaziaItem', {'identificador': Required[str], 'tipo_unidade': Required[Literal['1', '2', '3', '4', 1, 2, 3, 4]]}, total=False)

EmitterIssueMdfePayloadAquaviarioEmbarcacaoComboioItem = TypedDict('EmitterIssueMdfePayloadAquaviarioEmbarcacaoComboioItem', {'codigo': Required[str], 'identificador_balsa': Required[str]}, total=False)

EmitterIssueMdfePayloadAquaviarioTerminalCarregamentoItem = TypedDict('EmitterIssueMdfePayloadAquaviarioTerminalCarregamentoItem', {'codigo': Required[str], 'nome': Required[str]}, total=False)

EmitterIssueMdfePayloadAquaviarioTerminalDescarregamentoItem = TypedDict('EmitterIssueMdfePayloadAquaviarioTerminalDescarregamentoItem', {'codigo': Required[str], 'nome': Required[str]}, total=False)

EmitterIssueMdfePayloadAquaviarioTransporteVazioItem = TypedDict('EmitterIssueMdfePayloadAquaviarioTransporteVazioItem', {'identificador': Required[str], 'tipo_unidade': Required[Literal['1', '2', 1, 2]]}, total=False)

EmitterIssueMdfePayloadAquaviario = TypedDict('EmitterIssueMdfePayloadAquaviario', {'carga_vazia': list['EmitterIssueMdfePayloadAquaviarioCargaVaziaItem'], 'codigo_embarcacao': str, 'codigo_porto_destino': str, 'codigo_porto_embarque': str, 'embarcacao_comboio': list['EmitterIssueMdfePayloadAquaviarioEmbarcacaoComboioItem'], 'irin': str, 'nome_embarcacao': str, 'numero_viagem': str, 'porto_transbordo': str, 'terminal_carregamento': list['EmitterIssueMdfePayloadAquaviarioTerminalCarregamentoItem'], 'terminal_descarregamento': list['EmitterIssueMdfePayloadAquaviarioTerminalDescarregamentoItem'], 'tipo_embarcacao': str, 'tipo_navegacao': Literal['0', '1', 0, 1], 'transporte_vazio': list['EmitterIssueMdfePayloadAquaviarioTransporteVazioItem'], 'mmsi': str}, total=False)

EmitterIssueMdfePayloadCarregamentoItem = TypedDict('EmitterIssueMdfePayloadCarregamentoItem', {'codigo_municipio': str, 'nome_municipio': Required[str]}, total=False)

EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemEntregaParcial = TypedDict('EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemEntregaParcial', {'quantidade_parcial': Union[str, Union[int, float]], 'quantidade_total': Union[str, Union[int, float]]}, total=False)

EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItemEntregaParcial = TypedDict('EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItemEntregaParcial', {}, total=False)

EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItem = TypedDict('EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItem', {'classe_risco': str, 'grupo_embalagem': str, 'nome_embarque': str, 'numero_onu': Required[str], 'quantidade_total': Required[str], 'quantidade_volumes': str, 'entrega_parcial': 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItemEntregaParcial'}, total=False)

EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItemUnidadeCargaItem = TypedDict('EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItemUnidadeCargaItem', {'id_carga': Required[str], 'lacres': list[str], 'tipo_carga': Required[Literal['1', '2', '3', '4', 1, 2, 3, 4]], 'tipo': Union[Union[int, float], str], 'identificacao': str, 'quantidade_rateada': str}, total=False)

EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItem = TypedDict('EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItem', {'identificacao': Required[str], 'lacres': list[str], 'tipo': Required[Literal['1', '2', '3', '4', '5', '6', '7', 1, 2, 3, 4, 5, 6, 7]], 'unidade_carga': list['EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItemUnidadeCargaItem'], 'quantidade_rateada': str}, total=False)

EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItem = TypedDict('EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItem', {'chave': Required[str], 'codigo_barra': str, 'entrega_parcial': 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemEntregaParcial', 'indicador_reentrega': Literal['0', '1', 0, 1], 'periculosidade': list['EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItem'], 'unidade_transporte': list['EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItem']}, total=False)

EmitterIssueMdfePayloadDescarregamentoItem = TypedDict('EmitterIssueMdfePayloadDescarregamentoItem', {'codigo_municipio': str, 'documentos_fiscais': Required[list['EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItem']], 'nome_municipio': Required[str]}, total=False)

EmitterIssueMdfePayloadFerroviarioTrem = TypedDict('EmitterIssueMdfePayloadFerroviarioTrem', {'data_liberacao': str, 'destino': str, 'origem': str, 'prefixo': str}, total=False)

EmitterIssueMdfePayloadFerroviarioVagoesItem = TypedDict('EmitterIssueMdfePayloadFerroviarioVagoesItem', {'numero': Required[str], 'peso_bc': Required[str], 'peso_real': Required[str], 'sequencia_vagao': str, 'serie': Required[str], 'tipo_vagao': str, 'tonelada_util': Required[str]}, total=False)

EmitterIssueMdfePayloadFerroviario = TypedDict('EmitterIssueMdfePayloadFerroviario', {'trem': 'EmitterIssueMdfePayloadFerroviarioTrem', 'vagoes': list['EmitterIssueMdfePayloadFerroviarioVagoesItem']}, total=False)

EmitterIssueMdfePayloadProdutoPredominanteLotacaoCarregamento = TypedDict('EmitterIssueMdfePayloadProdutoPredominanteLotacaoCarregamento', {'cep': str, 'latitude': str, 'longitude': str}, total=False)

EmitterIssueMdfePayloadProdutoPredominanteLotacaoDescarregamento = TypedDict('EmitterIssueMdfePayloadProdutoPredominanteLotacaoDescarregamento', {'cep': str, 'latitude': str, 'longitude': str}, total=False)

EmitterIssueMdfePayloadProdutoPredominanteLotacao = TypedDict('EmitterIssueMdfePayloadProdutoPredominanteLotacao', {'carregamento': 'EmitterIssueMdfePayloadProdutoPredominanteLotacaoCarregamento', 'descarregamento': 'EmitterIssueMdfePayloadProdutoPredominanteLotacaoDescarregamento'}, total=False)

EmitterIssueMdfePayloadProdutoPredominante = TypedDict('EmitterIssueMdfePayloadProdutoPredominante', {'gtin': str, 'lotacao': 'EmitterIssueMdfePayloadProdutoPredominanteLotacao', 'ncm': str, 'nome': str, 'tipo_carga': Literal['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}, total=False)

EmitterIssueMdfePayloadRodoviarioCiotItem = TypedDict('EmitterIssueMdfePayloadRodoviarioCiotItem', {'cnpj_responsavel': str, 'codigo_ciot': Required[str], 'cpf_responsavel': str}, total=False)

EmitterIssueMdfePayloadRodoviarioCondutorItem = TypedDict('EmitterIssueMdfePayloadRodoviarioCondutorItem', {'cpf': Required[str], 'nome': Required[str]}, total=False)

EmitterIssueMdfePayloadRodoviarioContratanteItem = TypedDict('EmitterIssueMdfePayloadRodoviarioContratanteItem', {'cnpj': str, 'cpf': str}, total=False)

EmitterIssueMdfePayloadRodoviarioValePedagioItem = TypedDict('EmitterIssueMdfePayloadRodoviarioValePedagioItem', {'cnpj_fornecedor': Required[str], 'cnpj_responsavel': str, 'comprovante': Required[str], 'cpf_responsavel': str, 'valor': Required[Union[Union[int, float], str]], 'tipo': str}, total=False)

EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItemProprietario = TypedDict('EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItemProprietario', {'cnpj': str, 'cpf': str, 'ie': str, 'nome': str, 'razao_social': str, 'rntrc': str, 'tipo_proprietario': Literal['0', '1', '2', 0, 1, 2], 'uf': str}, total=False)

EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItem = TypedDict('EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItem', {'capacidade_kg': Required[str], 'capacidade_m3': str, 'codigo_agendamento_porto': str, 'codigo_interno': str, 'placa': Required[str], 'proprietario': 'EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItemProprietario', 'renavam': str, 'tara': Required[str], 'tipo_carroceria': Required[Literal['00', '01', '02', '03', '04', '05', 0, 1, 2, 3, 4, 5]], 'uf_licenciamento': Required[str]}, total=False)

EmitterIssueMdfePayloadRodoviarioVeiculoTracaoProprietario = TypedDict('EmitterIssueMdfePayloadRodoviarioVeiculoTracaoProprietario', {'cnpj': str, 'cpf': str, 'ie': str, 'nome': str, 'razao_social': str, 'rntrc': str, 'tipo_proprietario': Literal['0', '1', '2', 0, 1, 2], 'uf': str}, total=False)

EmitterIssueMdfePayloadRodoviarioVeiculoTracao = TypedDict('EmitterIssueMdfePayloadRodoviarioVeiculoTracao', {'capacidade_kg': str, 'capacidade_m3': str, 'codigo_interno': str, 'placa': str, 'proprietario': 'EmitterIssueMdfePayloadRodoviarioVeiculoTracaoProprietario', 'renavam': str, 'tara': str, 'tipo_carroceria': Literal['00', '01', '02', '03', '04', '05', 0, 1, 2, 3, 4, 5], 'tipo_rodado': Literal['01', '02', '03', '04', '05', '06', 1, 2, 3, 4, 5, 6], 'uf_licenciamento': str}, total=False)

EmitterIssueMdfePayloadRodoviario = TypedDict('EmitterIssueMdfePayloadRodoviario', {'ciot': list['EmitterIssueMdfePayloadRodoviarioCiotItem'], 'condutor': list['EmitterIssueMdfePayloadRodoviarioCondutorItem'], 'contratante': list['EmitterIssueMdfePayloadRodoviarioContratanteItem'], 'lacres': list[str], 'rntrc': str, 'vale_pedagio': list['EmitterIssueMdfePayloadRodoviarioValePedagioItem'], 'veiculo_reboque': list['EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItem'], 'veiculo_tracao': 'EmitterIssueMdfePayloadRodoviarioVeiculoTracao', 'combinacao_veicular': str, 'pagamento_frete': list['MdfeFreightPaymentGroup']}, total=False)

EmitterIssueMdfePayloadSeguroItemResponsavel = TypedDict('EmitterIssueMdfePayloadSeguroItemResponsavel', {'cnpj': str, 'cpf': str, 'tipo_responsavel': Literal['1', '2', 1, 2]}, total=False)

EmitterIssueMdfePayloadSeguroItemSeguradora = TypedDict('EmitterIssueMdfePayloadSeguroItemSeguradora', {'cnpj': str, 'nome_seguradora': str}, total=False)

EmitterIssueMdfePayloadSeguroItem = TypedDict('EmitterIssueMdfePayloadSeguroItem', {'numero_apolice': str, 'numero_averbacao': list[str], 'responsavel': Required['EmitterIssueMdfePayloadSeguroItemResponsavel'], 'seguradora': 'EmitterIssueMdfePayloadSeguroItemSeguradora'}, total=False)

EmitterIssueMdfePayload = TypedDict('EmitterIssueMdfePayload', {'aereo': 'EmitterIssueMdfePayloadAereo', 'ambiente': Required[Literal['1', '2', 1, 2]], 'aquaviario': 'EmitterIssueMdfePayloadAquaviario', 'carregamento': Required[list['EmitterIssueMdfePayloadCarregamentoItem']], 'data_inicio_viagem': str, 'descarregamento': Required[list['EmitterIssueMdfePayloadDescarregamentoItem']], 'emitente': Required[Literal['1', '2', '3', 1, 2, 3]], 'ferroviario': 'EmitterIssueMdfePayloadFerroviario', 'ind_canal_verde': Literal['0', '1', 0, 1], 'informacoes_complementares': str, 'informacoes_fisco': str, 'lacres': list[str], 'modalidade': Required[Literal['1', '2', '3', '4', 1, 2, 3, 4]], 'origem': str, 'percurso': list[str], 'peso_bruto': Required[str], 'produto_predominante': 'EmitterIssueMdfePayloadProdutoPredominante', 'rodoviario': 'EmitterIssueMdfePayloadRodoviario', 'seguro': list['EmitterIssueMdfePayloadSeguroItem'], 'transportador': Literal['1', '2', '3', 1, 2, 3], 'uf_carregamento': Required[str], 'uf_descarregamento': Required[str], 'unidade': Required[Literal['01', '02', 1, 2]], 'valor_carga': Required[str], 'url_notificacao': str}, total=False)

EmitterCloseMdfePayload = TypedDict('EmitterCloseMdfePayload', {'chave': str, 'codigo_municipio': str, 'municipio': str, 'uf': str, 'uuid': str}, total=False)

EmitterCancelMdfePayload = TypedDict('EmitterCancelMdfePayload', {'chave': str, 'justificativa': Required[str], 'uuid': str}, total=False)

EmitterAddMdfeConductorPayload = TypedDict('EmitterAddMdfeConductorPayload', {'chave': str, 'cpf': Required[str], 'nome': Required[str], 'uuid': str}, total=False)

MdfeDocumentedGroup465 = TypedDict('MdfeDocumentedGroup465', {'uuid': str, 'chave': str, 'serie': Union[Union[int, float], str], 'mdfe': Union[Union[int, float], str], 'status': str, 'motivo': str, 'xml': str, 'damdfe': str, 'log': list[JSONValue]}, total=False)

MdfeDocumentedGroup3210 = TypedDict('MdfeDocumentedGroup3210', {'uuid': str, 'uf': str, 'municipio': str, 'codigo_municipio': str}, total=False)

MdfeDocumentedGroup3297 = TypedDict('MdfeDocumentedGroup3297', {'uuid': str, 'justificativa': str}, total=False)

MdfeDocumentedGroup3362 = TypedDict('MdfeDocumentedGroup3362', {'uuid': str, 'cpf': str, 'nome': str}, total=False)

MdfeFreightPaymentGroupVariant0ComponentesPagamentoFreteItem = TypedDict('MdfeFreightPaymentGroupVariant0ComponentesPagamentoFreteItem', {'tipo_componente': Required[Literal[1, 2, 3, 4, 99, '1', '2', '3', '4', '01', '02', '03', '04', '99']], 'valor_componente': Required[str], 'descricao_componente': str}, total=False)

MdfeFreightPaymentGroupVariant0InformacoesBancarias = TypedDict('MdfeFreightPaymentGroupVariant0InformacoesBancarias', {'tipo_informacao_bancaria': Required[Literal[1, 2, 3, '1', '2', '3']], 'numero_banco': str, 'numero_agencia': str, 'cnpj_ipef': str, 'pix': str}, total=False)

MdfeFreightPaymentGroupVariant0InformacoesPagamentoPrazoItem = TypedDict('MdfeFreightPaymentGroupVariant0InformacoesPagamentoPrazoItem', {'data_vencimento_parcela': str, 'valor_parcela': str}, total=False)

MdfeFreightPaymentGroupVariant0 = TypedDict('MdfeFreightPaymentGroupVariant0', {'cpf': Required[str], 'nome': str, 'cnpj': str, 'razao_social': str, 'id_estrangeiro': str, 'valor_contrato': Required[str], 'forma_pagamento': Required[Literal[0, 1, '0', '1']], 'operacao_alto_desempenho': bool, 'valor_adiantamento': str, 'antecipar_adiantamento': bool, 'permissao_antecipacao_parcela': Literal[0, 1, 2, '0', '1', '2'], 'componentes_pagamento_frete': Required[list['MdfeFreightPaymentGroupVariant0ComponentesPagamentoFreteItem']], 'informacoes_bancarias': Required['MdfeFreightPaymentGroupVariant0InformacoesBancarias'], 'informacoes_pagamento_prazo': list['MdfeFreightPaymentGroupVariant0InformacoesPagamentoPrazoItem']}, total=False)

MdfeFreightPaymentGroupVariant1ComponentesPagamentoFreteItem = TypedDict('MdfeFreightPaymentGroupVariant1ComponentesPagamentoFreteItem', {'tipo_componente': Required[Literal[1, 2, 3, 4, 99, '1', '2', '3', '4', '01', '02', '03', '04', '99']], 'valor_componente': Required[str], 'descricao_componente': str}, total=False)

MdfeFreightPaymentGroupVariant1InformacoesBancarias = TypedDict('MdfeFreightPaymentGroupVariant1InformacoesBancarias', {'tipo_informacao_bancaria': Required[Literal[1, 2, 3, '1', '2', '3']], 'numero_banco': str, 'numero_agencia': str, 'cnpj_ipef': str, 'pix': str}, total=False)

MdfeFreightPaymentGroupVariant1InformacoesPagamentoPrazoItem = TypedDict('MdfeFreightPaymentGroupVariant1InformacoesPagamentoPrazoItem', {'data_vencimento_parcela': str, 'valor_parcela': str}, total=False)

MdfeFreightPaymentGroupVariant1 = TypedDict('MdfeFreightPaymentGroupVariant1', {'cpf': str, 'nome': str, 'cnpj': Required[str], 'razao_social': str, 'id_estrangeiro': str, 'valor_contrato': Required[str], 'forma_pagamento': Required[Literal[0, 1, '0', '1']], 'operacao_alto_desempenho': bool, 'valor_adiantamento': str, 'antecipar_adiantamento': bool, 'permissao_antecipacao_parcela': Literal[0, 1, 2, '0', '1', '2'], 'componentes_pagamento_frete': Required[list['MdfeFreightPaymentGroupVariant1ComponentesPagamentoFreteItem']], 'informacoes_bancarias': Required['MdfeFreightPaymentGroupVariant1InformacoesBancarias'], 'informacoes_pagamento_prazo': list['MdfeFreightPaymentGroupVariant1InformacoesPagamentoPrazoItem']}, total=False)

MdfeFreightPaymentGroupVariant2ComponentesPagamentoFreteItem = TypedDict('MdfeFreightPaymentGroupVariant2ComponentesPagamentoFreteItem', {'tipo_componente': Required[Literal[1, 2, 3, 4, 99, '1', '2', '3', '4', '01', '02', '03', '04', '99']], 'valor_componente': Required[str], 'descricao_componente': str}, total=False)

MdfeFreightPaymentGroupVariant2InformacoesBancarias = TypedDict('MdfeFreightPaymentGroupVariant2InformacoesBancarias', {'tipo_informacao_bancaria': Required[Literal[1, 2, 3, '1', '2', '3']], 'numero_banco': str, 'numero_agencia': str, 'cnpj_ipef': str, 'pix': str}, total=False)

MdfeFreightPaymentGroupVariant2InformacoesPagamentoPrazoItem = TypedDict('MdfeFreightPaymentGroupVariant2InformacoesPagamentoPrazoItem', {'data_vencimento_parcela': str, 'valor_parcela': str}, total=False)

MdfeFreightPaymentGroupVariant2 = TypedDict('MdfeFreightPaymentGroupVariant2', {'cpf': str, 'nome': str, 'cnpj': str, 'razao_social': str, 'id_estrangeiro': Required[str], 'valor_contrato': Required[str], 'forma_pagamento': Required[Literal[0, 1, '0', '1']], 'operacao_alto_desempenho': bool, 'valor_adiantamento': str, 'antecipar_adiantamento': bool, 'permissao_antecipacao_parcela': Literal[0, 1, 2, '0', '1', '2'], 'componentes_pagamento_frete': Required[list['MdfeFreightPaymentGroupVariant2ComponentesPagamentoFreteItem']], 'informacoes_bancarias': Required['MdfeFreightPaymentGroupVariant2InformacoesBancarias'], 'informacoes_pagamento_prazo': list['MdfeFreightPaymentGroupVariant2InformacoesPagamentoPrazoItem']}, total=False)

MdfeFreightPaymentGroup: TypeAlias = Union['MdfeFreightPaymentGroupVariant0', 'MdfeFreightPaymentGroupVariant1', 'MdfeFreightPaymentGroupVariant2']

emitterIssueMdfeResponse: TypeAlias = Union['MdfeFiscalResponse']

emitterCloseMdfeResponse: TypeAlias = Union['FiscalEventResponse']

emitterCancelMdfeResponse: TypeAlias = Union['FiscalEventResponse']

emitterAddMdfeConductorResponse: TypeAlias = Union['FiscalEventResponse']

emitterGetMdfeResponse: TypeAlias = Union['MdfeFiscalResponse']

emitterGetMdfeKeyParameter: TypeAlias = str

_bind_types(globals(), __name__, ['EmitterError', 'NfseServiceCodeAliquotaSugerida', 'NfseServiceCode', 'NfseParameterRequirements', 'NfseProviderStatus', 'NfcomServiceStatus', 'NfseFiscalResponseNfseSubstituida', 'NfseFiscalResponseInfoNfseItem', 'NfseFiscalResponseLogVariant0', 'NfseFiscalResponse', 'NfcomPaymentEventPagamentoVariant0', 'NfcomPaymentEvent', 'NfcomFiscalResponseLogVariant0Variant0', 'NfcomFiscalResponse', 'NfcomPaymentEvents', 'NfseManifestationRequest', 'CteFiscalResponseLogVariant0', 'CteFiscalResponseEventosPagamentoItem', 'CteFiscalResponse', 'MdfeFiscalResponseLogVariant0', 'MdfeFiscalResponse', 'DceFiscalResponseLogVariant0', 'DceFiscalResponse', 'FiscalEventResponseLogVariant0', 'FiscalEventResponse', 'CtePaymentEventsEventosPagamentoItem', 'CtePaymentEvents', 'EmitterIssueMdfePayloadAereo', 'EmitterIssueMdfePayloadAquaviarioCargaVaziaItem', 'EmitterIssueMdfePayloadAquaviarioEmbarcacaoComboioItem', 'EmitterIssueMdfePayloadAquaviarioTerminalCarregamentoItem', 'EmitterIssueMdfePayloadAquaviarioTerminalDescarregamentoItem', 'EmitterIssueMdfePayloadAquaviarioTransporteVazioItem', 'EmitterIssueMdfePayloadAquaviario', 'EmitterIssueMdfePayloadCarregamentoItem', 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemEntregaParcial', 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItemEntregaParcial', 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemPericulosidadeItem', 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItemUnidadeCargaItem', 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItemUnidadeTransporteItem', 'EmitterIssueMdfePayloadDescarregamentoItemDocumentosFiscaisItem', 'EmitterIssueMdfePayloadDescarregamentoItem', 'EmitterIssueMdfePayloadFerroviarioTrem', 'EmitterIssueMdfePayloadFerroviarioVagoesItem', 'EmitterIssueMdfePayloadFerroviario', 'EmitterIssueMdfePayloadProdutoPredominanteLotacaoCarregamento', 'EmitterIssueMdfePayloadProdutoPredominanteLotacaoDescarregamento', 'EmitterIssueMdfePayloadProdutoPredominanteLotacao', 'EmitterIssueMdfePayloadProdutoPredominante', 'EmitterIssueMdfePayloadRodoviarioCiotItem', 'EmitterIssueMdfePayloadRodoviarioCondutorItem', 'EmitterIssueMdfePayloadRodoviarioContratanteItem', 'EmitterIssueMdfePayloadRodoviarioValePedagioItem', 'EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItemProprietario', 'EmitterIssueMdfePayloadRodoviarioVeiculoReboqueItem', 'EmitterIssueMdfePayloadRodoviarioVeiculoTracaoProprietario', 'EmitterIssueMdfePayloadRodoviarioVeiculoTracao', 'EmitterIssueMdfePayloadRodoviario', 'EmitterIssueMdfePayloadSeguroItemResponsavel', 'EmitterIssueMdfePayloadSeguroItemSeguradora', 'EmitterIssueMdfePayloadSeguroItem', 'EmitterIssueMdfePayload', 'EmitterCloseMdfePayload', 'EmitterCancelMdfePayload', 'EmitterAddMdfeConductorPayload', 'MdfeDocumentedGroup465', 'MdfeDocumentedGroup3210', 'MdfeDocumentedGroup3297', 'MdfeDocumentedGroup3362', 'MdfeFreightPaymentGroupVariant0ComponentesPagamentoFreteItem', 'MdfeFreightPaymentGroupVariant0InformacoesBancarias', 'MdfeFreightPaymentGroupVariant0InformacoesPagamentoPrazoItem', 'MdfeFreightPaymentGroupVariant0', 'MdfeFreightPaymentGroupVariant1ComponentesPagamentoFreteItem', 'MdfeFreightPaymentGroupVariant1InformacoesBancarias', 'MdfeFreightPaymentGroupVariant1InformacoesPagamentoPrazoItem', 'MdfeFreightPaymentGroupVariant1', 'MdfeFreightPaymentGroupVariant2ComponentesPagamentoFreteItem', 'MdfeFreightPaymentGroupVariant2InformacoesBancarias', 'MdfeFreightPaymentGroupVariant2InformacoesPagamentoPrazoItem', 'MdfeFreightPaymentGroupVariant2', 'MdfeFreightPaymentGroup', 'emitterIssueMdfeResponse', 'emitterCloseMdfeResponse', 'emitterCancelMdfeResponse', 'emitterAddMdfeConductorResponse', 'emitterGetMdfeResponse', 'emitterGetMdfeKeyParameter'])
