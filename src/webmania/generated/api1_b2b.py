"""Generated from contracts/api1/b2b.openapi.json; SHA256 e60db118d379e3183298c15633bda63fc8b753c9967a8679b0dbb85615036f8b. Do not edit."""
from typing import Literal, Required, TypedDict, TypeAlias, Union
from ..types import JSONValue
from ..model_types import bind_types as _bind_types

B2bError = TypedDict('B2bError', {'error': JSONValue, 'message': str, 'success': bool}, total=False)

ResellerCreateCompaniesRequest = TypedDict('ResellerCreateCompaniesRequest', {'quantidade': Required[int]}, total=False)

ResellerCompanyCredentials = TypedDict('ResellerCompanyCredentials', {'consumer_key': Required[str], 'consumer_secret': Required[str], 'access_token': Required[str], 'access_token_secret': Required[str], 'bearer_access_token': Required[str], 'bearer_access_token_status': Literal['ready', 'pending'], 'bearer_access_token_pending': bool, 'direct_link_login': str}, total=False)

ResellerCreatedCompany = TypedDict('ResellerCreatedCompany', {'consumer_key': Required[str], 'consumer_secret': Required[str], 'access_token': Required[str], 'access_token_secret': Required[str], 'bearer_access_token': Required[str], 'bearer_access_token_status': Literal['ready', 'pending'], 'bearer_access_token_pending': bool, 'direct_link_login': str, 'id': Required[int], 'bearer_access_token_recovery_queued': Union[bool, None], 'bearer_access_token_recovery_queue_status': Union[str, None]}, total=False)

ResellerCreatedCompanies: TypeAlias = list['ResellerCreatedCompany']

ResellerCompany = TypedDict('ResellerCompany', {'cnpj': Union[str, None], 'cpf': Union[str, None], 'razao_social': Union[str, None], 'nome_completo': Union[str, None], 'cidade': Union[str, None], 'estado': Union[str, None], 'ie': Union[str, None], 'id': Required[int], 'unidade_empresa': Union[int, str, None], 'tipo_tributacao': Union[str, None], 'credenciais': Required['ResellerCompanyCredentials']}, total=False)

ResellerCompanies: TypeAlias = list['ResellerCompany']

ResellerCompanyProcessedRequests = TypedDict('ResellerCompanyProcessedRequests', {'cnpj': Union[str, None], 'cpf': Union[str, None], 'razao_social': Union[str, None], 'nome_completo': Union[str, None], 'cidade': Union[str, None], 'estado': Union[str, None], 'ie': Union[str, None], 'id': int, 'notas_processadas': Required[int]}, total=False)

ResellerProcessedRequests = TypedDict('ResellerProcessedRequests', {'total_notas_processadas': Required[int], 'empresas': Required[list['ResellerCompanyProcessedRequests']]}, total=False)

B2bFunctionalError = TypedDict('B2bFunctionalError', {'error': Required[JSONValue], 'message': str, 'success': bool}, total=False)

b2bV1CreateCompaniesResponse: TypeAlias = Union[Union['ResellerCreatedCompanies', 'B2bFunctionalError']]

b2bV1ListCompaniesResponse: TypeAlias = Union[Union['ResellerCompanies', 'B2bFunctionalError']]

b2bV1GetProcessedRequestsQuery = TypedDict('b2bV1GetProcessedRequestsQuery', {'mes': str, 'ano': str}, total=False)

b2bV1GetProcessedRequestsResponse: TypeAlias = Union[Union['ResellerProcessedRequests', 'B2bFunctionalError']]

_bind_types(globals(), __name__, ['B2bError', 'ResellerCreateCompaniesRequest', 'ResellerCompanyCredentials', 'ResellerCreatedCompany', 'ResellerCreatedCompanies', 'ResellerCompany', 'ResellerCompanies', 'ResellerCompanyProcessedRequests', 'ResellerProcessedRequests', 'B2bFunctionalError', 'b2bV1CreateCompaniesResponse', 'b2bV1ListCompaniesResponse', 'b2bV1GetProcessedRequestsQuery', 'b2bV1GetProcessedRequestsResponse'])
