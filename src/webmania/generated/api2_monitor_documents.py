"""Generated from contracts/api2/monitor-documents.openapi.json; SHA256 50e164f0761ca4d6db1cd908c796daaf3762c526e2496166a0cbcc4d36d63b98. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

MonitorError = TypedDict('MonitorError', {'error': str, 'message': str, 'msg': str, 'success': bool}, total=False)

MonitorPagination = TypedDict('MonitorPagination', {'current_page': Required[int], 'last_page': Required[int], 'per_page': Required[int], 'total': Required[int]}, total=False)

MonitorAddress = TypedDict('MonitorAddress', {'cep': str, 'municipio': str, 'estado': str, 'codigo_municipio': Union[str, int]}, total=False)

MonitorCompany = TypedDict('MonitorCompany', {'uuid': Required[str], 'status': int, 'cpf': str, 'cnpj': str, 'nome_completo': str, 'razao_social': str, 'im': str, 'endereco': 'MonitorAddress', 'modelos_download': list[str], 'categorias_download': int, 'ambiente_download': int, 'certificado_vencimento': str, 'url_notificacao': str, 'dfe_retroativas': bool, 'dfe_retroativas_total': int}, total=False)

MonitorMunicipalityRegistration = TypedDict('MonitorMunicipalityRegistration', {'uuid': Required[str], 'tipo_download': Required[Literal[1, 2]], 'municipio': Required[str], 'uf': Required[str], 'codigo_ibge': Required[str], 'login': str, 'im': str}, total=False)

MonitorAvailableMunicipality = TypedDict('MonitorAvailableMunicipality', {'municipio': str, 'uf': str, 'codigo_ibge': str, 'nativo': Required[bool], 'im': Required[bool], 'certificado': Required[bool], 'login_senha': Required[bool], 'cadastro_prefeitura': Required[bool], 'domicilio_fiscal_municipio': Required[bool], 'multiplos_servicos': Required[bool], 'download_emitidas': bool, 'download_recebidas': bool, 'guia_cadastro_prefeitura': str}, total=False)

MonitorDownloadStatisticsEmpresasItem = TypedDict('MonitorDownloadStatisticsEmpresasItem', {'empresa_uuid': Required[str], 'total_downloads': Required[int]}, total=False)

MonitorDownloadStatistics = TypedDict('MonitorDownloadStatistics', {'total_downloads': Required[int], 'empresas': Required[list['MonitorDownloadStatisticsEmpresasItem']]}, total=False)

MonitorCompanyPage = TypedDict('MonitorCompanyPage', {'data': Required[list['MonitorCompany']], 'meta': Required['MonitorPagination']}, total=False)

MonitorMunicipalityPage = TypedDict('MonitorMunicipalityPage', {'data': Required[list['MonitorMunicipalityRegistration']], 'meta': Required['MonitorPagination']}, total=False)

MonitorAvailableMunicipalities = TypedDict('MonitorAvailableMunicipalities', {'data': Required[list['MonitorAvailableMunicipality']]}, total=False)

MonitorPerson = TypedDict('MonitorPerson', {'cnpj': str, 'cpf': str, 'razao_social': str, 'nome_completo': str, 'ie': str, 'im': str, 'endereco': str, 'numero': str, 'complemento': str, 'bairro': str, 'cep': str, 'cidade': str, 'uf': str, 'telefone': str, 'email': str}, total=False)

MonitorManifestationStateVariant0 = TypedDict('MonitorManifestationStateVariant0', {'codigo': Required[int], 'descricao': Required[Union[str, None]], 'manifestado': Required[bool], 'automatica': Required[bool]}, total=False)

MonitorManifestationState: TypeAlias = Union['MonitorManifestationStateVariant0', None]

MonitorDocumentNfeTotaisIssqn = TypedDict('MonitorDocumentNfeTotaisIssqn', {'valor_servicos': Union[int, float], 'iss_bc': Union[int, float], 'iss_valor': Union[int, float], 'pis_valor': Union[int, float], 'cofins_valor': Union[int, float], 'data_competencia': str, 'deducao': Union[int, float], 'outras_retencoes': Union[int, float], 'desconto_incondicionado': Union[int, float], 'desconto_condicionado': Union[int, float], 'iss_retido_valor': Union[int, float], 'regime_especial_tributacao': str}, total=False)

MonitorDocumentNfeProdutosItemImpostosImpostoImportacao = TypedDict('MonitorDocumentNfeProdutosItemImpostosImpostoImportacao', {'ii_bc': Union[int, float], 'despesas_aduaneiras': Union[int, float], 'ii_valor': Union[int, float], 'iof_valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIpi = TypedDict('MonitorDocumentNfeProdutosItemImpostosIpi', {'situacao_tributaria': str, 'valor': Union[int, float], 'qtd_selo': Union[int, float], 'codigo_selo': str, 'aliquota': Union[int, float], 'base_calculo': Union[int, float], 'ipi_aliquota': Union[int, float], 'ipi_valor': Union[int, float], 'ipi_bc': Union[int, float], 'codigo_enquadramento': str}, total=False)

MonitorDocumentNfeProdutosItemImpostosCofins = TypedDict('MonitorDocumentNfeProdutosItemImpostosCofins', {'cofins_bc': Union[int, float], 'situacao_tributaria': str, 'valor': Union[int, float], 'cofins_valor': Union[int, float], 'aliquota': Union[int, float], 'base_calculo': Union[int, float], 'cofins_aliquota': Union[int, float], 'cofins_aliquota_valor': Union[int, float], 'cofins_quantidade_bc': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsEstadual = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsEstadual', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsMunicipal = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsMunicipal', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCbs = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCbs', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsEstadual = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsEstadual', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsMunicipal = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsMunicipal', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularCbs = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularCbs', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegular = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegular', {'ibs_estadual': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsEstadual', 'ibs_municipal': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsMunicipal', 'cbs': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularCbs'}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsEstadual = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsEstadual', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsMunicipal = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsMunicipal', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalCbs = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalCbs', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamental = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamental', {'ibs_estadual': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsEstadual', 'ibs_municipal': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsMunicipal', 'cbs': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalCbs'}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoMonofasica = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoMonofasica', {'quantidade_bc': Union[int, float], 'aliquota_ibs': Union[int, float], 'aliquota_cbs': Union[int, float], 'valor_ibs': Union[int, float], 'valor_cbs': Union[int, float], 'quantidade_bc_retencao': Union[int, float], 'aliquota_ibs_retencao': Union[int, float], 'aliquota_cbs_retencao': Union[int, float], 'valor_ibs_retencao': Union[int, float], 'valor_cbs_retencao': Union[int, float], 'quantidade_bc_retido': Union[int, float], 'aliquota_ibs_retido': Union[int, float], 'aliquota_cbs_retido': Union[int, float], 'valor_ibs_retido': Union[int, float], 'valor_cbs_retido': Union[int, float], 'aliquota_diferimento_ibs': Union[int, float], 'aliquota_diferimento_cbs': Union[int, float], 'valor_diferimento_ibs': Union[int, float], 'valor_diferimento_cbs': Union[int, float], 'valor_total_ibs': Union[int, float], 'valor_total_cbs': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsTransferenciaCredito = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsTransferenciaCredito', {'valor_ibs': Union[int, float], 'valor_cbs': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsAjusteCompetencia = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsAjusteCompetencia', {'competencia_apuracao': str, 'valor_ibs': Union[int, float], 'valor_cbs': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumido = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumido', {'classificacao': str, 'bc': Union[int, float], 'aliquota_ibs': Union[int, float], 'valor_ibs': Union[int, float], 'valor_ibs_condicionado_suspensao': Union[int, float], 'aliquota_cbs': Union[int, float], 'valor_cbs': Union[int, float], 'valor_cbs_condicionado_suspensao': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumidoZfm = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumidoZfm', {'competencia_apuracao': str, 'classificacao': str, 'valor_ibs': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbsEstornoCredito = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbsEstornoCredito', {'valor_ibs': Union[int, float], 'valor_cbs': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIbsCbs = TypedDict('MonitorDocumentNfeProdutosItemImpostosIbsCbs', {'situacao_tributaria': str, 'classificacao_tributaria': str, 'indicador_doacao': bool, 'bc': Union[int, float], 'valor_ibs': Union[int, float], 'ibs_estadual': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsEstadual', 'ibs_municipal': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsMunicipal', 'cbs': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCbs', 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'tributacao_regular': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegular', 'compra_governamental': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamental', 'tributacao_monofasica': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoMonofasica', 'transferencia_credito': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTransferenciaCredito', 'ajuste_competencia': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsAjusteCompetencia', 'credito_presumido': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumido', 'credito_presumido_zfm': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumidoZfm', 'estorno_credito': 'MonitorDocumentNfeProdutosItemImpostosIbsCbsEstornoCredito'}, total=False)

MonitorDocumentNfeProdutosItemImpostosIcms = TypedDict('MonitorDocumentNfeProdutosItemImpostosIcms', {'fcp_aliquota_uf_destino': Union[int, float], 'icms_aliquota_reducao': Union[int, float], 'icms_st_aliquota': Union[int, float], 'icms_bc_uf_destino': Union[int, float], 'icms_st_aliquota_reducao': Union[int, float], 'icms_valor_uf_destino': Union[int, float], 'icms_motivo_desoneracao': Union[int, float], 'icms_aliquota_efetiva': Union[int, float], 'icms_st_retido_bc': Union[int, float], 'icms_valor_operacao': Union[int, float], 'icms_modalidade_bc': Union[int, float], 'fcp_st_bc': Union[int, float], 'fcp_st_retido_aliquota': Union[int, float], 'fcp_bc_uf_destino': Union[int, float], 'fcp_st_retido_bc': Union[int, float], 'icms_substituto_valor': Union[int, float], 'icms_st_uf': Union[int, float], 'aliquota': Union[int, float], 'icms_aliquota_reducao_efetiva': Union[int, float], 'icms_valor': Union[int, float], 'fcp_st_aliquota': Union[int, float], 'icms_bc_efetiva': Union[int, float], 'fcp_bc': Union[int, float], 'origem': Union[int, float], 'icms_st_valor_dest': Union[int, float], 'icms_bc_operacao_propria': Union[int, float], 'icms_st_retido_valor': Union[int, float], 'icms_aliquota_diferimento': Union[int, float], 'icms_st_bc_dest': Union[int, float], 'icms_aliquota_interestadual': Union[int, float], 'codigo_cfop': str, 'icms_aliquota_uf_destino': Union[int, float], 'icms_valor_credito': Union[int, float], 'icms_aliquota_credito': Union[int, float], 'icms_st_aliquota_mva': Union[int, float], 'icms_st_bc': Union[int, float], 'valor': Union[int, float], 'fcp_st_retido_valor': Union[int, float], 'icms_bc': Union[int, float], 'icms_valor_efetivo': Union[int, float], 'fcp_st_valor': Union[int, float], 'base_calculo': Union[int, float], 'fcp_aliquota': Union[int, float], 'icms_aliquota_partilha_interestadual': Union[int, float], 'icms_valor_desonerado': Union[int, float], 'icms_st_valor': Union[int, float], 'icms_valor_uf_remetente': Union[int, float], 'situacao_tributaria': str, 'icms_aliquota': Union[int, float], 'fcp_valor_uf_destino': Union[int, float], 'icms_valor_diferimento': Union[int, float], 'fcp_valor': Union[int, float], 'icms_st_modalidade_bc': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosPis = TypedDict('MonitorDocumentNfeProdutosItemImpostosPis', {'pis_aliquota': Union[int, float], 'pis_bc': Union[int, float], 'situacao_tributaria': str, 'valor': Union[int, float], 'pis_quantidade_bc': Union[int, float], 'pis_valor': Union[int, float], 'aliquota': Union[int, float], 'base_calculo': Union[int, float], 'pis_aliquota_valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostosIssqn = TypedDict('MonitorDocumentNfeProdutosItemImpostosIssqn', {'iss_bc': Union[int, float], 'iss_aliquota': Union[int, float], 'iss_valor': Union[int, float], 'municipio_fato_gerador': str, 'item_servico': str, 'deducao': Union[int, float], 'retencoes': Union[int, float], 'desconto_incondicionado': Union[int, float], 'desconto_condicionado': Union[int, float], 'iss_retido_valor': Union[int, float], 'exigibilidade': str, 'codigo_servico': str, 'municipio_incidencia': str, 'pais': str, 'processo': str, 'incentivo_fiscal': str}, total=False)

MonitorDocumentNfeProdutosItemImpostosIpiDevolvido = TypedDict('MonitorDocumentNfeProdutosItemImpostosIpiDevolvido', {'percentual_devolvido': Union[int, float], 'ipi_devolvido_valor': Union[int, float]}, total=False)

MonitorDocumentNfeProdutosItemImpostos = TypedDict('MonitorDocumentNfeProdutosItemImpostos', {'imposto_importacao': 'MonitorDocumentNfeProdutosItemImpostosImpostoImportacao', 'ipi': 'MonitorDocumentNfeProdutosItemImpostosIpi', 'cofins': 'MonitorDocumentNfeProdutosItemImpostosCofins', 'ibs_cbs': 'MonitorDocumentNfeProdutosItemImpostosIbsCbs', 'icms': 'MonitorDocumentNfeProdutosItemImpostosIcms', 'pis': 'MonitorDocumentNfeProdutosItemImpostosPis', 'issqn': 'MonitorDocumentNfeProdutosItemImpostosIssqn', 'ipi_devolvido': 'MonitorDocumentNfeProdutosItemImpostosIpiDevolvido'}, total=False)

MonitorDocumentNfeProdutosItem = TypedDict('MonitorDocumentNfeProdutosItem', {'cfop': str, 'valor_unitario': Union[int, float], 'origem': str, 'cest': str, 'unidade_tributavel': str, 'impostos': 'MonitorDocumentNfeProdutosItemImpostos', 'nome': str, 'quantidade_tributavel': Union[int, float], 'descricao': str, 'quantidade': Union[int, float], 'subtotal_tributavel': Union[int, float], 'valor_total': Union[int, float], 'outras_despesas': Union[int, float], 'seguro': Union[int, float], 'unidade': str, 'desconto': Union[int, float], 'total': Union[int, float], 'gtin_tributavel': str, 'gtin': str, 'subtotal': Union[int, float], 'frete': Union[int, float], 'ncm': str, 'item': str, 'codigo': str}, total=False)

MonitorDocumentNfeProtocoloVariant1 = TypedDict('MonitorDocumentNfeProtocoloVariant1', {'motivo': str, 'status': str, 'data_recebimento': str, 'numero_protocolo': str}, total=False)

MonitorDocumentNfeTotais = TypedDict('MonitorDocumentNfeTotais', {'valor_desconto': Union[int, float], 'ii_valor': Union[int, float], 'valor_seguro': Union[int, float], 'fcp_st_retido_valor': Union[int, float], 'cofins_valor': Union[int, float], 'icms_bc': Union[int, float], 'ipi_devolvido_valor': Union[int, float], 'fcp_st_valor': Union[int, float], 'valor_produtos': Union[int, float], 'valor_outras_despesas': Union[int, float], 'icms_valor_desonerado': Union[int, float], 'valor_frete': Union[int, float], 'icms_st_valor': Union[int, float], 'valor_total_nfe': Union[int, float], 'pis_valor': Union[int, float], 'icms_valor': Union[int, float], 'ipi_valor': Union[int, float], 'fcp_valor': Union[int, float], 'icms_st_bc': Union[int, float]}, total=False)

MonitorDocumentNfeFatura = TypedDict('MonitorDocumentNfeFatura', {'valor_desconto': Union[int, float], 'valor_liquido': Union[int, float], 'valor': Union[int, float], 'valor_original': Union[int, float], 'desconto': Union[int, float], 'numero': str}, total=False)

MonitorDocumentNfePedido = TypedDict('MonitorDocumentNfePedido', {'bandeira': list[str], 'ID': str, 'informacoes_complementares': str, 'numero_compra': str, 'cnpj_credenciadora': list[str], 'intermediador': str, 'informacoes_fisco': str, 'desc_pagamento': list[str], 'numero_pedido': str, 'autorizacao': list[str], 'valor_pagamento': list[Union[int, float]], 'desconto': Union[int, float], 'forma_pagamento': list[str], 'cnpj_intermediador': str, 'frete': Union[int, float], 'presenca': str, 'id_intermediador': str, 'pagamento': list[str], 'modalidade_frete': str, 'tipo_integracao': list[str]}, total=False)

MonitorDocumentNfeResponsavelTecnico = TypedDict('MonitorDocumentNfeResponsavelTecnico', {'telefone': str, 'razao_social': str, 'cnpj': str, 'contato': str, 'email': str}, total=False)

MonitorDocumentNfeTransporteVeiculo = TypedDict('MonitorDocumentNfeTransporteVeiculo', {'placa': str, 'uf': str}, total=False)

MonitorDocumentNfeTransporteRetirada = TypedDict('MonitorDocumentNfeTransporteRetirada', {'cnpj': str, 'cpf': str, 'razao_social': str, 'nome_completo': str, 'nome_fantasia': str, 'ie': str, 'endereco': str, 'numero': str, 'complemento': str, 'bairro': str, 'cep': str, 'cidade': str, 'uf': str, 'telefone': str, 'email': str}, total=False)

MonitorDocumentNfeTransporteEntrega = TypedDict('MonitorDocumentNfeTransporteEntrega', {'cnpj': str, 'cpf': str, 'razao_social': str, 'nome_completo': str, 'nome_fantasia': str, 'ie': str, 'endereco': str, 'numero': str, 'complemento': str, 'bairro': str, 'cep': str, 'cidade': str, 'uf': str, 'telefone': str, 'email': str}, total=False)

MonitorDocumentNfeTransporteVolumesItem = TypedDict('MonitorDocumentNfeTransporteVolumesItem', {'quantidade': Union[int, float], 'especie': str, 'marca': str, 'numeracao': str, 'peso_liquido': Union[int, float], 'peso_bruto': Union[int, float]}, total=False)

MonitorDocumentNfeTransporteTransportadora = TypedDict('MonitorDocumentNfeTransporteTransportadora', {'cnpj': str, 'ie': str, 'bairro': str, 'cidade': str, 'cep': str, 'endereco': str, 'nome_fantasia': str, 'razao_social': str, 'telefone': str, 'uf': str, 'nome_completo': str, 'complemento': str, 'cpf': str, 'numero': str, 'email': str}, total=False)

MonitorDocumentNfeTransporte = TypedDict('MonitorDocumentNfeTransporte', {'peso_liquido': Union[int, float], 'volume': str, 'veiculo': 'MonitorDocumentNfeTransporteVeiculo', 'especie': str, 'numeracao': str, 'peso_bruto': Union[int, float], 'retirada': 'MonitorDocumentNfeTransporteRetirada', 'marca': str, 'entrega': 'MonitorDocumentNfeTransporteEntrega', 'volumes': list['MonitorDocumentNfeTransporteVolumesItem'], 'transportadora': 'MonitorDocumentNfeTransporteTransportadora', 'modalidade_frete': Union[int, float]}, total=False)

MonitorDocumentNfeDocs = TypedDict('MonitorDocumentNfeDocs', {'xml': Union[str, None], 'pdf': Union[str, None]}, total=False)

MonitorDocumentNfeParcelasItem = TypedDict('MonitorDocumentNfeParcelasItem', {'valor': Union[int, float], 'numero': Union[str, Union[int, float]], 'vencimento': str}, total=False)

MonitorDocumentNfeFornecedorVariant0 = TypedDict('MonitorDocumentNfeFornecedorVariant0', {'razao_social': str, 'documento': Union[str, None], 'uf': Union[str, None]}, total=False)

MonitorDocumentNfeTotaisIbsCbsCbs = TypedDict('MonitorDocumentNfeTotaisIbsCbsCbs', {'valor': Union[Union[int, float], str]}, total=False)

MonitorDocumentNfeTotaisIbsCbs = TypedDict('MonitorDocumentNfeTotaisIbsCbs', {'bc': Union[Union[int, float], str], 'valor_ibs': Union[Union[int, float], str], 'aliquota_ibs': Union[Union[int, float], str], 'aliquota_cbs': Union[Union[int, float], str], 'cbs': 'MonitorDocumentNfeTotaisIbsCbsCbs'}, total=False)

MonitorDocumentNfe = TypedDict('MonitorDocumentNfe', {'status': str, 'cfop': list[str], 'data_emissao': str, 'totais_issqn': 'MonitorDocumentNfeTotaisIssqn', 'produtos': list['MonitorDocumentNfeProdutosItem'], 'valor': Union[Union[int, float], str], 'protocolo': Union[str, 'MonitorDocumentNfeProtocoloVariant1'], 'finalidade': Union[int, float], 'totais': 'MonitorDocumentNfeTotais', 'fatura': 'MonitorDocumentNfeFatura', 'operacao': Union[int, float], 'pedido': 'MonitorDocumentNfePedido', 'natureza_operacao': str, 'responsavel_tecnico': 'MonitorDocumentNfeResponsavelTecnico', 'emitente': Union['MonitorPerson', None], 'transporte': 'MonitorDocumentNfeTransporte', 'chave': str, 'empresa_uuid': Required[str], 'docs': 'MonitorDocumentNfeDocs', 'modelo': Required[Literal['nfe']], 'cliente': Union['MonitorPerson', None], 'uuid': Required[str], 'serie': Union[Union[int, float], str], 'categoria': str, 'numero': Union[Union[int, float], str], 'parcelas': list['MonitorDocumentNfeParcelasItem'], 'data_captura': str, 'fornecedor': Union['MonitorDocumentNfeFornecedorVariant0', None], 'qtd_produtos': int, 'manifestacao': 'MonitorManifestationState', 'totais_ibs_cbs': 'MonitorDocumentNfeTotaisIbsCbs'}, total=False)

MonitorDocumentNfseTotais = TypedDict('MonitorDocumentNfseTotais', {'valor': Union[int, float], 'desconto_incondicionado': Union[int, float], 'desconto_condicionado': Union[int, float], 'iss_valor': Union[int, float], 'pis_valor': Union[int, float], 'cofins_valor': Union[int, float], 'inss_valor': Union[int, float], 'ir_valor': Union[int, float], 'csll_valor': Union[int, float], 'cp_valor': Union[int, float]}, total=False)

MonitorDocumentNfseImpostosIbsCbsCbs = TypedDict('MonitorDocumentNfseImpostosIbsCbsCbs', {'valor': Union[int, float], 'aliquota': Union[int, float], 'aliquota_efetiva': Union[int, float], 'aliquota_diferimento': Union[int, float]}, total=False)

MonitorDocumentNfseImpostosIbsCbsIbsEstadual = TypedDict('MonitorDocumentNfseImpostosIbsCbsIbsEstadual', {'valor': Union[int, float], 'aliquota': Union[int, float], 'aliquota_efetiva': Union[int, float], 'aliquota_diferimento': Union[int, float]}, total=False)

MonitorDocumentNfseImpostosIbsCbsIbsMunicipal = TypedDict('MonitorDocumentNfseImpostosIbsCbsIbsMunicipal', {'valor': Union[int, float], 'aliquota': Union[int, float], 'aliquota_efetiva': Union[int, float], 'aliquota_diferimento': Union[int, float]}, total=False)

MonitorDocumentNfseImpostosIbsCbsLocalidadeIncidencia = TypedDict('MonitorDocumentNfseImpostosIbsCbsLocalidadeIncidencia', {'codigo': str, 'descricao': str}, total=False)

MonitorDocumentNfseImpostosIbsCbs = TypedDict('MonitorDocumentNfseImpostosIbsCbs', {'bc': Union[int, float], 'cbs': 'MonitorDocumentNfseImpostosIbsCbsCbs', 'valor_ibs': Union[int, float], 'ibs_estadual': 'MonitorDocumentNfseImpostosIbsCbsIbsEstadual', 'ibs_municipal': 'MonitorDocumentNfseImpostosIbsCbsIbsMunicipal', 'finalidade_nfse': Union[int, float], 'situacao_tributaria': str, 'localidade_incidencia': 'MonitorDocumentNfseImpostosIbsCbsLocalidadeIncidencia', 'cod_indicador_operacao': str, 'indicador_destinatario': Union[int, float], 'classificacao_tributaria': str, 'valor_calculo_reembolso_repasse': Union[int, float]}, total=False)

MonitorDocumentNfseImpostos = TypedDict('MonitorDocumentNfseImpostos', {'tributacao_iss': Union[int, float], 'tributacao_descricao': str, 'iss_retido': Union[int, float], 'bc': Union[int, float], 'iss_aliquota': Union[int, float], 'iss_valor': Union[int, float], 'pis_aliquota': Union[int, float], 'pis_valor': Union[int, float], 'cofins_aliquota': Union[int, float], 'cofins_valor': Union[int, float], 'inss_aliquota': Union[int, float], 'inss_valor': Union[int, float], 'ir_aliquota': Union[int, float], 'ir_valor': Union[int, float], 'csll_aliquota': Union[int, float], 'csll_valor': Union[int, float], 'cp_aliquota': Union[int, float], 'cp_valor': Union[int, float], 'ibs_cbs': 'MonitorDocumentNfseImpostosIbsCbs'}, total=False)

MonitorDocumentNfseIdentificacaoNfseRps = TypedDict('MonitorDocumentNfseIdentificacaoNfseRps', {'serie': str, 'numero': Union[int, float], 'data_emissao': str}, total=False)

MonitorDocumentNfseIdentificacaoNfse = TypedDict('MonitorDocumentNfseIdentificacaoNfse', {'data_competencia': str, 'rps': 'MonitorDocumentNfseIdentificacaoNfseRps', 'codigo_verificacao': str, 'chave': str, 'provedor': str, 'nfse_substituida': Union[None, Union[int, float]]}, total=False)

MonitorDocumentNfseServicosItemLocalPrestacaoVariant1 = TypedDict('MonitorDocumentNfseServicosItemLocalPrestacaoVariant1', {'uf': str, 'cidade': str, 'codigo_municipio': str}, total=False)

MonitorDocumentNfseServicosItemImpostosIbsCbsCbs = TypedDict('MonitorDocumentNfseServicosItemImpostosIbsCbsCbs', {'valor': Union[int, float], 'aliquota': Union[int, float], 'aliquota_efetiva': Union[int, float], 'aliquota_diferimento': Union[int, float]}, total=False)

MonitorDocumentNfseServicosItemImpostosIbsCbsIbsEstadual = TypedDict('MonitorDocumentNfseServicosItemImpostosIbsCbsIbsEstadual', {'valor': Union[int, float], 'aliquota': Union[int, float], 'aliquota_efetiva': Union[int, float], 'aliquota_diferimento': Union[int, float]}, total=False)

MonitorDocumentNfseServicosItemImpostosIbsCbsIbsMunicipal = TypedDict('MonitorDocumentNfseServicosItemImpostosIbsCbsIbsMunicipal', {'valor': Union[int, float], 'aliquota': Union[int, float], 'aliquota_efetiva': Union[int, float], 'aliquota_diferimento': Union[int, float]}, total=False)

MonitorDocumentNfseServicosItemImpostosIbsCbsLocalidadeIncidencia = TypedDict('MonitorDocumentNfseServicosItemImpostosIbsCbsLocalidadeIncidencia', {'codigo': str, 'descricao': str}, total=False)

MonitorDocumentNfseServicosItemImpostosIbsCbs = TypedDict('MonitorDocumentNfseServicosItemImpostosIbsCbs', {'bc': Union[int, float], 'cbs': 'MonitorDocumentNfseServicosItemImpostosIbsCbsCbs', 'valor_ibs': Union[int, float], 'ibs_estadual': 'MonitorDocumentNfseServicosItemImpostosIbsCbsIbsEstadual', 'ibs_municipal': 'MonitorDocumentNfseServicosItemImpostosIbsCbsIbsMunicipal', 'finalidade_nfse': Union[int, float], 'situacao_tributaria': str, 'localidade_incidencia': 'MonitorDocumentNfseServicosItemImpostosIbsCbsLocalidadeIncidencia', 'cod_indicador_operacao': str, 'indicador_destinatario': Union[int, float], 'classificacao_tributaria': str, 'valor_calculo_reembolso_repasse': Union[int, float]}, total=False)

MonitorDocumentNfseServicosItemImpostos = TypedDict('MonitorDocumentNfseServicosItemImpostos', {'tributacao_iss': str, 'tributacao_descricao': str, 'iss_retido': Union[int, float], 'bc': Union[int, float], 'iss_aliquota': Union[int, float], 'iss_valor': Union[int, float], 'pis_aliquota': Union[int, float], 'pis_valor': Union[int, float], 'cofins_aliquota': Union[int, float], 'cofins_valor': Union[int, float], 'inss_aliquota': Union[int, float], 'inss_valor': Union[int, float], 'ir_aliquota': Union[int, float], 'ir_valor': Union[int, float], 'csll_aliquota': Union[int, float], 'csll_valor': Union[int, float], 'cp_aliquota': Union[int, float], 'cp_valor': Union[int, float], 'ibs_cbs': 'MonitorDocumentNfseServicosItemImpostosIbsCbs'}, total=False)

MonitorDocumentNfseServicosItem = TypedDict('MonitorDocumentNfseServicosItem', {'desconto_condicionado': Union[int, float], 'discriminacao': str, 'valor_liquido': Union[int, float], 'codigo_tributacao_municipio': str, 'valor': Union[int, float], 'codigo_cnae': str, 'codigo_servico': str, 'local_prestacao': Union[str, 'MonitorDocumentNfseServicosItemLocalPrestacaoVariant1'], 'impostos': 'MonitorDocumentNfseServicosItemImpostos', 'desconto_incondicionado': Union[int, float], 'valor_recebido': Union[int, float]}, total=False)

MonitorDocumentNfseLocalPrestacaoVariant1 = TypedDict('MonitorDocumentNfseLocalPrestacaoVariant1', {'cidade': str, 'uf': str, 'codigo_municipio': str}, total=False)

MonitorDocumentNfseDocs = TypedDict('MonitorDocumentNfseDocs', {'xml': Union[str, None], 'pdf': Union[str, None]}, total=False)

MonitorDocumentNfseFornecedorVariant0 = TypedDict('MonitorDocumentNfseFornecedorVariant0', {'razao_social': str, 'documento': Union[str, None], 'uf': Union[str, None]}, total=False)

MonitorDocumentNfse = TypedDict('MonitorDocumentNfse', {'status': str, 'discriminacao': str, 'data_emissao': str, 'codigo_tributacao_municipio': str, 'valor': Union[Union[int, float], str], 'codigo_cnae': str, 'totais': 'MonitorDocumentNfseTotais', 'impostos': 'MonitorDocumentNfseImpostos', 'desconto_incondicionado': Union[Union[int, float], str], 'identificacao_nfse': 'MonitorDocumentNfseIdentificacaoNfse', 'valor_recebido': Union[Union[int, float], str], 'tomador': Union['MonitorPerson', None], 'desconto_condicionado': Union[Union[int, float], str], 'valor_liquido': Union[Union[int, float], str], 'servicos': list['MonitorDocumentNfseServicosItem'], 'data_cancelamento': Union[str, None], 'codigo_servico': str, 'local_prestacao': Union[str, 'MonitorDocumentNfseLocalPrestacaoVariant1'], 'empresa_uuid': Required[str], 'prestador': Union['MonitorPerson', None], 'docs': 'MonitorDocumentNfseDocs', 'modelo': Required[Literal['nfse']], 'uuid': Required[str], 'serie': Union[Union[int, float], str], 'categoria': str, 'numero': Union[Union[int, float], str], 'data_captura': str, 'fornecedor': Union['MonitorDocumentNfseFornecedorVariant0', None]}, total=False)

MonitorDocumentMdfeCarregamentoItemDocumentosItem = TypedDict('MonitorDocumentMdfeCarregamentoItemDocumentosItem', {'tipo': str, 'chave': str}, total=False)

MonitorDocumentMdfeCarregamentoItem = TypedDict('MonitorDocumentMdfeCarregamentoItem', {'codigo_municipio': str, 'uf': str, 'cidade': str, 'nome_municipio': str, 'documentos': list['MonitorDocumentMdfeCarregamentoItemDocumentosItem']}, total=False)

MonitorDocumentMdfeSeguroItemResponsavel = TypedDict('MonitorDocumentMdfeSeguroItemResponsavel', {'tipo_responsavel': str, 'cnpj': str, 'cpf': str}, total=False)

MonitorDocumentMdfeSeguroItemSeguradora = TypedDict('MonitorDocumentMdfeSeguroItemSeguradora', {'cnpj': str, 'nome_seguradora': str}, total=False)

MonitorDocumentMdfeSeguroItem = TypedDict('MonitorDocumentMdfeSeguroItem', {'responsavel': 'MonitorDocumentMdfeSeguroItemResponsavel', 'seguradora': 'MonitorDocumentMdfeSeguroItemSeguradora', 'numero_apolice': str, 'numero_averbacao': list[str]}, total=False)

MonitorDocumentMdfePercursoItemVariant0 = TypedDict('MonitorDocumentMdfePercursoItemVariant0', {'uf': str, 'ordem': Union[int, float]}, total=False)

MonitorDocumentMdfeDescarregamentoItemDocumentosFiscaisItem = TypedDict('MonitorDocumentMdfeDescarregamentoItemDocumentosFiscaisItem', {'chave': str}, total=False)

MonitorDocumentMdfeDescarregamentoItemDocumentosItem = TypedDict('MonitorDocumentMdfeDescarregamentoItemDocumentosItem', {'tipo': str, 'chave': str}, total=False)

MonitorDocumentMdfeDescarregamentoItem = TypedDict('MonitorDocumentMdfeDescarregamentoItem', {'codigo_municipio': str, 'documentos_fiscais': list['MonitorDocumentMdfeDescarregamentoItemDocumentosFiscaisItem'], 'uf': str, 'cidade': str, 'nome_municipio': str, 'documentos': list['MonitorDocumentMdfeDescarregamentoItemDocumentosItem']}, total=False)

MonitorDocumentMdfeFerroviarioTrem = TypedDict('MonitorDocumentMdfeFerroviarioTrem', {'prefixo': str, 'data_liberacao': str, 'origem': str, 'destino': str}, total=False)

MonitorDocumentMdfeFerroviarioVagoesItem = TypedDict('MonitorDocumentMdfeFerroviarioVagoesItem', {'peso_bc': str, 'peso_real': str, 'tipo_vagao': str, 'serie': str, 'numero': str, 'sequencia_vagao': str, 'tonelada_util': str}, total=False)

MonitorDocumentMdfeFerroviario = TypedDict('MonitorDocumentMdfeFerroviario', {'trem': 'MonitorDocumentMdfeFerroviarioTrem', 'vagoes': list['MonitorDocumentMdfeFerroviarioVagoesItem']}, total=False)

MonitorDocumentMdfeProdutoPredominanteLotacaoCarregamento = TypedDict('MonitorDocumentMdfeProdutoPredominanteLotacaoCarregamento', {'cep': str, 'latitude': str, 'longitude': str}, total=False)

MonitorDocumentMdfeProdutoPredominanteLotacaoDescarregamento = TypedDict('MonitorDocumentMdfeProdutoPredominanteLotacaoDescarregamento', {'cep': str, 'latitude': str, 'longitude': str}, total=False)

MonitorDocumentMdfeProdutoPredominanteLotacao = TypedDict('MonitorDocumentMdfeProdutoPredominanteLotacao', {'carregamento': 'MonitorDocumentMdfeProdutoPredominanteLotacaoCarregamento', 'descarregamento': 'MonitorDocumentMdfeProdutoPredominanteLotacaoDescarregamento'}, total=False)

MonitorDocumentMdfeProdutoPredominante = TypedDict('MonitorDocumentMdfeProdutoPredominante', {'tipo_carga': str, 'nome': str, 'gtin': str, 'ncm': str, 'lotacao': 'MonitorDocumentMdfeProdutoPredominanteLotacao'}, total=False)

MonitorDocumentMdfeAquaviarioTerminalCarregamentoItem = TypedDict('MonitorDocumentMdfeAquaviarioTerminalCarregamentoItem', {'codigo': str, 'nome': str}, total=False)

MonitorDocumentMdfeAquaviarioTerminalDescarregamentoItem = TypedDict('MonitorDocumentMdfeAquaviarioTerminalDescarregamentoItem', {'codigo': str, 'nome': str}, total=False)

MonitorDocumentMdfeAquaviarioEmbarcacaoComboioItem = TypedDict('MonitorDocumentMdfeAquaviarioEmbarcacaoComboioItem', {'codigo': str, 'identificador_balsa': str}, total=False)

MonitorDocumentMdfeAquaviarioCargaVaziaItem = TypedDict('MonitorDocumentMdfeAquaviarioCargaVaziaItem', {'identificador': str, 'tipo_unidade': Union[int, float]}, total=False)

MonitorDocumentMdfeAquaviarioTransporteVazioItem = TypedDict('MonitorDocumentMdfeAquaviarioTransporteVazioItem', {'identificador': str, 'tipo_unidade': Union[int, float]}, total=False)

MonitorDocumentMdfeAquaviario = TypedDict('MonitorDocumentMdfeAquaviario', {'irin': str, 'tipo_embarcacao': str, 'codigo_embarcacao': str, 'nome_embarcacao': str, 'numero_viagem': str, 'codigo_porto_embarque': str, 'codigo_porto_destino': str, 'porto_transbordo': str, 'tipo_navegacao': str, 'terminal_carregamento': list['MonitorDocumentMdfeAquaviarioTerminalCarregamentoItem'], 'terminal_descarregamento': list['MonitorDocumentMdfeAquaviarioTerminalDescarregamentoItem'], 'embarcacao_comboio': list['MonitorDocumentMdfeAquaviarioEmbarcacaoComboioItem'], 'carga_vazia': list['MonitorDocumentMdfeAquaviarioCargaVaziaItem'], 'transporte_vazio': list['MonitorDocumentMdfeAquaviarioTransporteVazioItem']}, total=False)

MonitorDocumentMdfeRodoviarioContratantesItem = TypedDict('MonitorDocumentMdfeRodoviarioContratantesItem', {'cnpj': str, 'razao_social': str}, total=False)

MonitorDocumentMdfeRodoviarioVeiculoReboqueItemProprietario = TypedDict('MonitorDocumentMdfeRodoviarioVeiculoReboqueItemProprietario', {'cnpj': str, 'cpf': str, 'razao_social': str, 'nome_completo': str, 'ie': str, 'rntrc': str, 'uf': str, 'tipo_proprietario': Union[int, float]}, total=False)

MonitorDocumentMdfeRodoviarioVeiculoReboqueItem = TypedDict('MonitorDocumentMdfeRodoviarioVeiculoReboqueItem', {'codigo_interno': str, 'placa': str, 'renavam': str, 'tara': str, 'capacidade_kg': str, 'capacidade_m3': str, 'tipo_carroceria': str, 'uf_licenciamento': str, 'proprietario': 'MonitorDocumentMdfeRodoviarioVeiculoReboqueItemProprietario'}, total=False)

MonitorDocumentMdfeRodoviarioLacresItem = TypedDict('MonitorDocumentMdfeRodoviarioLacresItem', {'numero': str}, total=False)

MonitorDocumentMdfeRodoviarioVeiculosItemCondutor = TypedDict('MonitorDocumentMdfeRodoviarioVeiculosItemCondutor', {'cpf': str, 'nome': str}, total=False)

MonitorDocumentMdfeRodoviarioVeiculosItem = TypedDict('MonitorDocumentMdfeRodoviarioVeiculosItem', {'tara': Union[int, float], 'uf': str, 'capacidade_kg': Union[int, float], 'codigo_interno': str, 'placa': str, 'tipo_rodado': str, 'condutor': 'MonitorDocumentMdfeRodoviarioVeiculosItemCondutor', 'capacidade_m3': Union[int, float], 'tipo_carroceria': str, 'renavam': str}, total=False)

MonitorDocumentMdfeRodoviarioCiotItem = TypedDict('MonitorDocumentMdfeRodoviarioCiotItem', {'cnpj_responsavel': str, 'cpf_responsavel': str, 'numero': str, 'cpf_cnpj': str, 'codigo_ciot': str}, total=False)

MonitorDocumentMdfeRodoviarioContratanteItem = TypedDict('MonitorDocumentMdfeRodoviarioContratanteItem', {'cnpj': str, 'cpf': str}, total=False)

MonitorDocumentMdfeRodoviarioCondutorItem = TypedDict('MonitorDocumentMdfeRodoviarioCondutorItem', {'cpf': str, 'nome': str}, total=False)

MonitorDocumentMdfeRodoviarioVeiculoTracaoProprietario = TypedDict('MonitorDocumentMdfeRodoviarioVeiculoTracaoProprietario', {'cnpj': str, 'cpf': str, 'razao_social': str, 'nome_completo': str, 'ie': str, 'rntrc': str, 'uf': str, 'tipo_proprietario': Union[int, float]}, total=False)

MonitorDocumentMdfeRodoviarioVeiculoTracao = TypedDict('MonitorDocumentMdfeRodoviarioVeiculoTracao', {'codigo_interno': str, 'placa': str, 'renavam': str, 'tara': str, 'capacidade_kg': str, 'capacidade_m3': str, 'tipo_rodado': str, 'tipo_carroceria': str, 'uf_licenciamento': str, 'proprietario': 'MonitorDocumentMdfeRodoviarioVeiculoTracaoProprietario'}, total=False)

MonitorDocumentMdfeRodoviarioValePedagioVariant0 = TypedDict('MonitorDocumentMdfeRodoviarioValePedagioVariant0', {'cnpj_fornecedor': str, 'cnpj_responsavel': str, 'numero_comprovante': str, 'valor': Union[int, float]}, total=False)

MonitorDocumentMdfeRodoviarioValePedagioVariant1Item = TypedDict('MonitorDocumentMdfeRodoviarioValePedagioVariant1Item', {'cnpj_fornecedor': str, 'cnpj_responsavel': str, 'cpf_responsavel': str, 'valor': str, 'comprovante': str}, total=False)

MonitorDocumentMdfeRodoviario = TypedDict('MonitorDocumentMdfeRodoviario', {'contratantes': list['MonitorDocumentMdfeRodoviarioContratantesItem'], 'veiculo_reboque': list['MonitorDocumentMdfeRodoviarioVeiculoReboqueItem'], 'lacres': list['MonitorDocumentMdfeRodoviarioLacresItem'], 'veiculos': list['MonitorDocumentMdfeRodoviarioVeiculosItem'], 'ciot': list['MonitorDocumentMdfeRodoviarioCiotItem'], 'contratante': list['MonitorDocumentMdfeRodoviarioContratanteItem'], 'condutor': list['MonitorDocumentMdfeRodoviarioCondutorItem'], 'rntrc': str, 'veiculo_tracao': 'MonitorDocumentMdfeRodoviarioVeiculoTracao', 'vale_pedagio': Union['MonitorDocumentMdfeRodoviarioValePedagioVariant0', list['MonitorDocumentMdfeRodoviarioValePedagioVariant1Item']]}, total=False)

MonitorDocumentMdfeDocs = TypedDict('MonitorDocumentMdfeDocs', {'xml': Union[str, None], 'pdf': Union[str, None]}, total=False)

MonitorDocumentMdfeAereo = TypedDict('MonitorDocumentMdfeAereo', {'nacionalidade_aeronave': str, 'matricula_aeronave': str, 'numero_voo': str, 'aerodromo_embarque': str, 'aerodromo_destino': str, 'data_voo': str}, total=False)

MonitorDocumentMdfeFornecedorVariant0 = TypedDict('MonitorDocumentMdfeFornecedorVariant0', {'razao_social': str, 'documento': Union[str, None], 'uf': Union[str, None]}, total=False)

MonitorDocumentMdfe = TypedDict('MonitorDocumentMdfe', {'status': str, 'data_emissao': str, 'uf_carregamento': str, 'carregamento': list['MonitorDocumentMdfeCarregamentoItem'], 'valor': Union[Union[int, float], str], 'seguro': list['MonitorDocumentMdfeSeguroItem'], 'quantidade_mdfe': Union[int, float], 'percurso': list[Union['MonitorDocumentMdfePercursoItemVariant0', str]], 'quantidade_nfe': Union[int, float], 'descarregamento': list['MonitorDocumentMdfeDescarregamentoItem'], 'ferroviario': 'MonitorDocumentMdfeFerroviario', 'produto_predominante': 'MonitorDocumentMdfeProdutoPredominante', 'aquaviario': 'MonitorDocumentMdfeAquaviario', 'modalidade': Union[int, float], 'rodoviario': 'MonitorDocumentMdfeRodoviario', 'emitente': Union['MonitorPerson', None], 'chave': str, 'peso_bruto': Union[int, float], 'empresa_uuid': Required[str], 'docs': 'MonitorDocumentMdfeDocs', 'modelo': Required[Literal['mdfe']], 'uuid': Required[str], 'serie': Union[Union[int, float], str], 'categoria': str, 'numero': Union[Union[int, float], str], 'uf_descarregamento': str, 'aereo': 'MonitorDocumentMdfeAereo', 'quantidade_cte': Union[int, float], 'data_captura': str, 'fornecedor': Union['MonitorDocumentMdfeFornecedorVariant0', None]}, total=False)

MonitorDocumentCteDocumentosFiscaisItem = TypedDict('MonitorDocumentCteDocumentosFiscaisItem', {'tipo': int, 'chave': str, 'pin': str, 'previsao_entrega': str, 'modelo': str, 'numero': Union[str, Union[int, float]], 'serie': Union[str, Union[int, float]], 'data_emissao': str, 'valor_total': Union[Union[int, float], str], 'cfop': str, 'descricao': str}, total=False)

MonitorDocumentCteServicoDocumentosOriginariosItem = TypedDict('MonitorDocumentCteServicoDocumentosOriginariosItem', {'tipo': str, 'chave': str, 'serie': str, 'numero': str, 'data_emissao': str}, total=False)

MonitorDocumentCteServicoComponentesValorItem = TypedDict('MonitorDocumentCteServicoComponentesValorItem', {'nome': str, 'valor': Union[int, float]}, total=False)

MonitorDocumentCteServicoInformacoesCargaCubagem = TypedDict('MonitorDocumentCteServicoInformacoesCargaCubagem', {'quantidade': Union[int, float], 'unidade': str}, total=False)

MonitorDocumentCteServicoInformacoesCarga = TypedDict('MonitorDocumentCteServicoInformacoesCarga', {'valor_total': Union[int, float], 'produto_predominante': str, 'outras_caracteristicas': str, 'cubagem': 'MonitorDocumentCteServicoInformacoesCargaCubagem'}, total=False)

MonitorDocumentCteServico = TypedDict('MonitorDocumentCteServico', {'descricao': str, 'unidade_medida': str, 'tipo': Union[int, float], 'valor_total': Union[int, float], 'documentos_originarios': list['MonitorDocumentCteServicoDocumentosOriginariosItem'], 'componentes_valor': list['MonitorDocumentCteServicoComponentesValorItem'], 'quantidade_carga': Union[int, float], 'modal': str, 'tipo_servico': Union[int, float], 'informacoes_carga': 'MonitorDocumentCteServicoInformacoesCarga', 'valor_recebido': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsIbsEstadual = TypedDict('MonitorDocumentCteImpostosIbsCbsIbsEstadual', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsIbsMunicipal = TypedDict('MonitorDocumentCteImpostosIbsCbsIbsMunicipal', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsCbs = TypedDict('MonitorDocumentCteImpostosIbsCbsCbs', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsEstadual = TypedDict('MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsEstadual', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsMunicipal = TypedDict('MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsMunicipal', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsTributacaoRegularCbs = TypedDict('MonitorDocumentCteImpostosIbsCbsTributacaoRegularCbs', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsTributacaoRegular = TypedDict('MonitorDocumentCteImpostosIbsCbsTributacaoRegular', {'ibs_estadual': 'MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsEstadual', 'ibs_municipal': 'MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsMunicipal', 'cbs': 'MonitorDocumentCteImpostosIbsCbsTributacaoRegularCbs'}, total=False)

MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsEstadual = TypedDict('MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsEstadual', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsMunicipal = TypedDict('MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsMunicipal', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsCompraGovernamentalCbs = TypedDict('MonitorDocumentCteImpostosIbsCbsCompraGovernamentalCbs', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsCompraGovernamental = TypedDict('MonitorDocumentCteImpostosIbsCbsCompraGovernamental', {'ibs_estadual': 'MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsEstadual', 'ibs_municipal': 'MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsMunicipal', 'cbs': 'MonitorDocumentCteImpostosIbsCbsCompraGovernamentalCbs'}, total=False)

MonitorDocumentCteImpostosIbsCbsCreditoPresumido = TypedDict('MonitorDocumentCteImpostosIbsCbsCreditoPresumido', {'classificacao': str, 'aliquota_ibs': Union[int, float], 'valor_ibs': Union[int, float], 'valor_ibs_condicionado_suspensao': Union[int, float], 'aliquota_cbs': Union[int, float], 'valor_cbs': Union[int, float], 'valor_cbs_condicionado_suspensao': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbsEstornoCredito = TypedDict('MonitorDocumentCteImpostosIbsCbsEstornoCredito', {'valor_ibs': Union[int, float], 'valor_cbs': Union[int, float]}, total=False)

MonitorDocumentCteImpostosIbsCbs = TypedDict('MonitorDocumentCteImpostosIbsCbs', {'situacao_tributaria': str, 'classificacao_tributaria': str, 'indicador_doacao': bool, 'bc': Union[int, float], 'valor_ibs': Union[int, float], 'ibs_estadual': 'MonitorDocumentCteImpostosIbsCbsIbsEstadual', 'ibs_municipal': 'MonitorDocumentCteImpostosIbsCbsIbsMunicipal', 'cbs': 'MonitorDocumentCteImpostosIbsCbsCbs', 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'tributacao_regular': 'MonitorDocumentCteImpostosIbsCbsTributacaoRegular', 'compra_governamental': 'MonitorDocumentCteImpostosIbsCbsCompraGovernamental', 'credito_presumido': 'MonitorDocumentCteImpostosIbsCbsCreditoPresumido', 'estorno_credito': 'MonitorDocumentCteImpostosIbsCbsEstornoCredito'}, total=False)

MonitorDocumentCteImpostosIcms = TypedDict('MonitorDocumentCteImpostosIcms', {'situacao_tributaria': str, 'valor': Union[int, float], 'valor_credito': Union[int, float], 'percentual_credito': Union[int, float], 'aliquota': Union[int, float], 'percentual_reducao': Union[int, float], 'codigo_cfop': str, 'bc': Union[int, float]}, total=False)

MonitorDocumentCteImpostos = TypedDict('MonitorDocumentCteImpostos', {'ibs_cbs': 'MonitorDocumentCteImpostosIbsCbs', 'icms': 'MonitorDocumentCteImpostosIcms'}, total=False)

MonitorDocumentCteDocs = TypedDict('MonitorDocumentCteDocs', {'xml': Union[str, None], 'pdf': Union[str, None]}, total=False)

MonitorDocumentCteFornecedorVariant0 = TypedDict('MonitorDocumentCteFornecedorVariant0', {'razao_social': str, 'documento': Union[str, None], 'uf': Union[str, None]}, total=False)

MonitorDocumentCte = TypedDict('MonitorDocumentCte', {'status': str, 'cfop': list[str], 'data_emissao': str, 'documentos_fiscais': list['MonitorDocumentCteDocumentosFiscaisItem'], 'servico': 'MonitorDocumentCteServico', 'remetente': Union['MonitorPerson', None], 'valor': Union[Union[int, float], str], 'finalidade': Union[int, float], 'impostos': 'MonitorDocumentCteImpostos', 'expedidor': Union['MonitorPerson', None], 'natureza_operacao': str, 'uf_termino_prestacao': str, 'uf_inicio_prestacao': str, 'tomador': Union['MonitorPerson', None], 'recebedor': Union['MonitorPerson', None], 'modalidade': Union[int, float], 'emitente': Union['MonitorPerson', None], 'indicador_tomador': Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4'], 'destinatario': Union['MonitorPerson', None], 'chave': str, 'empresa_uuid': Required[str], 'docs': 'MonitorDocumentCteDocs', 'modelo': Required[Literal['cte']], 'uuid': Required[str], 'serie': Union[Union[int, float], str], 'categoria': str, 'numero': Union[Union[int, float], str], 'data_captura': str, 'fornecedor': Union['MonitorDocumentCteFornecedorVariant0', None], 'relacao_empresa': str}, total=False)

MonitorDocumentCteOsDocumentosFiscaisItem = TypedDict('MonitorDocumentCteOsDocumentosFiscaisItem', {'tipo': int, 'chave': str, 'pin': str, 'previsao_entrega': str, 'modelo': str, 'numero': Union[str, Union[int, float]], 'serie': Union[str, Union[int, float]], 'data_emissao': str, 'valor_total': Union[Union[int, float], str], 'cfop': str, 'descricao': str}, total=False)

MonitorDocumentCteOsServicoDocumentosOriginariosItem = TypedDict('MonitorDocumentCteOsServicoDocumentosOriginariosItem', {'tipo': str, 'chave': str, 'serie': str, 'numero': str, 'data_emissao': str}, total=False)

MonitorDocumentCteOsServicoComponentesValorItem = TypedDict('MonitorDocumentCteOsServicoComponentesValorItem', {'nome': str, 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsServicoInformacoesCargaCubagem = TypedDict('MonitorDocumentCteOsServicoInformacoesCargaCubagem', {'quantidade': Union[int, float], 'unidade': str}, total=False)

MonitorDocumentCteOsServicoInformacoesCarga = TypedDict('MonitorDocumentCteOsServicoInformacoesCarga', {'valor_total': Union[int, float], 'produto_predominante': str, 'outras_caracteristicas': str, 'cubagem': 'MonitorDocumentCteOsServicoInformacoesCargaCubagem'}, total=False)

MonitorDocumentCteOsServico = TypedDict('MonitorDocumentCteOsServico', {'descricao': str, 'unidade_medida': str, 'tipo': Union[int, float], 'valor_total': Union[int, float], 'documentos_originarios': list['MonitorDocumentCteOsServicoDocumentosOriginariosItem'], 'componentes_valor': list['MonitorDocumentCteOsServicoComponentesValorItem'], 'quantidade_carga': Union[int, float], 'modal': str, 'tipo_servico': Union[int, float], 'informacoes_carga': 'MonitorDocumentCteOsServicoInformacoesCarga', 'valor_recebido': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsIbsEstadual = TypedDict('MonitorDocumentCteOsImpostosIbsCbsIbsEstadual', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsIbsMunicipal = TypedDict('MonitorDocumentCteOsImpostosIbsCbsIbsMunicipal', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsCbs = TypedDict('MonitorDocumentCteOsImpostosIbsCbsCbs', {'aliquota': Union[int, float], 'valor': Union[int, float], 'aliquota_diferimento': Union[int, float], 'valor_diferimento': Union[int, float], 'valor_devolvido': Union[int, float], 'aliquota_reducao': Union[int, float], 'aliquota_efetiva': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsEstadual = TypedDict('MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsEstadual', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsMunicipal = TypedDict('MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsMunicipal', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularCbs = TypedDict('MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularCbs', {'aliquota_efetiva': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsTributacaoRegular = TypedDict('MonitorDocumentCteOsImpostosIbsCbsTributacaoRegular', {'ibs_estadual': 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsEstadual', 'ibs_municipal': 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsMunicipal', 'cbs': 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularCbs'}, total=False)

MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsEstadual = TypedDict('MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsEstadual', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsMunicipal = TypedDict('MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsMunicipal', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalCbs = TypedDict('MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalCbs', {'aliquota': Union[int, float], 'valor': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsCompraGovernamental = TypedDict('MonitorDocumentCteOsImpostosIbsCbsCompraGovernamental', {'ibs_estadual': 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsEstadual', 'ibs_municipal': 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsMunicipal', 'cbs': 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalCbs'}, total=False)

MonitorDocumentCteOsImpostosIbsCbsCreditoPresumido = TypedDict('MonitorDocumentCteOsImpostosIbsCbsCreditoPresumido', {'classificacao': str, 'aliquota_ibs': Union[int, float], 'valor_ibs': Union[int, float], 'valor_ibs_condicionado_suspensao': Union[int, float], 'aliquota_cbs': Union[int, float], 'valor_cbs': Union[int, float], 'valor_cbs_condicionado_suspensao': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbsEstornoCredito = TypedDict('MonitorDocumentCteOsImpostosIbsCbsEstornoCredito', {'valor_ibs': Union[int, float], 'valor_cbs': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostosIbsCbs = TypedDict('MonitorDocumentCteOsImpostosIbsCbs', {'situacao_tributaria': str, 'classificacao_tributaria': str, 'indicador_doacao': bool, 'bc': Union[int, float], 'valor_ibs': Union[int, float], 'ibs_estadual': 'MonitorDocumentCteOsImpostosIbsCbsIbsEstadual', 'ibs_municipal': 'MonitorDocumentCteOsImpostosIbsCbsIbsMunicipal', 'cbs': 'MonitorDocumentCteOsImpostosIbsCbsCbs', 'situacao_tributaria_regular': str, 'classificacao_tributaria_regular': str, 'tributacao_regular': 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegular', 'compra_governamental': 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamental', 'credito_presumido': 'MonitorDocumentCteOsImpostosIbsCbsCreditoPresumido', 'estorno_credito': 'MonitorDocumentCteOsImpostosIbsCbsEstornoCredito'}, total=False)

MonitorDocumentCteOsImpostosIcms = TypedDict('MonitorDocumentCteOsImpostosIcms', {'situacao_tributaria': str, 'valor': Union[int, float], 'valor_credito': Union[int, float], 'percentual_credito': Union[int, float], 'aliquota': Union[int, float], 'percentual_reducao': Union[int, float], 'codigo_cfop': str, 'bc': Union[int, float]}, total=False)

MonitorDocumentCteOsImpostos = TypedDict('MonitorDocumentCteOsImpostos', {'ibs_cbs': 'MonitorDocumentCteOsImpostosIbsCbs', 'icms': 'MonitorDocumentCteOsImpostosIcms'}, total=False)

MonitorDocumentCteOsDocs = TypedDict('MonitorDocumentCteOsDocs', {'xml': Union[str, None], 'pdf': Union[str, None]}, total=False)

MonitorDocumentCteOsFornecedorVariant0 = TypedDict('MonitorDocumentCteOsFornecedorVariant0', {'razao_social': str, 'documento': Union[str, None], 'uf': Union[str, None]}, total=False)

MonitorDocumentCteOs = TypedDict('MonitorDocumentCteOs', {'status': str, 'cfop': list[str], 'data_emissao': str, 'documentos_fiscais': list['MonitorDocumentCteOsDocumentosFiscaisItem'], 'servico': 'MonitorDocumentCteOsServico', 'valor': Union[Union[int, float], str], 'finalidade': Union[int, float], 'impostos': 'MonitorDocumentCteOsImpostos', 'natureza_operacao': str, 'uf_termino_prestacao': str, 'uf_inicio_prestacao': str, 'tomador': Union['MonitorPerson', None], 'modalidade': Union[int, float], 'emitente': Union['MonitorPerson', None], 'indicador_tomador': Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4'], 'chave': str, 'empresa_uuid': Required[str], 'docs': 'MonitorDocumentCteOsDocs', 'modelo': Required[Literal['cte_os']], 'uuid': Required[str], 'serie': Union[Union[int, float], str], 'categoria': str, 'numero': Union[Union[int, float], str], 'data_captura': str, 'fornecedor': Union['MonitorDocumentCteOsFornecedorVariant0', None], 'relacao_empresa': str}, total=False)

MonitorDocument: TypeAlias = Union['MonitorDocumentNfe', 'MonitorDocumentNfse', 'MonitorDocumentMdfe', 'MonitorDocumentCte', 'MonitorDocumentCteOs']

MonitorCursorPagination = TypedDict('MonitorCursorPagination', {'per_page': Required[int], 'next_cursor': Required[Union[str, None]], 'prev_cursor': Required[Union[str, None]]}, total=False)

MonitorDocumentPage = TypedDict('MonitorDocumentPage', {'data': Required[list['MonitorDocument']], 'meta': Required[Union['MonitorPagination', 'MonitorCursorPagination']]}, total=False)

MonitorReportFiltrosPeriodo = TypedDict('MonitorReportFiltrosPeriodo', {'de': str, 'ate': str}, total=False)

MonitorReportFiltros = TypedDict('MonitorReportFiltros', {'selecao_manual': int, 'periodo': 'MonitorReportFiltrosPeriodo', 'empresas': int, 'categoria': list[str], 'finalidade': list[str], 'operacao': list[str], 'modalidade': list[str], 'status': list[str], 'manifestacao': list[str]}, total=False)

MonitorReport = TypedDict('MonitorReport', {'uuid': Required[str], 'relatorio': Required[Literal['xml', 'csv', 'excel', 'pdf']], 'modelo': Required[str], 'status': Required[str], 'processado': int, 'total': int, 'criado_em': str, 'atualizado_em': str, 'filtros': 'MonitorReportFiltros', 'url': str, 'expira_em': str}, total=False)

MonitorReportPage = TypedDict('MonitorReportPage', {'data': Required[list['MonitorReport']], 'meta': Required['MonitorPagination']}, total=False)

MonitorSearchRequestFiltros = TypedDict('MonitorSearchRequestFiltros', {'ambiente': Literal[1, 2, '1', '2'], 'empresa_uuid': Union[str, list[str]], 'categoria': Union[Literal['emitidas', 'recebidas', 'transportadas', 'citadas', 'transportes_contratados', 'proprietario_veiculos'], list[Literal['emitidas', 'recebidas', 'transportadas', 'citadas', 'transportes_contratados', 'proprietario_veiculos']]], 'data_inicial': str, 'data_final': str, 'status': Union[Literal['aprovado', 'cancelado', 'encerrado', 'pendente'], list[Literal['aprovado', 'cancelado', 'encerrado', 'pendente']]], 'manifestacao': Union[Literal['pendente', 'confirmada', 'ciencia', 'desconhecida', 'nao-realizada'], list[Literal['pendente', 'confirmada', 'ciencia', 'desconhecida', 'nao-realizada']]], 'chave': str, 'numero': Union[Union[int, float], str], 'serie': Union[Union[int, float], str], 'valor': Union[Union[int, float], str], 'codigo_verificacao': str, 'fornecedor': str, 'pesquisa': str, 'relatorio': Literal['xml', 'csv', 'excel', 'pdf'], 'url_notificacao': str, 'per_page': int, 'novos_documentos': bool}, total=False)

MonitorSearchRequestFiltrosModelo = TypedDict('MonitorSearchRequestFiltrosModelo', {'finalidade': Union[Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4'], list[Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4']]], 'operacao': Union[Literal[0, 1, '0', '1'], list[Literal[0, 1, '0', '1']]], 'ncm': str, 'cfop': str, 'codigo_verificacao': str, 'serie_rps': str, 'numero_rps': Union[Union[int, float], str], 'codigo_cnae': str, 'codigo_servico': str, 'modalidade': Union[Literal[1, 2, 3, 4, 5, 6, '1', '2', '3', '4', '5', '6'], list[Literal[1, 2, 3, 4, 5, 6, '1', '2', '3', '4', '5', '6']]], 'uf_carregamento': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'uf_descarregamento': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'placa_veiculo': str, 'uf_inicio_prestacao': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'uf_termino_prestacao': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']}, total=False)

MonitorSearchRequest = TypedDict('MonitorSearchRequest', {'modelo': Literal['nfe', 'nfse', 'mdfe', 'cte', 'cte_os'], 'ambiente': Literal[1, 2, '1', '2'], 'empresa_uuid': Union[str, list[str]], 'categoria': Union[Literal['emitidas', 'recebidas', 'transportadas', 'citadas', 'transportes_contratados', 'proprietario_veiculos'], list[Literal['emitidas', 'recebidas', 'transportadas', 'citadas', 'transportes_contratados', 'proprietario_veiculos']]], 'data_inicial': str, 'data_final': str, 'status': Union[Literal['aprovado', 'cancelado', 'encerrado', 'pendente'], list[Literal['aprovado', 'cancelado', 'encerrado', 'pendente']]], 'manifestacao': Union[Literal['pendente', 'confirmada', 'ciencia', 'desconhecida', 'nao-realizada'], list[Literal['pendente', 'confirmada', 'ciencia', 'desconhecida', 'nao-realizada']]], 'chave': str, 'numero': Union[Union[int, float], str], 'serie': Union[Union[int, float], str], 'valor': Union[Union[int, float], str], 'codigo_verificacao': str, 'fornecedor': str, 'pesquisa': str, 'finalidade': Union[Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4'], list[Literal[0, 1, 2, 3, 4, '0', '1', '2', '3', '4']]], 'operacao': Union[Literal[0, 1, '0', '1'], list[Literal[0, 1, '0', '1']]], 'ncm': str, 'cfop': str, 'serie_rps': str, 'numero_rps': Union[Union[int, float], str], 'codigo_cnae': str, 'codigo_servico': str, 'modalidade': Union[Literal[1, 2, 3, 4, 5, 6, '1', '2', '3', '4', '5', '6'], list[Literal[1, 2, 3, 4, 5, 6, '1', '2', '3', '4', '5', '6']]], 'uf_carregamento': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'uf_descarregamento': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'placa_veiculo': str, 'uf_inicio_prestacao': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'uf_termino_prestacao': Literal['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], 'relatorio': Literal['xml', 'csv', 'excel', 'pdf'], 'documentos': list[str], 'url_notificacao': str, 'per_page': int, 'page': int, 'cursor': str, 'paginacao': Literal['offset', 'cursor'], 'ordenar_por': Literal['data_emissao', 'numero', 'valor'], 'ordem': Literal['asc', 'desc'], 'novos_documentos': bool, 'filtros': 'MonitorSearchRequestFiltros', 'filtros_modelo': 'MonitorSearchRequestFiltrosModelo'}, total=False)

MonitorEventAlteracoesItem = TypedDict('MonitorEventAlteracoesItem', {'grupo': str, 'campo': str, 'alteracao': str}, total=False)

MonitorEventMdfe = TypedDict('MonitorEventMdfe', {'protocolo': str, 'data_emissao': str, 'modalidade': Union[int, float], 'chave': str}, total=False)

MonitorEventLog = TypedDict('MonitorEventLog', {'nProt': str, 'dhRegEvento': str, 'cStat': str, 'xEvento': str, 'xMotivo': str, 'tpEvento': str}, total=False)

MonitorEvent = TypedDict('MonitorEvent', {'uuid': Required[str], 'documento_uuid': Required[str], 'protocolo': str, 'registrado_em': Required[str], 'data_captura': str, 'descricao_evento': str, 'cnpj_autor': str, 'cpf_autor': str, 'justificativa': str, 'correcao': str, 'chave_cte': str, 'protocolo_cte': str, 'data_entrega': str, 'documento_recebedor': str, 'nome_recebedor': str, 'data_encerramento': str, 'cidade_encerramento': str, 'uf_encerramento': str, 'tipo_evento': Required[Union[int, float]], 'resumo': Required[bool], 'alteracoes': list['MonitorEventAlteracoesItem'], 'latitude': Union[int, float], 'longitude': Union[int, float], 'chaves_nfe': list[str], 'mdfe': 'MonitorEventMdfe', 'log': 'MonitorEventLog', 'chave_substituta': str, 'cpf_condutor': str, 'nome_condutor': str}, total=False)

MonitorManifestationRequest = TypedDict('MonitorManifestationRequest', {'evento': Required[Literal[1, '1']], 'manifestacao': Required[Literal[1, 2, 3, 4, '1', '2', '3', '4']], 'justificativa': str}, total=False)

MonitorImportRequestVariant0 = TypedDict('MonitorImportRequestVariant0', {'empresa_uuid': Required[str], 'chave': Required[str], 'xml': str, 'url_arquivo_zip': str}, total=False)

MonitorImportRequestVariant1 = TypedDict('MonitorImportRequestVariant1', {'empresa_uuid': Required[str], 'chave': str, 'xml': Required[str], 'url_arquivo_zip': str}, total=False)

MonitorImportRequestVariant2 = TypedDict('MonitorImportRequestVariant2', {'empresa_uuid': Required[str], 'chave': str, 'xml': str, 'url_arquivo_zip': Required[str]}, total=False)

MonitorImportRequest: TypeAlias = Union['MonitorImportRequestVariant0', 'MonitorImportRequestVariant1', 'MonitorImportRequestVariant2']

MonitorImportStatusImportadosItem = TypedDict('MonitorImportStatusImportadosItem', {'arquivo': Required[str], 'uuid': Required[str]}, total=False)

MonitorImportStatusDescartadosItem = TypedDict('MonitorImportStatusDescartadosItem', {'arquivo': Required[str], 'motivo': Required[str]}, total=False)

MonitorImportStatus = TypedDict('MonitorImportStatus', {'uuid': Required[str], 'empresa_uuid': str, 'status': Required[str], 'processado': Required[int], 'total': int, 'importados': Required[list['MonitorImportStatusImportadosItem']], 'descartados': Required[list['MonitorImportStatusDescartadosItem']], 'erro': str}, total=False)

monitorSearchDocumentsQuery = TypedDict('monitorSearchDocumentsQuery', {'page': int, 'per_page': int}, total=False)

monitorSearchDocumentsResponse: TypeAlias = Union[Union['MonitorDocumentPage', 'MonitorReport']]

monitorGetDocumentQuery = TypedDict('monitorGetDocumentQuery', {'atualizar_status': Literal[0, 1, '0', '1']}, total=False)

monitorGetDocumentResponse: TypeAlias = Union['MonitorDocument']

monitorGetDocumentFdParameter: TypeAlias = str

monitorListDocumentEventsResponseVariant0 = TypedDict('monitorListDocumentEventsResponseVariant0', {'data': Required[list['MonitorEvent']]}, total=False)

monitorListDocumentEventsResponse: TypeAlias = Union['monitorListDocumentEventsResponseVariant0']

monitorListDocumentEventsFdParameter: TypeAlias = str

monitorManifestDocumentResponse: TypeAlias = Union['MonitorEvent']

monitorManifestDocumentFdParameter: TypeAlias = str

monitorListReportsQuery = TypedDict('monitorListReportsQuery', {'status': str, 'page': int, 'per_page': int}, total=False)

monitorListReportsResponse: TypeAlias = Union['MonitorReportPage']

monitorDownloadReportReportParameter: TypeAlias = str

monitorImportDocumentResponse: TypeAlias = Union[Union['MonitorDocument', 'MonitorImportStatus']]

monitorGetImportStatusResponse: TypeAlias = Union['MonitorImportStatus']

monitorGetImportStatusUuidParameter: TypeAlias = str

_bind_types(globals(), __name__, ['MonitorError', 'MonitorPagination', 'MonitorAddress', 'MonitorCompany', 'MonitorMunicipalityRegistration', 'MonitorAvailableMunicipality', 'MonitorDownloadStatisticsEmpresasItem', 'MonitorDownloadStatistics', 'MonitorCompanyPage', 'MonitorMunicipalityPage', 'MonitorAvailableMunicipalities', 'MonitorPerson', 'MonitorManifestationStateVariant0', 'MonitorManifestationState', 'MonitorDocumentNfeTotaisIssqn', 'MonitorDocumentNfeProdutosItemImpostosImpostoImportacao', 'MonitorDocumentNfeProdutosItemImpostosIpi', 'MonitorDocumentNfeProdutosItemImpostosCofins', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsEstadual', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsIbsMunicipal', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCbs', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsEstadual', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularIbsMunicipal', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegularCbs', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoRegular', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsEstadual', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalIbsMunicipal', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamentalCbs', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCompraGovernamental', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTributacaoMonofasica', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsTransferenciaCredito', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsAjusteCompetencia', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumido', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsCreditoPresumidoZfm', 'MonitorDocumentNfeProdutosItemImpostosIbsCbsEstornoCredito', 'MonitorDocumentNfeProdutosItemImpostosIbsCbs', 'MonitorDocumentNfeProdutosItemImpostosIcms', 'MonitorDocumentNfeProdutosItemImpostosPis', 'MonitorDocumentNfeProdutosItemImpostosIssqn', 'MonitorDocumentNfeProdutosItemImpostosIpiDevolvido', 'MonitorDocumentNfeProdutosItemImpostos', 'MonitorDocumentNfeProdutosItem', 'MonitorDocumentNfeProtocoloVariant1', 'MonitorDocumentNfeTotais', 'MonitorDocumentNfeFatura', 'MonitorDocumentNfePedido', 'MonitorDocumentNfeResponsavelTecnico', 'MonitorDocumentNfeTransporteVeiculo', 'MonitorDocumentNfeTransporteRetirada', 'MonitorDocumentNfeTransporteEntrega', 'MonitorDocumentNfeTransporteVolumesItem', 'MonitorDocumentNfeTransporteTransportadora', 'MonitorDocumentNfeTransporte', 'MonitorDocumentNfeDocs', 'MonitorDocumentNfeParcelasItem', 'MonitorDocumentNfeFornecedorVariant0', 'MonitorDocumentNfeTotaisIbsCbsCbs', 'MonitorDocumentNfeTotaisIbsCbs', 'MonitorDocumentNfe', 'MonitorDocumentNfseTotais', 'MonitorDocumentNfseImpostosIbsCbsCbs', 'MonitorDocumentNfseImpostosIbsCbsIbsEstadual', 'MonitorDocumentNfseImpostosIbsCbsIbsMunicipal', 'MonitorDocumentNfseImpostosIbsCbsLocalidadeIncidencia', 'MonitorDocumentNfseImpostosIbsCbs', 'MonitorDocumentNfseImpostos', 'MonitorDocumentNfseIdentificacaoNfseRps', 'MonitorDocumentNfseIdentificacaoNfse', 'MonitorDocumentNfseServicosItemLocalPrestacaoVariant1', 'MonitorDocumentNfseServicosItemImpostosIbsCbsCbs', 'MonitorDocumentNfseServicosItemImpostosIbsCbsIbsEstadual', 'MonitorDocumentNfseServicosItemImpostosIbsCbsIbsMunicipal', 'MonitorDocumentNfseServicosItemImpostosIbsCbsLocalidadeIncidencia', 'MonitorDocumentNfseServicosItemImpostosIbsCbs', 'MonitorDocumentNfseServicosItemImpostos', 'MonitorDocumentNfseServicosItem', 'MonitorDocumentNfseLocalPrestacaoVariant1', 'MonitorDocumentNfseDocs', 'MonitorDocumentNfseFornecedorVariant0', 'MonitorDocumentNfse', 'MonitorDocumentMdfeCarregamentoItemDocumentosItem', 'MonitorDocumentMdfeCarregamentoItem', 'MonitorDocumentMdfeSeguroItemResponsavel', 'MonitorDocumentMdfeSeguroItemSeguradora', 'MonitorDocumentMdfeSeguroItem', 'MonitorDocumentMdfePercursoItemVariant0', 'MonitorDocumentMdfeDescarregamentoItemDocumentosFiscaisItem', 'MonitorDocumentMdfeDescarregamentoItemDocumentosItem', 'MonitorDocumentMdfeDescarregamentoItem', 'MonitorDocumentMdfeFerroviarioTrem', 'MonitorDocumentMdfeFerroviarioVagoesItem', 'MonitorDocumentMdfeFerroviario', 'MonitorDocumentMdfeProdutoPredominanteLotacaoCarregamento', 'MonitorDocumentMdfeProdutoPredominanteLotacaoDescarregamento', 'MonitorDocumentMdfeProdutoPredominanteLotacao', 'MonitorDocumentMdfeProdutoPredominante', 'MonitorDocumentMdfeAquaviarioTerminalCarregamentoItem', 'MonitorDocumentMdfeAquaviarioTerminalDescarregamentoItem', 'MonitorDocumentMdfeAquaviarioEmbarcacaoComboioItem', 'MonitorDocumentMdfeAquaviarioCargaVaziaItem', 'MonitorDocumentMdfeAquaviarioTransporteVazioItem', 'MonitorDocumentMdfeAquaviario', 'MonitorDocumentMdfeRodoviarioContratantesItem', 'MonitorDocumentMdfeRodoviarioVeiculoReboqueItemProprietario', 'MonitorDocumentMdfeRodoviarioVeiculoReboqueItem', 'MonitorDocumentMdfeRodoviarioLacresItem', 'MonitorDocumentMdfeRodoviarioVeiculosItemCondutor', 'MonitorDocumentMdfeRodoviarioVeiculosItem', 'MonitorDocumentMdfeRodoviarioCiotItem', 'MonitorDocumentMdfeRodoviarioContratanteItem', 'MonitorDocumentMdfeRodoviarioCondutorItem', 'MonitorDocumentMdfeRodoviarioVeiculoTracaoProprietario', 'MonitorDocumentMdfeRodoviarioVeiculoTracao', 'MonitorDocumentMdfeRodoviarioValePedagioVariant0', 'MonitorDocumentMdfeRodoviarioValePedagioVariant1Item', 'MonitorDocumentMdfeRodoviario', 'MonitorDocumentMdfeDocs', 'MonitorDocumentMdfeAereo', 'MonitorDocumentMdfeFornecedorVariant0', 'MonitorDocumentMdfe', 'MonitorDocumentCteDocumentosFiscaisItem', 'MonitorDocumentCteServicoDocumentosOriginariosItem', 'MonitorDocumentCteServicoComponentesValorItem', 'MonitorDocumentCteServicoInformacoesCargaCubagem', 'MonitorDocumentCteServicoInformacoesCarga', 'MonitorDocumentCteServico', 'MonitorDocumentCteImpostosIbsCbsIbsEstadual', 'MonitorDocumentCteImpostosIbsCbsIbsMunicipal', 'MonitorDocumentCteImpostosIbsCbsCbs', 'MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsEstadual', 'MonitorDocumentCteImpostosIbsCbsTributacaoRegularIbsMunicipal', 'MonitorDocumentCteImpostosIbsCbsTributacaoRegularCbs', 'MonitorDocumentCteImpostosIbsCbsTributacaoRegular', 'MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsEstadual', 'MonitorDocumentCteImpostosIbsCbsCompraGovernamentalIbsMunicipal', 'MonitorDocumentCteImpostosIbsCbsCompraGovernamentalCbs', 'MonitorDocumentCteImpostosIbsCbsCompraGovernamental', 'MonitorDocumentCteImpostosIbsCbsCreditoPresumido', 'MonitorDocumentCteImpostosIbsCbsEstornoCredito', 'MonitorDocumentCteImpostosIbsCbs', 'MonitorDocumentCteImpostosIcms', 'MonitorDocumentCteImpostos', 'MonitorDocumentCteDocs', 'MonitorDocumentCteFornecedorVariant0', 'MonitorDocumentCte', 'MonitorDocumentCteOsDocumentosFiscaisItem', 'MonitorDocumentCteOsServicoDocumentosOriginariosItem', 'MonitorDocumentCteOsServicoComponentesValorItem', 'MonitorDocumentCteOsServicoInformacoesCargaCubagem', 'MonitorDocumentCteOsServicoInformacoesCarga', 'MonitorDocumentCteOsServico', 'MonitorDocumentCteOsImpostosIbsCbsIbsEstadual', 'MonitorDocumentCteOsImpostosIbsCbsIbsMunicipal', 'MonitorDocumentCteOsImpostosIbsCbsCbs', 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsEstadual', 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularIbsMunicipal', 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegularCbs', 'MonitorDocumentCteOsImpostosIbsCbsTributacaoRegular', 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsEstadual', 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalIbsMunicipal', 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamentalCbs', 'MonitorDocumentCteOsImpostosIbsCbsCompraGovernamental', 'MonitorDocumentCteOsImpostosIbsCbsCreditoPresumido', 'MonitorDocumentCteOsImpostosIbsCbsEstornoCredito', 'MonitorDocumentCteOsImpostosIbsCbs', 'MonitorDocumentCteOsImpostosIcms', 'MonitorDocumentCteOsImpostos', 'MonitorDocumentCteOsDocs', 'MonitorDocumentCteOsFornecedorVariant0', 'MonitorDocumentCteOs', 'MonitorDocument', 'MonitorCursorPagination', 'MonitorDocumentPage', 'MonitorReportFiltrosPeriodo', 'MonitorReportFiltros', 'MonitorReport', 'MonitorReportPage', 'MonitorSearchRequestFiltros', 'MonitorSearchRequestFiltrosModelo', 'MonitorSearchRequest', 'MonitorEventAlteracoesItem', 'MonitorEventMdfe', 'MonitorEventLog', 'MonitorEvent', 'MonitorManifestationRequest', 'MonitorImportRequestVariant0', 'MonitorImportRequestVariant1', 'MonitorImportRequestVariant2', 'MonitorImportRequest', 'MonitorImportStatusImportadosItem', 'MonitorImportStatusDescartadosItem', 'MonitorImportStatus', 'monitorSearchDocumentsQuery', 'monitorSearchDocumentsResponse', 'monitorGetDocumentQuery', 'monitorGetDocumentResponse', 'monitorGetDocumentFdParameter', 'monitorListDocumentEventsResponseVariant0', 'monitorListDocumentEventsResponse', 'monitorListDocumentEventsFdParameter', 'monitorManifestDocumentResponse', 'monitorManifestDocumentFdParameter', 'monitorListReportsQuery', 'monitorListReportsResponse', 'monitorDownloadReportReportParameter', 'monitorImportDocumentResponse', 'monitorGetImportStatusResponse', 'monitorGetImportStatusUuidParameter'])
