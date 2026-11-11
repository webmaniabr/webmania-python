"""Generated explicit methods. Do not edit."""
from __future__ import annotations
from typing import Any, ForwardRef, Literal, Union
from ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse
from . import api2_monitor_documents as m0
from . import api2_monitor_documents as m1
from . import api2_monitor_documents as m2
from . import api2_monitor_documents as m3
from . import api2_monitor_documents as m4
from . import api2_monitor_documents as m5
from . import api2_monitor_documents as m6
from . import api2_monitor_documents as m7
from . import api2_monitor_management as m8
from . import api2_monitor_management as m9
from . import api2_monitor_management as m10
from . import api2_monitor_management as m11
from . import api2_monitor_management as m12
from . import api2_monitor_reads as m13
from . import api2_monitor_reads as m14
from . import api2_monitor_reads as m15
from . import api2_monitor_reads as m16
from . import api2_monitor_reads as m17
from . import api2_monitor_reads as m18

class MonitorMethods:
    _execute: Any

    def search_documents(self, request: m0.MonitorSearchRequest, *, query: m0.monitorSearchDocumentsQuery | None = None, options: CallOptions | None = None) -> m0.monitorSearchDocumentsResponse:
        """Search documents or create an export report. Contract conditions remain applicable."""
        return self._execute('monitorSearchDocuments', request, {}, query, options, None)

    def get_document(self, *, fd: m1.monitorGetDocumentFdParameter, query: m1.monitorGetDocumentQuery | None = None, options: CallOptions | None = None) -> m1.monitorGetDocumentResponse:
        """Get a fiscal document. Contract conditions remain applicable."""
        return self._execute('monitorGetDocument', UNSET, {'fd': fd}, query, options, None)

    def list_document_events(self, *, fd: m2.monitorListDocumentEventsFdParameter, options: CallOptions | None = None) -> m2.monitorListDocumentEventsResponse:
        """List a document event history. Contract conditions remain applicable."""
        return self._execute('monitorListDocumentEvents', UNSET, {'fd': fd}, None, options, None)

    def manifest_document(self, request: m3.MonitorManifestationRequest, *, fd: m3.monitorManifestDocumentFdParameter, options: CallOptions | None = None) -> m3.monitorManifestDocumentResponse:
        """Submit recipient manifestation. Contract conditions remain applicable."""
        return self._execute('monitorManifestDocument', request, {'fd': fd}, None, options, None)

    def list_reports(self, *, query: m4.monitorListReportsQuery | None = None, options: CallOptions | None = None) -> m4.monitorListReportsResponse:
        """List export reports. Contract conditions remain applicable."""
        return self._execute('monitorListReports', UNSET, {}, query, options, None)

    def download_report(self, *, report: m5.monitorDownloadReportReportParameter, options: CallOptions | None = None) -> FileResponse:
        """Download a completed report. Contract conditions remain applicable."""
        return self._execute('monitorDownloadReport', UNSET, {'report': report}, None, options, None)

    def import_document(self, request: m6.MonitorImportRequest, *, options: CallOptions | None = None) -> m6.monitorImportDocumentResponse:
        """Import by access key, XML or ZIP. Contract conditions remain applicable."""
        return self._execute('monitorImportDocument', request, {}, None, options, None)

    def get_import_status(self, *, uuid: m7.monitorGetImportStatusUuidParameter, options: CallOptions | None = None) -> m7.monitorGetImportStatusResponse:
        """Read ZIP import progress. Contract conditions remain applicable."""
        return self._execute('monitorGetImportStatus', UNSET, {'uuid': uuid}, None, options, None)

    def create_company(self, request: m8.MonitorCreateCompanyRequest, *, options: CallOptions | None = None) -> m8.monitorCreateCompanyResponse:
        """Create a monitored company. Contract conditions remain applicable."""
        return self._execute('monitorCreateCompany', request, {}, None, options, None)

    def update_company(self, request: m9.MonitorUpdateCompanyRequest, *, company: m9.monitorUpdateCompanyCompanyParameter, options: CallOptions | None = None) -> m9.monitorUpdateCompanyResponse:
        """Update a monitored company. Contract conditions remain applicable."""
        return self._execute('monitorUpdateCompany', request, {'company': company}, None, options, None)

    def create_company_municipality(self, request: m10.MonitorCreateMunicipalityRequest, *, company: m10.monitorCreateCompanyMunicipalityCompanyParameter, options: CallOptions | None = None) -> m10.monitorCreateCompanyMunicipalityResponse:
        """Register a municipality for monitoring. Contract conditions remain applicable."""
        return self._execute('monitorCreateCompanyMunicipality', request, {'company': company}, None, options, None)

    def update_company_municipality(self, request: m11.MonitorUpdateMunicipalityRequest, *, company: m11.monitorUpdateCompanyMunicipalityCompanyParameter, download: m11.monitorUpdateCompanyMunicipalityDownloadParameter, options: CallOptions | None = None) -> m11.monitorUpdateCompanyMunicipalityResponse:
        """Update municipality credentials. Contract conditions remain applicable."""
        return self._execute('monitorUpdateCompanyMunicipality', request, {'company': company, 'download': download}, None, options, None)

    def delete_company_municipality(self, *, company: m12.monitorDeleteCompanyMunicipalityCompanyParameter, download: m12.monitorDeleteCompanyMunicipalityDownloadParameter, options: CallOptions | None = None) -> m12.monitorDeleteCompanyMunicipalityResponse:
        """Stop municipality monitoring. Contract conditions remain applicable."""
        return self._execute('monitorDeleteCompanyMunicipality', UNSET, {'company': company, 'download': download}, None, options, None)

    def list_companies(self, *, query: m13.monitorListCompaniesQuery | None = None, options: CallOptions | None = None) -> m13.monitorListCompaniesResponse:
        """List monitored companies. Contract conditions remain applicable."""
        return self._execute('monitorListCompanies', UNSET, {}, query, options, None)

    def get_company(self, *, company: m14.monitorGetCompanyCompanyParameter, options: CallOptions | None = None) -> m14.monitorGetCompanyResponse:
        """Get a monitored company. Contract conditions remain applicable."""
        return self._execute('monitorGetCompany', UNSET, {'company': company}, None, options, None)

    def list_company_municipalities(self, *, company: m15.monitorListCompanyMunicipalitiesCompanyParameter, query: m15.monitorListCompanyMunicipalitiesQuery | None = None, options: CallOptions | None = None) -> m15.monitorListCompanyMunicipalitiesResponse:
        """List configured nonnative NFS-e municipality monitoring. Contract conditions remain applicable."""
        return self._execute('monitorListCompanyMunicipalities', UNSET, {'company': company}, query, options, None)

    def get_company_municipality(self, *, company: m16.monitorGetCompanyMunicipalityCompanyParameter, download: m16.monitorGetCompanyMunicipalityDownloadParameter, options: CallOptions | None = None) -> m16.monitorGetCompanyMunicipalityResponse:
        """Get a municipality-monitoring registration. Contract conditions remain applicable."""
        return self._execute('monitorGetCompanyMunicipality', UNSET, {'company': company, 'download': download}, None, options, None)

    def list_available_municipalities(self, *, query: m17.monitorListAvailableMunicipalitiesQuery | None = None, options: CallOptions | None = None) -> m17.monitorListAvailableMunicipalitiesResponse:
        """List or look up NFS-e municipalities. Contract conditions remain applicable."""
        return self._execute('monitorListAvailableMunicipalities', UNSET, {}, query, options, None)

    def get_download_statistics(self, *, query: m18.monitorGetDownloadStatisticsQuery | None = None, options: CallOptions | None = None) -> m18.monitorGetDownloadStatisticsResponse:
        """Get monthly document-download statistics. Contract conditions remain applicable."""
        return self._execute('monitorGetDownloadStatistics', UNSET, {}, query, options, None)
