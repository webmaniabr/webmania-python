"""Generated from contracts/api1/fiscal.openapi.json; SHA256 43712eba9626482c0fafa40915a9b4c0bdf0db32fd71d2c2c4397ad06c3efb42. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

AccessKey: TypeAlias = str

Uuid: TypeAlias = str

Environment: TypeAlias = Union[Literal[1, 2], Literal['1', '2']]

Decimal: TypeAlias = Union[str, Union[int, float]]

Api1ErrorLogVariant1 = TypedDict('Api1ErrorLogVariant1', {'cStat': Union[str, int], 'xMotivo': str}, total=False)

Api1Error = TypedDict('Api1Error', {'error': Required[Union[str, list[str]]], 'message': str, 'code': Union[str, int], 'status': str, 'log': Union[str, 'Api1ErrorLogVariant1']}, total=False)

SefazLogEventoVariant0 = TypedDict('SefazLogEventoVariant0', {'cStat': Union[str, int], 'xMotivo': str, 'nProt': str}, total=False)

SefazLogEventoVariant1Item = TypedDict('SefazLogEventoVariant1Item', {'cStat': Union[str, int], 'xMotivo': str, 'nProt': str}, total=False)

SefazLog = TypedDict('SefazLog', {'cStat': Union[str, int], 'xMotivo': str, 'nProt': str, 'tpAmb': Union[str, int], 'dhRecbto': str, 'chNFe': str, 'verAplic': str, 'evento': Union['SefazLogEventoVariant0', list['SefazLogEventoVariant1Item']]}, total=False)

NfeDocument = TypedDict('NfeDocument', {'uuid': Required['Uuid'], 'status': Required[str], 'motivo': str, 'nfe': Union[str, int], 'serie': Union[str, int], 'recibo': str, 'chave': str, 'modelo': str, 'epec': bool, 'xml': str, 'xml_cancelamento': str, 'danfe': str, 'danfe_simples': str, 'danfe_etiqueta': str, 'log': Union['SefazLog', str, list['SefazLog'], None], 'log_cancelamento': Union['SefazLog', str, list['SefazLog'], None], 'data': str, 'evento': Union[str, int], 'dacce': str, 'protocolo_evento': str, 'url_notificacao': str}, total=False)

NfeEventResult = TypedDict('NfeEventResult', {'uuid': Required['Uuid'], 'status': Required[str], 'evento': Union[str, int], 'modelo': str, 'chave': str, 'cod_evento': str, 'xml': str, 'dacce': str, 'protocolo_evento': str, 'log': Union['SefazLog', str, list['SefazLog'], None], 'motivo': str}, total=False)

NfeCancelResult = TypedDict('NfeCancelResult', {'status': Required[str], 'xml': str, 'xml_cancelamento': str, 'log': Union['SefazLog', str, list['SefazLog'], None], 'motivo': str}, total=False)

NfeVoidResult = TypedDict('NfeVoidResult', {'xml': Required[str], 'log': Union['SefazLog', str, list['SefazLog'], None]}, total=False)

NfeCertificateValidity = TypedDict('NfeCertificateValidity', {'expiration': Required[int]}, total=False)

NfeSefazStatus = TypedDict('NfeSefazStatus', {'status': Required[Literal['online', 'offline']]}, total=False)

NfeLookupRequestVariant0 = TypedDict('NfeLookupRequestVariant0', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'ID': str, 'id': str, 'ambiente': 'Environment'}, total=False)

NfeLookupRequestVariant1 = TypedDict('NfeLookupRequestVariant1', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'ID': str, 'id': str, 'ambiente': 'Environment'}, total=False)

NfeLookupRequestVariant2 = TypedDict('NfeLookupRequestVariant2', {'chave': 'AccessKey', 'uuid': 'Uuid', 'ID': Required[str], 'id': str, 'ambiente': 'Environment'}, total=False)

NfeLookupRequestVariant3 = TypedDict('NfeLookupRequestVariant3', {'chave': 'AccessKey', 'uuid': 'Uuid', 'ID': str, 'id': Required[str], 'ambiente': 'Environment'}, total=False)

NfeLookupRequest: TypeAlias = Union['NfeLookupRequestVariant0', 'NfeLookupRequestVariant1', 'NfeLookupRequestVariant2', 'NfeLookupRequestVariant3']

NfeCorrectionRequestVariant0 = TypedDict('NfeCorrectionRequestVariant0', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'correcao': Required[str], 'ambiente': 'Environment', 'evento': int, 'url_notificacao': str}, total=False)

NfeCorrectionRequestVariant1 = TypedDict('NfeCorrectionRequestVariant1', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'correcao': Required[str], 'ambiente': 'Environment', 'evento': int, 'url_notificacao': str}, total=False)

NfeCorrectionRequest: TypeAlias = Union['NfeCorrectionRequestVariant0', 'NfeCorrectionRequestVariant1']

NfeManifestationRequest = TypedDict('NfeManifestationRequest', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'evento': Required[Union[Literal['210200', '210210', '210220', '210240'], Literal[210200, 210210, 210220, 210240]]], 'justificativa': str}, total=False)

NfeCancelRequestVariant0 = TypedDict('NfeCancelRequestVariant0', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'motivo': Required[str], 'nfce_referenciada': 'AccessKey'}, total=False)

NfeCancelRequestVariant1 = TypedDict('NfeCancelRequestVariant1', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'motivo': Required[str], 'nfce_referenciada': 'AccessKey'}, total=False)

NfeCancelRequest: TypeAlias = Union['NfeCancelRequestVariant0', 'NfeCancelRequestVariant1']

NfeVoidRequest = TypedDict('NfeVoidRequest', {'sequencia': Required[str], 'motivo': Required[str], 'ambiente': Required['Environment'], 'serie': Required[str], 'modelo': Required[Literal['1', '2']], 'ver_aplic': str}, total=False)

NfePaymentEventItem = TypedDict('NfePaymentEventItem', {'indicador_pagamento': int, 'forma_pagamento': Required[str], 'desc_pagamento': str, 'valor_pagamento': Required[Union[str, Union[int, float]]], 'data_pagamento': Required[str], 'cnpj_transacional_pag': str, 'uf_pagamento': str, 'cnpj_instituicao_financeira': str, 'bandeira': str, 'autorizacao': str, 'cnpj_beneficiario': str, 'uf_beneficiario': str}, total=False)

NfePaymentEventRequestVariant0 = TypedDict('NfePaymentEventRequestVariant0', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'pagamento': Required['NfePaymentEventItem'], 'pagamentos': list['NfePaymentEventItem'], 'ambiente': 'Environment', 'evento': int, 'url_notificacao': str}, total=False)

NfePaymentEventRequestVariant1 = TypedDict('NfePaymentEventRequestVariant1', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'pagamento': 'NfePaymentEventItem', 'pagamentos': Required[list['NfePaymentEventItem']], 'ambiente': 'Environment', 'evento': int, 'url_notificacao': str}, total=False)

NfePaymentEventRequestVariant2 = TypedDict('NfePaymentEventRequestVariant2', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'pagamento': Required['NfePaymentEventItem'], 'pagamentos': list['NfePaymentEventItem'], 'ambiente': 'Environment', 'evento': int, 'url_notificacao': str}, total=False)

NfePaymentEventRequestVariant3 = TypedDict('NfePaymentEventRequestVariant3', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'pagamento': 'NfePaymentEventItem', 'pagamentos': Required[list['NfePaymentEventItem']], 'ambiente': 'Environment', 'evento': int, 'url_notificacao': str}, total=False)

NfePaymentEventRequest: TypeAlias = Union['NfePaymentEventRequestVariant0', 'NfePaymentEventRequestVariant1', 'NfePaymentEventRequestVariant2', 'NfePaymentEventRequestVariant3']

NfePaymentEventCancelRequest = TypedDict('NfePaymentEventCancelRequest', {'uuid': Required[str], 'url_notificacao': str}, total=False)

NfeIbsCbsEventCancelRequest = TypedDict('NfeIbsCbsEventCancelRequest', {'uuid': Required[str], 'ambiente': 'Environment', 'url_notificacao': str}, total=False)

TaxClassDeleteRequest = TypedDict('TaxClassDeleteRequest', {'referencia': Required[Union[str, list[str]]]}, total=False)

TaxClassDeleteItem = TypedDict('TaxClassDeleteItem', {'referencia': Required[str], 'msg': str, 'error': str}, total=False)

TaxClassNoResults = TypedDict('TaxClassNoResults', {'msg': Required[str]}, total=False)

TaxClassListItem = TypedDict('TaxClassListItem', {'referencia': str, 'descricao': str, 'icms': Union[list['TaxClassListIcms'], 'TaxClassListGroupObject'], 'ipi': list['TaxClassListIpi'], 'pis': Union[list['TaxClassListPis'], 'TaxClassListGroupObject', Union[int, float]], 'cofins': Union[list['TaxClassListCofins'], 'TaxClassListGroupObject', Union[int, float]], 'issqn': list['TaxClassListIssqn'], 'ibs_cbs': Union[list['TaxClassListIbsCbs'], 'TaxClassListGroupObject'], 'informacoes_fisco': str, 'informacoes_complementares': str, 'tipo': str, 'tributos_federais': Union[str, Union[int, float]], 'tributos_estaduais': Union[str, Union[int, float]], 'type': Required[str], 'data': str, 'updated_date': str, 'status': str}, total=False)

TaxClassListIcms = TypedDict('TaxClassListIcms', {'tipo_tributacao': str, 'cenario': str, 'tipo_pessoa': str, 'nao_contribuinte': Union[bool, Literal['0', '1']], 'codigo_cfop': str, 'situacao_tributaria': str, 'aliquota_importacao': Union[str, Union[int, float]], 'aliquota_credito': Union[str, Union[int, float]], 'aliquota_reducao_destino': Union[str, Union[int, float]], 'aliquota_mva': 'TaxClassListStateRates', 'aliquota': 'TaxClassListStateRates', 'aliquota_st': 'TaxClassListStateRates', 'aliquota_fcp': 'TaxClassListStateRates', 'aliquota_fcp_st': 'TaxClassListStateRates', 'aliquota_diferimento': Union[str, Union[int, float]], 'aliquota_diferimento_fcp': Union[str, Union[int, float]], 'aliquota_reducao': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]], 'aliquota_efetiva_icms': Union[str, Union[int, float]], 'aliquota_efetiva_icms_st': Union[str, Union[int, float]], 'codigo_beneficio_reducao_bc': str, 'motivo_desoneracao': str, 'deducao_desoneracao': str, 'motivo_desoneracao_st': str, 'beneficio_fiscal': list['G043'], 'credito_presumido': list['TaxClassListIcmsPresumedCredit']}, total=False)

TaxClassListIpi = TypedDict('TaxClassListIpi', {'cenario': str, 'tipo_pessoa': str, 'situacao_tributaria': str, 'codigo_enquadramento': str, 'aliquota': Union[str, Union[int, float], None]}, total=False)

TaxClassListPis = TypedDict('TaxClassListPis', {'cenario': str, 'tipo_pessoa': str, 'situacao_tributaria': str, 'aliquota': Union[str, Union[int, float], None]}, total=False)

TaxClassListCofins = TypedDict('TaxClassListCofins', {'cenario': str, 'tipo_pessoa': str, 'situacao_tributaria': str, 'aliquota': Union[str, Union[int, float], None]}, total=False)

TaxClassListGroupObject = TypedDict('TaxClassListGroupObject', {}, total=False)

TaxClassListIssqn = TypedDict('TaxClassListIssqn', {'cenario': str, 'tipo_pessoa': str, 'codigo_cfop': str, 'exigibilidade': str, 'item_servico': str, 'incentivo_fiscal': str, 'aliquota': Union[str, Union[int, float], None], 'municipio': str, 'codigo_servico': str}, total=False)

TaxClassListIbsCbs = TypedDict('TaxClassListIbsCbs', {'cenario': str, 'tipo_pessoa': str, 'situacao_tributaria': str, 'classificacao_tributaria': str, 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'TaxClassListIbsCbsDeferral', 'ibs_municipal': 'TaxClassListIbsCbsDeferral', 'cbs': 'TaxClassListIbsCbsDeferral', 'credito_presumido': 'TaxClassListPresumedCredit'}, total=False)

TaxClassListPresumedCredit = TypedDict('TaxClassListPresumedCredit', {'classificacao': Union[str, None], 'aliquota_ibs': Union[str, Union[int, float]], 'aliquota_cbs': Union[str, Union[int, float]]}, total=False)

TaxClassListStateRate = TypedDict('TaxClassListStateRate', {'estado': str, 'aliquota': Union[str, Union[int, float]]}, total=False)

TaxClassListBareRate: TypeAlias = Union[str, Union[int, float]]

TaxClassListStateRates: TypeAlias = Union[list[Union['TaxClassListStateRate', 'TaxClassListBareRate']], 'TaxClassListStateRate', 'TaxClassListBareRate', None]

TaxClassListIcmsPresumedCredit = TypedDict('TaxClassListIcmsPresumedCredit', {'estado': str, 'codigo_beneficio_fiscal': str, 'aliquota': Union[str, Union[int, float]]}, total=False)

TaxClassListIbsCbsDeferral = TypedDict('TaxClassListIbsCbsDeferral', {'aliquota_diferimento': Union[str, Union[int, float]]}, total=False)

G002 = TypedDict('G002', {'uuid': str, 'status': str, 'motivo': str, 'nfe': int, 'serie': int, 'recibo': str, 'chave': str, 'modelo': str, 'epec': bool, 'xml': str, 'danfe': str, 'log': Union['SefazLog', str, list['SefazLog'], None], 'data': 'NfeIssueRequest', 'log_cancelamento': Union['SefazLog', str, list['SefazLog'], None]}, total=False)

G003 = TypedDict('G003', {'ID': str, 'operacao': int, 'natureza_operacao': str, 'modelo': str, 'finalidade': int, 'ambiente': int, 'tipo_credito': int, 'tipo_debito': int, 'url_notificacao': str, 'cliente': 'NfeCustomer', 'produtos': list['NfeProduct'], 'pedido': 'NfeOrder', 'transporte': 'NfeTransport', 'fatura': 'G028', 'parcelas': list['G029'], 'exportacao': 'G030', 'agropecuario': 'G031', 'compra_governamental': 'G034', 'inscricao_suframa': str, 'codigo_indicador_operacao': str}, total=False)

G004 = TypedDict('G004', {'data_emissao': str, 'data_entrada_saida': str, 'data_previsao_entrega': str, 'data_servico': str}, total=False)

G005 = TypedDict('G005', {'nfe_referenciada': Union['AccessKey', list['AccessKey']], 'cte_referenciada': Union['AccessKey', list['AccessKey']], 'ecf_referenciada': Union['G006', list['G006']], 'nf_rural_referenciada': Union['G007', list['G007']]}, total=False)

G006 = TypedDict('G006', {'modelo': Required[str], 'n_ecf': Required[str], 'n_coo': Required[str]}, total=False)

G007 = TypedDict('G007', {'uf': str, 'data': str, 'cpf': str, 'cnpj': str, 'ie': str, 'modelo': str, 'serie': str, 'numero': str}, total=False)

G008 = TypedDict('G008', {'calculo_impostos': bool, 'previa_danfe': bool, 'assincrono': bool}, total=False)

G009 = TypedDict('G009', {'cpf': str, 'nome_completo': str, 'cnpj': str, 'razao_social': str, 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': str, 'complemento': str, 'numero': str, 'bairro': str, 'cidade': str, 'uf': str, 'cep': str, 'telefone': str, 'email': str}, total=False)

G010 = TypedDict('G010', {'id_estrangeiro': str, 'nome_estrangeiro': str, 'cod_pais': str, 'nome_pais': str, 'endereco': str, 'bairro': str, 'numero': str, 'complemento': str}, total=False)

G011 = TypedDict('G011', {'ID': int, 'item': int, 'nome': str, 'codigo': str, 'ncm': str, 'quantidade': Union[str, Union[int, float]], 'quantidade_tributavel': Union[str, Union[int, float]], 'unidade': str, 'unidade_tributavel': str, 'peso': Union[str, Union[int, float]], 'origem': int, 'desconto': Union[str, Union[int, float]], 'subtotal': Union[str, Union[int, float]], 'subtotal_tributavel': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]], 'ind_valor_total': int, 'classe_imposto': str, 'impostos': 'G069', 'dfe_referenciado': 'G015', 'cest': str, 'beneficio_fiscal': str, 'informacoes_adicionais': str, 'ind_escala': str, 'cnpj_fabricante': str, 'gtin': str, 'gtin_tributavel': str, 'cod_barras': str, 'cod_barras_tributavel': str, 'nve': str, 'nrecopi': str, 'ativo_permanente': bool, 'veiculo_usado': Union[str, Union[int, float]], 'ex_ipi': str, 'combustiveis': 'G016', 'medicamento': 'G018', 'armamentos': 'G019', 'veiculos_novos': 'G020', 'rastro': list['G014']}, total=False)

G012 = TypedDict('G012', {'drawback': str, 'reg_exportacao': str, 'nfe_exportacao': str, 'qtd_exportacao': Union[str, Union[int, float]]}, total=False)

G013 = TypedDict('G013', {'subtotal': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]], 'ndoc_importacao': str, 'ddoc_importacao': str, 'local_desembaraco': str, 'uf_desembaraco': str, 'data_desembaraco': str, 'via_transporte': str, 'intermediacao': str, 'adicao': str, 'seq_adicao': str, 'fabricante': str, 'desc_di': Union[str, Union[int, float]], 'afrmm': Union[str, Union[int, float]], 'cnpj_terceiro': str, 'cpf_terceiro': str, 'uf_terceiro': str, 'cod_exportador': str, 'nfci': str}, total=False)

G014 = TypedDict('G014', {'lote': Required[str], 'quantidade': Required[Union[str, Union[int, float]]], 'data_fabricacao': Required[str], 'data_validade': Required[str], 'codigo_agregacao': str}, total=False)

G015 = TypedDict('G015', {'chave': Required[str], 'item': Required[int]}, total=False)

G016 = TypedDict('G016', {'codigo_anp': Required[str], 'descricao_anp': Required[str], 'uf_consumo': Required[str], 'percentual_glp': Union[str, Union[int, float]], 'percentual_gnn': Union[str, Union[int, float]], 'percentual_gni': Union[str, Union[int, float]], 'percentual_biodiesel': Union[str, Union[int, float]], 'partida': Union[str, Union[int, float]], 'codif': str, 'qtd_temperatura': Union[str, Union[int, float]], 'bc_cide': Union[str, Union[int, float]], 'valor_cide': Union[str, Union[int, float]], 'bico': int, 'bomba': int, 'tanque': int, 'encerrante_inicio': int, 'encerrante_final': int, 'origem': list['G017']}, total=False)

G017 = TypedDict('G017', {'indicador_importacao': str, 'uf_origem': str, 'percentual_originario': Union[str, Union[int, float]]}, total=False)

G018 = TypedDict('G018', {'codigo_anvisa': Required[str], 'pmc': Required[Union[str, Union[int, float]]]}, total=False)

G019 = TypedDict('G019', {'tipo': Required[int], 'serie_arma': Required[str], 'serie_cano': Required[str], 'descricao': Required[str]}, total=False)

G020 = TypedDict('G020', {'tipo_operacao': Required[int], 'chassi': Required[str], 'cor': Required[str], 'cor_descricao': Required[str], 'cv': Required[str], 'cilindrada': Required[str], 'peso_liquido': Required[int], 'peso_bruto': Required[int], 'serie': Required[str], 'tipo_combustivel': Required[int], 'numero_motor': Required[str], 'cmt': Required[Union[str, Union[int, float]]], 'dist': Required[str], 'ano_modelo': Required[str], 'ano_fabricacao': Required[str], 'tipo_pintura': Required[str], 'tipo_veiculo': Required[int], 'especie_veiculo': Required[int], 'vin': Required[str], 'condicao_veiculo': Required[int], 'marca_modelo': Required[str], 'cor_denatran': Required[int], 'lotacao': Required[int], 'restricao': Required[int]}, total=False)

G021 = TypedDict('G021', {'presenca': int, 'intermediador': int, 'cnpj_intermediador': str, 'id_intermediador': str, 'modalidade_frete': int, 'frete': Union[str, Union[int, float]], 'desconto': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]], 'despesas_acessorias': Union[str, Union[int, float]], 'despesas_aduaneiras': Union[str, Union[int, float]], 'informacoes_fisco': str, 'informacoes_complementares': str, 'observacoes_contribuinte': list['NfeContributorObservation'], 'pedido_compra': str, 'contrato': str, 'nota_empenho': str}, total=False)

G022 = TypedDict('G022', {'pagamento': Union[int, list[int]], 'forma_pagamento': Union[Literal['01', '02', '03', '04', '05', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '90', '91', '99'], list[Literal['01', '02', '03', '04', '05', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '90', '91', '99']]], 'desc_pagamento': Union[str, list[str]], 'data_pagamento': Union[str, list[str]], 'cnpj_transacional_pag': Union[str, list[str]], 'uf_estabelecimento_pag': Union[str, list[str]], 'tipo_integracao': Union[int, list[int]], 'valor_pagamento': Union[Union[str, Union[int, float]], list[Union[str, Union[int, float]]]], 'cnpj_credenciadora': Union[str, list[str]], 'bandeira': Union[str, list[str]], 'autorizacao': Union[str, list[str]], 'cnpj_beneficiario': Union[str, list[str]], 'id_terminal_pag': Union[str, list[str]]}, total=False)

G023 = TypedDict('G023', {'volume': str, 'especie': str, 'peso_bruto': Union[str, Union[int, float]], 'peso_liquido': Union[str, Union[int, float]], 'marca': str, 'numeracao': str, 'lacres': str, 'reboque': list['G025'], 'entrega': 'G026', 'retirada': 'G027'}, total=False)

G024 = TypedDict('G024', {'cnpj': str, 'razao_social': str, 'ie': str, 'cpf': str, 'nome_completo': str, 'endereco': str, 'uf': str, 'cidade': str, 'cep': str, 'placa': str, 'uf_veiculo': str, 'rntc': str, 'seguro': Union[str, Union[int, float]]}, total=False)

G025 = TypedDict('G025', {'placa': str, 'uf_veiculo': str, 'rntc': str, 'vagao': int, 'balsa': str}, total=False)

G026Variant0 = TypedDict('G026Variant0', {'cnpj': Required[str], 'razao_social': str, 'ie': str, 'cpf': str, 'nome_completo': str, 'nome_estrangeiro': str, 'cod_pais': str, 'pais': str, 'uf': Required[str], 'cep': Required[str], 'endereco': Required[str], 'numero': Required[str], 'complemento': str, 'bairro': Required[str], 'cidade': Required[str], 'telefone': str, 'email': str}, total=False)

G026Variant1 = TypedDict('G026Variant1', {'cnpj': str, 'razao_social': str, 'ie': str, 'cpf': Required[str], 'nome_completo': str, 'nome_estrangeiro': str, 'cod_pais': str, 'pais': str, 'uf': Required[str], 'cep': Required[str], 'endereco': Required[str], 'numero': Required[str], 'complemento': str, 'bairro': Required[str], 'cidade': Required[str], 'telefone': str, 'email': str}, total=False)

G026Variant2 = TypedDict('G026Variant2', {'cnpj': str, 'razao_social': str, 'ie': str, 'cpf': str, 'nome_completo': str, 'nome_estrangeiro': Required[str], 'cod_pais': str, 'pais': str, 'uf': str, 'cep': str, 'endereco': Required[str], 'numero': Required[str], 'complemento': str, 'bairro': Required[str], 'cidade': Required[str], 'telefone': str, 'email': str}, total=False)

G026: TypeAlias = Union['G026Variant0', 'G026Variant1', 'G026Variant2']

G027Variant0 = TypedDict('G027Variant0', {'cnpj': Required[str], 'razao_social': str, 'ie': str, 'cpf': str, 'nome_completo': str, 'nome_estrangeiro': str, 'cod_pais': str, 'pais': str, 'uf': Required[str], 'cep': Required[str], 'endereco': Required[str], 'numero': Required[str], 'complemento': str, 'bairro': Required[str], 'cidade': Required[str], 'telefone': str, 'email': str}, total=False)

G027Variant1 = TypedDict('G027Variant1', {'cnpj': str, 'razao_social': str, 'ie': str, 'cpf': Required[str], 'nome_completo': str, 'nome_estrangeiro': str, 'cod_pais': str, 'pais': str, 'uf': Required[str], 'cep': Required[str], 'endereco': Required[str], 'numero': Required[str], 'complemento': str, 'bairro': Required[str], 'cidade': Required[str], 'telefone': str, 'email': str}, total=False)

G027Variant2 = TypedDict('G027Variant2', {'cnpj': str, 'razao_social': str, 'ie': str, 'cpf': str, 'nome_completo': str, 'nome_estrangeiro': Required[str], 'cod_pais': str, 'pais': str, 'uf': str, 'cep': str, 'endereco': Required[str], 'numero': Required[str], 'complemento': str, 'bairro': Required[str], 'cidade': Required[str], 'telefone': str, 'email': str}, total=False)

G027: TypeAlias = Union['G027Variant0', 'G027Variant1', 'G027Variant2']

G028 = TypedDict('G028', {'numero': Required[str], 'valor': Required[Union[str, Union[int, float]]], 'desconto': Required[Union[str, Union[int, float]]], 'valor_liquido': Required[Union[str, Union[int, float]]]}, total=False)

G029 = TypedDict('G029', {'vencimento': Required[str], 'valor': Required[Union[str, Union[int, float]]]}, total=False)

G030 = TypedDict('G030', {'uf_embarque': Required[str], 'local_embarque': Required[str], 'local_despacho': str}, total=False)

G031Variant0 = TypedDict('G031Variant0', {'defensivos': Required[list['G032']], 'guia_transito': 'G033'}, total=False)

G031Variant1 = TypedDict('G031Variant1', {'defensivos': list['G032'], 'guia_transito': Required['G033']}, total=False)

G031: TypeAlias = Union['G031Variant0', 'G031Variant1']

G032 = TypedDict('G032', {'numero_receituario': Required[str], 'cpf_responsavel_tecnico': Required[str]}, total=False)

G033 = TypedDict('G033', {'tipo': Required[int], 'uf': Required[str], 'serie': str, 'numero': Required[str]}, total=False)

G034 = TypedDict('G034', {'tipo_ente_governamental': Required[str], 'percentual_redutor': Required[Union[str, Union[int, float]]], 'tipo_operacao_governamental': Required[str], 'dfes_anteriores': list['AccessKey']}, total=False)

G035 = TypedDict('G035', {'referencia': str, 'descricao': str, 'icms': list['G037'], 'ipi': list['G045'], 'pis': list['G046'], 'cofins': list['G047'], 'issqn': list['G048'], 'ibs_cbs': list['G049'], 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

G037 = TypedDict('G037', {'tipo_tributacao': Required[str], 'cenario': Required[str], 'tipo_pessoa': Required[str], 'nao_contribuinte': bool, 'codigo_cfop': Required[str], 'situacao_tributaria': Required[str], 'aliquota_importacao': Union[str, Union[int, float]], 'aliquota_credito': Union[str, Union[int, float]], 'aliquota_reducao_destino': Union[str, Union[int, float]], 'aliquota_mva': list['G038'], 'aliquota_icms': list['G039'], 'aliquota_icms_st': list['G040'], 'aliquota_fcp': list['G041'], 'aliquota_fcp_st': list['G042'], 'aliquota_diferimento': Union[str, Union[int, float]], 'aliquota_diferimento_fcp': Union[str, Union[int, float]], 'aliquota_reducao': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]], 'aliquota_efetiva_icms': Union[str, Union[int, float]], 'aliquota_efetiva_icms_st': Union[str, Union[int, float]], 'codigo_beneficio_reducao_bc': str, 'motivo_desoneracao': str, 'deducao_desoneracao': str, 'motivo_desoneracao_st': str, 'beneficio_fiscal': list['G043'], 'credito_presumido': list['G044']}, total=False)

G038 = TypedDict('G038', {'estado': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G039 = TypedDict('G039', {'estado': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G040 = TypedDict('G040', {'estado': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G041 = TypedDict('G041', {'estado': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G042 = TypedDict('G042', {'estado': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G043 = TypedDict('G043', {'estado': Required[str], 'codigo': Required[str]}, total=False)

G044 = TypedDict('G044', {'estado': Required[str], 'codigo_beneficio_fiscal': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G045 = TypedDict('G045', {'cenario': Required[str], 'tipo_pessoa': Required[str], 'situacao_tributaria': Required[str], 'codigo_enquadramento': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G046 = TypedDict('G046', {'cenario': Required[str], 'tipo_pessoa': Required[str], 'situacao_tributaria': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G047 = TypedDict('G047', {'cenario': Required[str], 'tipo_pessoa': Required[str], 'situacao_tributaria': Required[str], 'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

G048 = TypedDict('G048', {'cenario': Required[str], 'tipo_pessoa': Required[str], 'codigo_cfop': Required[str], 'exigibilidade': Required[str], 'item_servico': Required[str], 'incentivo_fiscal': Required[str], 'aliquota': Required[Union[str, Union[int, float]]], 'municipio': str, 'codigo_servico': str}, total=False)

G049 = TypedDict('G049', {'cenario': Required[str], 'tipo_pessoa': Required[str], 'situacao_tributaria': Required[str], 'classificacao_tributaria': Required[str], 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'G050', 'ibs_municipal': 'G050', 'cbs': 'G050', 'credito_presumido': 'G051'}, total=False)

G050 = TypedDict('G050', {'aliquota_diferimento': Union[str, Union[int, float]]}, total=False)

G051 = TypedDict('G051', {'classificacao': Required[str], 'aliquota_ibs': Union[str, Union[int, float]], 'aliquota_cbs': Union[str, Union[int, float]]}, total=False)

G052 = TypedDict('G052', {'referencia': str, 'descricao': Required[str], 'tipo': Required[str], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int}, total=False)

G053 = TypedDict('G053', {'situacao_tributaria': Required[str], 'classificacao_tributaria': Required[str], 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'G054', 'ibs_municipal': 'G054', 'cbs': 'G054', 'credito_presumido': str}, total=False)

G054 = TypedDict('G054', {'aliquota_diferimento': Required[Union[str, Union[int, float]]]}, total=False)

G055 = TypedDict('G055', {'codigo_servico': Required[str], 'natureza_operacao': Required[str], 'exigibilidade_iss': Required[str], 'iss_retido': Required[str], 'responsavel_retencao': str, 'codigo_cnae': str, 'codigo_tributacao_municipio': str}, total=False)

G056 = TypedDict('G056', {'codigo_cnae': Required[str], 'codigo_servico': str, 'local_prestacao': Required[str], 'cep_local_prestacao': str, 'iss_retido': Required[str]}, total=False)

G057 = TypedDict('G057', {'codigo_servico': Required[str], 'tipo_tributacao': Required[str], 'iss_retido': Required[str], 'responsavel_retencao': str, 'codigo_cnae': str}, total=False)

G058 = TypedDict('G058', {'cfps': Required[list['G059']], 'id_cnae': Required[str], 'situacao_tributaria': Required[str], 'iss_retido': Required[str]}, total=False)

G059 = TypedDict('G059', {'cenario': Required[str], 'codigo_cfps': Required[str]}, total=False)

G060 = TypedDict('G060', {'codigo_servico': Required[str], 'regime_recolhimento': Required[str], 'forma_recolhimento': Required[str]}, total=False)

G061 = TypedDict('G061', {'codigo_servico': Required[str], 'iss_retido': Required[str], 'responsavel_retencao': str, 'codigo_cnae': str, 'codigo_tributacao_municipio': str, 'tributacao': Required[list['G062']]}, total=False)

G062 = TypedDict('G062', {'cenario': Required[int], 'exigibilidade_iss': Required[str], 'deducoes': Union[str, Union[int, float]], 'iss': Union[str, Union[int, float]], 'pis': Union[str, Union[int, float]], 'cofins': Union[str, Union[int, float]], 'inss': Union[str, Union[int, float]], 'ir': Union[str, Union[int, float]], 'csll': Union[str, Union[int, float]]}, total=False)

G063 = TypedDict('G063', {'codigo_servico': Required[str], 'iss_retido': Required[str], 'responsavel_retencao': str}, total=False)

G064 = TypedDict('G064', {'tipo_emissao': Required[str], 'codigo_servico': Required[str], 'codigo_tributacao_municipio': str, 'tributacao_iss': Required[int], 'tipo_imunidade': int, 'retencao_iss': Required[str], 'cst_pis_cofins': str, 'retencao_pis_cofins': int, 'ibs_cbs': 'G065'}, total=False)

G065 = TypedDict('G065', {'situacao_tributaria': Required[str], 'classificacao_tributaria': Required[str], 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'G054', 'ibs_municipal': 'G054', 'cbs': 'G054', 'credito_presumido': str}, total=False)

G066 = TypedDict('G066', {'codigo_servico': Required[str], 'tributacao': Required[int], 'iss_retido': Required[str], 'responsavel_retencao': str}, total=False)

G067 = TypedDict('G067', {'referencia': Union[str, list[str]]}, total=False)

G068 = TypedDict('G068', {'cnpj': str, 'contato': str, 'email': str, 'telefone': str, 'id_csrt': str, 'csrt': str}, total=False)

G069 = TypedDict('G069', {'icms': 'NfeIcms', 'ipi': 'G092', 'pis': 'G093', 'cofins': 'G094', 'issqn': 'G095', 'retencao_tributos': 'G096', 'importacao': 'G097', 'ibs_cbs': 'G100'}, total=False)

G070 = TypedDict('G070', {'aliquota': Union[str, Union[int, float]], 'aliquota_fcp': Union[str, Union[int, float]], 'aliquota_interestadual': Union[str, Union[int, float]], 'codigo_cfop': str, 'situacao_tributaria': str, 'aliquota_importacao': Union[str, Union[int, float]], 'industria': str, 'majoracao': Union[str, Union[int, float]], 'bc_icms': Union[str, Union[int, float]], 'bc_icms_st': Union[str, Union[int, float]], 'valor_icms': Union[str, Union[int, float]], 'aliquota_diferimento': Union[str, Union[int, float]], 'credito_presumido': list['G091']}, total=False)

G071 = TypedDict('G071', {'aliquota_credito': Union[str, Union[int, float]]}, total=False)

G072 = TypedDict('G072', {'aliquota_st': Union[str, Union[int, float]], 'aliquota_fcp_st': Union[str, Union[int, float]], 'aliquota_mva': Union[str, Union[int, float]], 'aliquota_credito': Union[str, Union[int, float]], 'aliquota_reducao': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]]}, total=False)

G073 = TypedDict('G073', {'aliquota_st': Union[str, Union[int, float]], 'aliquota_fcp_st': Union[str, Union[int, float]], 'aliquota_mva': Union[str, Union[int, float]], 'aliquota_reducao': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]]}, total=False)

G074 = TypedDict('G074', {'bc_st_retido': Union[str, Union[int, float]], 'aliquota_st_retido': Union[str, Union[int, float]], 'valor_st_retido': Union[str, Union[int, float]], 'valor_icms_substituto': Union[str, Union[int, float]], 'valor_fcp_retido': Union[str, Union[int, float]], 'aliquota_fcp_retido': Union[str, Union[int, float]], 'aliquota_bc_efetivo': Union[str, Union[int, float]], 'aliquota_icms_efetivo': Union[str, Union[int, float]]}, total=False)

G075 = TypedDict('G075', {'aliquota': Union[str, Union[int, float]], 'aliquota_fcp': Union[str, Union[int, float]], 'aliquota_interestadual': Union[str, Union[int, float]], 'codigo_cfop': str, 'situacao_tributaria': str, 'aliquota_importacao': Union[str, Union[int, float]], 'industria': str, 'majoracao': Union[str, Union[int, float]], 'difal_antecipacao': bool, 'codigo_beneficio_reducao_bc': str, 'bc_icms': Union[str, Union[int, float]], 'valor_icms': Union[str, Union[int, float]], 'bc_icms_st': Union[str, Union[int, float]], 'credito_presumido': list['G091']}, total=False)

G076 = TypedDict('G076', {'pauta_fiscal': Union[str, Union[int, float]]}, total=False)

G077 = TypedDict('G077', {'quantidade_bc': Union[str, Union[int, float]]}, total=False)

G078 = TypedDict('G078', {'aliquota_st': Union[str, Union[int, float]], 'aliquota_fcp_st': Union[str, Union[int, float]], 'aliquota_mva': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]], 'motivo_desoneracao_st': str}, total=False)

G079 = TypedDict('G079', {'quantidade_retencao': Union[str, Union[int, float]], 'aliquota_retencao': Union[str, Union[int, float]], 'percentual_reducao': Union[str, Union[int, float]], 'motivo_reducao': str, 'quantidade_bc': Union[str, Union[int, float]]}, total=False)

G080 = TypedDict('G080', {'aliquota_reducao': Union[str, Union[int, float]], 'motivo_desoneracao': str, 'deducao_desoneracao': str}, total=False)

G081 = TypedDict('G081', {'motivo_desoneracao': str, 'deducao_desoneracao': str}, total=False)

G082 = TypedDict('G082', {'motivo_desoneracao': str, 'deducao_desoneracao': str}, total=False)

G083 = TypedDict('G083', {'aliquota_diferimento': Union[str, Union[int, float]], 'aliquota_diferimento_fcp': Union[str, Union[int, float]], 'codigo_beneficio_reducao_bc': str, 'motivo_desoneracao': str}, total=False)

G084 = TypedDict('G084', {'aliquota_diferimento': Union[str, Union[int, float]], 'quantidade_bc': Union[str, Union[int, float]]}, total=False)

G085 = TypedDict('G085', {'bc_st_retido': Union[str, Union[int, float]], 'aliquota_st_retido': Union[str, Union[int, float]], 'valor_st_retido': Union[str, Union[int, float]], 'bc_st_dest': Union[str, Union[int, float]], 'valor_st_dest': Union[str, Union[int, float]], 'valor_fcp_retido': Union[str, Union[int, float]], 'aliquota_fcp_retido': Union[str, Union[int, float]], 'aliquota_bc_efetivo': Union[str, Union[int, float]], 'aliquota_icms_efetivo': Union[str, Union[int, float]]}, total=False)

G086 = TypedDict('G086', {'quantidade_bc': Union[str, Union[int, float]]}, total=False)

G087 = TypedDict('G087', {'aliquota_st': Union[str, Union[int, float]], 'aliquota_fcp_st': Union[str, Union[int, float]], 'aliquota_mva': Union[str, Union[int, float]], 'aliquota_reducao': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]], 'motivo_desoneracao': str, 'motivo_desoneracao_st': str, 'deducao_desoneracao': str}, total=False)

G088 = TypedDict('G088', {'aliquota_mva': Union[str, Union[int, float]]}, total=False)

G089 = TypedDict('G089', {'pauta_fiscal': Union[str, Union[int, float]]}, total=False)

G090 = TypedDict('G090', {'valor_operacao': Union[str, Union[int, float]]}, total=False)

G091 = TypedDict('G091', {'codigo_beneficio_fiscal': str, 'aliquota': Union[str, Union[int, float]], 'valor': Union[str, Union[int, float]]}, total=False)

G092 = TypedDict('G092', {'situacao_tributaria': Required[str], 'codigo_enquadramento': Required[Union[int, str]], 'aliquota': Required[Union[str, Union[int, float]]], 'percentual_devolvido': Union[str, Union[int, float]], 'ipi_devolvido': Union[str, Union[int, float]], 'codigo_selo': str, 'qtd_selo': str, 'bc_ipi': Union[str, Union[int, float]]}, total=False)

G093 = TypedDict('G093', {'situacao_tributaria': Required[str], 'aliquota': Required[Union[str, Union[int, float]]], 'majoracao': Union[str, Union[int, float]], 'bc_pis': Union[str, Union[int, float]]}, total=False)

G094 = TypedDict('G094', {'situacao_tributaria': Required[str], 'aliquota': Required[Union[str, Union[int, float]]], 'majoracao': Union[str, Union[int, float]], 'bc_cofins': Union[str, Union[int, float]]}, total=False)

G095 = TypedDict('G095', {'codigo_cfop': Required[str], 'exigibilidade': Required[int], 'item_servico': Required[str], 'incentivo_fiscal': Required[str], 'aliquota': Required[Union[str, Union[int, float]]], 'deducao': Union[str, Union[int, float]], 'retencoes': Union[str, Union[int, float]], 'desconto_incondicionado': Union[str, Union[int, float]], 'desconto_condicionado': Union[str, Union[int, float]], 'iss_retido': Union[str, Union[int, float]], 'municipio': str, 'codigo_servico': str, 'processo': str, 'cnae': str}, total=False)

G096 = TypedDict('G096', {'valor_pis': Union[str, Union[int, float]], 'valor_cofins': Union[str, Union[int, float]], 'valor_csll': Union[str, Union[int, float]], 'bc_irrf': Union[str, Union[int, float]], 'valor_irrf': Union[str, Union[int, float]], 'bc_previdencia': Union[str, Union[int, float]], 'valor_previdencia': Union[str, Union[int, float]]}, total=False)

G097 = TypedDict('G097', {'aliquota': Required[Union[str, Union[int, float]]], 'iof': Union[str, Union[int, float]]}, total=False)

G100 = TypedDict('G100', {'situacao_tributaria': Required[str], 'classificacao_tributaria': Required[str], 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'G101', 'ibs_municipal': 'G102', 'cbs': 'G103', 'tributacao_monofasica': 'G105', 'credito_presumido': 'G106', 'transferencia_credito': 'G108', 'ajuste_competencia': 'G109', 'estorno_credito': 'G110', 'base_calculo': Union[str, Union[int, float]]}, total=False)

G101 = TypedDict('G101', {'aliquota_diferimento': Union[str, Union[int, float]], 'valor_devolvido': Union[str, Union[int, float]]}, total=False)

G102 = TypedDict('G102', {'aliquota_diferimento': Union[str, Union[int, float]], 'valor_devolvido': Union[str, Union[int, float]]}, total=False)

G103 = TypedDict('G103', {'aliquota_diferimento': Union[str, Union[int, float]], 'percentual_devolvido': Union[str, Union[int, float]], 'valor_devolvido': Union[str, Union[int, float]], 'alc_zfm_cbs': 'G104'}, total=False)

G104 = TypedDict('G104', {'tipo_aplicacao': Required[str], 'numero_processo_suframa': str, 'aliquota_efetiva_referencia': Required[Union[str, Union[int, float]]], 'valor_efetivo_referencia': Required[Union[str, Union[int, float]]]}, total=False)

G105 = TypedDict('G105', {'quantidade_bc': Union[str, Union[int, float]], 'aliquota_ibs': Union[str, Union[int, float]], 'aliquota_cbs': Union[str, Union[int, float]], 'quantidade_bc_retencao': Union[str, Union[int, float]], 'aliquota_ibs_retencao': Union[str, Union[int, float]], 'aliquota_cbs_retencao': Union[str, Union[int, float]], 'quantidade_bc_retido': Union[str, Union[int, float]], 'aliquota_ibs_retido': Union[str, Union[int, float]], 'aliquota_cbs_retido': Union[str, Union[int, float]], 'aliquota_diferimento_ibs': Union[str, Union[int, float]], 'aliquota_diferimento_cbs': Union[str, Union[int, float]]}, total=False)

G106 = TypedDict('G106', {'classificacao': Required[str], 'bc': Required[Union[str, Union[int, float]]], 'aliquota_ibs': Union[str, Union[int, float]], 'aliquota_cbs': Union[str, Union[int, float]]}, total=False)

G108 = TypedDict('G108', {'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]]}, total=False)

G109 = TypedDict('G109', {'competencia_apuracao': Required[str], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]]}, total=False)

G110 = TypedDict('G110', {'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]]}, total=False)

G111 = TypedDict('G111', {'chave': str, 'uuid': str, 'natureza_operacao': str, 'ambiente': int, 'classe_imposto': str, 'codigo_cfop': str, 'produtos': list[int], 'quantidade': list[Union[str, Union[int, float]]], 'volume': str, 'informacoes_fisco': str, 'informacoes_complementares': str, 'url_notificacao': str}, total=False)

G112 = TypedDict('G112', {'operacao': int, 'natureza_operacao': str, 'codigo_cfop': str, 'valor_icms': Union[str, Union[int, float]], 'valor_icms_st': Union[str, Union[int, float]], 'ambiente': int, 'cliente': 'NfeCustomer', 'situacao_tributaria': str, 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

G113 = TypedDict('G113', {'chave': str, 'uuid': str, 'operacao': int, 'natureza_operacao': str, 'ambiente': int, 'cliente': 'NfeCustomer', 'produtos': list['NfeComplementProduct'], 'impostos': 'NfeComplementTaxes', 'agropecuario': 'G031', 'documento_adicao': 'G119', 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

G114ImpostosIbsCbs = TypedDict('G114ImpostosIbsCbs', {}, total=False)

G114Impostos = TypedDict('G114Impostos', {'ibs_cbs': 'G114ImpostosIbsCbs'}, total=False)

G114 = TypedDict('G114', {'quantidade': Union[str, Union[int, float]], 'subtotal': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]], 'codigo_cfop': str, 'situacao_tributaria': str, 'impostos': 'G114Impostos', 'beneficio_fiscal': str, 'gtin': str, 'gtin_tributavel': str, 'cod_barras': str, 'cod_barras_tributavel': str, 'unidade_tributavel': str, 'subtotal_tributavel': Union[str, Union[int, float]], 'quantidade_tributavel': Union[str, Union[int, float]]}, total=False)

G115 = TypedDict('G115', {'codigo_cfop': Required[str], 'situacao_tributaria': Required[str], 'bc_icms': Required[Union[str, Union[int, float]]], 'valor_icms': Required[Union[str, Union[int, float]]], 'valor_operacao': Union[str, Union[int, float]], 'valor_fcp': Union[str, Union[int, float]], 'aliquota_diferimento': Union[str, Union[int, float]], 'beneficio_fiscal': str}, total=False)

G116 = TypedDict('G116', {'codigo_cfop': Required[str], 'situacao_tributaria': Required[str], 'bc_icms_st': Required[Union[str, Union[int, float]]], 'valor_icms_st': Required[Union[str, Union[int, float]]], 'valor_fcp_st': Union[str, Union[int, float]], 'aliquota_mva': Required[Union[str, Union[int, float]]], 'beneficio_fiscal': str}, total=False)

G117 = TypedDict('G117', {'codigo_cfop': Required[str], 'bc_ipi': Required[Union[str, Union[int, float]]], 'valor_ipi': Required[Union[str, Union[int, float]]]}, total=False)

G118 = TypedDict('G118', {'codigo_cfop': Required[str], 'exigibilidade': Required[int], 'item_servico': Required[str], 'incentivo_fiscal': Required[str], 'bc_issqn': Required[Union[str, Union[int, float]]], 'valor_issqn': Required[Union[str, Union[int, float]]]}, total=False)

G119 = TypedDict('G119', {'ndoc_importacao': Required[str], 'ddoc_importacao': Required[str], 'uf_desembaraco': Required[str], 'local_desembaraco': Required[str], 'data_desembaraco': Required[str], 'via_transporte': Required[str], 'intermediacao': Required[str], 'fabricante': Required[str], 'adicao': Required[str], 'seq_adicao': Required[str], 'afrmm': str}, total=False)

G120 = TypedDict('G120', {'finalidade': int, 'tipo_credito': int, 'nfe_referenciada': Union[str, list[str]]}, total=False)

G121 = TypedDict('G121', {'finalidade': int, 'tipo_debito': int}, total=False)

G122DfeReferenciado = TypedDict('G122DfeReferenciado', {'chave': str, 'item': int}, total=False)

G122 = TypedDict('G122', {'dfe_referenciado': 'G122DfeReferenciado'}, total=False)

G123 = TypedDict('G123', {'chave': str, 'uuid': str, 'correcao': str, 'ambiente': int, 'evento': int, 'url_notificacao': str}, total=False)

G124 = TypedDict('G124', {'chave': str, 'ambiente': int, 'evento': str, 'justificativa': str}, total=False)

G125 = TypedDict('G125', {'chave': str, 'ambiente': int, 'cod_evento': str, 'evento': int, 'url_notificacao': str}, total=False)

G127ControleEstoque = TypedDict('G127ControleEstoque', {'quantidade': Union[str, Union[int, float]], 'unidade': str}, total=False)

G127 = TypedDict('G127', {'item': int, 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]], 'controle_estoque': 'G127ControleEstoque'}, total=False)

G128ControleEstoque = TypedDict('G128ControleEstoque', {'quantidade_perecimento': Union[str, Union[int, float]], 'unidade_perecimento': str, 'valor_ibs_estorno': Union[str, Union[int, float]], 'valor_cbs_estorno': Union[str, Union[int, float]]}, total=False)

G128 = TypedDict('G128', {'item': int, 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]], 'controle_estoque': 'G128ControleEstoque'}, total=False)

G129ControleEstoque = TypedDict('G129ControleEstoque', {'quantidade_nao_fornecida': Union[str, Union[int, float]], 'unidade_nao_fornecida': str}, total=False)

G129 = TypedDict('G129', {'item': int, 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]], 'controle_estoque': 'G129ControleEstoque'}, total=False)

G130 = TypedDict('G130', {'data_previsao_entrega': str}, total=False)

G131CreditoPresumido = TypedDict('G131CreditoPresumido', {'classificacao': str, 'aliquota_ibs': Union[str, Union[int, float]], 'aliquota_cbs': Union[str, Union[int, float]], 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]]}, total=False)

G131 = TypedDict('G131', {'item': int, 'base_calculo': Union[str, Union[int, float]], 'credito_presumido': 'G131CreditoPresumido'}, total=False)

G132ControleEstoque = TypedDict('G132ControleEstoque', {'quantidade_perecimento': Union[str, Union[int, float]], 'unidade_perecimento': str}, total=False)

G132 = TypedDict('G132', {'item': int, 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]], 'controle_estoque': 'G132ControleEstoque'}, total=False)

G133 = TypedDict('G133', {'indicador_aceitacao': int}, total=False)

G134ControleEstoque = TypedDict('G134ControleEstoque', {'quantidade_imobilizada': Union[str, Union[int, float]], 'unidade_imobilizada': str}, total=False)

G134 = TypedDict('G134', {'item': int, 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]], 'controle_estoque': 'G134ControleEstoque'}, total=False)

G135ControleEstoque = TypedDict('G135ControleEstoque', {'quantidade_combustivel': Union[str, Union[int, float]], 'unidade_combustivel': str}, total=False)

G135 = TypedDict('G135', {'item': int, 'valor_ibs': Union[str, Union[int, float]], 'valor_cbs': Union[str, Union[int, float]], 'controle_estoque': 'G135ControleEstoque'}, total=False)

G136 = TypedDict('G136', {'item': int, 'valor_credito_ibs': Union[str, Union[int, float]], 'valor_credito_cbs': Union[str, Union[int, float]]}, total=False)

G137 = TypedDict('G137', {'uuid': str, 'ambiente': int, 'url_notificacao': str}, total=False)

G138 = TypedDict('G138', {'chave': str, 'uuid': str, 'pagamento': 'NfePaymentEventItem', 'pagamentos': list['NfePaymentEventItem'], 'ambiente': int, 'evento': int, 'url_notificacao': str}, total=False)

G139 = TypedDict('G139', {'indicador_pagamento': int, 'forma_pagamento': str, 'desc_pagamento': str, 'valor_pagamento': Union[str, Union[int, float]], 'data_pagamento': str, 'cnpj_transacional_pag': str, 'uf_pagamento': str, 'cnpj_instituicao_financeira': str, 'bandeira': str, 'autorizacao': str, 'cnpj_beneficiario': str, 'uf_beneficiario': str}, total=False)

G140 = TypedDict('G140', {'uuid': str, 'url_notificacao': str}, total=False)

G141 = TypedDict('G141', {'chave': str, 'uuid': str, 'ID': str}, total=False)

G142 = TypedDict('G142', {'chave': str, 'uuid': str, 'motivo': str, 'nfce_referenciada': str}, total=False)

G143 = TypedDict('G143', {'sequencia': str, 'motivo': str, 'ambiente': int, 'serie': str, 'modelo': str}, total=False)

G144 = TypedDict('G144', {'data_inicio': str, 'data_final': str, 'numero_inicio': str, 'numero_final': str, 'modelo': str, 'relatorio': str, 'separar_pdf': int, 'status': str, 'ordem': str, 'url_notificacao': str}, total=False)

G145 = TypedDict('G145', {'tipo_tributacao': str, 'regime_tributario': str, 'cnpj': str, 'razao_social': str, 'cpf': str, 'nome_completo': str, 'nome_fantasia': str, 'ie': str, 'im': str, 'unidade_empresa': str, 'email': str, 'telefone': str, 'conta_bancaria_banco': str, 'conta_bancaria_agencia': str, 'conta_bancaria_numero': str, 'conta_bancaria_digito': str, 'contabilidade': str, 'url_notificacao': str, 'logomarca': str}, total=False)

G146 = TypedDict('G146', {'cep': str, 'endereco': str, 'numero': str, 'complemento': str, 'bairro': str, 'cidade': str, 'uf': str}, total=False)

G147 = TypedDict('G147', {'nfe_serie': int, 'nfe_numero': int, 'nfe_numero_dev': int, 'informacoes_fisco': str, 'cnae_issqn': str}, total=False)

G148 = TypedDict('G148', {'nfce_serie': int, 'nfce_numero': int, 'nfce_id_csc': str, 'nfce_codigo_csc': str, 'nfce_numero_dev': int, 'nfce_id_csc_dev': str, 'nfce_codigo_csc_dev': str, 'informacoes_fisco': str}, total=False)

G149 = TypedDict('G149', {'cte_serie': int, 'cte_number': int, 'cte_number_dev': int, 'cte_os_serie': int, 'cte_os_number': int, 'cte_os_number_dev': int, 'taf_cte_os': str, 'registro_estadual_cte_os': str}, total=False)

G150 = TypedDict('G150', {'dce_serie': int, 'dce_numero': int, 'dce_numero_dev': int, 'tipo_emissor_dce': int, 'numero_site_autorizador': int, 'site_marketplace': str}, total=False)

G151 = TypedDict('G151', {'nfse_rps_serie': str, 'nfse_rps_numero': int, 'cnae': Union[str, list[str]], 'nfse_login': str, 'nfse_password': str, 'nfse_token': str, 'regime_apuracao_sn': str, 'regime_especial_nacional': str, 'regime_especial_municipal': str, 'nfse_lote_rps_numero': int, 'nfse_rps_numero_dev': int}, total=False)

G152 = TypedDict('G152', {'certificado': str, 'certificado_senha': str}, total=False)

G153 = TypedDict('G153', {'partilha_icms_contribuinte': bool, 'partilha_icms_isento': bool, 'orientacao_danfe': str, 'microcervejaria': bool, 'icms_ref_sp': bool, 'refeicoes_sp': bool, 'icms_ref_df': bool, 'exclusao_icms_pis_cofins': bool, 'exclusao_difal_pis_cofins': bool, 'deduzir_desconto_ipi': bool, 'base_calculo_ipi_sem_frete': bool, 'email_automatico_nfse': bool, 'ativar_epec': str, 'ocultar_total_etiqueta': str}, total=False)

NfeIcms = TypedDict('NfeIcms', {'aliquota': Union[str, Union[int, float]], 'aliquota_fcp': Union[str, Union[int, float]], 'aliquota_interestadual': Union[str, Union[int, float]], 'codigo_cfop': Required[str], 'situacao_tributaria': Required[str], 'aliquota_importacao': Union[str, Union[int, float]], 'industria': str, 'majoracao': Union[str, Union[int, float]], 'bc_icms': Union[str, Union[int, float]], 'bc_icms_st': Union[str, Union[int, float]], 'valor_icms': Union[str, Union[int, float]], 'aliquota_diferimento': Union[str, Union[int, float]], 'credito_presumido': list['G091'], 'aliquota_credito': Union[str, Union[int, float]], 'aliquota_st': Union[str, Union[int, float]], 'aliquota_fcp_st': Union[str, Union[int, float]], 'aliquota_mva': Union[str, Union[int, float]], 'aliquota_reducao': Union[str, Union[int, float]], 'aliquota_reducao_st': Union[str, Union[int, float]], 'bc_st_retido': Union[str, Union[int, float]], 'aliquota_st_retido': Union[str, Union[int, float]], 'valor_st_retido': Union[str, Union[int, float]], 'valor_icms_substituto': Union[str, Union[int, float]], 'valor_fcp_retido': Union[str, Union[int, float]], 'aliquota_fcp_retido': Union[str, Union[int, float]], 'aliquota_bc_efetivo': Union[str, Union[int, float]], 'aliquota_icms_efetivo': Union[str, Union[int, float]], 'difal_antecipacao': bool, 'codigo_beneficio_reducao_bc': str, 'pauta_fiscal': Union[str, Union[int, float]], 'quantidade_bc': Union[str, Union[int, float]], 'motivo_desoneracao_st': str, 'quantidade_retencao': Union[str, Union[int, float]], 'aliquota_retencao': Union[str, Union[int, float]], 'percentual_reducao': Union[str, Union[int, float]], 'motivo_reducao': str, 'motivo_desoneracao': str, 'deducao_desoneracao': str, 'aliquota_diferimento_fcp': Union[str, Union[int, float]], 'bc_st_dest': Union[str, Union[int, float]], 'valor_st_dest': Union[str, Union[int, float]], 'valor_operacao': Union[str, Union[int, float]], 'codigo_beneficio_fiscal': str, 'valor': Union[str, Union[int, float]]}, total=False)

NfeContributorObservation = TypedDict('NfeContributorObservation', {'campo': Required[str], 'texto': Required[str]}, total=False)

NfeOrder = TypedDict('NfeOrder', {'presenca': Required[int], 'intermediador': int, 'cnpj_intermediador': str, 'id_intermediador': str, 'modalidade_frete': Required[int], 'frete': Union[str, Union[int, float]], 'desconto': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]], 'despesas_acessorias': Union[str, Union[int, float]], 'despesas_aduaneiras': Union[str, Union[int, float]], 'informacoes_fisco': str, 'informacoes_complementares': str, 'observacoes_contribuinte': list['NfeContributorObservation'], 'pedido_compra': str, 'contrato': str, 'nota_empenho': str, 'pagamento': Required[Union[int, list[int]]], 'forma_pagamento': Required[Union[Literal['01', '02', '03', '04', '05', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '90', '91', '99'], list[Literal['01', '02', '03', '04', '05', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '90', '91', '99']]]], 'desc_pagamento': Union[str, list[str]], 'data_pagamento': Union[str, list[str]], 'cnpj_transacional_pag': Union[str, list[str]], 'uf_estabelecimento_pag': Union[str, list[str]], 'tipo_integracao': Union[int, list[int]], 'valor_pagamento': Union[Union[str, Union[int, float]], list[Union[str, Union[int, float]]]], 'cnpj_credenciadora': Union[str, list[str]], 'bandeira': Union[str, list[str]], 'autorizacao': Union[str, list[str]], 'cnpj_beneficiario': Union[str, list[str]], 'id_terminal_pag': Union[str, list[str]]}, total=False)

NfeTransport = TypedDict('NfeTransport', {'volume': str, 'especie': str, 'peso_bruto': Union[str, Union[int, float]], 'peso_liquido': Union[str, Union[int, float]], 'marca': str, 'numeracao': str, 'lacres': str, 'reboque': list['G025'], 'entrega': 'G026', 'retirada': 'G027', 'cnpj': str, 'razao_social': str, 'ie': str, 'cpf': str, 'nome_completo': str, 'endereco': str, 'uf': str, 'cidade': str, 'cep': str, 'placa': str, 'uf_veiculo': str, 'rntc': str, 'seguro': Union[str, Union[int, float]]}, total=False)

NfeCustomer = TypedDict('NfeCustomer', {'cpf': str, 'nome_completo': str, 'cnpj': str, 'razao_social': str, 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': str, 'complemento': str, 'numero': str, 'bairro': str, 'cidade': str, 'uf': str, 'cep': str, 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': str, 'cod_pais': str, 'nome_pais': str}, total=False)

NfeProduct = TypedDict('NfeProduct', {'ID': int, 'item': int, 'nome': Required[str], 'codigo': Required[str], 'ncm': Required[str], 'quantidade': Required[Union[str, Union[int, float]]], 'quantidade_tributavel': Union[str, Union[int, float]], 'unidade': Required[str], 'unidade_tributavel': str, 'peso': Union[str, Union[int, float]], 'origem': int, 'desconto': Union[str, Union[int, float]], 'subtotal': Required[Union[str, Union[int, float]]], 'subtotal_tributavel': Union[str, Union[int, float]], 'total': Required[Union[str, Union[int, float]]], 'ind_valor_total': int, 'classe_imposto': str, 'impostos': 'G069', 'dfe_referenciado': 'G015', 'cest': str, 'beneficio_fiscal': str, 'informacoes_adicionais': str, 'ind_escala': str, 'cnpj_fabricante': str, 'gtin': str, 'gtin_tributavel': str, 'cod_barras': str, 'cod_barras_tributavel': str, 'nve': str, 'nrecopi': str, 'ativo_permanente': bool, 'veiculo_usado': Union[str, Union[int, float]], 'ex_ipi': str, 'combustiveis': 'G016', 'medicamento': 'G018', 'armamentos': 'G019', 'veiculos_novos': 'G020', 'rastro': list['G014'], 'drawback': str, 'reg_exportacao': str, 'nfe_exportacao': str, 'qtd_exportacao': Union[str, Union[int, float]], 'ndoc_importacao': str, 'ddoc_importacao': str, 'local_desembaraco': str, 'uf_desembaraco': str, 'data_desembaraco': str, 'via_transporte': str, 'intermediacao': str, 'adicao': str, 'seq_adicao': str, 'fabricante': str, 'desc_di': Union[str, Union[int, float]], 'afrmm': Union[str, Union[int, float]], 'cnpj_terceiro': str, 'cpf_terceiro': str, 'uf_terceiro': str, 'cod_exportador': str, 'nfci': str}, total=False)

NfeIssueRequest = TypedDict('NfeIssueRequest', {'ID': str, 'operacao': Required[Literal[0, 1]], 'natureza_operacao': Required[str], 'modelo': Required[Union[Literal['1', '2', 'nfe', 'nfce'], Literal[1, 2]]], 'finalidade': Required[Literal[1, 3, 4, 5, 6]], 'ambiente': Required['Environment'], 'tipo_credito': Literal[1, 2, 3, 4, 5, 6], 'tipo_debito': Literal[1, 2, 3, 4, 5, 6, 7, 8], 'url_notificacao': str, 'cliente': 'NfeCustomer', 'produtos': Required[list['NfeProduct']], 'pedido': Required['NfeOrder'], 'transporte': 'NfeTransport', 'fatura': 'G028', 'parcelas': list['G029'], 'exportacao': 'G030', 'agropecuario': 'G031', 'compra_governamental': 'G034', 'inscricao_suframa': str, 'codigo_indicador_operacao': str, 'data_emissao': str, 'data_entrada_saida': str, 'data_previsao_entrega': str, 'data_servico': str, 'nfe_referenciada': Union[str, list[str]], 'cte_referenciada': Union['AccessKey', list['AccessKey']], 'ecf_referenciada': Union['G006', list['G006']], 'nf_rural_referenciada': Union['G007', list['G007']], 'calculo_impostos': bool, 'previa_danfe': bool, 'assincrono': bool, 'responsavel_tecnico': 'G068', 'duplicatas': list['G029']}, total=False)

Nfe55IssueRequestClienteVariant0 = TypedDict('Nfe55IssueRequestClienteVariant0', {'cpf': Required[str], 'nome_completo': Required[str], 'cnpj': str, 'razao_social': str, 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': Required[str], 'complemento': str, 'numero': Required[str], 'bairro': Required[str], 'cidade': Required[str], 'uf': Required[str], 'cep': Required[str], 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': str, 'cod_pais': str, 'nome_pais': str}, total=False)

Nfe55IssueRequestClienteVariant1 = TypedDict('Nfe55IssueRequestClienteVariant1', {'cpf': str, 'nome_completo': str, 'cnpj': Required[str], 'razao_social': Required[str], 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': Required[str], 'complemento': str, 'numero': Required[str], 'bairro': Required[str], 'cidade': Required[str], 'uf': Required[str], 'cep': Required[str], 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': str, 'cod_pais': str, 'nome_pais': str}, total=False)

Nfe55IssueRequestClienteVariant2 = TypedDict('Nfe55IssueRequestClienteVariant2', {'cpf': str, 'nome_completo': str, 'cnpj': str, 'razao_social': str, 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': Required[str], 'complemento': str, 'numero': str, 'bairro': Required[str], 'cidade': str, 'uf': str, 'cep': str, 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': Required[str], 'cod_pais': Required[str], 'nome_pais': Required[str]}, total=False)

Nfe55IssueRequest = TypedDict('Nfe55IssueRequest', {'ID': str, 'operacao': Required[Literal[0, 1]], 'natureza_operacao': Required[str], 'modelo': Required[Union[Literal['1', 1, 'nfe']]], 'finalidade': Required[Literal[1, 3, 4, 5, 6]], 'ambiente': Required['Environment'], 'tipo_credito': Literal[1, 2, 3, 4, 5, 6], 'tipo_debito': Literal[1, 2, 3, 4, 5, 6, 7, 8], 'url_notificacao': str, 'cliente': Required[Union['Nfe55IssueRequestClienteVariant0', 'Nfe55IssueRequestClienteVariant1', 'Nfe55IssueRequestClienteVariant2']], 'produtos': Required[list['NfeProduct']], 'pedido': Required['NfeOrder'], 'transporte': 'NfeTransport', 'fatura': 'G028', 'parcelas': list['G029'], 'exportacao': 'G030', 'agropecuario': 'G031', 'compra_governamental': 'G034', 'inscricao_suframa': str, 'codigo_indicador_operacao': str, 'data_emissao': str, 'data_entrada_saida': str, 'data_previsao_entrega': str, 'data_servico': str, 'nfe_referenciada': Union[str, list[str]], 'cte_referenciada': Union['AccessKey', list['AccessKey']], 'ecf_referenciada': Union['G006', list['G006']], 'nf_rural_referenciada': Union['G007', list['G007']], 'calculo_impostos': bool, 'previa_danfe': bool, 'assincrono': bool, 'responsavel_tecnico': 'G068', 'duplicatas': list['G029']}, total=False)

Nfce65IssueRequest = TypedDict('Nfce65IssueRequest', {'ID': str, 'operacao': Required[Literal[0, 1]], 'natureza_operacao': Required[str], 'modelo': Required[Union[Literal['2', 2, 'nfce']]], 'finalidade': Required[Literal[1, 3, 4, 5, 6]], 'ambiente': Required['Environment'], 'tipo_credito': Literal[1, 2, 3, 4, 5, 6], 'tipo_debito': Literal[1, 2, 3, 4, 5, 6, 7, 8], 'url_notificacao': str, 'cliente': 'NfeCustomer', 'produtos': Required[list['NfeProduct']], 'pedido': Required['NfeOrder'], 'transporte': 'NfeTransport', 'fatura': 'G028', 'parcelas': list['G029'], 'exportacao': 'G030', 'agropecuario': 'G031', 'compra_governamental': 'G034', 'inscricao_suframa': str, 'codigo_indicador_operacao': str, 'data_emissao': str, 'data_entrada_saida': str, 'data_previsao_entrega': str, 'data_servico': str, 'nfe_referenciada': Union[str, list[str]], 'cte_referenciada': Union['AccessKey', list['AccessKey']], 'ecf_referenciada': Union['G006', list['G006']], 'nf_rural_referenciada': Union['G007', list['G007']], 'calculo_impostos': bool, 'previa_danfe': bool, 'assincrono': bool, 'responsavel_tecnico': 'G068', 'duplicatas': list['G029']}, total=False)

NfeReturnRequestVariant0 = TypedDict('NfeReturnRequestVariant0', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'classe_imposto': Required[str], 'codigo_cfop': str, 'produtos': list[int], 'quantidade': list[Union[str, Union[int, float]]], 'volume': str, 'informacoes_fisco': str, 'informacoes_complementares': str, 'url_notificacao': str, 'ver_aplic': str}, total=False)

NfeReturnRequestVariant1 = TypedDict('NfeReturnRequestVariant1', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'classe_imposto': Required[str], 'codigo_cfop': str, 'produtos': list[int], 'quantidade': list[Union[str, Union[int, float]]], 'volume': str, 'informacoes_fisco': str, 'informacoes_complementares': str, 'url_notificacao': str, 'ver_aplic': str}, total=False)

NfeReturnRequestVariant2 = TypedDict('NfeReturnRequestVariant2', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'classe_imposto': str, 'codigo_cfop': Required[str], 'produtos': list[int], 'quantidade': list[Union[str, Union[int, float]]], 'volume': str, 'informacoes_fisco': str, 'informacoes_complementares': str, 'url_notificacao': str, 'ver_aplic': str}, total=False)

NfeReturnRequestVariant3 = TypedDict('NfeReturnRequestVariant3', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'classe_imposto': str, 'codigo_cfop': Required[str], 'produtos': list[int], 'quantidade': list[Union[str, Union[int, float]]], 'volume': str, 'informacoes_fisco': str, 'informacoes_complementares': str, 'url_notificacao': str, 'ver_aplic': str}, total=False)

NfeReturnRequest: TypeAlias = Union['NfeReturnRequestVariant0', 'NfeReturnRequestVariant1', 'NfeReturnRequestVariant2', 'NfeReturnRequestVariant3']

NfeAdjustmentRequest = TypedDict('NfeAdjustmentRequest', {'operacao': Required[int], 'natureza_operacao': Required[str], 'codigo_cfop': Required[str], 'valor_icms': Union[str, Union[int, float]], 'valor_icms_st': Union[str, Union[int, float]], 'ambiente': Required['Environment'], 'cliente': Required['NfeCustomer'], 'situacao_tributaria': str, 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

NfeComplementTaxes = TypedDict('NfeComplementTaxes', {'icms': 'G115', 'icms_st': 'G116', 'ipi': 'G117', 'issqn': 'G118', 'ibs_cbs': 'NfeComplementIbsCbs'}, total=False)

NfeComplementProduct = TypedDict('NfeComplementProduct', {'ID': int, 'item': int, 'nome': str, 'codigo': str, 'ncm': str, 'quantidade': Union[str, Union[int, float]], 'quantidade_tributavel': Union[str, Union[int, float]], 'unidade': str, 'unidade_tributavel': str, 'peso': Union[str, Union[int, float]], 'origem': int, 'desconto': Union[str, Union[int, float]], 'subtotal': Union[str, Union[int, float]], 'subtotal_tributavel': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]], 'ind_valor_total': int, 'classe_imposto': str, 'impostos': 'G069', 'dfe_referenciado': 'G015', 'cest': str, 'beneficio_fiscal': str, 'informacoes_adicionais': str, 'ind_escala': str, 'cnpj_fabricante': str, 'gtin': str, 'gtin_tributavel': str, 'cod_barras': str, 'cod_barras_tributavel': str, 'nve': str, 'nrecopi': str, 'ativo_permanente': bool, 'veiculo_usado': Union[str, Union[int, float]], 'ex_ipi': str, 'combustiveis': 'G016', 'medicamento': 'G018', 'armamentos': 'G019', 'veiculos_novos': 'G020', 'rastro': list['G014'], 'codigo_cfop': str, 'situacao_tributaria': str}, total=False)

NfeComplementRequestVariant0 = TypedDict('NfeComplementRequestVariant0', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'operacao': Required[int], 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'cliente': Required['NfeCustomer'], 'produtos': Required[list['NfeComplementProduct']], 'impostos': 'NfeComplementTaxes', 'agropecuario': 'G031', 'documento_adicao': 'G119', 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

NfeComplementRequestVariant1 = TypedDict('NfeComplementRequestVariant1', {'chave': Required['AccessKey'], 'uuid': 'Uuid', 'operacao': Required[int], 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'cliente': Required['NfeCustomer'], 'produtos': list['NfeComplementProduct'], 'impostos': Required['NfeComplementTaxes'], 'agropecuario': 'G031', 'documento_adicao': 'G119', 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

NfeComplementRequestVariant2 = TypedDict('NfeComplementRequestVariant2', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'operacao': Required[int], 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'cliente': Required['NfeCustomer'], 'produtos': Required[list['NfeComplementProduct']], 'impostos': 'NfeComplementTaxes', 'agropecuario': 'G031', 'documento_adicao': 'G119', 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

NfeComplementRequestVariant3 = TypedDict('NfeComplementRequestVariant3', {'chave': 'AccessKey', 'uuid': Required['Uuid'], 'operacao': Required[int], 'natureza_operacao': Required[str], 'ambiente': Required['Environment'], 'cliente': Required['NfeCustomer'], 'produtos': list['NfeComplementProduct'], 'impostos': Required['NfeComplementTaxes'], 'agropecuario': 'G031', 'documento_adicao': 'G119', 'informacoes_fisco': str, 'informacoes_complementares': str}, total=False)

NfeComplementRequest: TypeAlias = Union['NfeComplementRequestVariant0', 'NfeComplementRequestVariant1', 'NfeComplementRequestVariant2', 'NfeComplementRequestVariant3']

NfeProductTaxClass = TypedDict('NfeProductTaxClass', {'referencia': str, 'descricao': Required[str], 'icms': Required[list['G037']], 'ipi': Required[list['G045']], 'pis': Required[list['G046']], 'cofins': Required[list['G047']], 'issqn': list['G048'], 'ibs_cbs': list['G049'], 'informacoes_fisco': str, 'informacoes_complementares': str, 'tipo': Literal['nfe'], 'tributos_federais': Union[str, Union[int, float]], 'tributos_estaduais': Union[str, Union[int, float]]}, total=False)

NfseTaxClassProvider55 = TypedDict('NfseTaxClassProvider55', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_servico': str, 'natureza_operacao': str, 'exigibilidade_iss': str, 'iss_retido': str, 'responsavel_retencao': str, 'codigo_cnae': str, 'codigo_tributacao_municipio': str}, total=False)

NfseTaxClassProvider56 = TypedDict('NfseTaxClassProvider56', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_cnae': str, 'codigo_servico': str, 'local_prestacao': str, 'cep_local_prestacao': str, 'iss_retido': str}, total=False)

NfseTaxClassProvider57 = TypedDict('NfseTaxClassProvider57', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_servico': str, 'tipo_tributacao': str, 'iss_retido': str, 'responsavel_retencao': str, 'codigo_cnae': str}, total=False)

NfseTaxClassProvider58 = TypedDict('NfseTaxClassProvider58', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'cfps': list['G059'], 'id_cnae': str, 'situacao_tributaria': str, 'iss_retido': str}, total=False)

NfseTaxClassProvider60 = TypedDict('NfseTaxClassProvider60', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_servico': str, 'regime_recolhimento': str, 'forma_recolhimento': str}, total=False)

NfseTaxClassProvider61 = TypedDict('NfseTaxClassProvider61', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_servico': str, 'iss_retido': str, 'responsavel_retencao': str, 'codigo_cnae': str, 'codigo_tributacao_municipio': str, 'tributacao': list['G062']}, total=False)

NfseTaxClassProvider63 = TypedDict('NfseTaxClassProvider63', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_servico': str, 'iss_retido': str, 'responsavel_retencao': str}, total=False)

NfseTaxClassProvider64 = TypedDict('NfseTaxClassProvider64', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G065', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'tipo_emissao': str, 'codigo_servico': str, 'codigo_tributacao_municipio': str, 'tributacao_iss': int, 'tipo_imunidade': int, 'retencao_iss': str, 'cst_pis_cofins': str, 'retencao_pis_cofins': int}, total=False)

NfseTaxClassProvider66 = TypedDict('NfseTaxClassProvider66', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfse']], 'ibs_cbs': 'G053', 'iss': int, 'pis': int, 'cofins': int, 'inss': int, 'ir': int, 'csll': int, 'codigo_servico': str, 'tributacao': int, 'iss_retido': str, 'responsavel_retencao': str}, total=False)

NfseServiceTaxClass: TypeAlias = Union['NfseTaxClassProvider55', 'NfseTaxClassProvider56', 'NfseTaxClassProvider57', 'NfseTaxClassProvider58', 'NfseTaxClassProvider60', 'NfseTaxClassProvider61', 'NfseTaxClassProvider63', 'NfseTaxClassProvider64', 'NfseTaxClassProvider66']

FiscalTaxClassRequest: TypeAlias = Union['NfeProductTaxClass', 'NfseServiceTaxClass', 'NfcomCommunicationTaxClass', list[Union['NfeProductTaxClass', 'NfseServiceTaxClass', 'NfcomCommunicationTaxClass']]]

TaxClassCreatedResult = TypedDict('TaxClassCreatedResult', {'referencia': Required[str], 'descricao': str, 'data': str}, total=False)

NfcomClassIcms = TypedDict('NfcomClassIcms', {'situacao_tributaria': Required[Literal['00', '20', '40', '51', '60', '90']], 'origem': Union[Literal['0', '1', '2', '3', '4', '5', '6', '7', '8'], int], 'aliquota': Union[str, Union[int, float]], 'percentual_reducao': Union[str, Union[int, float]], 'aliquota_fcp': Union[str, Union[int, float]], 'codigo_cfop': str}, total=False)

NfcomClassPisCofins = TypedDict('NfcomClassPisCofins', {'situacao_tributaria': Required[Literal['01', '02', '06', '07', '08', '09', '49']], 'aliquota': Union[str, Union[int, float]]}, total=False)

NfcomClassContribution = TypedDict('NfcomClassContribution', {'aliquota': Required[Union[str, Union[int, float]]]}, total=False)

NfcomCommunicationTaxClass = TypedDict('NfcomCommunicationTaxClass', {'referencia': str, 'descricao': Required[str], 'tipo': Required[Literal['nfcom']], 'codigo_classificacao': Required[Literal['100101', '100201', '100301', '100401', '200101', '200201', '200301', '300101', '300102', '300103', '300104', '300105', '300106', '300107', '300108', '300109', '300201', '300301', '300401', '400101', '400201', '400301', '400401', '400501', '450101', '500101', '500102', '500201', '500301', '500401', '500501', '500601', '600101', '600201', '600301', '600401', '600501', '600601', '700101', '700201', '700301', '700401', '700501', '700601', '800101', '800201', '800301', '800401', '800501', '800601', '800701', '800801', '800901', '801001', '1000101', '1000201', '1000301', '1000401', '1000402', '1000501', '1000601', '1000701', '1100101', '1100201', '1100301', '1100401', '1100501', '1100601', '1100701', '1200101', '1300101', '5900101', '5900201', '5900301', '5900401', '5900501']], 'icms': Required['NfcomClassIcms'], 'pis': Required['NfcomClassPisCofins'], 'cofins': Required['NfcomClassPisCofins'], 'fust': 'NfcomClassContribution', 'funttel': 'NfcomClassContribution'}, total=False)

FiscalCompanyUpdateRequest = TypedDict('FiscalCompanyUpdateRequest', {'tipo_tributacao': str, 'regime_tributario': str, 'cnpj': str, 'razao_social': str, 'cpf': str, 'nome_completo': str, 'nome_fantasia': str, 'ie': str, 'im': str, 'unidade_empresa': str, 'email': str, 'telefone': str, 'conta_bancaria_banco': str, 'conta_bancaria_agencia': str, 'conta_bancaria_numero': str, 'conta_bancaria_digito': str, 'contabilidade': Union[str, list[str]], 'url_notificacao': str, 'logomarca': str, 'cep': str, 'endereco': str, 'numero': str, 'complemento': str, 'bairro': str, 'cidade': str, 'uf': str, 'nfe_serie': int, 'nfe_numero': int, 'nfe_numero_dev': int, 'informacoes_fisco': str, 'cnae_issqn': str, 'nfce_serie': int, 'nfce_numero': int, 'nfce_id_csc': str, 'nfce_codigo_csc': str, 'nfce_numero_dev': int, 'nfce_id_csc_dev': str, 'nfce_codigo_csc_dev': str, 'cte_serie': int, 'cte_number': int, 'cte_number_dev': int, 'cte_os_serie': int, 'cte_os_number': int, 'cte_os_number_dev': int, 'taf_cte_os': str, 'registro_estadual_cte_os': str, 'dce_serie': int, 'dce_numero': int, 'dce_numero_dev': int, 'tipo_emissor_dce': int, 'numero_site_autorizador': int, 'site_marketplace': str, 'nfse_rps_serie': str, 'nfse_rps_numero': int, 'cnae': Union[str, list[str], None], 'nfse_login': str, 'nfse_password': str, 'nfse_token': str, 'regime_apuracao_sn': str, 'regime_especial_nacional': str, 'regime_especial_municipal': str, 'nfse_lote_rps_numero': int, 'nfse_rps_numero_dev': int, 'certificado': str, 'certificado_senha': str, 'partilha_icms_contribuinte': bool, 'partilha_icms_isento': bool, 'orientacao_danfe': str, 'microcervejaria': bool, 'icms_ref_sp': bool, 'refeicoes_sp': bool, 'icms_ref_df': bool, 'exclusao_icms_pis_cofins': bool, 'exclusao_difal_pis_cofins': bool, 'deduzir_desconto_ipi': bool, 'base_calculo_ipi_sem_frete': bool, 'email_automatico_nfse': bool, 'ativar_epec': str, 'ocultar_total_etiqueta': str, 'validar_setup_completo': bool}, total=False)

FiscalCompanyUpdateResultWarningsItem = TypedDict('FiscalCompanyUpdateResultWarningsItem', {'code': str, 'message': str}, total=False)

FiscalCompanyUpdateResultCredenciais = TypedDict('FiscalCompanyUpdateResultCredenciais', {'consumer_key': str, 'consumer_secret': str, 'access_token': str, 'access_token_secret': str, 'bearer_access_token': str}, total=False)

FiscalCompanyUpdateResult = TypedDict('FiscalCompanyUpdateResult', {'success': Required[str], 'alerts': list[str], 'warnings': list['FiscalCompanyUpdateResultWarningsItem'], 'bearer_access_token_status': str, 'bearer_access_token_pending': bool, 'credenciais': 'FiscalCompanyUpdateResultCredenciais'}, total=False)

FiscalReportRequestVariant0 = TypedDict('FiscalReportRequestVariant0', {'data_inicio': Required[str], 'data_final': Required[str], 'numero_inicio': str, 'numero_final': str, 'modelo': Required[Literal['nfe', 'nfce', 'nfse', 'cte', 'cte_os', 'mdfe', 'nfcom', 'dce', 'cce', 'mde']], 'relatorio': Required[Literal['csv', 'excel', 'xml', 'danfe', 'danfe_simples', 'danfe_etiqueta', 'damdfe', 'dacte', 'danfecom']], 'separar_pdf': int, 'status': Literal['emitidas', 'canceladas', 'denegadas', 'inutilizadas', 'encerradas'], 'ordem': Literal['data_emissao', 'numeracao', 'ordem_alfabetica', 'id_pedido'], 'url_notificacao': str, 'email': str}, total=False)

FiscalReportRequestVariant1 = TypedDict('FiscalReportRequestVariant1', {'data_inicio': str, 'data_final': str, 'numero_inicio': Required[str], 'numero_final': Required[str], 'modelo': Required[Literal['nfe', 'nfce', 'nfse', 'cte', 'cte_os', 'mdfe', 'nfcom', 'dce', 'cce', 'mde']], 'relatorio': Required[Literal['csv', 'excel', 'xml', 'danfe', 'danfe_simples', 'danfe_etiqueta', 'damdfe', 'dacte', 'danfecom']], 'separar_pdf': int, 'status': Literal['emitidas', 'canceladas', 'denegadas', 'inutilizadas', 'encerradas'], 'ordem': Literal['data_emissao', 'numeracao', 'ordem_alfabetica', 'id_pedido'], 'url_notificacao': str, 'email': str}, total=False)

FiscalReportRequest: TypeAlias = Union['FiscalReportRequestVariant0', 'FiscalReportRequestVariant1']

FiscalReportResult = TypedDict('FiscalReportResult', {'uuid': Required['Uuid'], 'status': Required[str], 'data_inicio': str, 'data_final': str, 'numero_inicio': Union[str, int], 'numero_final': Union[str, int], 'modelo': str, 'relatorio': str, 'total': int, 'processado': int, 'url': str, 'expira': str, 'reason': str}, total=False)

IbsCbs112110Details = TypedDict('IbsCbs112110Details', {'indicador_quitacao': Union[Literal['1'], Literal[1]]}, total=False)

IbsCbs112110Request = TypedDict('IbsCbs112110Request', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112110']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'indicador_quitacao': Union[Literal['1'], Literal[1]], 'informacoes_evento': 'IbsCbs112110Details'}, total=False)

IbsCbs112120DetailsItensItemControleEstoque = TypedDict('IbsCbs112120DetailsItensItemControleEstoque', {'quantidade': Required[Union[str, Union[int, float]]], 'unidade': Required[str]}, total=False)

IbsCbs112120DetailsItensItem = TypedDict('IbsCbs112120DetailsItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112120DetailsItensItemControleEstoque']}, total=False)

IbsCbs112120Details = TypedDict('IbsCbs112120Details', {'itens': Required[list['IbsCbs112120DetailsItensItem']]}, total=False)

IbsCbs112120RequestVariant0ItensItemControleEstoque = TypedDict('IbsCbs112120RequestVariant0ItensItemControleEstoque', {'quantidade': Required[Union[str, Union[int, float]]], 'unidade': Required[str]}, total=False)

IbsCbs112120RequestVariant0ItensItem = TypedDict('IbsCbs112120RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112120RequestVariant0ItensItemControleEstoque']}, total=False)

IbsCbs112120RequestVariant0 = TypedDict('IbsCbs112120RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112120']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs112120RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs112120Details'}, total=False)

IbsCbs112120RequestVariant1ItensItemControleEstoque = TypedDict('IbsCbs112120RequestVariant1ItensItemControleEstoque', {'quantidade': Required[Union[str, Union[int, float]]], 'unidade': Required[str]}, total=False)

IbsCbs112120RequestVariant1ItensItem = TypedDict('IbsCbs112120RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112120RequestVariant1ItensItemControleEstoque']}, total=False)

IbsCbs112120RequestVariant1 = TypedDict('IbsCbs112120RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112120']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs112120RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs112120Details']}, total=False)

IbsCbs112120Request: TypeAlias = Union['IbsCbs112120RequestVariant0', 'IbsCbs112120RequestVariant1']

IbsCbs112130DetailsItensItemControleEstoque = TypedDict('IbsCbs112130DetailsItensItemControleEstoque', {'quantidade_perecimento': Required[Union[str, Union[int, float]]], 'unidade_perecimento': Required[str], 'valor_ibs_estorno': Required[Union[str, Union[int, float]]], 'valor_cbs_estorno': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs112130DetailsItensItem = TypedDict('IbsCbs112130DetailsItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112130DetailsItensItemControleEstoque']}, total=False)

IbsCbs112130Details = TypedDict('IbsCbs112130Details', {'itens': Required[list['IbsCbs112130DetailsItensItem']]}, total=False)

IbsCbs112130RequestVariant0ItensItemControleEstoque = TypedDict('IbsCbs112130RequestVariant0ItensItemControleEstoque', {'quantidade_perecimento': Required[Union[str, Union[int, float]]], 'unidade_perecimento': Required[str], 'valor_ibs_estorno': Required[Union[str, Union[int, float]]], 'valor_cbs_estorno': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs112130RequestVariant0ItensItem = TypedDict('IbsCbs112130RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112130RequestVariant0ItensItemControleEstoque']}, total=False)

IbsCbs112130RequestVariant0 = TypedDict('IbsCbs112130RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112130']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs112130RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs112130Details'}, total=False)

IbsCbs112130RequestVariant1ItensItemControleEstoque = TypedDict('IbsCbs112130RequestVariant1ItensItemControleEstoque', {'quantidade_perecimento': Required[Union[str, Union[int, float]]], 'unidade_perecimento': Required[str], 'valor_ibs_estorno': Required[Union[str, Union[int, float]]], 'valor_cbs_estorno': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs112130RequestVariant1ItensItem = TypedDict('IbsCbs112130RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112130RequestVariant1ItensItemControleEstoque']}, total=False)

IbsCbs112130RequestVariant1 = TypedDict('IbsCbs112130RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112130']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs112130RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs112130Details']}, total=False)

IbsCbs112130Request: TypeAlias = Union['IbsCbs112130RequestVariant0', 'IbsCbs112130RequestVariant1']

IbsCbs112140DetailsItensItemControleEstoque = TypedDict('IbsCbs112140DetailsItensItemControleEstoque', {'quantidade_nao_fornecida': Required[Union[str, Union[int, float]]], 'unidade_nao_fornecida': Required[str]}, total=False)

IbsCbs112140DetailsItensItem = TypedDict('IbsCbs112140DetailsItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112140DetailsItensItemControleEstoque']}, total=False)

IbsCbs112140Details = TypedDict('IbsCbs112140Details', {'itens': Required[list['IbsCbs112140DetailsItensItem']]}, total=False)

IbsCbs112140RequestVariant0ItensItemControleEstoque = TypedDict('IbsCbs112140RequestVariant0ItensItemControleEstoque', {'quantidade_nao_fornecida': Required[Union[str, Union[int, float]]], 'unidade_nao_fornecida': Required[str]}, total=False)

IbsCbs112140RequestVariant0ItensItem = TypedDict('IbsCbs112140RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112140RequestVariant0ItensItemControleEstoque']}, total=False)

IbsCbs112140RequestVariant0 = TypedDict('IbsCbs112140RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112140']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs112140RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs112140Details'}, total=False)

IbsCbs112140RequestVariant1ItensItemControleEstoque = TypedDict('IbsCbs112140RequestVariant1ItensItemControleEstoque', {'quantidade_nao_fornecida': Required[Union[str, Union[int, float]]], 'unidade_nao_fornecida': Required[str]}, total=False)

IbsCbs112140RequestVariant1ItensItem = TypedDict('IbsCbs112140RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs112140RequestVariant1ItensItemControleEstoque']}, total=False)

IbsCbs112140RequestVariant1 = TypedDict('IbsCbs112140RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112140']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs112140RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs112140Details']}, total=False)

IbsCbs112140Request: TypeAlias = Union['IbsCbs112140RequestVariant0', 'IbsCbs112140RequestVariant1']

IbsCbs112150Details = TypedDict('IbsCbs112150Details', {'data_previsao_entrega': Required[str]}, total=False)

IbsCbs112150RequestVariant0 = TypedDict('IbsCbs112150RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112150']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'data_previsao_entrega': Required[str], 'informacoes_evento': 'IbsCbs112150Details'}, total=False)

IbsCbs112150RequestVariant1 = TypedDict('IbsCbs112150RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['112150']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'data_previsao_entrega': str, 'informacoes_evento': Required['IbsCbs112150Details']}, total=False)

IbsCbs112150Request: TypeAlias = Union['IbsCbs112150RequestVariant0', 'IbsCbs112150RequestVariant1']

IbsCbs211110DetailsItensItemCreditoPresumido = TypedDict('IbsCbs211110DetailsItensItemCreditoPresumido', {'classificacao': Required[str], 'aliquota_ibs': Required[Union[str, Union[int, float]]], 'aliquota_cbs': Required[Union[str, Union[int, float]]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs211110DetailsItensItem = TypedDict('IbsCbs211110DetailsItensItem', {'item': Required[Union[str, int]], 'base_calculo': Required[Union[str, Union[int, float]]], 'credito_presumido': Required['IbsCbs211110DetailsItensItemCreditoPresumido']}, total=False)

IbsCbs211110Details = TypedDict('IbsCbs211110Details', {'itens': Required[list['IbsCbs211110DetailsItensItem']]}, total=False)

IbsCbs211110RequestVariant0ItensItemCreditoPresumido = TypedDict('IbsCbs211110RequestVariant0ItensItemCreditoPresumido', {'classificacao': Required[str], 'aliquota_ibs': Required[Union[str, Union[int, float]]], 'aliquota_cbs': Required[Union[str, Union[int, float]]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs211110RequestVariant0ItensItem = TypedDict('IbsCbs211110RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'base_calculo': Required[Union[str, Union[int, float]]], 'credito_presumido': Required['IbsCbs211110RequestVariant0ItensItemCreditoPresumido']}, total=False)

IbsCbs211110RequestVariant0 = TypedDict('IbsCbs211110RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211110']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs211110RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs211110Details'}, total=False)

IbsCbs211110RequestVariant1ItensItemCreditoPresumido = TypedDict('IbsCbs211110RequestVariant1ItensItemCreditoPresumido', {'classificacao': Required[str], 'aliquota_ibs': Required[Union[str, Union[int, float]]], 'aliquota_cbs': Required[Union[str, Union[int, float]]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs211110RequestVariant1ItensItem = TypedDict('IbsCbs211110RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'base_calculo': Required[Union[str, Union[int, float]]], 'credito_presumido': Required['IbsCbs211110RequestVariant1ItensItemCreditoPresumido']}, total=False)

IbsCbs211110RequestVariant1 = TypedDict('IbsCbs211110RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211110']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs211110RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs211110Details']}, total=False)

IbsCbs211110Request: TypeAlias = Union['IbsCbs211110RequestVariant0', 'IbsCbs211110RequestVariant1']

IbsCbs211124DetailsItensItemControleEstoque = TypedDict('IbsCbs211124DetailsItensItemControleEstoque', {'quantidade_perecimento': Required[Union[str, Union[int, float]]], 'unidade_perecimento': Required[str]}, total=False)

IbsCbs211124DetailsItensItem = TypedDict('IbsCbs211124DetailsItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211124DetailsItensItemControleEstoque']}, total=False)

IbsCbs211124Details = TypedDict('IbsCbs211124Details', {'itens': Required[list['IbsCbs211124DetailsItensItem']]}, total=False)

IbsCbs211124RequestVariant0ItensItemControleEstoque = TypedDict('IbsCbs211124RequestVariant0ItensItemControleEstoque', {'quantidade_perecimento': Required[Union[str, Union[int, float]]], 'unidade_perecimento': Required[str]}, total=False)

IbsCbs211124RequestVariant0ItensItem = TypedDict('IbsCbs211124RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211124RequestVariant0ItensItemControleEstoque']}, total=False)

IbsCbs211124RequestVariant0 = TypedDict('IbsCbs211124RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211124']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs211124RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs211124Details'}, total=False)

IbsCbs211124RequestVariant1ItensItemControleEstoque = TypedDict('IbsCbs211124RequestVariant1ItensItemControleEstoque', {'quantidade_perecimento': Required[Union[str, Union[int, float]]], 'unidade_perecimento': Required[str]}, total=False)

IbsCbs211124RequestVariant1ItensItem = TypedDict('IbsCbs211124RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211124RequestVariant1ItensItemControleEstoque']}, total=False)

IbsCbs211124RequestVariant1 = TypedDict('IbsCbs211124RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211124']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs211124RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs211124Details']}, total=False)

IbsCbs211124Request: TypeAlias = Union['IbsCbs211124RequestVariant0', 'IbsCbs211124RequestVariant1']

IbsCbs211128Details = TypedDict('IbsCbs211128Details', {'indicador_aceitacao': Required[Union[Literal['0', '1'], Literal[0, 1]]]}, total=False)

IbsCbs211128RequestVariant0 = TypedDict('IbsCbs211128RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211128']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'indicador_aceitacao': Required[Union[Literal['0', '1'], Literal[0, 1]]], 'informacoes_evento': 'IbsCbs211128Details'}, total=False)

IbsCbs211128RequestVariant1 = TypedDict('IbsCbs211128RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211128']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'indicador_aceitacao': Union[Literal['0', '1'], Literal[0, 1]], 'informacoes_evento': Required['IbsCbs211128Details']}, total=False)

IbsCbs211128Request: TypeAlias = Union['IbsCbs211128RequestVariant0', 'IbsCbs211128RequestVariant1']

IbsCbs211130DetailsItensItemControleEstoque = TypedDict('IbsCbs211130DetailsItensItemControleEstoque', {'quantidade_imobilizada': Required[Union[str, Union[int, float]]], 'unidade_imobilizada': Required[str]}, total=False)

IbsCbs211130DetailsItensItem = TypedDict('IbsCbs211130DetailsItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211130DetailsItensItemControleEstoque']}, total=False)

IbsCbs211130Details = TypedDict('IbsCbs211130Details', {'itens': Required[list['IbsCbs211130DetailsItensItem']]}, total=False)

IbsCbs211130RequestVariant0ItensItemControleEstoque = TypedDict('IbsCbs211130RequestVariant0ItensItemControleEstoque', {'quantidade_imobilizada': Required[Union[str, Union[int, float]]], 'unidade_imobilizada': Required[str]}, total=False)

IbsCbs211130RequestVariant0ItensItem = TypedDict('IbsCbs211130RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211130RequestVariant0ItensItemControleEstoque']}, total=False)

IbsCbs211130RequestVariant0 = TypedDict('IbsCbs211130RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211130']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs211130RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs211130Details'}, total=False)

IbsCbs211130RequestVariant1ItensItemControleEstoque = TypedDict('IbsCbs211130RequestVariant1ItensItemControleEstoque', {'quantidade_imobilizada': Required[Union[str, Union[int, float]]], 'unidade_imobilizada': Required[str]}, total=False)

IbsCbs211130RequestVariant1ItensItem = TypedDict('IbsCbs211130RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211130RequestVariant1ItensItemControleEstoque']}, total=False)

IbsCbs211130RequestVariant1 = TypedDict('IbsCbs211130RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211130']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs211130RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs211130Details']}, total=False)

IbsCbs211130Request: TypeAlias = Union['IbsCbs211130RequestVariant0', 'IbsCbs211130RequestVariant1']

IbsCbs211140DetailsItensItemControleEstoque = TypedDict('IbsCbs211140DetailsItensItemControleEstoque', {'quantidade_combustivel': Required[Union[str, Union[int, float]]], 'unidade_combustivel': Required[str]}, total=False)

IbsCbs211140DetailsItensItem = TypedDict('IbsCbs211140DetailsItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211140DetailsItensItemControleEstoque']}, total=False)

IbsCbs211140Details = TypedDict('IbsCbs211140Details', {'itens': Required[list['IbsCbs211140DetailsItensItem']]}, total=False)

IbsCbs211140RequestVariant0ItensItemControleEstoque = TypedDict('IbsCbs211140RequestVariant0ItensItemControleEstoque', {'quantidade_combustivel': Required[Union[str, Union[int, float]]], 'unidade_combustivel': Required[str]}, total=False)

IbsCbs211140RequestVariant0ItensItem = TypedDict('IbsCbs211140RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211140RequestVariant0ItensItemControleEstoque']}, total=False)

IbsCbs211140RequestVariant0 = TypedDict('IbsCbs211140RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211140']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs211140RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs211140Details'}, total=False)

IbsCbs211140RequestVariant1ItensItemControleEstoque = TypedDict('IbsCbs211140RequestVariant1ItensItemControleEstoque', {'quantidade_combustivel': Required[Union[str, Union[int, float]]], 'unidade_combustivel': Required[str]}, total=False)

IbsCbs211140RequestVariant1ItensItem = TypedDict('IbsCbs211140RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_ibs': Required[Union[str, Union[int, float]]], 'valor_cbs': Required[Union[str, Union[int, float]]], 'controle_estoque': Required['IbsCbs211140RequestVariant1ItensItemControleEstoque']}, total=False)

IbsCbs211140RequestVariant1 = TypedDict('IbsCbs211140RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211140']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs211140RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs211140Details']}, total=False)

IbsCbs211140Request: TypeAlias = Union['IbsCbs211140RequestVariant0', 'IbsCbs211140RequestVariant1']

IbsCbs211150DetailsItensItem = TypedDict('IbsCbs211150DetailsItensItem', {'item': Required[Union[str, int]], 'valor_credito_ibs': Required[Union[str, Union[int, float]]], 'valor_credito_cbs': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs211150Details = TypedDict('IbsCbs211150Details', {'itens': Required[list['IbsCbs211150DetailsItensItem']]}, total=False)

IbsCbs211150RequestVariant0ItensItem = TypedDict('IbsCbs211150RequestVariant0ItensItem', {'item': Required[Union[str, int]], 'valor_credito_ibs': Required[Union[str, Union[int, float]]], 'valor_credito_cbs': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs211150RequestVariant0 = TypedDict('IbsCbs211150RequestVariant0', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211150']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': Required[list['IbsCbs211150RequestVariant0ItensItem']], 'informacoes_evento': 'IbsCbs211150Details'}, total=False)

IbsCbs211150RequestVariant1ItensItem = TypedDict('IbsCbs211150RequestVariant1ItensItem', {'item': Required[Union[str, int]], 'valor_credito_ibs': Required[Union[str, Union[int, float]]], 'valor_credito_cbs': Required[Union[str, Union[int, float]]]}, total=False)

IbsCbs211150RequestVariant1 = TypedDict('IbsCbs211150RequestVariant1', {'chave': Required['AccessKey'], 'ambiente': Required['Environment'], 'cod_evento': Required[Literal['211150']], 'evento': int, 'url_notificacao': str, 'nSeqEvento': int, 'itens': list['IbsCbs211150RequestVariant1ItensItem'], 'informacoes_evento': Required['IbsCbs211150Details']}, total=False)

IbsCbs211150Request: TypeAlias = Union['IbsCbs211150RequestVariant0', 'IbsCbs211150RequestVariant1']

NfeIbsCbsEventRequest: TypeAlias = Union['IbsCbs112110Request', 'IbsCbs112120Request', 'IbsCbs112130Request', 'IbsCbs112140Request', 'IbsCbs112150Request', 'IbsCbs211110Request', 'IbsCbs211124Request', 'IbsCbs211128Request', 'IbsCbs211130Request', 'IbsCbs211140Request', 'IbsCbs211150Request']

Nfe55CustomerVariant0 = TypedDict('Nfe55CustomerVariant0', {'cpf': Required[str], 'nome_completo': Required[str], 'cnpj': str, 'razao_social': str, 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': Required[str], 'complemento': str, 'numero': Required[str], 'bairro': Required[str], 'cidade': Required[str], 'uf': Required[str], 'cep': Required[str], 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': str, 'cod_pais': str, 'nome_pais': str}, total=False)

Nfe55CustomerVariant1 = TypedDict('Nfe55CustomerVariant1', {'cpf': str, 'nome_completo': str, 'cnpj': Required[str], 'razao_social': Required[str], 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': Required[str], 'complemento': str, 'numero': Required[str], 'bairro': Required[str], 'cidade': Required[str], 'uf': Required[str], 'cep': Required[str], 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': str, 'cod_pais': str, 'nome_pais': str}, total=False)

Nfe55CustomerVariant2 = TypedDict('Nfe55CustomerVariant2', {'cpf': str, 'nome_completo': str, 'cnpj': str, 'razao_social': str, 'ie': str, 'suframa': str, 'substituto_tributario': str, 'consumidor_final': int, 'contribuinte': int, 'microcervejaria': bool, 'endereco': Required[str], 'complemento': str, 'numero': str, 'bairro': Required[str], 'cidade': str, 'uf': str, 'cep': str, 'telefone': str, 'email': str, 'id_estrangeiro': str, 'nome_estrangeiro': Required[str], 'cod_pais': Required[str], 'nome_pais': Required[str]}, total=False)

Nfe55Customer: TypeAlias = Union['Nfe55CustomerVariant0', 'Nfe55CustomerVariant1', 'Nfe55CustomerVariant2']

NfeComplementIbsCbs = TypedDict('NfeComplementIbsCbs', {'situacao_tributaria': Required[str], 'classificacao_tributaria': Required[str], 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'ibs_estadual': 'G101', 'ibs_municipal': 'G102', 'cbs': 'G103', 'tributacao_monofasica': 'G105', 'credito_presumido': 'G106', 'transferencia_credito': 'G108', 'ajuste_competencia': 'G109', 'estorno_credito': 'G110', 'base_calculo': Required[Union[str, Union[int, float]]]}, total=False)

NfePreviewResult = TypedDict('NfePreviewResult', {'danfe': Required[str]}, total=False)

NfeTaxCalculationResultImpostos = TypedDict('NfeTaxCalculationResultImpostos', {'ipi': Union[str, Union[int, float]], 'icms': Union[str, Union[int, float]], 'icms_st': Union[str, Union[int, float]], 'pis': Union[str, Union[int, float]], 'cofins': Union[str, Union[int, float]], 'fcp_st': Union[str, Union[int, float]], 'fcp_dest': Union[str, Union[int, float]], 'fcp_dest_base': Union[str, Union[int, float]], 'issqn': Union[str, Union[int, float]], 'total_tributacao': Union[str, Union[int, float]], 'icms_desoneracao': Union[str, Union[int, float]], 'importacao': Union[str, Union[int, float]]}, total=False)

NfeTaxCalculationResultAliquotas = TypedDict('NfeTaxCalculationResultAliquotas', {'icms': list[Union[str, Union[int, float]]], 'icms_diferimento': list[Union[str, Union[int, float]]], 'icms_st': list[Union[str, Union[int, float]]], 'pis': list[Union[str, Union[int, float]]], 'cofins': list[Union[str, Union[int, float]]], 'ipi': list[Union[str, Union[int, float]]]}, total=False)

NfeTaxCalculationResultPedido = TypedDict('NfeTaxCalculationResultPedido', {'produtos': Union[str, Union[int, float]], 'frete': Union[str, Union[int, float]], 'desconto': Union[str, Union[int, float]], 'despesas_acessorias': Union[str, Union[int, float]], 'seguro': Union[str, Union[int, float]], 'total': Union[str, Union[int, float]]}, total=False)

NfeTaxCalculationResult = TypedDict('NfeTaxCalculationResult', {'impostos': Required['NfeTaxCalculationResultImpostos'], 'aliquotas': Required['NfeTaxCalculationResultAliquotas'], 'pedido': Required['NfeTaxCalculationResultPedido']}, total=False)

NfeIssueResult: TypeAlias = Union['NfeDocument', 'NfePreviewResult', 'NfeTaxCalculationResult']

NfeNotification = TypedDict('NfeNotification', {'uuid': Required['Uuid'], 'status': Required[str], 'motivo': str, 'nfe': Union[str, int], 'serie': Union[str, int], 'recibo': str, 'chave': str, 'modelo': str, 'epec': bool, 'xml': str, 'xml_cancelamento': str, 'danfe': str, 'danfe_simples': str, 'danfe_etiqueta': str, 'log': Union['SefazLog', str, list['SefazLog'], None], 'log_cancelamento': Union['SefazLog', str, list['SefazLog'], None], 'data': 'NfeIssueRequest', 'evento': Union[str, int], 'dacce': str, 'protocolo_evento': str, 'url_notificacao': str}, total=False)

nfeGetCertificateValidityResponse: TypeAlias = Union[Union['NfeCertificateValidity', 'Api1Error']]

nfeGetSefazStatusResponse: TypeAlias = Union[Union['NfeSefazStatus', 'Api1Error']]

nfeGetDocumentQuery = TypedDict('nfeGetDocumentQuery', {'chave': 'AccessKey', 'uuid': str, 'ID': str, 'id': str, 'ambiente': 'Environment'}, total=False)

nfeGetDocumentResponse: TypeAlias = Union[Union[Union['NfeDocument', list['NfeDocument']], 'Api1Error']]

nfeQueryDocumentResponse: TypeAlias = Union[Union[Union['NfeDocument', list['NfeDocument']], 'Api1Error']]

nfeCreateCorrectionResponse: TypeAlias = Union[Union['NfeEventResult', 'Api1Error']]

nfeCreateManifestationResponse: TypeAlias = Union[Union['NfeEventResult', 'Api1Error']]

nfeCancelDocumentResponse: TypeAlias = Union[Union['NfeCancelResult', 'Api1Error']]

nfeVoidNumberingResponse: TypeAlias = Union[Union['NfeVoidResult', 'Api1Error']]

nfeCreatePaymentEventResponse: TypeAlias = Union[Union['NfeEventResult', 'Api1Error']]

nfeCancelPaymentEventResponse: TypeAlias = Union[Union['NfeEventResult', 'Api1Error']]

nfeCancelIbsCbsEventResponse: TypeAlias = Union[Union['NfeEventResult', 'Api1Error']]

nfeListTaxClassesResponse: TypeAlias = Union[Union[list['TaxClassListItem'], 'TaxClassNoResults', 'Api1Error']]

nfeDeleteTaxClassesResponse: TypeAlias = Union[Union[list['TaxClassDeleteItem'], 'Api1Error']]

nfeSaveTaxClassesResponse: TypeAlias = Union[Union['TaxClassCreatedResult', 'Api1Error']]

nfeIssueDocumentResponse: TypeAlias = Union[Union['NfeIssueResult', 'Api1Error']]

nfeIssueReturnResponse: TypeAlias = Union[Union['NfeDocument', 'Api1Error']]

nfeIssueAdjustmentResponse: TypeAlias = Union[Union['NfeDocument', 'Api1Error']]

nfeIssueComplementResponse: TypeAlias = Union[Union['NfeDocument', 'Api1Error']]

fiscalUpdateCompanyResponse: TypeAlias = Union[Union['FiscalCompanyUpdateResult', 'Api1Error']]

fiscalCreateOrPollReportResponse: TypeAlias = Union[Union['FiscalReportResult', 'Api1Error']]

nfeCreateIbsCbsEventResponse: TypeAlias = Union[Union['NfeEventResult', 'Api1Error']]

_bind_types(globals(), __name__, ['AccessKey', 'Uuid', 'Environment', 'Decimal', 'Api1ErrorLogVariant1', 'Api1Error', 'SefazLogEventoVariant0', 'SefazLogEventoVariant1Item', 'SefazLog', 'NfeDocument', 'NfeEventResult', 'NfeCancelResult', 'NfeVoidResult', 'NfeCertificateValidity', 'NfeSefazStatus', 'NfeLookupRequestVariant0', 'NfeLookupRequestVariant1', 'NfeLookupRequestVariant2', 'NfeLookupRequestVariant3', 'NfeLookupRequest', 'NfeCorrectionRequestVariant0', 'NfeCorrectionRequestVariant1', 'NfeCorrectionRequest', 'NfeManifestationRequest', 'NfeCancelRequestVariant0', 'NfeCancelRequestVariant1', 'NfeCancelRequest', 'NfeVoidRequest', 'NfePaymentEventItem', 'NfePaymentEventRequestVariant0', 'NfePaymentEventRequestVariant1', 'NfePaymentEventRequestVariant2', 'NfePaymentEventRequestVariant3', 'NfePaymentEventRequest', 'NfePaymentEventCancelRequest', 'NfeIbsCbsEventCancelRequest', 'TaxClassDeleteRequest', 'TaxClassDeleteItem', 'TaxClassNoResults', 'TaxClassListItem', 'TaxClassListIcms', 'TaxClassListIpi', 'TaxClassListPis', 'TaxClassListCofins', 'TaxClassListGroupObject', 'TaxClassListIssqn', 'TaxClassListIbsCbs', 'TaxClassListPresumedCredit', 'TaxClassListStateRate', 'TaxClassListBareRate', 'TaxClassListStateRates', 'TaxClassListIcmsPresumedCredit', 'TaxClassListIbsCbsDeferral', 'G002', 'G003', 'G004', 'G005', 'G006', 'G007', 'G008', 'G009', 'G010', 'G011', 'G012', 'G013', 'G014', 'G015', 'G016', 'G017', 'G018', 'G019', 'G020', 'G021', 'G022', 'G023', 'G024', 'G025', 'G026Variant0', 'G026Variant1', 'G026Variant2', 'G026', 'G027Variant0', 'G027Variant1', 'G027Variant2', 'G027', 'G028', 'G029', 'G030', 'G031Variant0', 'G031Variant1', 'G031', 'G032', 'G033', 'G034', 'G035', 'G037', 'G038', 'G039', 'G040', 'G041', 'G042', 'G043', 'G044', 'G045', 'G046', 'G047', 'G048', 'G049', 'G050', 'G051', 'G052', 'G053', 'G054', 'G055', 'G056', 'G057', 'G058', 'G059', 'G060', 'G061', 'G062', 'G063', 'G064', 'G065', 'G066', 'G067', 'G068', 'G069', 'G070', 'G071', 'G072', 'G073', 'G074', 'G075', 'G076', 'G077', 'G078', 'G079', 'G080', 'G081', 'G082', 'G083', 'G084', 'G085', 'G086', 'G087', 'G088', 'G089', 'G090', 'G091', 'G092', 'G093', 'G094', 'G095', 'G096', 'G097', 'G100', 'G101', 'G102', 'G103', 'G104', 'G105', 'G106', 'G108', 'G109', 'G110', 'G111', 'G112', 'G113', 'G114ImpostosIbsCbs', 'G114Impostos', 'G114', 'G115', 'G116', 'G117', 'G118', 'G119', 'G120', 'G121', 'G122DfeReferenciado', 'G122', 'G123', 'G124', 'G125', 'G127ControleEstoque', 'G127', 'G128ControleEstoque', 'G128', 'G129ControleEstoque', 'G129', 'G130', 'G131CreditoPresumido', 'G131', 'G132ControleEstoque', 'G132', 'G133', 'G134ControleEstoque', 'G134', 'G135ControleEstoque', 'G135', 'G136', 'G137', 'G138', 'G139', 'G140', 'G141', 'G142', 'G143', 'G144', 'G145', 'G146', 'G147', 'G148', 'G149', 'G150', 'G151', 'G152', 'G153', 'NfeIcms', 'NfeContributorObservation', 'NfeOrder', 'NfeTransport', 'NfeCustomer', 'NfeProduct', 'NfeIssueRequest', 'Nfe55IssueRequestClienteVariant0', 'Nfe55IssueRequestClienteVariant1', 'Nfe55IssueRequestClienteVariant2', 'Nfe55IssueRequest', 'Nfce65IssueRequest', 'NfeReturnRequestVariant0', 'NfeReturnRequestVariant1', 'NfeReturnRequestVariant2', 'NfeReturnRequestVariant3', 'NfeReturnRequest', 'NfeAdjustmentRequest', 'NfeComplementTaxes', 'NfeComplementProduct', 'NfeComplementRequestVariant0', 'NfeComplementRequestVariant1', 'NfeComplementRequestVariant2', 'NfeComplementRequestVariant3', 'NfeComplementRequest', 'NfeProductTaxClass', 'NfseTaxClassProvider55', 'NfseTaxClassProvider56', 'NfseTaxClassProvider57', 'NfseTaxClassProvider58', 'NfseTaxClassProvider60', 'NfseTaxClassProvider61', 'NfseTaxClassProvider63', 'NfseTaxClassProvider64', 'NfseTaxClassProvider66', 'NfseServiceTaxClass', 'FiscalTaxClassRequest', 'TaxClassCreatedResult', 'NfcomClassIcms', 'NfcomClassPisCofins', 'NfcomClassContribution', 'NfcomCommunicationTaxClass', 'FiscalCompanyUpdateRequest', 'FiscalCompanyUpdateResultWarningsItem', 'FiscalCompanyUpdateResultCredenciais', 'FiscalCompanyUpdateResult', 'FiscalReportRequestVariant0', 'FiscalReportRequestVariant1', 'FiscalReportRequest', 'FiscalReportResult', 'IbsCbs112110Details', 'IbsCbs112110Request', 'IbsCbs112120DetailsItensItemControleEstoque', 'IbsCbs112120DetailsItensItem', 'IbsCbs112120Details', 'IbsCbs112120RequestVariant0ItensItemControleEstoque', 'IbsCbs112120RequestVariant0ItensItem', 'IbsCbs112120RequestVariant0', 'IbsCbs112120RequestVariant1ItensItemControleEstoque', 'IbsCbs112120RequestVariant1ItensItem', 'IbsCbs112120RequestVariant1', 'IbsCbs112120Request', 'IbsCbs112130DetailsItensItemControleEstoque', 'IbsCbs112130DetailsItensItem', 'IbsCbs112130Details', 'IbsCbs112130RequestVariant0ItensItemControleEstoque', 'IbsCbs112130RequestVariant0ItensItem', 'IbsCbs112130RequestVariant0', 'IbsCbs112130RequestVariant1ItensItemControleEstoque', 'IbsCbs112130RequestVariant1ItensItem', 'IbsCbs112130RequestVariant1', 'IbsCbs112130Request', 'IbsCbs112140DetailsItensItemControleEstoque', 'IbsCbs112140DetailsItensItem', 'IbsCbs112140Details', 'IbsCbs112140RequestVariant0ItensItemControleEstoque', 'IbsCbs112140RequestVariant0ItensItem', 'IbsCbs112140RequestVariant0', 'IbsCbs112140RequestVariant1ItensItemControleEstoque', 'IbsCbs112140RequestVariant1ItensItem', 'IbsCbs112140RequestVariant1', 'IbsCbs112140Request', 'IbsCbs112150Details', 'IbsCbs112150RequestVariant0', 'IbsCbs112150RequestVariant1', 'IbsCbs112150Request', 'IbsCbs211110DetailsItensItemCreditoPresumido', 'IbsCbs211110DetailsItensItem', 'IbsCbs211110Details', 'IbsCbs211110RequestVariant0ItensItemCreditoPresumido', 'IbsCbs211110RequestVariant0ItensItem', 'IbsCbs211110RequestVariant0', 'IbsCbs211110RequestVariant1ItensItemCreditoPresumido', 'IbsCbs211110RequestVariant1ItensItem', 'IbsCbs211110RequestVariant1', 'IbsCbs211110Request', 'IbsCbs211124DetailsItensItemControleEstoque', 'IbsCbs211124DetailsItensItem', 'IbsCbs211124Details', 'IbsCbs211124RequestVariant0ItensItemControleEstoque', 'IbsCbs211124RequestVariant0ItensItem', 'IbsCbs211124RequestVariant0', 'IbsCbs211124RequestVariant1ItensItemControleEstoque', 'IbsCbs211124RequestVariant1ItensItem', 'IbsCbs211124RequestVariant1', 'IbsCbs211124Request', 'IbsCbs211128Details', 'IbsCbs211128RequestVariant0', 'IbsCbs211128RequestVariant1', 'IbsCbs211128Request', 'IbsCbs211130DetailsItensItemControleEstoque', 'IbsCbs211130DetailsItensItem', 'IbsCbs211130Details', 'IbsCbs211130RequestVariant0ItensItemControleEstoque', 'IbsCbs211130RequestVariant0ItensItem', 'IbsCbs211130RequestVariant0', 'IbsCbs211130RequestVariant1ItensItemControleEstoque', 'IbsCbs211130RequestVariant1ItensItem', 'IbsCbs211130RequestVariant1', 'IbsCbs211130Request', 'IbsCbs211140DetailsItensItemControleEstoque', 'IbsCbs211140DetailsItensItem', 'IbsCbs211140Details', 'IbsCbs211140RequestVariant0ItensItemControleEstoque', 'IbsCbs211140RequestVariant0ItensItem', 'IbsCbs211140RequestVariant0', 'IbsCbs211140RequestVariant1ItensItemControleEstoque', 'IbsCbs211140RequestVariant1ItensItem', 'IbsCbs211140RequestVariant1', 'IbsCbs211140Request', 'IbsCbs211150DetailsItensItem', 'IbsCbs211150Details', 'IbsCbs211150RequestVariant0ItensItem', 'IbsCbs211150RequestVariant0', 'IbsCbs211150RequestVariant1ItensItem', 'IbsCbs211150RequestVariant1', 'IbsCbs211150Request', 'NfeIbsCbsEventRequest', 'Nfe55CustomerVariant0', 'Nfe55CustomerVariant1', 'Nfe55CustomerVariant2', 'Nfe55Customer', 'NfeComplementIbsCbs', 'NfePreviewResult', 'NfeTaxCalculationResultImpostos', 'NfeTaxCalculationResultAliquotas', 'NfeTaxCalculationResultPedido', 'NfeTaxCalculationResult', 'NfeIssueResult', 'NfeNotification', 'nfeGetCertificateValidityResponse', 'nfeGetSefazStatusResponse', 'nfeGetDocumentQuery', 'nfeGetDocumentResponse', 'nfeQueryDocumentResponse', 'nfeCreateCorrectionResponse', 'nfeCreateManifestationResponse', 'nfeCancelDocumentResponse', 'nfeVoidNumberingResponse', 'nfeCreatePaymentEventResponse', 'nfeCancelPaymentEventResponse', 'nfeCancelIbsCbsEventResponse', 'nfeListTaxClassesResponse', 'nfeDeleteTaxClassesResponse', 'nfeSaveTaxClassesResponse', 'nfeIssueDocumentResponse', 'nfeIssueReturnResponse', 'nfeIssueAdjustmentResponse', 'nfeIssueComplementResponse', 'fiscalUpdateCompanyResponse', 'fiscalCreateOrPollReportResponse', 'nfeCreateIbsCbsEventResponse'])
