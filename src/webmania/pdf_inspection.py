"""Bounded lexical recognition of PDF encryption entries; absence stays unknown."""
from collections import deque

WHITE = {0, 9, 10, 12, 13, 32}
DELIMITERS = WHITE | set(b'()<>[]{}/%')


def encryption_entry(data):
    """Recognize /Encrypt in trailer or /Type /XRef dictionaries only.

    This is deliberately not a PDF validator. Opaque strings/comments/known
    streams do not count as encryption evidence. Unknown streams stop inspection.
    """
    position = 0
    inspected = 0
    buffered = deque()
    incomplete = False
    bound = min(len(data), 4 * 1024 * 1024)

    def read():
        nonlocal position, inspected, incomplete
        if buffered: return buffered.popleft()
        inspected += 1
        if inspected > 100000: incomplete = True; return None
        while position < bound:
            byte = data[position]
            if byte in WHITE: position += 1; continue
            if byte == 37:
                while position < bound and data[position] not in (10, 13): position += 1
                continue
            break
        if position >= bound:
            if bound < len(data): incomplete = True
            return None
        byte = data[position]; position += 1
        if byte == 40:
            level = 1
            while position < bound and level:
                current = data[position]; position += 1
                if current == 92: position += 1
                elif current == 40: level += 1
                elif current == 41: level -= 1
            if level: incomplete = True
            return ('opaque', '')
        if byte == 60:
            if position < bound and data[position] == 60: position += 1; return ('dict', '')
            while position < bound and data[position] != 62: position += 1
            if position >= bound: incomplete = True
            position += 1
            return ('opaque', '')
        if byte == 62 and position < bound and data[position] == 62: position += 1; return ('enddict', '')
        if byte == 91: return ('array', '')
        if byte == 93: return ('endarray', '')
        name = byte == 47
        word = bytearray() if name else bytearray([byte])
        oversized = False
        while position < bound and data[position] not in DELIMITERS:
            current = data[position]; position += 1
            if name and current == 35 and position + 1 < bound:
                try: current = int(data[position:position + 2], 16); position += 2
                except ValueError: pass
            if len(word) < 64: word.append(current)
            else: oversized = True
        return ('name' if name else 'word', '' if oversized else word.decode('latin-1'))

    frames = []
    trailer = False
    closed_length = None
    token = read()
    while token:
        if incomplete: return False
        kind, value = token
        if kind == 'word' and value == 'stream':
            if frames or closed_length is None: return False
            if position < bound and data[position] == 13: position += 1
            if position >= bound or data[position] != 10: return False
            position += 1
            if closed_length > bound - position: return False
            position += closed_length
            if read() != ('word', 'endstream'): return False
            closed_length = None; trailer = False; token = read(); continue
        closed_length = None
        if kind in ['enddict', 'endarray']:
            if not frames: return False
            frame = frames.pop()
            if (kind == 'enddict') != (frame['kind'] == 'dict'): return False
            if frame['kind'] == 'dict':
                if frame['encrypted'] and (frame['trailer'] or frame['xref']): return True
                if not frames: closed_length = frame.get('length')
            trailer = False; token = read(); continue
        frame = frames[-1] if frames else None
        if frame and frame['kind'] == 'dict':
            if frame['expect_key']:
                if kind != 'name': return False
                frame['key'] = value; frame['expect_key'] = False; token = read(); continue
            reference = False
            if kind == 'word' and value.isdecimal():
                second = read()
                third = read() if second and second[0] == 'word' and second[1].isdecimal() else None
                reference = third == ('word', 'R')
                if not reference:
                    for item in reversed([x for x in [second, third] if x is not None]): buffered.appendleft(item)
            key = frame.get('key')
            if key == 'Encrypt' and (kind == 'dict' or reference): frame['encrypted'] = True
            if key == 'Type' and token == ('name', 'XRef'): frame['xref'] = True
            if key == 'Length' and kind == 'word' and not reference and value.isdecimal(): frame['length'] = int(value)
            frame['expect_key'] = True; frame.pop('key', None)
        if kind in ['dict', 'array']:
            if len(frames) >= 64: return False
            frames.append({'kind': kind, 'expect_key': True, 'trailer': trailer and not frames, 'xref': False, 'encrypted': False})
        trailer = not frames and token == ('word', 'trailer')
        token = read()
    return False
