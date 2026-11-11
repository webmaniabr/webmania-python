"""Protected HTTP Location metadata. No resolution, fetch or origin authorization."""
from __future__ import annotations
import ipaddress
import re
from urllib.parse import parse_qsl, unquote, urlsplit
from .errors import WebmaniaError

_URI = re.compile(r"^[A-Za-z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+$", re.ASCII)
_PATH_UUID = re.compile(r'(?<![0-9a-f])[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}(?![0-9a-f])', re.I | re.ASCII)
_HOST_LABEL = re.compile(r'^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$', re.ASCII)


def validated_location(value: str) -> str:
    invalid = type(value) is not str
    normalized = ''
    if not invalid:
        # Outer OWS belongs to the HTTP field, not the URI reference. Folding
        # and control characters are rejected before any URI parsing can hide them.
        invalid = len(value) > 65536 or any(ord(c) < 32 and c != '\t' or ord(c) == 127 for c in value)
        normalized = value.strip(' \t')
        invalid = invalid or not normalized or _URI.fullmatch(normalized) is None
        invalid = invalid or bool(re.search(r'%(?![0-9A-Fa-f]{2})|%(?:0[ad]|00)', normalized, re.I))
        invalid = invalid or normalized.startswith('///') or bool(re.search(r',(?:https?:)?//', normalized, re.I))
    parts = None
    if not invalid:
        try:
            parts = urlsplit(normalized)
            if parts.scheme and parts.scheme.lower() not in ['http', 'https']: invalid = True
            if parts.scheme and not parts.netloc: invalid = True
            if normalized.startswith('//') and not parts.netloc: invalid = True
            if parts.username is not None or parts.password is not None: invalid = True
            if parts.netloc:
                host = parts.hostname
                if not host or parts.netloc.endswith(':'): invalid = True
                else:
                    try: ipaddress.ip_address(host)
                    except ValueError:
                        if any(_HOST_LABEL.fullmatch(label) is None for label in host.removesuffix('.').split('.')):
                            invalid = True
                _ = parts.port
        except (ValueError, TypeError, UnicodeError):
            invalid = True
    if invalid or parts is None:
        raise WebmaniaError('protocol', 'Invalid or ambiguous HTTP redirect Location.')
    return normalized


class ProtectedLocation:
    """A private URI reference, recoverable only through an explicit call."""
    __slots__ = ('__reference',)

    def __init__(self, value: str) -> None:
        self.__reference = validated_location(value)

    def reveal(self) -> str:
        """Return the original URI reference; this does not authorize its origin."""
        return self.__reference

    @property
    def redacted(self) -> str:
        return '[redacted]'

    @property
    def is_relative(self) -> bool:
        return not bool(urlsplit(self.__reference).scheme)

    def __repr__(self) -> str: return 'ProtectedLocation([redacted])'
    def __str__(self) -> str: return 'ProtectedLocation([redacted])'


def location_diagnostic_values(value):
    """Diagnostic-only tokenization, including encoded delimiters and invalid URIs."""
    if not isinstance(value, str): return []
    values = {value, value.strip(' \t')}
    decoded = value
    for _ in range(3):
        decoded = unquote(decoded)
        values.add(decoded)
        # Delimiters are split after decoding as well as before; malformed
        # neighboring escapes do not hide a known private component.
        values.update(re.split(r'[/?:#&;=\[\]@]+', decoded))
    # Schemes, authorities and parameter names are structural public vocabulary.
    return [v for v in values if v and v.lower() not in {'http', 'https', 'token', 'cap', 'file'}]


def location_path_uuids(value):
    """UUIDs in a redirect path are known private UUIDs; query tokens are opaque."""
    if not isinstance(value, str): return []
    try: path = urlsplit(value).path
    except (ValueError, TypeError, UnicodeError):
        # Diagnostic-only separation, never URI repair or acceptance. Split raw
        # delimiters before percent-decoding so authority/userinfo and query
        # tokens cannot be mistaken for UUIDs in the path.
        reference = value.strip(' \t').split('#', 1)[0].split('?', 1)[0]
        prefix = re.match(r'(?:[A-Za-z][A-Za-z0-9+.-]*:)?//', reference, re.ASCII)
        if prefix is None: return []
        _, separator, suffix = reference[prefix.end():].partition('/')
        path = '/' + suffix if separator else ''
    return _PATH_UUID.findall(unquote(path))
