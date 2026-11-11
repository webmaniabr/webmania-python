"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api1_b2b as m0
from . import api1_b2b as m1
from . import api1_b2b as m2

class ResellerMethods:
    _execute: Any

    def create_companies(self, request: m0.ResellerCreateCompaniesRequest, *, options: CallOptions | None = None) -> m0.b2bV1CreateCompaniesResponse:
        """Create reseller company slots. Contract conditions remain applicable."""
        return self._execute('b2bV1CreateCompanies', request, {}, None, options, None)

    def list_companies(self, *, options: CallOptions | None = None) -> m1.b2bV1ListCompaniesResponse:
        """List reseller-owned companies and their credentials. Contract conditions remain applicable."""
        return self._execute('b2bV1ListCompanies', UNSET, {}, None, options, None)

    def get_processed_requests(self, *, query: m2.b2bV1GetProcessedRequestsQuery | None = None, options: CallOptions | None = None) -> m2.b2bV1GetProcessedRequestsResponse:
        """Count processed production notes by reseller company. Contract conditions remain applicable."""
        return self._execute('b2bV1GetProcessedRequests', UNSET, {}, query, options, None)
