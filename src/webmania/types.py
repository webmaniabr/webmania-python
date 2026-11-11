"""Public value types. JSON values are never coerced by the SDK."""
from __future__ import annotations
from dataclasses import dataclass, field
from threading import Event
from typing import Literal, Mapping, TypeAlias, TypeVar
from .redirects import ProtectedLocation

JSONValue: TypeAlias = 'None | bool | int | float | str | list[JSONValue] | dict[str, JSONValue]'


class _Unset:
    def __repr__(self) -> str:
        return 'UNSET'


UNSET = _Unset()


@dataclass(frozen=True, repr=False)
class CompanyCredentials:
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str

    def __repr__(self) -> str:
        return 'CompanyCredentials([redacted])'


@dataclass(frozen=True, repr=False)
class ResellerCredentials:
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str

    def __repr__(self) -> str:
        return 'ResellerCredentials([redacted])'


@dataclass(frozen=True)
class CallOptions:
    timeout: float | None = None
    max_response_bytes: int | None = None
    cancel: Event | None = field(default=None, repr=False)
    _known_capabilities: tuple[str, ...] = field(default=(), repr=False)
    _known_uuid_capabilities: tuple[str, ...] = field(default=(), repr=False)


@dataclass(frozen=True, repr=False)
class FileAuth:
    """Explicit, non-fallback access mode for a single file transfer."""
    mode: Literal['company', 'issuer', 'document_token', 'anonymous', 'capability']
    token: str | None = None

    def __repr__(self) -> str:
        return 'FileAuth(mode=' + repr(self.mode) + ', token=[redacted])'


@dataclass(frozen=True, repr=False)
class FileResponse:
    data: bytes
    media_type: str
    status: int
    # Capabilities, file names and response contents remain private success values.
    content_disposition: str | None = None
    protection: Literal['not_established', 'protected'] = 'not_established'

    def __repr__(self) -> str:
        return f'FileResponse(status={self.status}, size={len(self.data)}, protection={self.protection!r})'


@dataclass(frozen=True, repr=False)
class FileRedirectResponse:
    """Documented 302 metadata. No file bytes or automatic destination access."""
    location: ProtectedLocation
    status: Literal[302] = field(default=302, init=False)

    def to_dict(self) -> dict[str, object]:
        return {'status': self.status, 'location': self.location.redacted}

    def __repr__(self) -> str:
        return 'FileRedirectResponse(status=302, location=[redacted])'


_Payload = TypeVar('_Payload', bound=Mapping[str, object])

def with_additional_fields(payload: _Payload, additions: dict[str, JSONValue]) -> _Payload:
    """Copy a typed object with new fields; operation schemas still control legality.

    Python 3.11 TypedDict cannot express open property types. This explicit helper
    preserves that model identity while refusing accidental overwrites.
    """
    from copy import deepcopy
    from .errors import WebmaniaError
    if not isinstance(payload, dict) or not isinstance(additions, dict) or any(not isinstance(k, str) for k in additions) or payload.keys() & additions.keys():
        raise WebmaniaError('validation', 'Additional fields require distinct string keys on an object.')
    from .client import depth_limit
    invalid = False
    try:
        depth_limit(payload); depth_limit(additions)
        result = {**deepcopy(payload), **deepcopy(additions)}
        depth_limit(result)
    except (ValueError, TypeError, RecursionError):
        invalid = True
    if invalid:
        raise WebmaniaError('validation', 'Additional fields require finite JSON with bounded depth.')
    return result  # type: ignore[return-value]
