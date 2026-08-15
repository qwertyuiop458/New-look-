#!/usr/bin/env python3
"""Минимальный парсер Java class-файлов + дизассемблер.

Используется для верификации протокола FreeJ2ME Anbu/SDL и анализа
точек инструментирования (research/runtime). Ничего не модифицирует.
"""
import struct, sys, io

# --- constant pool tags ---
TAG = {1:'Utf8',3:'Integer',4:'Float',5:'Long',6:'Double',7:'Class',8:'String',
       9:'Fieldref',10:'Methodref',11:'InterfaceMethodref',12:'NameAndType',
       15:'MethodHandle',16:'MethodType',17:'Dynamic',18:'InvokeDynamic',19:'Module',20:'Package'}

class ClassFile:
    def __init__(self, data):
        self.data = data
        self.cp = []          # constant pool: list of (tag, info)
        self.methods = []     # list of dicts
        self.fields = []
        self.this_class = None
        self.super_class = None
        self.parse()

    def u1(self, f): return f.read(1)[0]
    def u2(self, f): return struct.unpack('>H', f.read(2))[0]
    def u4(self, f): return struct.unpack('>I', f.read(4))[0]

    def parse(self):
        f = io.BytesIO(self.data)
        magic = self.u4(f)
        assert magic == 0xCAFEBABE, hex(magic)
        self.minor = self.u2(f); self.major = self.u2(f)
        cp_count = self.u2(f)
        i = 1
        while i < cp_count:
            tag = self.u1(f)
            if tag == 1:
                ln = self.u2(f)
                val = f.read(ln).decode('utf-8', 'replace')
                self.cp.append((tag, val))
            elif tag in (3, 4):
                self.cp.append((tag, self.u4(f)))
            elif tag in (5, 6):
                self.cp.append((tag, self.u8(f)))
                self.cp.append(None)  # second slot of Long/Double
                i += 1
            elif tag in (7, 8, 16, 19, 20):
                self.cp.append((tag, self.u2(f)))
            elif tag in (9, 10, 11, 12, 17, 18):
                self.cp.append((tag, (self.u2(f), self.u2(f))))
            elif tag == 15:
                self.cp.append((tag, (self.u1(f), self.u2(f))))
            else:
                raise ValueError(f'unknown tag {tag} at cp {i}')
            i += 1
        self.access = self.u2(f)
        self.this_class = self.u2(f)
        self.super_class = self.u2(f)
        iface_count = self.u2(f)
        self.interfaces = [self.u2(f) for _ in range(iface_count)]
        field_count = self.u2(f)
        for _ in range(field_count):
            self.fields.append(self.parse_member(f))
        method_count = self.u2(f)
        for _ in range(method_count):
            self.methods.append(self.parse_member(f))

    def u8(self, f): return struct.unpack('>Q', f.read(8))[0]

    def parse_member(self, f):
        m = {'access': self.u2(f), 'name_idx': self.u2(f), 'desc_idx': self.u2(f),
             'attrs': []}
        n = self.u2(f)
        for _ in range(n):
            an = self.u2(f); ln = self.u4(f)
            m['attrs'].append((an, f.read(ln)))
        return m

    def utf(self, idx):
        t, v = self.cp[idx-1]
        assert t == 1, t
        return v

    def name(self, m): return self.utf(m['name_idx'])
    def desc(self, m): return self.utf(m['desc_idx'])

    def get_code(self, m):
        for an, av in m['attrs']:
            if self.utf(an) == 'Code':
                return av
        return None

    def className(self):
        return self.utf(self.cp[self.this_class-1][1])

    def method_ref(self, idx):
        t, (cls, nt) = self.cp[idx-1]
        cname = self.utf(self.cp[cls-1][1])
        nt = self.cp[nt-1]
        nt_name = self.utf(nt[1][0])
        nt_desc = self.utf(nt[1][1])
        return cname, nt_name, nt_desc


def parse_code(cf, m):
    """Возвращает (max_stack, max_locals, code_bytes, exception_table, attrs)."""
    code = cf.get_code(m)
    f = io.BytesIO(code)
    max_stack = cf.u2(f); max_locals = cf.u2(f)
    code_len = cf.u4(f)
    code_bytes = f.read(code_len)
    exc_len = cf.u2(f)
    exc = []
    for _ in range(exc_len):
        exc.append((cf.u2(f), cf.u2(f), cf.u2(f), cf.u2(f)))
    n = cf.u2(f)
    attrs = []
    for _ in range(n):
        an = cf.u2(f); ln = cf.u4(f)
        attrs.append((cf.utf(an), f.read(ln)))
    return max_stack, max_locals, code_bytes, exc, attrs


OPS = {
    0x02:'iconst_m1',0x03:'iconst_0',0x04:'iconst_1',0x05:'iconst_2',
    0x06:'iconst_3',0x07:'iconst_4',0x08:'iconst_5',
    0x09:'lconst_0',0x0a:'lconst_1',0x0b:'fconst_0',0x0c:'fconst_1',
    0x0d:'fconst_2',0x0e:'dconst_0',0x0f:'dconst_1',
    0x10:'bipush',0x11:'sipush',
    0x12:'ldc', 0x13:'ldc_w', 0x14:'ldc2_w',
    0x15:'iload', 0x16:'lload', 0x17:'fload', 0x18:'dload', 0x19:'aload',
    0x1a:'iload_0',0x1b:'iload_1',0x1c:'iload_2',0x1d:'iload_3',
    0x1e:'lload_0',0x1f:'lload_1',0x20:'lload_2',0x21:'lload_3',
    0x22:'fload_0',0x23:'fload_1',0x24:'fload_2',0x25:'fload_3',
    0x26:'dload_0',0x27:'dload_1',0x28:'dload_2',0x29:'dload_3',
    0x2a:'aload_0',0x2b:'aload_1',0x2c:'aload_2',0x2d:'aload_3',
    0x2e:'iaload',0x2f:'laload',0x30:'faload',0x31:'daload',
    0x32:'aaload',0x33:'baload',0x34:'caload',0x35:'saload',
    0x36:'istore',0x37:'lstore',0x38:'fstore',0x39:'dstore',0x3a:'astore',
    0x3b:'istore_0',0x3c:'istore_1',0x3d:'istore_2',0x3e:'istore_3',
    0x3f:'lstore_0',0x40:'lstore_1',0x41:'lstore_2',0x42:'lstore_3',
    0x43:'fstore_0',0x44:'fstore_1',0x45:'fstore_2',0x46:'fstore_3',
    0x47:'dstore_0',0x48:'dstore_1',0x49:'dstore_2',0x4a:'dstore_3',
    0x4b:'astore_0',0x4c:'astore_1',0x4d:'astore_2',0x4e:'astore_3',
    0x53:'iastore',0x54:'lastore',0x55:'fastore',0x56:'dastore',0x57:'aastore',
    0x58:'bastore',0x59:'castore',0x5a:'sastore',
    0x60:'iadd',0x61:'ladd',0x62:'fadd',0x63:'dadd',0x64:'isub',0x65:'lsub',
    0x66:'fsub',0x67:'dsub',0x68:'imul',0x69:'lmul',0x6a:'fmul',0x6b:'dmul',
    0x6c:'idiv',0x6d:'ldiv',0x6e:'fdiv',0x6f:'ddiv',0x70:'irem',0x71:'lrem',
    0x72:'frem',0x73:'drem',0x74:'ineg',0x75:'lneg',0x76:'fneg',0x77:'dneg',
    0x78:'ishl',0x79:'lshl',0x7a:'ishr',0x7b:'lshr',0x7c:'iushr',0x7d:'lushr',
    0x7e:'iand',0x7f:'land',0x80:'ior',0x81:'lor',0x82:'ixor',0x83:'lxor',
    0x84:'iinc',0x85:'i2l',0x86:'i2f',0x87:'i2d',0x88:'l2i',0x89:'l2f',0x8a:'l2d',
    0x8b:'f2i',0x8c:'f2l',0x8d:'f2d',0x8e:'d2i',0x8f:'d2l',0x90:'d2f',0x91:'i2b',
    0x92:'i2c',0x93:'i2s',
    0x94:'lcmp',0x95:'fcmpl',0x96:'fcmpg',0x97:'dcmpl',0x98:'dcmpg',
    0x99:'ifeq',0x9a:'ifne',0x9b:'iflt',0x9c:'ifge',0x9d:'ifgt',0x9e:'ifle',
    0x9f:'if_icmpeq',0xa0:'if_icmpne',0xa1:'if_icmplt',0xa2:'if_icmpge',
    0xa3:'if_icmpgt',0xa4:'if_icmple',0xa5:'if_acmpeq',0xa6:'if_acmpne',
    0xa7:'goto',0xa8:'jsr',0xa9:'ret',
    0xac:'ireturn',0xad:'lreturn',0xae:'freturn',0xaf:'dreturn',0xb0:'areturn',
    0xb1:'return',
    0xb2:'getstatic',0xb3:'putstatic',0xb4:'getfield',0xb5:'putfield',
    0xb6:'invokevirtual',0xb7:'invokespecial',0xb8:'invokestatic',
    0xb9:'invokeinterface',0xba:'invokedynamic',
    0xbb:'new',0xbc:'newarray',0xbd:'anewarray',0xbe:'arraylength',0xbf:'athrow',
    0xc0:'checkcast',0xc1:'instanceof',0xc2:'monitorenter',0xc3:'monitorexit',
    0xc4:'wide',0xc5:'multianewarray',0xc6:'ifnull',0xc7:'ifnonnull',
    0xc8:'goto_w',0xc9:'jsr_w',
}

def disasm(cf, code_bytes, label_mode='offsets'):
    """Простой дизассемблер; возвращает список (offset, mnemonic, operand)."""
    out = []
    i = 0
    n = len(code_bytes)
    while i < n:
        op = code_bytes[i]
        off = i
        if op == 0x00: out.append((off, 'nop', None)); i += 1; continue
        name = OPS.get(op, f'op_{op:02x}')
        if op in (0x10,):  # bipush
            out.append((off, name, code_bytes[i+1])); i += 2
        elif op == 0x11:   # sipush
            out.append((off, name, struct.unpack('>h', code_bytes[i+1:i+3])[0])); i += 3
        elif op in (0x12,):
            out.append((off, name, code_bytes[i+1])); i += 2
        elif op in (0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x36,0x37,0x38,0x39,0x3a,
                    0xb2,0xb3,0xb4,0xb5,0xb6,0xb7,0xb8,0xbb,0xc0,0xc1,0xc5):
            out.append((off, name, struct.unpack('>H', code_bytes[i+1:i+3])[0])); i += 3
        elif op in (0x99,0x9a,0x9b,0x9c,0x9d,0x9e,0x9f,0xa0,0xa1,0xa2,0xa3,0xa4,
                    0xa5,0xa6,0xa7,0xa8,0xc6,0xc7):
            out.append((off, name, struct.unpack('>h', code_bytes[i+1:i+3])[0])); i += 3
        elif op == 0xb9:
            out.append((off, name, struct.unpack('>H', code_bytes[i+1:i+3])[0])); i += 5
        elif op == 0xba:
            out.append((off, name, struct.unpack('>H', code_bytes[i+1:i+3])[0])); i += 5
        elif op == 0xbc:
            out.append((off, name, code_bytes[i+1])); i += 2
        elif op == 0x84:   # iinc
            out.append((off, name, (code_bytes[i+1], code_bytes[i+2]))); i += 3
        elif op == 0xaa:   # tableswitch
            pad = (4 - ((i + 1) % 4)) % 4
            j = i + 1 + pad
            default = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
            lo = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
            hi = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
            cases = []
            for k in range(lo, hi+1):
                cases.append(f'{k}:{off + struct.unpack(">i", code_bytes[j:j+4])[0]}'); j += 4
            out.append((off, 'tableswitch', f'default->{off+default} ' + ' '.join(cases)))
            i = j
        elif op == 0xab:   # lookupswitch
            pad = (4 - ((i + 1) % 4)) % 4
            j = i + 1 + pad
            default = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
            npairs = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
            cases = []
            for k in range(npairs):
                key = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
                tgt = struct.unpack('>i', code_bytes[j:j+4])[0]; j += 4
                cases.append(f'{key}->{off+tgt}')
            out.append((off, 'lookupswitch', f'default->{off+default} ' + ' '.join(cases)))
            i = j
        elif op == 0xc4:   # wide
            out.append((off, 'wide', None)); i += 1
        elif op in (0x1a,0x1b,0x1c,0x1d,0x2a,0x2b,0x2c,0x2d,0x3b,0x3c,0x3d,0x3e,
                    0x4b,0x4c,0x4d,0x4e):
            out.append((off, name, None)); i += 1
        elif op == 0xa9:
            out.append((off, name, code_bytes[i+1])); i += 2
        elif op in (0xc8, 0xc9):
            out.append((off, name, struct.unpack('>i', code_bytes[i+1:i+5])[0])); i += 5
        elif op in (0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6a,0x6b,
                    0x6c,0x6d,0x6e,0x6f,0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,
                    0x78,0x79,0x7a,0x7b,0x7c,0x7d,0x7e,0x7f,0x80,0x81,0x82,0x83,
                    0x85,0x86,0x87,0x88,0x89,0x8a,0x8b,0x8c,0x8d,0x8e,0x8f,0x90,
                    0x91,0x92,0x93,0x94,0x95,0x96,0x97,0x98,0xac,0xad,0xae,0xaf,
                    0xb0,0xb1,0xbe,0xbf,0xc2,0xc3):
            out.append((off, name, None)); i += 1
        else:
            out.append((off, f'op_{op:02x}', None)); i += 1
    return out


def main():
    path = sys.argv[1]
    data = open(path, 'rb').read()
    cf = ClassFile(data)
    print(f'class {cf.className()} major={cf.major}')
    if len(sys.argv) > 2:
        want = sys.argv[2]
        for m in cf.methods:
            name = cf.name(m)
            desc = cf.desc(m)
            if name == want or (want == '*' and name not in ('<init>',)):
                print(f'--- method {name}{desc}')
                code = cf.get_code(m)
                if code is None:
                    print('    (abstract/native)')
                    continue
                ms, ml, cb, exc, attrs = parse_code(cf, m)
                print(f'    max_stack={ms} max_locals={ml} code_len={len(cb)}')
                for off, mn, op in disasm(cf, cb):
                    if op is not None:
                        if mn in ('invokevirtual','invokestatic','invokespecial','invokeinterface','getstatic','putstatic','getfield','putfield','new','ldc','ldc_w','checkcast','instanceof','anewarray'):
                            if mn.startswith('invoke') or mn in ('getstatic','putstatic','getfield','putfield'):
                                try:
                                    c, n2, d2 = cf.method_ref(op)
                                    opstr = f'{c}.{n2}{d2}'
                                except Exception:
                                    opstr = f'cp#{op}'
                            else:
                                t, v = cf.cp[op-1]
                                if t == 7:
                                    opstr = cf.utf(v)
                                elif t == 8:
                                    opstr = repr(cf.utf(v))
                                else:
                                    opstr = f'cp#{op}'
                        elif mn in ('ifeq','ifne','goto','if_icmpeq','if_icmpne','ifnull','ifnonnull','if_icmplt','if_icmpgt','if_icmple','if_icmpge','iflt','ifge','ifgt','ifle'):
                            opstr = f'->{off+op}'
                        else:
                            opstr = str(op)
                        print(f'    {off:04d}: {mn} {opstr}')
                    else:
                        print(f'    {off:04d}: {mn}')
    else:
        print('fields:')
        for fl in cf.fields:
            print(f'  {cf.name(fl)} {cf.desc(fl)}')
        print('methods:')
        for m in cf.methods:
            print(f'  {cf.name(m)}{cf.desc(m)}')

if __name__ == '__main__':
    main()
