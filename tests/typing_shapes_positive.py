"""Positive consumers for composed request shapes; checked by mypy --strict."""
from webmania import MutationReference
from webmania.generated.api1_fiscal import (
    NfeCancelRequest, NfeCorrectionRequest, Nfe55Customer, IbsCbs112120Request,
)
from webmania.generated.api2_monitor_documents import MonitorImportRequest
from webmania.generated.api2_mdfe_issuance import MdfeFreightPaymentGroup

cancel: NfeCancelRequest = {'uuid': 'abcdefab-cdef-4abc-8def-abcdefabcdef', 'motivo': 'Synthetic cancellation reason'}
correction: NfeCorrectionRequest = {'uuid': 'abcdefab-cdef-4abc-8def-abcdefabcdef', 'correcao': 'Synthetic correction reason'}
customer: Nfe55Customer = {'cpf': '00000000000', 'nome_completo': 'Synthetic person', 'endereco': 'Synthetic street', 'numero': '1', 'bairro': 'Synthetic district', 'cidade': 'Synthetic city', 'uf': 'SP', 'cep': '01001-000'}
import_request: MonitorImportRequest = {'empresa_uuid': 'abcdefab-cdef-4abc-8def-abcdefabcdef', 'xml': '<synthetic/>'}


def cancellation_reason(payload: NfeCancelRequest) -> str:
    return payload['motivo']


def correction_text(payload: NfeCorrectionRequest) -> str:
    return payload['correcao']


def customer_cpf(payload: Nfe55Customer) -> str | None:
    return payload.get('cpf')


def import_company(payload: MonitorImportRequest) -> str:
    return payload['empresa_uuid']


def event_key(payload: IbsCbs112120Request) -> str:
    return payload['chave']


def freight_amount(payload: MdfeFreightPaymentGroup) -> str | int | float:
    return payload['valor_contrato']


def recovery_uuid(reference: MutationReference) -> str | int | None:
    return reference.reveal().get('uuid')
