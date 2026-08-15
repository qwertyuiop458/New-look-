#!/usr/bin/env python3
"""TEST-001: REAL RUNTIME — INPUT + STATE + ENTITY TRACE.

BOOT -> MENU -> NEW GAME -> PROFILE -> CHARACTER SELECT -> LOADING -> GAMEPLAY

Реальный оригинальный JAR (SHA-256 1111f12b...) через FreeJ2ME SDL (Anbu),
инструментирование — внешнее, через JDWP (jar не модифицируется; используется
отдельная копия instrumented.jar). Клавиши — через sdl_interface stub
(5-байтовые пакеты в stderr, протокол верифицирован по байткоду Anbu).

Использование:
  python3 test_001_driver.py prepare|smoke|flow|all
"""
import os, sys, json, time, shutil, subprocess, socket, hashlib, struct

ROOT = "/home/user/New-look-/research/runtime"
JAR_ORIG = os.path.join(ROOT, "jar", "original.jar")
JAR_INST = os.path.join(ROOT, "jar", "instrumented.jar")
JAR_SHA = "1111f12bd94e5693bbdd9acab4726e5b543730b9137504af1e8a8ecb09f00d4e"
EMU_JAR = os.path.join(ROOT, "tools", "freej2me-sdl.jar")
JAVA = os.path.join(ROOT, "tools", "nodejdk", "node_modules",
                    "@spcookie", "erii-runtime-linux-x64", "jdk-17.0.19+10-jre", "bin", "java")
JDB_PORT = 18765
CTRL_PORT = 18766
EVID = os.path.join(ROOT, "evidence", "real", "test-001")
RES = os.path.join(ROOT, "results", "test-001")

sys.path.insert(0, ROOT)
from jdwp import JDWP, Writer

# ---------------- keymap (useFlag=0, верифицирован по Anbu.getMobileKey) ----------------
KEYMAP = {
    "UP": 1073741906, "DOWN": 1073741905, "LEFT": 1073741904, "RIGHT": 1073741903,
    "FIRE": 13, "DIGIT_0": 48, "DIGIT_1": 49, "DIGIT_2": 50, "DIGIT_3": 51,
    "DIGIT_4": 52, "DIGIT_5": 53, "DIGIT_6": 54, "DIGIT_7": 55, "DIGIT_8": 56,
    "DIGIT_9": 57, "STAR": 42, "POUND": 35,
    "SOFT_LEFT": -6, "SOFT_RIGHT": -7, "BACK": 27, "QUIT": -1,
}
NOT_DELIVERABLE = {"SOFT_LEFT", "SOFT_RIGHT"}

class Emu:
    def __init__(self):
        self.proc = None
        self.jdwp = None
        self.ctrl = None
        self.classes = {}

    def start(self, logfile):
        os.makedirs(RES, exist_ok=True)
        env = dict(os.environ)
        env["SDL_OUT_DIR"] = EVID
        env["SDL_LOG"] = os.path.join(RES, "sdl_interface.log")
        env["SDL_CTRL_PORT"] = str(CTRL_PORT)
        env["SDL_SAVE_EVERY"] = "30"
        env["SDL_SAVE_FIRST"] = "3"
        cmd = [
            JAVA,
            f"-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=127.0.0.1:{JDB_PORT}",
            "-Djava.library.path=" + os.path.join(ROOT, "tools"),
            "-cp", EMU_JAR,
            "org.recompile.freej2me.Anbu",
            "file://" + JAR_INST, "240", "320", "1",
        ]
        self.proc = subprocess.Popen(
            cmd, cwd=ROOT, env=env,
            stdout=open(logfile, "wb"), stderr=subprocess.STDOUT)
        deadline = time.time() + 60
        while time.time() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError(f"emulator exited early rc={self.proc.returncode}")
            try:
                self.jdwp = JDWP("127.0.0.1", JDB_PORT, timeout=5)
                break
            except OSError:
                time.sleep(0.5)
        if self.jdwp is None:
            raise RuntimeError("JDWP connect failed")
        self.jdwp.vm_version()
        deadline = time.time() + 60
        while time.time() < deadline:
            try:
                cls = self.jdwp.all_classes()
                if "Lg;" in cls and "Lf;" in cls:
                    self.classes = cls
                    return
            except Exception:
                pass
            time.sleep(0.5)
        raise RuntimeError("game classes not loaded")

    def ctrl_cmd(self, cmd, timeout=3):
        if self.ctrl is None:
            self.ctrl = socket.create_connection(("127.0.0.1", CTRL_PORT), timeout=5)
            self.ctrl.settimeout(timeout)
        self.ctrl.sendall((cmd + "\n").encode())
        return self.ctrl.recv(256).decode().strip()

    def key(self, name, hold=0.06):
        code = KEYMAP[name]
        if name in NOT_DELIVERABLE:
            raise ValueError(f"{name} not deliverable by emulator key pipeline (see input-protocol.md)")
        self.ctrl_cmd(f"KEY {code} 1")
        time.sleep(hold)
        self.ctrl_cmd(f"KEY {code} 0")

    def stop(self):
        try:
            if self.jdwp:
                self.jdwp.cmd(1, 10)  # VM.Exit
        except Exception:
            pass
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.proc.kill()


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def prepare():
    os.makedirs(EVID, exist_ok=True)
    os.makedirs(RES, exist_ok=True)
    assert sha(JAR_ORIG) == JAR_SHA, "ORIGINAL JAR INTEGRITY FAILED"
    shutil.copyfile(JAR_ORIG, JAR_INST)
    assert sha(JAR_INST) == JAR_SHA
    print("jar ok:", JAR_SHA)
    for d in (EVID, RES):
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)
    return {"jar_sha256": JAR_SHA, "instrumented_jar": JAR_INST,
            "instrumentation": "JDWP external (jar bytes unchanged)"}


def snap_global(jdwp, gid, fmap):
    ids = [fmap["state"], fmap["sub"], fmap["bB"], fmap["bC"], fmap["bF"],
           fmap["by"], fmap["bz"], fmap["ey"], fmap["ez"], fmap["u"], fmap["v"],
           fmap["aF"], fmap["x"], fmap["w"], fmap["dm"], fmap["dn"], fmap["T"], fmap["U"]]
    vals = jdwp.get_static(gid, ids)
    return {
        "state": vals[0][1], "sub": vals[1][1], "bB": vals[2][1], "bC": vals[3][1],
        "bF": vals[4][1], "by": vals[5][1], "bz": vals[6][1],
        "ey": vals[7][1], "ez": vals[8][1], "u": vals[9][1], "v": vals[10][1],
        "aF": vals[11][1], "x": vals[12][1], "w": vals[13][1],
        "dm": vals[14][1], "dn": vals[15][1], "T": vals[16][1], "U": vals[17][1],
    }


def snap_entities(jdwp, gid, fmap, grid_names, fids, cids):
    """Прочитать все 12 сеток сущностей f[][][] — полный снимок.
    Чтения во время перестроения мира (загрузка миссии) могут падать —
    такие ячейки пропускаются."""
    entities = []
    debug = os.environ.get("SDL_DEBUG_ENTITIES")
    for gname in grid_names:
        try:
            grid_val = jdwp.get_static(gid, [fmap["grid_" + gname]])[0]
        except Exception as e:
            if debug: print(f'  DBG {gname}: get_static ERR {e}')
            continue
        grid_id = grid_val[1]
        if not grid_id:
            continue
        try:
            n1 = jdwp.array_length(grid_id)
        except Exception as e:
            if debug: print(f'  DBG {gname}: len ERR {e}')
            continue
        # Структура (установлена экспериментально): grid[mission][map] = f[]
        # — третий уровень: список сущностей карты.
        for i1 in range(n1):
            try:
                _, row1 = jdwp.array_values(grid_id, i1, 1)
            except Exception:
                continue
            aid = row1[0][1]
            if not aid:
                continue
            try:
                n2 = jdwp.array_length(aid)
            except Exception:
                continue
            # пакетное чтение всей строки карт (минимизация JDWP-трафика)
            try:
                _, row2_all = jdwp.array_values(aid, 0, n2)
            except Exception:
                continue
            for i2, cell in enumerate(row2_all):
                try:
                    earr = cell[1]
                    if not earr:
                        continue
                    ne = jdwp.array_length(earr)
                    if ne <= 0:
                        continue
                    _, ent_all = jdwp.array_values(earr, 0, ne)
                except Exception as e:
                    if debug: print(f'  DBG {gname}[{i1}][{i2}]: list ERR {e}')
                    continue
                for i3, ent in enumerate(ent_all):
                    try:
                        fid = ent[1]
                        if not fid:
                            continue
                        vals = jdwp.obj_fields(fid, [fids["L"], fids["g"], fids["a"], fids["K"], fids["M"]])
                        L = vals[0][1]; garr = vals[1][1]; pos = vals[2][1]
                        K = vals[3][1]; M = vals[4][1]
                        props = None
                        if garr:
                            ln = jdwp.array_length(garr)
                            if ln > 0:
                                _, pv = jdwp.array_values(garr, 0, ln)
                                props = [v[1] for v in pv]
                        x = y = None
                        if pos:
                            pv = jdwp.obj_fields(pos, [cids["x"], cids["y"]])
                            x = pv[0][1]; y = pv[1][1]
                        entities.append({
                            "grid": gname, "i": i1, "j": i2, "k": i3, "L": L, "K": K, "M": M,
                            "props": props, "x": x, "y": y,
                        })
                    except Exception as e:
                        if debug: print(f'  DBG {gname}[{i1}][{i2}][{i3}]: ent ERR {type(e).__name__} {e}')
                        continue
    return entities


def build_field_maps(jdwp, gid, fid, cid):
    """(name, desc)-пары уникальны в байткоде (проверено по classfile g.class);
    state/substate = поля (a,I)/(b,I), в которые пишет g.d(II)V."""
    gf = {}
    for fid_, name, sig, mod in jdwp.fields(gid):
        if sig == "I" and name in ("a", "b", "aF", "bB", "bC", "bF", "by", "bz", "ey", "ez",
                                   "u", "v", "x", "w", "dm", "dn", "T", "U"):
            gf[name] = fid_
        if sig == "[[[Lf;":
            gf["grid_" + name] = fid_
    gf["state"] = gf["a"]
    gf["sub"] = gf["b"]
    ff = {}
    for fid_, name, sig, mod in jdwp.fields(fid):
        if name == "L" and sig == "I":
            ff["L"] = fid_
        elif name == "g" and sig == "[I":
            ff["g"] = fid_
        elif name == "a" and sig == "Lc;":
            ff["a"] = fid_
        elif name in ("K", "M") and sig == "I":
            ff[name] = fid_
    cc = {}
    for fid_, name, sig, mod in jdwp.fields(cid):
        if name == "a" and sig == "I":
            cc["x"] = fid_
        elif name == "b" and sig == "I":
            cc["y"] = fid_
    return gf, ff, cc


def latest_frame():
    p = os.path.join(EVID, "latest.png")
    if os.path.exists(p):
        return p
    return None


def smoke(emu):
    """INPUT SMOKE TEST: key -> sdl_interface -> emulator -> received key."""
    gid = emu.classes["Lg;"][1]
    fid = emu.classes["Lf;"][1]
    cid = emu.classes["Lc;"][1]
    gf, ff, cc = build_field_maps(emu.jdwp, gid, fid, cid)
    timer_sig = "Lorg/recompile/freej2me/Anbu$SDL$SDLKeyTimerTask;"
    tid = emu.classes.get(timer_sig)
    timer_mid = None
    if tid:
        for mid, name, sig, mod in emu.jdwp.methods(tid[1]):
            if name == "run" and sig == "()V":
                timer_mid = mid
                break
    result = {
        "test": "input-smoke-test", "timestamp": time.time(),
        "runtime": "FreeJ2ME SDL (Anbu) x86 JRE17",
        "emulator": "freej2me-sdl.jar",
        "jar_sha256": sha(JAR_INST),
    }
    try:
        r = emu.ctrl_cmd("PING")
        result["control_channel"] = {"status": "OK" if r == "PONG" else "BAD", "reply": r}
    except Exception as e:
        result["control_channel"] = {"status": "ERROR", "error": str(e)}
    req = None
    if timer_mid:
        req = emu.jdwp.set_breakpoint(tid[1], timer_mid, 0x89, suspend=0)
        result["breakpoint"] = {"class": timer_sig, "method": "run()V",
                                "code_index": "0x89 (putfield code)", "request_id": req}
    before = snap_global(emu.jdwp, gid, gf)
    emu.key("FIRE", hold=0.15)
    time.sleep(0.6)
    events = emu.jdwp.drain_events(timeout=0.5)
    parsed = []
    for ev in events:
        parsed.extend(emu.jdwp.parse_composite(ev))
    if req is not None:
        try:
            emu.jdwp.cmd(15, 2, Writer().u4(req).b)
        except Exception:
            pass
    after = snap_global(emu.jdwp, gid, gf)
    result["sent"] = {"key": "FIRE", "code": KEYMAP["FIRE"],
                      "packet_hex": "press: 01 00 00 00 0d | release: 00 00 00 00 0d"}
    result["received"] = {
        "key_packet_breakpoint_hits": len(parsed),
        "events": parsed,
        "state_before": before, "state_after": after,
    }
    result["verdict"] = ("KEY_RECEIVED" if parsed else "NO_EVIDENCE")
    result["alive"] = emu.proc.poll() is None
    return result


def save_evidence(label):
    lp = latest_frame()
    if lp:
        dst = os.path.join(EVID, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar", "jar_sha256": sha(JAR_INST),
                "test_id": "TEST-001"}
        with open(dst + ".json", "w") as f:
            json.dump(meta, f, indent=1)
        return dst
    return None


def flow(emu, script):
    """Прогнать сценарий с адаптивными примитивами."""
    gid = emu.classes["Lg;"][1]
    fid = emu.classes["Lf;"][1]
    cid = emu.classes["Lc;"][1]
    gf, ff, cc = build_field_maps(emu.jdwp, gid, fid, cid)
    grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))
    traces = []
    entities_log = []
    snapshots = []
    t0 = time.time()
    prev = None

    def sample(tag):
        st = snap_global(emu.jdwp, gid, gf)
        snapshots.append({"t": round(time.time() - t0, 3), "tag": tag, "global": st})
        return st

    def trace_changes(cur, tag):
        nonlocal prev
        if prev is None:
            prev = cur
            return
        for k in ("state", "sub", "bB", "bC", "bF", "by", "bz", "u", "v", "aF",
                  "x", "w", "dm", "dn", "T", "U"):
            if prev.get(k) != cur.get(k):
                traces.append({"t": round(time.time() - t0, 3), "field": k,
                               "old_value": prev.get(k), "new_value": cur.get(k),
                               "source": tag})
        prev = cur

    def wait(t, tag):
        deadline = time.time() + t
        while time.time() < deadline:
            time.sleep(0.25)
            trace_changes(sample(tag), tag)

    def wait_until(field, value, tag, timeout=30):
        deadline = time.time() + timeout
        while time.time() < deadline:
            time.sleep(0.25)
            s = sample(tag)
            trace_changes(s, tag)
            if s.get(field) == value:
                return True
        return False

    def key_step(key, hold=0.06, gap=0.4):
        emu.key(key, hold=hold)
        time.sleep(gap)
        s = sample(key)
        trace_changes(s, key)
        return s

    def nav_to(target_v, key="DOWN", max_presses=20):
        """Навигация по меню: жать key пока v != target.

        Особенности реального рантайма (наблюдённые):
        * нажатия при x==0 (меню неактивно) теряются, но переводят меню в x==1;
        * часть нажатий даёт серию из 5 шагов (артефакт конвейера кадров
          эмулятора) — курсор проходит 2->3->4->5->6->7 за ~100мс;
        * поэтому после КАЖДОГО нажатия опрашиваем v с частотой ~30мс,
          чтобы поймать целевой пункт во время серии.
        """
        def poll_until_v(target, window):
            t0 = time.time()
            while time.time() - t0 < window:
                s = snap_global(emu.jdwp, gid, gf)
                if s["v"] == target:
                    return True
                time.sleep(0.02)
            return False

        # активируем меню первым нажатием (оно теряется, но x: 0->1, dm: 0->4)
        s = snap_global(emu.jdwp, gid, gf)
        if s.get("x") != 1 or s.get("dm") != 4:
            key_step(key)
            time.sleep(0.6)
        for _ in range(max_presses):
            if snap_global(emu.jdwp, gid, gf)["v"] == target_v:
                return True
            emu.key(key, hold=0.04)
            if poll_until_v(target_v, window=1.2):
                return True
            time.sleep(0.15)
        return snap_global(emu.jdwp, gid, gf)["v"] == target_v

    def entity_snapshot(tag):
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        entities_log.append({"t": round(time.time() - t0, 3), "tag": tag,
                             "count": len(ents), "entities": ents})
        print(f"[flow] {tag}: entities={len(ents)}")
        return ents

    try:
        for step in script:
            act = step.get("action")
            tag = step.get("label", act or "")
            if act == "wait":
                wait(step.get("t", 1.0), tag)
            elif act == "wait_until":
                ok = wait_until(step.get("field"), step.get("value"), tag,
                                step.get("timeout", 30))
                print(f"[flow] {tag}: reached={ok}")
            elif act == "key":
                key_step(step.get("key"), step.get("hold", 0.06), step.get("gap", 0.4))
            elif act == "nav_to":
                ok = nav_to(step.get("target"), step.get("key", "DOWN"),
                            step.get("max", 12))
                print(f"[flow] {tag}: v={snap_global(emu.jdwp, gid, gf)['v']} ok={ok}")
            elif act == "snapshot":
                save_evidence(tag)
                print(f"[flow] {tag}: saved {os.path.join(EVID, tag + '.png')}")
            elif act == "entity_snapshot":
                entity_snapshot(tag)
            elif act == "key_until":
                """Жать key каждые interval секунд, ПОКА field == value (застрявший экран)."""
                ok = False
                for _ in range(step.get("max", 15)):
                    s = snap_global(emu.jdwp, gid, gf)
                    if s.get(step.get("field")) != step.get("value"):
                        ok = True
                        break
                    emu.key(step.get("key"), hold=0.15)
                    time.sleep(step.get("interval", 2.0))
                print(f"[flow] {tag}: left={ok}")
            elif act == "print":
                s = sample(tag)
                print(f"[flow] {tag}: state={s['state']} sub={s['sub']} bB={s['bB']} "
                      f"bC={s['bC']} bF={s['bF']} u={s['u']} v={s['v']} aF={s['aF']} "
                      f"x={s['x']} w={s['w']} dm={s['dm']} dn={s['dn']} T={s['T']} U={s['U']}")
            else:
                print(f"[flow] unknown action {act}")
    except Exception:
        import traceback
        traceback.print_exc()
    # финальный снимок сущностей
    entity_snapshot("final")
    with open(os.path.join(RES, "state-trace.json"), "w") as f:
        json.dump({"test": "TEST-001", "generated": time.time(), "events": traces,
                   "snapshots": snapshots}, f, indent=1, default=str)
    with open(os.path.join(RES, "entity-trace.json"), "w") as f:
        json.dump({"test": "TEST-001", "generated": time.time(), "snapshots": entities_log},
                  f, indent=1, default=str)
    print(f"[flow] traces: {len(traces)} events, {len(snapshots)} snapshots, "
          f"{len(entities_log)} entity snapshots")
    return traces, snapshots, entities_log


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    if stage in ("prepare", "all"):
        prep = prepare()
        print(json.dumps(prep, indent=1))
    if stage in ("smoke", "flow", "all"):
        emu = Emu()
        stdout_log = os.path.join(RES, "runtime-stdout.log")
        try:
            emu.start(stdout_log)
            print("[emu] started, classes loaded")
            if stage in ("smoke", "all"):
                res = smoke(emu)
                with open(os.path.join(RES, "input-smoke-test.json"), "w") as f:
                    json.dump(res, f, indent=1, default=str)
                print("[smoke]", json.dumps(res.get("verdict"), default=str))
            if stage in ("flow", "all"):
                script_path = os.path.join(RES, "flow-script.json")
                if not os.path.exists(script_path):
                    script_path = os.path.join(ROOT, "test-001-flow.json")
                with open(script_path) as f:
                    script = json.load(f)
                flow(emu, script)
        finally:
            emu.stop()

if __name__ == "__main__":
    main()
