"""Webmania fiscal SDK preview; synchronous and service isolated."""
from .client import NfeClient, EmitterClient, MonitorClient, ResellerClient, NfeFilesClient, EmitterFilesClient, ReportFilesClient
from .errors import WebmaniaError, MutationReference
from .types import CompanyCredentials, ResellerCredentials, FileAuth, FileResponse, FileRedirectResponse, ProtectedLocation, CallOptions, UNSET, with_additional_fields

from .pagination import PageContinuation

__version__ = '0.1.0a8'
__all__ = ['NfeClient', 'EmitterClient', 'MonitorClient', 'ResellerClient', 'NfeFilesClient', 'EmitterFilesClient', 'ReportFilesClient',
           'WebmaniaError', 'MutationReference', 'PageContinuation', 'CompanyCredentials', 'ResellerCredentials', 'FileAuth', 'FileResponse', 'FileRedirectResponse', 'ProtectedLocation', 'CallOptions', 'UNSET', 'with_additional_fields']
