"""JSON Schema 2020-12 and exact decimal-text bounds; no numeric coercion."""
from __future__ import annotations
from decimal import Decimal, InvalidOperation
import json
from importlib.resources import files
from jsonschema import Draft202012Validator, FormatChecker, ValidationError, validators
from .errors import WebmaniaError, PUBLIC_FIELDS


def decimal_bound(validator, bound, instance, schema, *, minimum):
    if not isinstance(instance, (str, int, float)) or isinstance(instance, bool): return
    invalid = False
    try:
        value = Decimal(str(instance))
        edge = Decimal(bound)
        invalid = not value.is_finite() or (value < edge if minimum else value > edge)
    except (InvalidOperation, ValueError, TypeError):
        invalid = True
    if invalid:
        yield ValidationError('Value violates an exact decimal bound.')


def minimum(v, b, i, s): return decimal_bound(v, b, i, s, minimum=True)
def maximum(v, b, i, s): return decimal_bound(v, b, i, s, minimum=False)
Validator = validators.extend(Draft202012Validator, {'x-sdk-numeric-minimum': minimum, 'x-sdk-numeric-maximum': maximum})
OPERATIONS = json.loads(files('webmania').joinpath('contracts/operations.json').read_text(encoding='utf-8'))
DOCUMENTS = {}
for module in sorted({o['module'] for o in OPERATIONS.values()}):
    DOCUMENTS[module] = json.loads(files('webmania').joinpath('contracts/' + module + '.json').read_text(encoding='utf-8'))


def _public_fields():
    pending = list(DOCUMENTS.values())
    while pending:
        node = pending.pop()
        if isinstance(node, dict):
            PUBLIC_FIELDS.update(node.get('properties', {}))
            pending.extend(node.values())
        elif isinstance(node, list): pending.extend(node)


_public_fields()


def validate(module, schema, value, *, response=False):
    full = {'components': DOCUMENTS[module]['components'], **schema}
    # Draft validators reject bool-as-int and never modify input values.
    error = next(Validator(full, format_checker=FormatChecker()).iter_errors(value), None)
    if error is not None:
        names = set()
        def collect(node):
            if isinstance(node, dict):
                names.update(node.get('properties', {}))
                for child in node.values(): collect(child)
            elif isinstance(node, list):
                for child in node: collect(child)
        collect(DOCUMENTS[module]['components']['schemas'])
        path = [str(part) if isinstance(part, int) or part in names else '[additional-field]' for part in error.absolute_path]
        raise WebmaniaError('response_schema' if response else 'validation',
                            'Response does not match the pinned contract.' if response else 'Request does not match the pinned contract.',
                            response={'validator': error.validator, 'path': '/' + '/'.join(path)})


def operation(oid):
    record = OPERATIONS[oid]
    doc = DOCUMENTS[record['module']]
    spec = doc['paths'][record['path']][record['verb'].lower()]
    return record, doc, spec
