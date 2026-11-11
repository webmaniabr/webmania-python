"""Generated from contracts/api2/monitor-reads.openapi.json; SHA256 eaf603cf14473a17bffb498f064e2f18a016d5eb28964cda86332a3edc34776e. Do not edit."""
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

monitorListCompaniesQuery = TypedDict('monitorListCompaniesQuery', {'page': int, 'per_page': int, 'pesquisa': str}, total=False)

monitorListCompaniesResponse: TypeAlias = Union['MonitorCompanyPage']

monitorGetCompanyResponse: TypeAlias = Union['MonitorCompany']

monitorGetCompanyCompanyParameter: TypeAlias = str

monitorListCompanyMunicipalitiesQuery = TypedDict('monitorListCompanyMunicipalitiesQuery', {'page': int, 'per_page': int, 'municipio': str, 'uf': str, 'codigo_ibge': str}, total=False)

monitorListCompanyMunicipalitiesResponse: TypeAlias = Union['MonitorMunicipalityPage']

monitorListCompanyMunicipalitiesCompanyParameter: TypeAlias = str

monitorGetCompanyMunicipalityResponse: TypeAlias = Union['MonitorMunicipalityRegistration']

monitorGetCompanyMunicipalityCompanyParameter: TypeAlias = str

monitorGetCompanyMunicipalityDownloadParameter: TypeAlias = str

monitorListAvailableMunicipalitiesQuery = TypedDict('monitorListAvailableMunicipalitiesQuery', {'codigo_ibge': str}, total=False)

monitorListAvailableMunicipalitiesResponse: TypeAlias = Union[Union['MonitorAvailableMunicipalities', 'MonitorAvailableMunicipality']]

monitorGetDownloadStatisticsQuery = TypedDict('monitorGetDownloadStatisticsQuery', {'ano': int, 'mes': Union[int, float]}, total=False)

monitorGetDownloadStatisticsResponse: TypeAlias = Union['MonitorDownloadStatistics']

_bind_types(globals(), __name__, ['MonitorError', 'MonitorPagination', 'MonitorAddress', 'MonitorCompany', 'MonitorMunicipalityRegistration', 'MonitorAvailableMunicipality', 'MonitorDownloadStatisticsEmpresasItem', 'MonitorDownloadStatistics', 'MonitorCompanyPage', 'MonitorMunicipalityPage', 'MonitorAvailableMunicipalities', 'monitorListCompaniesQuery', 'monitorListCompaniesResponse', 'monitorGetCompanyResponse', 'monitorGetCompanyCompanyParameter', 'monitorListCompanyMunicipalitiesQuery', 'monitorListCompanyMunicipalitiesResponse', 'monitorListCompanyMunicipalitiesCompanyParameter', 'monitorGetCompanyMunicipalityResponse', 'monitorGetCompanyMunicipalityCompanyParameter', 'monitorGetCompanyMunicipalityDownloadParameter', 'monitorListAvailableMunicipalitiesQuery', 'monitorListAvailableMunicipalitiesResponse', 'monitorGetDownloadStatisticsQuery', 'monitorGetDownloadStatisticsResponse'])
