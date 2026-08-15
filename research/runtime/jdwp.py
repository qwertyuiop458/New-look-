#!/usr/bin/env python3
"""Минимальный JDWP-клиент (Java Debug Wire Protocol) для внешнего трассирования
игры без изменения JAR. Используется TEST-001 (runtime instrumentation).

Поддерживает: handshake, AllClasses, Fields/Methods, GetValues (static/instance),
ArrayReference, breakpoint/method-entry события, resume.
"""
import socket, struct, threading, queue, time

class JDWPError(Exception):
    pass

class Packet:
    __slots__ = ('id', 'flags', 'cmdset', 'cmd', 'data')
    def __init__(self, pid, flags, cmdset, cmd, data):
        self.id, self.flags, self.cmdset, self.cmd, self.data = pid, flags, cmdset, cmd, data

class Reader:
    """Буфер для декодирования JDWP-данных."""
    def __init__(self, data):
        self.d = data; self.p = 0
    def u1(self):
        v = self.d[self.p]; self.p += 1; return v
    def u2(self):
        v = struct.unpack_from('>H', self.d, self.p)[0]; self.p += 2; return v
    def u4(self):
        v = struct.unpack_from('>I', self.d, self.p)[0]; self.p += 4; return v
    def u8(self):
        v = struct.unpack_from('>Q', self.d, self.p)[0]; self.p += 8; return v
    def s(self):
        ln = self.u4()
        v = self.d[self.p:self.p+ln].decode('utf-8', 'replace'); self.p += ln
        return v
    def val(self):
        tag = self.d[self.p]; self.p += 1
        if tag == ord('B'): return ('byte', self.u1())
        if tag == ord('Z'): return ('bool', bool(self.u1()))
        if tag == ord('S'): return ('short', self._i2())
        if tag == ord('C'): return ('char', self.u2())
        if tag == ord('I'): return ('int', self._i4())
        if tag == ord('J'): return ('long', self._i8())
        if tag == ord('F'): return ('float', struct.unpack('>f', self.d[self.p:self.p+4])[0])
        if tag == ord('D'): return ('double', struct.unpack('>d', self.d[self.p:self.p+8])[0])
        if tag == ord('L') or tag == ord('['): return ('obj', self.u8())
        if tag == ord('s'): return ('str', self.u8())
        if tag == ord('V'): return ('void', None)
        raise JDWPError(f'unknown value tag {chr(tag)}')
    def _i2(self):
        v = struct.unpack_from('>h', self.d, self.p)[0]; self.p += 2; return v
    def _i4(self):
        v = struct.unpack_from('>i', self.d, self.p)[0]; self.p += 4; return v
    def _i8(self):
        v = struct.unpack_from('>q', self.d, self.p)[0]; self.p += 8; return v

class Writer:
    def __init__(self):
        self.b = bytearray()
    def u1(self, v): self.b.append(v & 0xff); return self
    def u2(self, v): self.b += struct.pack('>H', v & 0xffff); return self
    def u4(self, v): self.b += struct.pack('>I', v & 0xffffffff); return self
    def u8(self, v): self.b += struct.pack('>Q', v & 0xffffffffffffffff); return self
    def s(self, v):
        raw = v.encode('utf-8', 'replace')
        self.u4(len(raw)); self.b += raw; return self
    def val(self, tag, value):
        self.u1(ord(tag))
        if tag == 'B': self.u1(value)
        elif tag == 'Z': self.u1(1 if value else 0)
        elif tag == 'S': self.u2(value & 0xffff)
        elif tag == 'C': self.u2(value & 0xffff)
        elif tag == 'I': self.u4(value & 0xffffffff)
        elif tag == 'J': self.u8(value & 0xffffffffffffffff)
        elif tag in ('L', '['): self.u8(value & 0xffffffffffffffff)
        elif tag == 's': self.u8(value & 0xffffffffffffffff)
        else: raise JDWPError(f'cannot write tag {tag}')
        return self

class JDWP:
    def __init__(self, host='127.0.0.1', port=8765, timeout=10):
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self.sock.settimeout(0.2)
        self.sock.sendall(b'JDWP-Handshake')
        ack = self.sock.recv(14)
        if ack != b'JDWP-Handshake':
            raise JDWPError(f'bad handshake: {ack!r}')
        self.pid = 1
        self.lock = threading.Lock()
        self.events = queue.Queue()
        self._reader_thread = threading.Thread(target=self._read_loop, daemon=True)
        self._reader_thread.start()
        self.classes = {}   # signature -> typeID
        self.field_ids = {} # (signature, name, desc) -> fieldID
        self.method_ids = {}  # (signature, name, desc) -> methodID

    # ---------- wire ----------
    def _send(self, cmdset, cmd, data):
        with self.lock:
            pid = self.pid; self.pid += 1
            hdr = struct.pack('>IIBBB', 11 + len(data), pid, 0, cmdset, cmd)
            self.sock.sendall(hdr + bytes(data))
        return pid

    def _read_loop(self):
        buf = b''
        while True:
            try:
                chunk = self.sock.recv(65536)
            except socket.timeout:
                continue
            except OSError:
                return
            if not chunk:
                return
            buf += chunk
            while len(buf) >= 11:
                (length,) = struct.unpack_from('>I', buf, 0)
                if len(buf) < length:
                    break
                pkt = buf[:length]
                buf = buf[length:]
                pid, flags = struct.unpack_from('>IB', pkt, 4)
                data = pkt[11:]
                if flags & 0x80:
                    errcode = struct.unpack_from('>H', pkt, 9)[0]
                    self.events.put(('reply', pid, data, errcode))
                else:
                    cmdset, cmd = pkt[8], pkt[9]
                    self.events.put(('event', data))

    def _wait_reply(self, pid, timeout=15):
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                item = self.events.get(timeout=0.5)
            except queue.Empty:
                continue
            if len(item) == 4:
                kind, rpid, data, errcode = item
            else:
                kind, rpid, data = item
                errcode = 0
            if kind == 'reply' and rpid == pid:
                if errcode != 0:
                    raise JDWPError(f'JDWP command error {errcode}')
                return Reader(data)
            else:
                self.events.put(item)
        raise JDWPError('reply timeout')

    def cmd(self, cmdset, cmd, data=b'', timeout=15):
        pid = self._send(cmdset, cmd, data)
        return self._wait_reply(pid, timeout)

    # ---------- VM ----------
    def vm_version(self):
        r = self.cmd(1, 1)
        desc = r.s(); r.u4(); r.u4(); r.s(); r.s()
        return desc

    def all_classes(self):
        r = self.cmd(1, 3)
        n = r.u4()
        out = {}
        for _ in range(n):
            tag = r.u1(); tid = r.u8(); sig = r.s(); status = r.u4()
            out[sig] = (tag, tid, status)
        return out

    def classes_by_signature(self, sig):
        w = Writer().s(sig)
        r = self.cmd(1, 2, w.b)
        n = r.u4()
        out = []
        for _ in range(n):
            tag = r.u1(); tid = r.u8(); status = r.u4()
            out.append((tag, tid, status))
        return out

    def resume(self):
        self.cmd(1, 9)

    # ---------- ReferenceType ----------
    def fields(self, tid):
        r = self.cmd(2, 4, Writer().u8(tid).b)
        n = r.u4()
        out = []
        for _ in range(n):
            fid = r.u8(); name = r.s(); sig = r.s(); mod = r.u4()
            out.append((fid, name, sig, mod))
        return out

    def methods(self, tid):
        r = self.cmd(2, 5, Writer().u8(tid).b)
        n = r.u4()
        out = []
        for _ in range(n):
            mid = r.u8(); name = r.s(); sig = r.s(); mod = r.u4()
            out.append((mid, name, sig, mod))
        return out

    def get_static(self, tid, field_ids):
        w = Writer().u8(tid).u4(len(field_ids))
        for f in field_ids:
            w.u8(f)
        r = self.cmd(2, 6, w.b)
        n = r.u4()
        vals = []
        for _ in range(n):
            vals.append(r.val())
        return vals

    # ---------- ObjectReference ----------
    def obj_fields(self, oid, field_ids):
        w = Writer().u8(oid).u4(len(field_ids))
        for f in field_ids:
            w.u8(f)
        r = self.cmd(9, 2, w.b)
        n = r.u4()
        vals = []
        for _ in range(n):
            vals.append(r.val())
        return vals

    # ---------- ArrayReference ----------
    def array_length(self, aid):
        r = self.cmd(13, 1, Writer().u8(aid).b)
        return r.u4()

    def array_values(self, aid, first, length):
        w = Writer().u8(aid).u4(first).u4(length)
        r = self.cmd(13, 2, w.b)
        # Наблюдаемый формат reply (OpenJDK 17): type-символ (1 байт),
        # затем count u4, затем values: для ссылочных типов — (tag+id),
        # для примитивов — сырые значения без тега.
        typ = chr(r.u1())
        n = r.u4()
        vals = []
        for _ in range(n):
            if typ in ('L', '['):
                vals.append(r.val())
            else:
                # примитив: сырое значение
                if typ == 'B': vals.append(('byte', r.u1()))
                elif typ == 'Z': vals.append(('bool', bool(r.u1())))
                elif typ == 'S': vals.append(('short', r._i2()))
                elif typ == 'C': vals.append(('char', r.u2()))
                elif typ == 'I': vals.append(('int', r._i4()))
                elif typ == 'J': vals.append(('long', r._i8()))
                elif typ == 'F': vals.append(('float', struct.unpack('>f', r.d[r.p:r.p+4])[0])); r.p += 4
                elif typ == 'D': vals.append(('double', struct.unpack('>d', r.d[r.p:r.p+8])[0])); r.p += 8
                else:
                    raise JDWPError(f'unknown array component type {typ}')
        return typ, vals

    # ---------- Events ----------
    def set_breakpoint(self, tid, mid, code_index=0, suspend=0, request_id=None):
        """kind=2 BREAKPOINT; mod=LocationOnly(7): typeTag(1)=2 class, tid, mid, codeIndex(u8)."""
        w = Writer().u1(2).u1(suspend)
        # modifiers count
        w.u4(1)
        w.u1(7)          # LocationOnly
        w.u1(2)          # typeTag: class
        w.u8(tid)
        w.u8(mid)
        w.u8(code_index)
        r = self.cmd(15, 1, w.b)
        return r.u4()

    def set_method_entry(self, tid, suspend=0):
        """kind=4 METHOD_ENTRY; mod=MethodEntryOnly(9): classID."""
        w = Writer().u1(4).u1(suspend)
        w.u4(1)
        w.u1(9)
        w.u8(tid)
        r = self.cmd(15, 1, w.b)
        return r.u4()

    def drain_events(self, timeout=0.1):
        """Собрать накопленные события; вернуть список (raw_data)."""
        out = []
        deadline = time.time() + timeout
        while True:
            try:
                item = self.events.get(timeout=max(0, deadline - time.time()))
            except queue.Empty:
                break
            if len(item) == 4:
                kind, rpid, data, errcode = item
                if kind == 'reply':
                    self.events.put(item)
                else:
                    out.append(data)
            else:
                kind, data = item
                out.append(data)
        return out

    def parse_composite(self, data):
        """Разобрать Event.Composite: вернуть список dict."""
        r = Reader(data)
        suspend = r.u1()
        n = r.u4()
        events = []
        for _ in range(n):
            kind = r.u1(); req = r.u4()
            ev = {'kind': kind, 'request': req, 'suspend': suspend}
            if kind == 2:  # BREAKPOINT
                tag = r.u1(); cls = r.u8(); mid = r.u8(); idx = r.u8()
                ev.update(type_tag=tag, class_id=cls, method_id=mid, code_index=idx)
                ev['thread'] = r.u8()
            elif kind == 4:  # METHOD_ENTRY
                ev['thread'] = r.u8()
                tag = r.u1(); cls = r.u8(); mid = r.u8()
                ev.update(type_tag=tag, class_id=cls, method_id=mid)
            elif kind == 1:  # VM_START
                ev['thread'] = r.u8()
            elif kind == 6:  # THREAD_START
                ev['thread'] = r.u8()
            elif kind == 7:  # THREAD_END
                ev['thread'] = r.u8()
            elif kind == 100:  # VM_DEATH
                pass
            else:
                # неизвестное событие — пропускаем (данные не разбираем дальше)
                pass
            events.append(ev)
        return events
