"""Bounded stdlib structural checks; no filesystem extraction or external resolution."""
import io
import posixpath
import re
import struct
import zipfile
import zlib
from urllib.parse import unquote, urlsplit
from xml.parsers import expat
from xml.etree import ElementTree as ET

MAX_PART = 8 * 1024 * 1024
MAX_TOTAL = 32 * 1024 * 1024


def xml_document(data):
    if len(data) > MAX_PART: raise ValueError('XML byte bound.')
    parser = expat.ParserCreate(namespace_separator='}')
    builder = ET.TreeBuilder()
    depth = count = attributes = 0
    def name(value): return '{' + value if '}' in value else value
    def start(tag, attrs):
        nonlocal depth, count, attributes
        depth += 1; count += 1; attributes += len(attrs)
        if depth > 64 or count > 100000 or attributes > 100000 or len(attrs) > 2048: raise ValueError('XML structural bound.')
        builder.start(name(tag), {name(k): v for k, v in attrs.items()})
    def end(tag):
        nonlocal depth
        builder.end(name(tag)); depth -= 1
    def refused(*_): raise ValueError('XML declarations/entities are unsupported.')
    parser.StartElementHandler = start
    parser.EndElementHandler = end
    parser.CharacterDataHandler = builder.data
    parser.StartDoctypeDeclHandler = refused
    parser.EntityDeclHandler = refused
    parser.ExternalEntityRefHandler = refused
    parser.SetParamEntityParsing(expat.XML_PARAM_ENTITY_PARSING_NEVER)
    try: parser.Parse(data, True)
    except expat.ExpatError: raise ValueError('Malformed XML.') from None
    return builder.close()


def zip_parts(data):
    if len(data) > MAX_TOTAL: raise ValueError('Archive byte bound.')
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
        infos = archive.infolist()
        if len(infos) > 2048 or sum(i.file_size for i in infos) > MAX_TOTAL: raise ValueError('Archive expansion bound.')
        names = set(); ranges = []; result = {}
        for item in infos:
            name = item.filename
            if name in names or not name or '\\' in name or '\0' in name or name.startswith('/') or any(x in ['.', '..'] for x in name.split('/')):
                raise ValueError('Ambiguous member name.')
            names.add(name)
            if item.flag_bits & ~0x808 or item.compress_type not in (0, 8) or item.file_size > MAX_PART or item.file_size > max(1048576, item.compress_size * 128):
                raise ValueError('Unsupported or excessive member.')
            offset = item.header_offset
            if offset < 0 or offset + 30 > archive.start_dir: raise ValueError('Invalid member offset.')
            fields = struct.unpack_from('<4s5H3I2H', data, offset)
            sig, version, flags, method, _, _, crc, packed, unpacked, nlen, xlen = fields
            start = offset + 30 + nlen + xlen
            finish = start + item.compress_size
            expected_name = name.encode('utf-8' if flags & 0x800 else 'cp437')
            if sig != b'PK\x03\x04' or flags != item.flag_bits or method != item.compress_type or data[offset+30:offset+30+nlen] != expected_name or finish > archive.start_dir:
                raise ValueError('Local/central disagreement.')
            expected = (item.CRC, item.compress_size, item.file_size)
            if flags & 8:
                if any(a not in (0, b) for a, b in zip((crc, packed, unpacked), expected)): raise ValueError('Descriptor disagreement.')
                position = finish + (4 if data[finish:finish+4] == b'PK\x07\x08' else 0)
                if position + 12 > archive.start_dir or struct.unpack_from('<3I', data, position) != expected: raise ValueError('Invalid data descriptor.')
                finish = position + 12
            elif (crc, packed, unpacked) != expected: raise ValueError('Local/central size or CRC disagreement.')
            ranges.append((offset, finish))
            with archive.open(item) as member: content = member.read(MAX_PART + 1)
            if len(content) != item.file_size: raise ValueError('Inflated size disagreement.')
            result[name] = content
        ranges.sort()
        if any(right > next_left for (_, right), (next_left, _) in zip(ranges, ranges[1:])): raise ValueError('Overlapping members.')
        # Bound and pin the central directory and classic end record.
        cursor = archive.start_dir
        for item in infos:
            if data[cursor:cursor+4] != b'PK\x01\x02' or cursor + 46 > len(data): raise ValueError('Central directory structure.')
            nlen, xlen, clen = struct.unpack_from('<3H', data, cursor + 28)
            disk = struct.unpack_from('<H', data, cursor + 34)[0]
            if disk: raise ValueError('Multi-disk archive.')
            cursor += 46 + nlen + xlen + clen
        if data[cursor:cursor+4] != b'PK\x05\x06' or cursor + 22 > len(data): raise ValueError('Unsupported ZIP directory.')
        disk, startdisk, countdisk, count, size, start, comment = struct.unpack_from('<4H2IH', data, cursor+4)
        if disk or startdisk or countdisk != len(infos) or count != len(infos) or start != archive.start_dir or size != cursor - archive.start_dir or cursor + 22 + comment != len(data):
            raise ValueError('ZIP directory disagreement.')
        return result
    except (zipfile.BadZipFile, NotImplementedError, RuntimeError, UnicodeError, struct.error, EOFError, zlib.error, OSError):
        raise ValueError('Malformed or unsupported ZIP.') from None


CT = 'http://schemas.openxmlformats.org/package/2006/content-types'
REL = 'http://schemas.openxmlformats.org/package/2006/relationships'
MAIN = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
DOC = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
BOOK = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml'
SHEET = 'application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml'
RELTYPE = 'application/vnd.openxmlformats-package.relationships+xml'


def xlsx_package(parts):
    roots = {n: xml_document(v) for n, v in parts.items() if n.endswith(('.xml', '.rels'))}
    ct = roots.get('[Content_Types].xml')
    if ct is None or ct.tag != '{'+CT+'}Types': raise ValueError('Missing content types.')
    defaults = {}; overrides = {}
    for child in ct:
        if child.tag == '{'+CT+'}Default': key, table = child.get('Extension'), defaults
        elif child.tag == '{'+CT+'}Override': key, table = child.get('PartName'), overrides
        else: raise ValueError('Content type namespace.')
        if not key or key in table or not child.get('ContentType'): raise ValueError('Duplicate content type.')
        table[key] = child.get('ContentType')
    def content_type(name): return overrides.get('/'+name, defaults.get(name.rsplit('.',1)[-1]))
    def relationships(name, base):
        root = roots.get(name)
        if root is None or root.tag != '{'+REL+'}Relationships' or content_type(name) != RELTYPE: raise ValueError('Missing relationships.')
        result = {}
        for child in root:
            if child.tag != '{'+REL+'}Relationship' or child.get('TargetMode', 'Internal') != 'Internal': raise ValueError('Unsupported relationship.')
            key, target, kind = child.get('Id'), child.get('Target'), child.get('Type')
            if not key or key in result or not target or not kind: raise ValueError('Ambiguous relationship.')
            decoded = unquote(target)
            parsed = urlsplit(decoded)
            if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or '\\' in decoded or decoded.startswith('/'): raise ValueError('External relationship.')
            target = posixpath.normpath(posixpath.join(base, decoded))
            if target.startswith('../') or target in ['.', '..'] or target not in parts: raise ValueError('Unresolved relationship.')
            result[key] = (kind, target)
        return result
    rootrels = relationships('_rels/.rels', '')
    books = [v for v in rootrels.values() if v[0] in [DOC+'/officeDocument', 'http://purl.oclc.org/ooxml/officeDocument/relationships/officeDocument']]
    if len(books) != 1: raise ValueError('Ambiguous workbook.')
    book = books[0][1]
    workbook = roots.get(book)
    if workbook is None or content_type(book) != BOOK: raise ValueError('Workbook content type.')
    main = workbook.tag.removesuffix('}workbook').removeprefix('{')
    if workbook.tag != '{'+main+'}workbook' or main not in [MAIN, 'http://purl.oclc.org/ooxml/spreadsheetml/main']: raise ValueError('Workbook namespace.')
    doc = DOC if main == MAIN else 'http://purl.oclc.org/ooxml/officeDocument/relationships'
    if books[0][0] != doc+'/officeDocument': raise ValueError('Workbook relationship namespace family.')
    base, basename = posixpath.split(book)
    rels = relationships(posixpath.join(base, '_rels', basename+'.rels'), base)
    sheets = workbook.findall('{'+main+'}sheets')
    if len(sheets) != 1 or not len(sheets[0]): raise ValueError('Missing sheets.')
    seen = set()
    for sheet in sheets[0]:
        key = sheet.get('{'+doc+'}id')
        if sheet.tag != '{'+main+'}sheet' or not key or key in seen or key not in rels: raise ValueError('Sheet relationship identity.')
        seen.add(key)
        kind, target = rels[key]
        if kind != doc+'/worksheet' or content_type(target) != SHEET or roots[target].tag != '{'+main+'}worksheet': raise ValueError('Worksheet graph disagreement.')
    # Wrong-parent/wrong-namespace sheet elements cannot be hidden elsewhere.
    if sum(1 for node in workbook.iter() if node.tag.rsplit('}',1)[-1] == 'sheet') != len(seen): raise ValueError('Sheet parent disagreement.')
