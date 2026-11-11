"""Conservative classic-xref PDF subset with resolved Catalog/Pages graph."""
import re

WHITE = b'\x00\t\n\x0c\r '
DELIM = WHITE + b'()<>[]{}/%'


class Parser:
    def __init__(self, data):
        if len(data) > 4 * 1024 * 1024: raise ValueError('PDF byte bound.')
        self.data = data
        self.tokens = 0

    def skip(self, p):
        while p < len(self.data):
            if self.data[p] in WHITE: p += 1
            elif self.data[p] == 37:
                end = re.search(rb'[\r\n]', self.data[p:])
                p = p + end.end() if end else len(self.data)
            else: break
        return p

    def word(self, p):
        p = self.skip(p); end = p
        while end < len(self.data) and self.data[end] not in DELIM: end += 1
        if end == p: raise ValueError('Expected PDF word.')
        return self.data[p:end], end

    def value(self, p, depth=0):
        self.tokens += 1
        if depth > 64 or self.tokens > 100000: raise ValueError('PDF value bound.')
        p = self.skip(p)
        if p >= len(self.data): raise ValueError('Truncated PDF value.')
        data = self.data
        if data[p:p+2] == b'<<':
            result = {}; p += 2
            while True:
                p = self.skip(p)
                if data[p:p+2] == b'>>': return result, p+2
                key, p = self.value(p, depth+1)
                if not isinstance(key, tuple) or key[0] != 'name' or key[1] in result: raise ValueError('Ambiguous PDF dictionary.')
                result[key[1]], p = self.value(p, depth+1)
        if data[p:p+1] == b'[':
            result = []; p += 1
            while True:
                p = self.skip(p)
                if data[p:p+1] == b']': return result, p+1
                child, p = self.value(p, depth+1); result.append(child)
        if data[p:p+1] == b'/':
            end = p+1
            while end < len(data) and data[end] not in DELIM: end += 1
            name = data[p+1:end]
            if re.search(rb'#(?![0-9a-fA-F]{2})', name): raise ValueError('Malformed PDF name.')
            name = re.sub(rb'#([0-9a-fA-F]{2})', lambda m: bytes([int(m[1],16)]), name)
            return ('name', name.decode('latin-1')), end
        if data[p:p+1] == b'(':
            p += 1; nesting = 1
            while p < len(data) and nesting:
                char = data[p]; p += 1
                if char == 92:
                    if p >= len(data): break
                    if data[p:p+2] == b'\r\n': p += 2
                    else: p += 1
                elif char == 40: nesting += 1
                elif char == 41: nesting -= 1
                if nesting > 64: raise ValueError('PDF string depth.')
            if nesting: raise ValueError('Unterminated PDF string.')
            return b'[opaque string]', p
        if data[p:p+1] == b'<':
            end = data.find(b'>',p+1)
            if end < 0 or re.search(rb'[^0-9a-fA-F\x00\t\n\x0c\r ]',data[p+1:end]): raise ValueError('Malformed PDF hex string.')
            return b'[opaque hex]', end+1
        word, end = self.word(p)
        if re.fullmatch(rb'[+-]?\d+', word):
            if len(word) > 16: raise ValueError('PDF integer bound.')
            number = int(word)
            try:
                second, q = self.word(end)
                third, r = self.word(q)
                if re.fullmatch(rb'\d+', second) and third == b'R':
                    generation = int(second)
                    if number < 1 or generation > 65535: raise ValueError('PDF reference bound.')
                    return ('ref',number,generation), r
            except ValueError: pass
            return number, end
        if re.fullmatch(rb'[+-]?(?:\d+\.\d*|\.\d+)',word): return float(word), end
        if word in (b'true',b'false'): return word == b'true', end
        if word == b'null': return None, end
        raise ValueError('Unsupported PDF value.')


def pdf_document(data):
    if not re.match(rb'%PDF-1\.[0-7](?:\r\n|\n|\r)',data): raise ValueError('Unsupported PDF header.')
    parser = Parser(data)
    match = re.search(rb'startxref\s+(\d+)\s+%%EOF[\x00\t\n\x0c\r ]*$',data)
    if not match: raise ValueError('Missing classic PDF end record.')
    entries = {}; sections = {}; trailers = []; active = set()
    def xref(offset):
        if offset in active or len(active) >= 16 or data[offset:offset+4] != b'xref': raise ValueError('Invalid classic xref chain.')
        active.add(offset); p = offset+4; table = {}
        while True:
            p = parser.skip(p)
            if data[p:p+7] == b'trailer':
                trailer, end = parser.value(p+7)
                if not isinstance(trailer,dict) or not isinstance(trailer.get('Size'),int) or trailer['Size'] > 2049 or any(k in trailer for k in ['XRefStm']): raise ValueError('Unsupported trailer.')
                sections[offset] = end; trailers.append(trailer)
                for number, value in table.items(): entries.setdefault(number,value)
                previous = trailer.get('Prev')
                if previous is not None:
                    if type(previous) is not int or previous >= offset or previous < 0: raise ValueError('Invalid Prev.')
                    xref(previous)
                return
            first, p = parser.word(p); count, p = parser.word(p)
            if not first.isdigit() or not count.isdigit() or len(first)>5 or len(count)>5: raise ValueError('Invalid xref subsection.')
            first, count = int(first),int(count)
            if count > 2049 or first+count > 2049: raise ValueError('Xref object bound.')
            for number in range(first,first+count):
                off,p = parser.word(p); generation,p = parser.word(p); state,p = parser.word(p)
                if not off.isdigit() or len(off)>10 or not generation.isdigit() or len(generation)>5 or state not in [b'n',b'f'] or number in table: raise ValueError('Malformed xref entry.')
                table[number] = (int(off),int(generation),state)
    xref(int(match[1]))
    root = next((t['Root'] for t in trailers if 'Root' in t),None)
    if any('Encrypt' in t for t in trailers): raise ValueError('Protected PDF.')
    objects = {}; resolving = set(); starts = set(); physical_xrefs = set()
    def object_at(number, generation):
        key=(number,generation)
        if key in objects: return objects[key]
        if key in resolving or len(resolving)>64: raise ValueError('Cyclic object.')
        entry=entries.get(number)
        if entry is None or entry[1] != generation or entry[2] != b'n': raise ValueError('Unresolved live reference.')
        p=entry[0]
        header=re.match(rb'(\d+)\s+(\d+)\s+obj(?=[\x00\t\n\x0c\r /<\[(])',data[p:])
        if not header or (int(header[1]),int(header[2])) != key: raise ValueError('Xref/object disagreement.')
        resolving.add(key)
        value,end=parser.value(p+header.end())
        end=parser.skip(end); stream=False
        if data[end:end+6] == b'stream':
            if not isinstance(value,dict): raise ValueError('Invalid stream dictionary.')
            stream=True; length=value.get('Length')
            if isinstance(length,tuple) and length[0]=='ref': length=object_at(length[1],length[2])[0]
            if type(length) is not int or length<0 or length>len(data): raise ValueError('Unsupported stream length.')
            end+=6
            if data[end:end+2]==b'\r\n': end+=2
            elif data[end:end+1] in [b'\r',b'\n']: end+=1
            else: raise ValueError('Missing stream EOL.')
            end+=length
            if data[end:end+2]==b'\r\n': end+=2
            elif data[end:end+1] in [b'\r',b'\n']: end+=1
            if data[end:end+9]!=b'endstream': raise ValueError('Stream length disagreement.')
            end=parser.skip(end+9)
        if data[end:end+6]!=b'endobj' or end+6<len(data) and data[end+6] not in DELIM: raise ValueError('Missing endobj.')
        if isinstance(value,dict) and value.get('Type') in [('name','ObjStm'),('name','XRef')]: raise ValueError('Unsupported object/xref stream.')
        resolving.remove(key); objects[key]=(value,stream,end+6)
        return objects[key]
    # Walk physical top-level boundaries: an xref offset into a string, comment
    # or stream cannot masquerade as an object or prior xref section.
    p=data.find(b'\n')+1 if b'\n' in data[:16] else data.find(b'\r')+1
    while True:
        p=parser.skip(p)
        if p>=len(data): break
        if p in sections:
            physical_xrefs.add(p); p=sections[p]; continue
        if data[p:p+9]==b'startxref':
            word,p=parser.word(p+9)
            if not word.isdigit(): raise ValueError('Invalid startxref.')
            continue
        header=re.match(rb'(\d+)\s+(\d+)\s+obj\b',data[p:])
        if not header: raise ValueError('Unsupported physical PDF structure.')
        key=(int(header[1]),int(header[2])); starts.add(p)
        # Older revised objects are parsed using their physical location too.
        saved=entries.get(key[0]); cached=objects.pop(key,None)
        entries[key[0]]=(p,key[1],b'n')
        value,stream,end=object_at(*key)
        if saved is None: entries.pop(key[0],None)
        else: entries[key[0]]=saved
        if cached is None: objects.pop(key,None)
        else: objects[key]=cached
        p=end
        if len(starts)>2048: raise ValueError('PDF object bound.')
    if physical_xrefs != set(sections) or any(off not in starts for off,_,state in entries.values() if state==b'n'): raise ValueError('Nonphysical xref target.')
    def resolve(value):
        if not isinstance(value,tuple) or value[0]!='ref': raise ValueError('Expected indirect object.')
        obj,stream,_=object_at(value[1],value[2])
        if stream: raise ValueError('Structural object cannot be a stream.')
        return obj
    catalog=resolve(root)
    if not isinstance(catalog,dict) or catalog.get('Type')!=('name','Catalog'): raise ValueError('Expected live Catalog.')
    visited=set()
    def pages(ref,parent=None,media=None,resources=None,depth=0):
        if depth>64 or ref in visited: raise ValueError('Cyclic page tree.')
        visited.add(ref); node=resolve(ref)
        if not isinstance(node,dict) or parent is not None and node.get('Parent')!=parent: raise ValueError('Page parent disagreement.')
        media=node.get('MediaBox',media); resources=node.get('Resources',resources)
        if node.get('Type')==('name','Pages'):
            kids=node.get('Kids'); count=node.get('Count')
            if not isinstance(kids,list) or type(count) is not int or count<1: raise ValueError('Invalid Pages.')
            actual=sum(pages(child,ref,media,resources,depth+1) for child in kids)
            if count!=actual: raise ValueError('Page Count disagreement.')
            return actual
        if node.get('Type')!=('name','Page'): raise ValueError('Expected Page.')
        if isinstance(media,tuple): media=resolve(media)
        if isinstance(resources,tuple): resources=resolve(resources)
        if not isinstance(media,list) or len(media)!=4 or any(type(x) not in [int,float] for x in media) or media[0]>=media[2] or media[1]>=media[3] or not isinstance(resources,dict): raise ValueError('Missing effective Page fields.')
        return 1
    pages(catalog.get('Pages'))
