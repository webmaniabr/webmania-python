#!/usr/bin/env python3
"""Generate schemas, TypedDict models and explicit synchronous methods from Git inputs.

The canonical contract is identified by its ``contract_digest``: the SHA-256 of the canonical
JSON of the ``module path -> SHA-256`` map of the manifest modules (sorted keys, UTF-8,
``,``/``:`` separators). Generation refuses a source whose digest differs from the pin.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_DIGEST = '371a499f74012bb6b41f23642869dee4954e8394dcba7642edc701aedb3dd59e'


def snake(value):
    value = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', value)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', value).lower()


def contract_digest(modules):
    canonical = json.dumps(dict(sorted(modules.items())), separators=(',', ':'), ensure_ascii=False)
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


def run(source, revision, check, expected_digest=CONTRACT_DIGEST):
    def source_bytes(path):
        return subprocess.check_output(['git', '-C', str(source), 'show', revision + ':' + path])
    manifest = json.loads(source_bytes('contracts/manifest.json'))
    digest = contract_digest({path: hashlib.sha256(source_bytes(path)).hexdigest() for path in manifest['contracts']})
    if digest != expected_digest:
        raise SystemExit('Canonical contract_digest ' + digest + ' differs from the pinned ' + expected_digest + '.')
    outputs = {}
    records = []
    methods = {n: [] for n in ['Nfe', 'Emitter', 'Monitor', 'Reseller', 'NfeFiles', 'EmitterFiles', 'ReportFiles']}
    operation_index = {}
    model_count = 0
    for path in manifest['contracts']:
        raw = source_bytes(path)
        doc = json.loads(raw)
        module = path.removeprefix('contracts/').replace('/', '_').replace('.openapi.json', '').replace('-', '_')
        outputs[f'src/webmania/contracts/{module}.json'] = raw.decode('utf-8')
        records.append({'contract': path, 'sha256': hashlib.sha256(raw).hexdigest(), 'module': module})
        definitions = []
        schemas = doc['components']['schemas']
        created = set()

        def merge_shape(left, right):
            merged = {**left, **right}
            properties = dict(left.get('properties', {}))
            for key, child in right.get('properties', {}).items():
                prior = properties.get(key)
                if prior is not None and prior and child and prior != child:
                    properties[key] = {'allOf': [prior, child]}
                else:
                    properties[key] = child or prior or {}
            if 'properties' in left or 'properties' in right: merged['properties'] = properties
            if 'required' in left or 'required' in right:
                merged['required'] = sorted(set(left.get('required', [])) | set(right.get('required', [])))
            return merged

        def composed_shapes(schema, seen=frozenset()):
            """Distribute structural intersections while retaining common fields.

            Conditional tax/provider constraints remain in runtime JSON Schema;
            this projection models declared properties and presence alternatives.
            """
            if '$ref' in schema:
                key = schema['$ref'].rsplit('/', 1)[-1]
                if key in seen: raise ValueError('Cyclic composition reference: ' + key)
                targets = composed_shapes(schemas[key], seen | {key})
                siblings = {k: v for k, v in schema.items() if k != '$ref'}
                return [merge_shape(target, siblings) for target in targets]
            base = {k: v for k, v in schema.items() if k not in ['allOf', 'anyOf', 'oneOf']}
            variants = [base]
            for child in schema.get('allOf', []):
                projected = composed_shapes(child, seen)
                variants = [merge_shape(left, right) for left in variants for right in projected]
            for union in ['anyOf', 'oneOf']:
                if union in schema:
                    alternatives = [variant for child in schema[union] for variant in composed_shapes(child, seen)]
                    variants = [merge_shape(left, right) for left in variants for right in alternatives]
            return variants

        def type_for(schema, name):
            if '$ref' in schema:
                structural = {'type', 'properties', 'required', 'allOf', 'anyOf', 'oneOf'}
                if not structural.intersection(schema):
                    return repr(schema['$ref'].rsplit('/', 1)[-1])
                variants = composed_shapes(schema)
                types = [type_for(variant, name if len(variants) == 1 else name + 'Variant' + str(i)) for i, variant in enumerate(variants)]
                return types[0] if len(types) == 1 else 'Union[' + ', '.join(dict.fromkeys(types)) + ']'
            if 'allOf' in schema or any(union in schema and any(k in schema for k in ['type', 'properties', 'required']) for union in ['anyOf', 'oneOf']):
                variants = composed_shapes(schema)
                types = [type_for(variant, name if len(variants) == 1 else name + 'Variant' + str(i)) for i, variant in enumerate(variants)]
                return types[0] if len(types) == 1 else 'Union[' + ', '.join(dict.fromkeys(types)) + ']'
            for union in ['anyOf', 'oneOf']:
                if union in schema:
                    types = [type_for(x, name + 'Variant' + str(i)) for i, x in enumerate(schema[union])]
                    return 'Union[' + ', '.join(dict.fromkeys(types)) + ']'
            if 'const' in schema:
                return 'Literal[' + repr(schema['const']) + ']'
            if 'enum' in schema:
                values = [x for x in schema['enum'] if not isinstance(x, float)]
                literal = 'Literal[' + ', '.join(repr(x) for x in values) + ']'
                if any(isinstance(x, float) for x in schema['enum']):
                    # typing.Literal excludes float. Runtime enum validation retains
                    # the precise permitted values while static typing admits float.
                    return 'Union[' + literal + ', float]' if values else 'float'
                return literal
            kind = schema.get('type')
            if isinstance(kind, list):
                return 'Union[' + ', '.join(type_for({**schema, 'type': t}, name + str(i)) for i, t in enumerate(kind)) + ']'
            if kind == 'object' or 'properties' in schema:
                if name not in created:
                    created.add(name)
                    props = []
                    properties = dict(schema.get('properties', {}))
                    for key in schema.get('required', []): properties.setdefault(key, {})
                    for key, child in properties.items():
                        hint = type_for(child, name + ''.join(s.title() for s in re.split(r'[^a-zA-Z0-9]+', key)))
                        if key in schema.get('required', []): hint = 'Required[' + hint + ']'
                        props.append(repr(key) + ': ' + hint)
                    definitions.append(name + ' = TypedDict(' + repr(name) + ', {' + ', '.join(props) + '}, total=False)')
                return repr(name)
            if kind == 'array': return 'list[' + type_for(schema.get('items', {}), name + 'Item') + ']'
            return {'string': 'str', 'number': 'Union[int, float]', 'integer': 'int', 'boolean': 'bool', 'null': 'None'}.get(kind, 'JSONValue')

        for name, schema in schemas.items():
            hint = type_for(schema, name)
            if name not in created:
                created.add(name); definitions.append(name + ': TypeAlias = ' + hint)
        for route, item in doc['paths'].items():
            for verb, operation in item.items():
                if not isinstance(operation, dict) or 'operationId' not in operation: continue
                oid = operation['operationId']
                if module == 'api1_fiscal': client, method = 'Nfe', re.sub(r'^(nfe|fiscal)', '', oid)
                elif module == 'api1_b2b': client, method = 'Reseller', oid.removeprefix('b2bV1')
                elif module == 'api1_files': client, method = 'NfeFiles', re.sub(r'^(nfe|fiscal)', '', oid)
                elif module == 'api2_emitter_files': client, method = 'EmitterFiles', oid.removeprefix('file')
                elif module == 'api2_reports': client, method = 'ReportFiles', re.sub(r'^(nfe|fiscal)', '', oid)
                elif module.startswith('api2_monitor'): client, method = 'Monitor', oid.removeprefix('monitor')
                else: client, method = 'Emitter', oid.removeprefix('emitter')
                method = snake(method)
                body = operation.get('requestBody', {}).get('content', {}).get('application/json', {}).get('schema')
                bodytype = type_for(body, oid + 'Request') if body is not None else None
                params = operation.get('parameters', []) + item.get('parameters', [])
                query = {'type': 'object', 'properties': {p['name']: p['schema'] for p in params if p['in'] == 'query'}, 'additionalProperties': False, 'required': [p['name'] for p in params if p['in'] == 'query' and p.get('required')]}
                if query['properties']: type_for(query, oid + 'Query')
                binary = any(c.get('schema', {}).get('format') == 'binary' for k, v in operation['responses'].items() if k.startswith('2') for c in v.get('content', {}).values())
                returns = [v['content']['application/json']['schema'] for k, v in operation['responses'].items() if k.startswith('2') and 'application/json' in v.get('content', {})]
                documented_redirect = binary and operation['responses'].get('302', {}).get('headers', {}).get('Location', {}).get('required') is True
                restype = 'FileResponse | FileRedirectResponse' if documented_redirect else 'FileResponse' if binary else type_for({'anyOf': returns}, oid + 'Response') if returns else 'JSONValue'
                if not binary:
                    definitions.append(oid + 'Response: TypeAlias = ' + restype)
                    restype = repr(oid + 'Response')
                # Literal annotations retain type identity while preventing dependency cycles.
                def annotation(expr): return 'm.' + expr[1:-1] if expr.startswith("'") else expr
                args = ['self']
                if body is not None: args.append('request: ' + annotation(bodytype))
                args.append('*')
                for p in params:
                    if p['in'] == 'path':
                        pname = oid + p['name'].title() + 'Parameter'
                        definitions.append(pname + ': TypeAlias = ' + type_for(p['schema'], pname + 'Value'))
                        args.append(p['name'] + ': m.' + pname)
                if query['properties']: args.append('query: m.' + oid + 'Query | None = None')
                if client.endswith('Files'): args.append('auth: FileAuth')
                args.append('options: CallOptions | None = None')
                pathargs = '{' + ', '.join(repr(p['name']) + ': ' + p['name'] for p in params if p['in'] == 'path') + '}'
                qarg = 'query' if query['properties'] else 'None'
                barg = 'request' if body is not None else 'UNSET'
                aarg = 'auth' if client.endswith('Files') else 'None'
                code = '\n    def ' + method + '(' + ', '.join(args) + ') -> ' + (annotation(restype) if restype.startswith("'") else restype) + ':\n'
                code += '        """' + operation.get('summary', oid).replace('"', "'").replace('\n', ' ') + '. Contract conditions remain applicable."""\n'
                code += '        return self._execute(' + repr(oid) + ', ' + barg + ', ' + pathargs + ', ' + qarg + ', options, ' + aarg + ')\n'
                methods[client].append((module, code))
                operation_index[oid] = {'module': module, 'path': route, 'verb': verb.upper(), 'client': client, 'method': method, 'query_schema': query}
        header = '"""Generated from ' + path + '; SHA256 ' + records[-1]['sha256'] + '. Do not edit."""\nfrom typing import Literal, Required, TypedDict, TypeAlias, Union\nfrom ..types import JSONValue\nfrom ..model_types import bind_types as _bind_types\n\n'
        names = [line.split(' = ', 1)[0].split(':', 1)[0] for line in definitions]
        outputs['src/webmania/generated/' + module + '.py'] = header + '\n\n'.join(definitions) + '\n\n_bind_types(globals(), __name__, ' + repr(names) + ')\n'
        model_count += len(definitions)
    for client, entries in methods.items():
        imports = []
        chunks = []
        # A unique module alias per generated method avoids duplicate schema-name collisions.
        for i, (module, code) in enumerate(entries):
            alias = 'm' + str(i)
            imports.append('from . import ' + module + ' as ' + alias)
            chunks.append(code.replace('m.', alias + '.'))
        outputs['src/webmania/generated/' + snake(client) + '_methods.py'] = '"""Generated explicit methods. Do not edit."""\nfrom __future__ import annotations\nfrom typing import Any, ForwardRef, Literal, Union\nfrom ..types import UNSET, JSONValue, CallOptions, FileAuth, FileResponse, FileRedirectResponse\n' + '\n'.join(imports) + '\n\nclass ' + client + 'Methods:\n    _execute: Any\n' + ''.join(chunks)
    outputs['src/webmania/contracts/operations.json'] = json.dumps(operation_index, ensure_ascii=False, indent=2) + '\n'
    outputs['src/webmania/generated/__init__.py'] = '"""Typed models for each pinned public contract module."""\n'
    lock = {'schema_version': 2, 'source_repository': 'https://github.com/webmaniabr/webmania-openapi', 'contract_digest': digest, 'operation_count': len(operation_index), 'model_count': model_count, 'inputs': records}
    outputs['contracts.lock.json'] = json.dumps(lock, indent=2) + '\n'
    outputs['src/webmania/contracts/lock.json'] = outputs['contracts.lock.json']
    for target, text in outputs.items():
        file = ROOT / target
        data = text.encode('utf-8')
        if check:
            if not file.exists() or file.read_bytes() != data: raise SystemExit('Generated output differs: ' + target)
        else:
            file.parent.mkdir(parents=True, exist_ok=True); file.write_bytes(data)
    print(json.dumps({'operations': len(operation_index), 'models': model_count, 'check': check}))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, required=True, help='webmania-openapi Git checkout')
    p.add_argument('--revision', default='HEAD', help='Git revision of the checkout to read (default HEAD)')
    p.add_argument('--check', action='store_true')
    a = p.parse_args()
    run(a.source, a.revision, a.check)
