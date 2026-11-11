"""Bounded structured error diagnostics with contextual redaction."""
from __future__ import annotations
import json
from decimal import Decimal, InvalidOperation
import math
import re
import unicodedata
from urllib.parse import quote, quote_plus

SENSITIVE = re.compile(r'password|senha|certificate|certificado|token|secret|consumer.?key|authorization|credential|credencia|url|xml|pdf|conteudo|content|base64', re.I)
UUID = re.compile(r'^[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$', re.I | re.ASCII)
NUMERIC = re.compile(r'(?<![\w.])[-+]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][-+]?[0-9]+)?(?![\w.])')
PUBLIC_FIELDS = {'body', 'query'}
URL = re.compile(r'(?i)\b(?:https?|ftp)://[^\s<>"\x27]+')


def json_containers(value):
    """Walk the full, finite serialized snapshot without a second depth policy."""
    pending = [value]
    visited = set()
    while pending:
        node = pending.pop()
        if isinstance(node, (dict, list, tuple)):
            if id(node) in visited: continue
            visited.add(id(node))
        yield node
        if isinstance(node, dict): pending.extend(node.values())
        elif isinstance(node, (list, tuple)): pending.extend(node)


def scalar_values(value):
    for node in json_containers(value):
        if isinstance(node, dict):
            # Extensible request keys can themselves contain private data.
            yield from (str(k) for k, child in node.items() if str(k) not in PUBLIC_FIELDS and not (re.fullmatch(r'[a-z_][a-z0-9_]*', str(k)) and isinstance(child, (bool, int, float))))
        elif isinstance(node, bool): continue
        elif isinstance(node, (str, int, float)): yield str(node)


def uuid_values(value):
    for node in json_containers(value):
        if isinstance(node, dict):
            for key, child in node.items():
                if str(key).lower() in ['uuid', 'fd', 'report', 'company', 'download', 'empresa_uuid'] and isinstance(child, str) and UUID.fullmatch(child):
                    yield child


def sensitive_values(value):
    for node in json_containers(value):
        if isinstance(node, dict):
            for key, child in node.items():
                if SENSITIVE.search(str(key)): yield from scalar_values(child)


class Redactor:
    def __init__(self, secrets=(), request=None, uuid_secrets=(), contextual_values=()):
        values = list(secrets) + list(scalar_values(request))
        scoped = set(contextual_values) - set(values)
        values += list(scoped)
        boundary = set()
        uuids = {u for u in list(uuid_secrets) + list(uuid_values(request)) if isinstance(u, str) and UUID.fullmatch(u)}
        self.uuid_pattern = re.compile('(?=(' + '|'.join(re.escape(u) for u in sorted(uuids)) + '))', re.I | re.ASCII) if uuids else None
        expanded = set()
        self.numeric_values = set()
        for v in values:
            if not isinstance(v, str) or not v:
                continue
            for form in {v, unicodedata.normalize('NFC', v), unicodedata.normalize('NFD', v)}:
                encoded = {quote(form, safe=''), quote_plus(form, safe='')}
                if v in scoped and len(v) <= 3: boundary.update({form, *encoded})
                expanded.update({form, json.dumps(form, ensure_ascii=True)[1:-1], *encoded})
                expanded.update(re.sub(r'%[0-9A-F]{2}', lambda m: m.group(0).lower(), x) for x in encoded)
                if len(form) <= 128 and re.fullmatch(r'[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?', form):
                    try:
                        number = Decimal(form)
                        if number.is_finite() and abs(number.adjusted()) <= 128:
                            expanded.add(format(number, 'f'))
                            if number == number.to_integral_value(): expanded.add(str(int(number)))
                            approximate = float(number)
                            if math.isfinite(approximate):
                                expanded.add(str(approximate))
                                self.numeric_values.add(approximate)
                    except (InvalidOperation, ValueError, OverflowError): pass
        self.values = sorted(expanded, key=lambda v: (-len(v), v))
        self.pattern = re.compile('(?=(' + '|'.join((r'(?<!\w)' + re.escape(v) + r'(?!\w)' if v in boundary else re.escape(v)) for v in self.values) + '))') if self.values else None
        self.remaining = 512

    def has_private_match(self, value):
        text = str(value)
        return bool(URL.search(text) or
                    self.uuid_pattern is not None and self.uuid_pattern.search(text) or
                    self.pattern is not None and self.pattern.search(text) or
                    any(self.numeric_known(m.group(0)) for m in NUMERIC.finditer(text)))

    def numeric_known(self, value):
        try:
            number = float(value)
            return math.isfinite(number) and number in self.numeric_values
        except (ValueError, TypeError, OverflowError):
            return False

    def segment(self, text):
        # Lookahead discovers a match at every original offset, including starts
        # inside another secret. The longest literal at one offset contains all
        # shorter matches there, so at most one interval per pattern is needed.
        intervals = []
        for pattern in (self.uuid_pattern, self.pattern):
            if pattern:
                intervals.extend((m.start(1), m.end(1), False) for m in pattern.finditer(text))
        intervals.extend((m.start(), m.end(), False) for m in NUMERIC.finditer(text) if self.numeric_known(m.group(0)))
        intervals.extend((m.start(), m.end(), True) for m in URL.finditer(text))
        intervals.sort()
        result = []
        previous = 0
        start = end = 0
        url = False
        for left, right, is_url in intervals:
            if left > end:
                if end > start:
                    result.extend((text[previous:start], '[redacted-url]' if url else '[redacted]'))
                    previous = end
                start, end, url = left, right, is_url
            else:
                end = max(end, right)
                url = url or is_url
        if end > start:
            result.extend((text[previous:start], '[redacted-url]' if url else '[redacted]'))
            previous = end
        result.append(text[previous:])
        return ''.join(result)

    def text(self, value):
        if len(str(value)) > 4096: return '[truncated]'
        return self.segment(str(value))[:1024]

    def clean(self, value, depth=0):
        self.remaining -= 1
        if self.remaining < 0 or depth > 12:
            return '[truncated]'
        if isinstance(value, dict):
            result = {}
            for i, (key, child) in enumerate(value.items()):
                if i >= 64: result['[truncated]'] = True; break
                safe_key = self.text(key)
                if safe_key in result: safe_key = '[redacted-key-' + str(i) + ']'
                result[safe_key] = '[redacted]' if SENSITIVE.search(str(key)) else self.clean(child, depth + 1)
            return result
        if isinstance(value, list):
            return [self.clean(v, depth + 1) for v in value[:64]] + (['[truncated]'] if len(value) > 64 else [])
        if isinstance(value, str): return self.text(value)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if self.numeric_known(value) or str(value) in self.values or (isinstance(value, float) and (not math.isfinite(value) or str(int(value)) in self.values)):
                return '[redacted]'
            return value
        if isinstance(value, bool) and ('true' if value else 'false') in self.values:
            return '[redacted]'
        return value if value is None or isinstance(value, bool) else '[redacted]'


class MutationReference:
    """Private recovery selectors; ordinary diagnostics never reveal values."""
    __slots__ = ('__selectors',)

    def __init__(self, selectors: dict[str, str | int]) -> None:
        # Values originate from a serialized JSON snapshot, not mutable input.
        self.__selectors = json.dumps(selectors, ensure_ascii=False, allow_nan=False)

    @property
    def redacted(self) -> dict[str, str]:
        return {key: '[redacted]' for key in json.loads(self.__selectors)}

    def reveal(self) -> dict[str, str | int]:
        """Explicitly recover a private copy to query a prior fiscal attempt."""
        return json.loads(self.__selectors)

    def __repr__(self) -> str: return 'MutationReference([redacted])'
    def __str__(self) -> str: return 'MutationReference([redacted])'


def mutation_reference(request, path_params, secrets, uuid_secrets=(), *, capability_access=False):
    if capability_access: return None
    candidates = {k: request[k] for k in ['ID', 'id', 'uuid', 'chave'] if isinstance(request, dict) and k in request}
    candidates.update(path_params)
    forbidden = Redactor(list(secrets) + list(sensitive_values(request)), uuid_secrets=uuid_secrets)
    selectors = {}
    for key, value in candidates.items():
        if isinstance(value, (str, int)) and not isinstance(value, bool) and value != '':
            # Recover only caller-provided selectors that do not collide with
            # credentials, sensitive request fields, URLs or known capabilities.
            if not forbidden.has_private_match(value): selectors[key] = value
    return MutationReference(selectors) if selectors else None


class WebmaniaError(Exception):
    """No raw HTTP body, request, URL, credential, or low-level cause is retained."""
    def __init__(self, kind, message, *, status=None, response=None, correlation_id=None,
                 outcome=None, request_reference=None, request_id=None, location=None):
        super().__init__(message)
        self.kind = kind
        self.status = status
        self.response = response
        self.correlation_id = correlation_id
        self.outcome = outcome
        self.request_reference = request_reference
        self.request_id = request_id
        self.location = location

    def to_dict(self) -> dict[str, object]:
        return {'kind': self.kind, 'message': str(self), 'status': self.status,
                'response': self.response, 'correlation_id': self.correlation_id,
                'outcome': self.outcome, 'request_id': self.request_id,
                'location': '[redacted]' if self.location is not None else None,
                'request_reference': self.request_reference.redacted if isinstance(self.request_reference, MutationReference) else None}

    def __repr__(self):
        return f'WebmaniaError(kind={self.kind!r}, status={self.status!r}, outcome={self.outcome!r})'
