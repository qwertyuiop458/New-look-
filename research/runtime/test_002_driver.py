#!/usr/bin/env python3
"""TEST-002: REAL RUNTIME AI + MISSION OBJECT TRACE.

Проверка на живом оригинальном JAR (SHA-256 1111f12b...):
  ENTITY -> AI STATE -> MOVEMENT -> TARGET -> ATTACK -> DAMAGE
  L==10 mission object -> cB -> damage -> completion condition

Инструментирование — внешнее JDWP (jar не изменяется; instrumented.jar
побайтово идентичен оригиналу). Движение игрока — реальные клавиши через
sdl_interface stub (протокол TEST-001).

Фазы:
  prep   — дойти до геймплея (state 6), как в TEST-001
  recon  — разведка: игрок, враги, L==10, g.i/cB
  ai     — AI-трассировка выбранного врага (idle -> approach -> attack)
  mo     — mission object: cB/cy/Q, урон, completion
"""
import os, sys, json, time, shutil, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from test_001_driver import (Emu, build_field_maps, snap_global, snap_entities,
                             KEYMAP, JAR_SHA, RES, EVID, latest_frame)

RES2 = os.path.join(ROOT, "results", "test-002")
EVID2 = os.path.join(ROOT, "evidence", "real", "test-002")

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---------- расширенный снимок ----------

EXTRA_FIELDS = ["cB", "cy", "cz", "cU", "cW", "cY", "cb", "cw", "cS", "bO", "bQ"]

def build_maps2(jdwp, gid, fid, cid):
    gf, ff, cc = build_field_maps(jdwp, gid, fid, cid)
    for fid_, name, sig, mod in jdwp.fields(gid):
        if sig == "I" and name in EXTRA_FIELDS:
            gf[name] = fid_
        if sig == "[I" and name == "Q":
            gf["Q"] = fid_
        if sig == "Lf;" and name == "i":
            gf["i"] = fid_
        if sig == "Lf;" and name == "c":
            gf["player"] = fid_
    return gf, ff, cc

def snap_mo(jdwp, gid, gf):
    """Миссионный объект: g.i, cB, cy, cz, Q[], позиция активного объекта."""
    ids = [gf["i"], gf["cB"], gf["cy"], gf["cz"], gf["Q"],
           gf["cU"], gf["cW"], gf["cY"], gf["cb"], gf["cw"], gf["cS"]]
    vals = jdwp.get_static(gid, ids)
    mo = {"i": vals[0][1], "cB": vals[1][1], "cy": vals[2][1], "cz": vals[3][1],
          "Q": None, "cU": vals[5][1], "cW": vals[6][1], "cY": vals[7][1],
          "cb": vals[8][1], "cw": vals[9][1], "cS": vals[10][1]}
    if vals[4][1]:
        try:
            ln = jdwp.array_length(vals[4][1])
            _, qv = jdwp.array_values(vals[4][1], 0, ln)
            mo["Q"] = [v[1] for v in qv]
        except Exception:
            mo["Q"] = None
    if mo["i"]:
        oid = mo["i"]
        try:
            r = jdwp.cmd(9, 1, __import__("jdwp").Writer().u8(oid).b, timeout=3)
            mo["i_type"] = r.u1()
        except Exception:
            pass
    return mo

def read_entity(jdwp, fids, cids, fid):
    """Прочитать сущность f целиком (props + позиция)."""
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
    return {"L": L, "props": props, "x": x, "y": y, "K": K, "M": M}

def read_player(jdwp, gid, gf, fids, cids):
    """Игрок g.c (Lf;) — HP g[7], позиция."""
    p = jdwp.get_static(gid, [gf["player"]])[0][1]
    if not p:
        return None
    e = read_entity(jdwp, fids, cids, p)
    e["fid"] = p
    return e

def enemies_all(jdwp, gid, gf, fids, cids, grid_names):
    ents = snap_entities(jdwp, gid, gf, grid_names, fids, cids)
    return [e for e in ents if e["L"] == 3]

def dist2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def save_frame(label):
    lp = latest_frame()
    if lp:
        os.makedirs(EVID2, exist_ok=True)
        dst = os.path.join(EVID2, label + ".png")
        shutil.copyfile(lp, dst)
        meta = {"timestamp": time.time(), "runtime": "FreeJ2ME SDL Anbu",
                "emulator": "freej2me-sdl.jar", "jar_sha256": sha(
                    os.path.join(ROOT, "jar", "instrumented.jar")),
                "test_id": "TEST-002"}
        json.dump(meta, open(dst + ".json", "w"), indent=1)
        return dst
    return None

# ---------- фазы ----------

def reach_gameplay(emu, gf, gid):
    """Дойти до геймплея (state 6) — последовательность TEST-001."""
    def st():
        return snap_global(emu.jdwp, gid, gf)
    time.sleep(6)
    for _ in range(8):
        if st()["u"] == 0:
            break
        emu.key("FIRE", hold=0.15)
        time.sleep(2.5)
    emu.key("FIRE", hold=0.15); time.sleep(2)
    emu.key("FIRE", hold=0.15); time.sleep(3)
    for _ in range(4):
        if st()["u"] == 9:
            break
        emu.key("FIRE", hold=0.15); time.sleep(2.5)
    emu.key("FIRE", hold=0.15); time.sleep(3)
    t0 = time.time()
    while st()["state"] != 6 and time.time() - t0 < 90:
        emu.key("FIRE", hold=0.15)
        time.sleep(2.5)
    return st()["state"] == 6

def move_towards(emu, jdwp, gf, fids, cids, gid, target_xy, seconds, key_hold=0.35, gap=0.15):
    """Игрок идёт к точке (x,y) — клавиши по разнице координат (с коррекцией)."""
    t0 = time.time()
    while time.time() - t0 < seconds:
        pl = read_player(jdwp, gid, gf, fids, cids)
        if not pl or not pl["x"]:
            time.sleep(0.2)
            continue
        dx = target_xy[0] - pl["x"]
        dy = target_xy[1] - pl["y"]
        key = None
        if abs(dx) > 20000 and abs(dx) > abs(dy):
            key = "RIGHT" if dx > 0 else "LEFT"
        elif abs(dy) > 20000:
            key = "DOWN" if dy > 0 else "UP"
        if key:
            emu.key(key, hold=key_hold)
        else:
            break
        time.sleep(gap)
    return read_player(jdwp, gid, gf, fids, cids)

def ai_trace_cycle(emu, jdwp, gid, gf, fids, cids, grid_names, enemy_sel, duration,
                   actions=None, label=""):
    """Трассировка врага: снимки каждые ~120 мс + опциональные действия."""
    traces = []
    t0 = time.time()
    def snap(tag):
        e = read_entity(jdwp, fids, cids, enemy_sel)
        pl = read_player(jdwp, gid, gf, fids, cids)
        mo = snap_mo(jdwp, gid, gf)
        g = snap_global(jdwp, gid, gf)
        rec = {
            "t": round(time.time()-t0, 3), "tag": tag,
            "enemy": e, "player": pl, "mo": mo, "global": {k: g[k] for k in
                ("state","sub","bB","bF","by","bz","T","U")},
        }
        traces.append(rec)
        return rec
    end = time.time() + duration
    while time.time() < end:
        snap(label)
        if actions:
            for a in actions:
                a(emu)
        time.sleep(0.12)
    snap(label + "-end")
    return traces

def phase_mo(emu, jdwp, gid, gf, ff, cc, grid_names):
    """MISSION OBJECT: подход к L==10, триггер g.i/cB, урон, completion."""
    out = {"phase": "mission-object"}
    l10 = [e for e in snap_entities(jdwp, gid, gf, grid_names, ff, cc) if e["L"] == 10 and e["x"]]
    pl = read_player(jdwp, gid, gf, ff, cc)
    pxy = (pl["x"], pl["y"])
    if not l10:
        out["error"] = "no L10 entities"
        return out
    target = min(l10, key=lambda e: dist2((e["x"], e["y"]), pxy))
    out["target"] = target
    print("[t2:mo] target L10 at", (target["x"], target["y"]),
          "dist_px=", int((dist2((target["x"], target["y"]), pxy) ** 0.5) / 16384))
    # подход с трассировкой i/cB
    mo_trace = []
    t0 = time.time()
    def mo_snap(tag):
        mo = snap_mo(jdwp, gid, gf)
        pl = read_player(jdwp, gid, gf, ff, cc)
        mo_trace.append({"t": round(time.time()-t0, 3), "tag": tag, "mo": mo,
                         "player_xy": (pl["x"], pl["y"]) if pl else None})
        return mo
    mo_snap("before")
    # идём к цели до 20 секунд, каждые 0.4с снимаем
    t_end = time.time() + 20
    while time.time() < t_end:
        pl = read_player(jdwp, gid, gf, ff, cc)
        if not pl or not pl["x"]:
            break
        dx = target["x"] - pl["x"]; dy = target["y"] - pl["y"]
        d = (dx*dx + dy*dy) ** 0.5
        if d < 50000:
            break
        key = None
        if abs(dx) > abs(dy):
            key = "RIGHT" if dx > 0 else "LEFT"
        else:
            key = "DOWN" if dy > 0 else "UP"
        emu.key(key, hold=0.3)
        mo = mo_snap("approach")
        time.sleep(0.2)
    mo_snap("near")
    save_frame("mission-object")
    print("[t2:mo] near: i=", mo_trace[-1]["mo"]["i"], "cB=", mo_trace[-1]["mo"]["cB"],
          "cy=", mo_trace[-1]["mo"]["cy"])
    # если объект активен (i) — атакуем
    if mo_trace[-1]["mo"]["i"]:
        for shot in range(6):
            before = snap_mo(jdwp, gid, gf)
            emu.key("FIRE", hold=0.15)
            time.sleep(0.7)
            after = snap_mo(jdwp, gid, gf)
            mo_trace.append({"t": round(time.time()-t0, 3), "tag": f"attack-{shot}",
                             "mo": after, "cB_before": before["cB"], "cB_after": after["cB"]})
            print(f"[t2:mo] attack {shot}: cB {before['cB']} -> {after['cB']}")
            if after["cB"] <= 0:
                break
            time.sleep(0.3)
        # дождаться state 7 (completion) если cB <= 0
        g = snap_global(jdwp, gid, gf)
        if after["cB"] <= 0:
            t_end = time.time() + 15
            while time.time() < t_end:
                g = snap_global(jdwp, gid, gf)
                if g["state"] == 7:
                    break
                time.sleep(0.5)
            out["completion"] = {"cB": after["cB"], "state": g["state"],
                                 "observed": g["state"] == 7}
            print("[t2:mo] completion:", out["completion"])
    out["trace"] = mo_trace
    json.dump(out, open(os.path.join(RES2, "mission-object-trace.json"), "w"),
              indent=1, default=str)
    return out


def phase_ai(emu, jdwp, gid, gf, ff, cc, grid_names):
    """AI TRACE: подход к ближайшему врагу, наблюдение state/HP/velocity/timer,
    aggro distance, attack cycle, damage."""
    out = {"phase": "ai"}
    en = [e for e in snap_entities(jdwp, gid, gf, grid_names, ff, cc)
          if e["L"] == 3 and e["x"]]
    pl = read_player(jdwp, gid, gf, ff, cc)
    pxy = (pl["x"], pl["y"])
    # выбираем живого врага (HP>0, state<100), ближайшего по Манхэттену
    def alive(e):
        p = e["props"] or []
        return len(p) > 16 and (p[7] or 0) > 0 and (p[12] or 0) < 100
    live = [e for e in en if alive(e)]
    pool = live if live else en
    enemy = min(pool, key=lambda e: abs(e["x"]-pxy[0]) + abs(e["y"]-pxy[1]))
    out["enemy_selected"] = enemy
    out["enemies_live"] = len(live)
    print("[t2:ai] enemy at", (enemy["x"], enemy["y"]),
          "dist_px=", int((dist2((enemy["x"], enemy["y"]), pxy) ** 0.5) / 16384),
          "hp=", (enemy["props"] or [None]*20)[7], "live_pool=", len(live), "/", len(en))
    # 1) IDLE-наблюдение (враг далеко, до подхода)
    def sel_enemy():
        ents = snap_entities(jdwp, gid, gf, grid_names, ff, cc)
        for e in ents:
            if e["L"] == 3 and e["grid"] == enemy["grid"] and e["i"] == enemy["i"] \
                    and e["j"] == enemy["j"] and e["k"] == enemy["k"] and e["x"]:
                return e
        return None
    idle = []
    t0 = time.time()
    for _ in range(20):
        e = sel_enemy()
        pl = read_player(jdwp, gid, gf, ff, cc)
        if e:
            idle.append({"t": round(time.time()-t0, 3),
                         "state": (e["props"] or [None]*20)[12],
                         "hp": (e["props"] or [None]*20)[7],
                         "v13": (e["props"] or [None]*20)[13],
                         "v14": (e["props"] or [None]*20)[14],
                         "ex": e["x"], "ey": e["y"],
                         "px": pl["x"] if pl else None, "py": pl["y"] if pl else None})
        time.sleep(0.15)
    out["idle"] = idle
    save_frame("enemy-before")
    # 2) APPROACH: идём к врагу, снимаем каждые 0.15с
    approach = []
    t0 = time.time()
    t_end = time.time() + 90
    prev_state = None
    last_pl_xy = None
    stuck_t = 0
    while time.time() < t_end:
        e = sel_enemy()
        pl = read_player(jdwp, gid, gf, ff, cc)
        if not e or not pl or not pl["x"]:
            break
        e = read_entity(jdwp, ff, cc, e["fid"])
        pl = read_player(jdwp, gid, gf, ff, cc)
        dx = e["x"] - pl["x"]; dy = e["y"] - pl["y"]
        d = (dx*dx + dy*dy) ** 0.5
        rec = {"t": round(time.time()-t0, 3), "dist_px": round(d / 16384, 1),
               "state": (e["props"] or [None]*20)[12],
               "hp": (e["props"] or [None]*20)[7],
               "v13": (e["props"] or [None]*20)[13],
               "v14": (e["props"] or [None]*20)[14],
               "timer15": (e["props"] or [None]*20)[15],
               "flags16": (e["props"] or [None]*20)[16],
               "sub10": (e["props"] or [None]*20)[10],
               "ex": e["x"], "ey": e["y"],
               "px": pl["x"], "py": pl["y"],
               "player_hp": (pl["props"] or [None]*20)[7],
               "gs": snap_global(jdwp, gid, gf)}
        approach.append(rec)
        if prev_state is not None and rec["state"] != prev_state:
            print(f"[t2:ai] STATE {prev_state} -> {rec['state']} at dist_px={rec['dist_px']} t={rec['t']}")
        prev_state = rec["state"]
        # движение с анти-застреванием: если игрок не сдвинулся за ~2.5с — обход
        if d > 30000:
            key = None
            if abs(dx) > abs(dy):
                key = "RIGHT" if dx > 0 else "LEFT"
            else:
                key = "DOWN" if dy > 0 else "UP"
            emu.key(key, hold=0.3)
            if last_pl_xy is not None and last_pl_xy == (pl["x"], pl["y"]):
                stuck_t += 1
                if stuck_t >= 8:
                    # обход: перпендикуляр 1.5с
                    alt = {"UP": "LEFT", "DOWN": "RIGHT", "LEFT": "UP", "RIGHT": "DOWN"}[key]
                    emu.key(alt, hold=1.2)
                    stuck_t = 0
            else:
                stuck_t = 0
            last_pl_xy = (pl["x"], pl["y"])
        else:
            # рядом: стоим, ждём атаки
            pass
        time.sleep(0.12)
        if len(approach) % 30 == 0:
            print(f"[t2:ai] ... t={rec['t']} dist={rec['dist_px']} state={rec['state']} "
                  f"ehp={rec['hp']} php={rec['player_hp']}")
    save_frame("enemy-approach")
    out["approach"] = approach
    # 3) ATTACK CYCLE: стоим рядом до 30с, ловим атаку врага
    attack = []
    t0 = time.time()
    t_end = time.time() + 30
    while time.time() < t_end:
        e = sel_enemy()
        pl = read_player(jdwp, gid, gf, ff, cc)
        if not e or not pl:
            break
        e = read_entity(jdwp, ff, cc, e["fid"])
        pl = read_player(jdwp, gid, gf, ff, cc)
        rec = {"t": round(time.time()-t0, 3),
               "state": (e["props"] or [None]*20)[12],
               "hp": (e["props"] or [None]*20)[7],
               "timer15": (e["props"] or [None]*20)[15],
               "player_hp": (pl["props"] or [None]*20)[7],
               "ex": e["x"], "ey": e["y"],
               "px": pl["x"], "py": pl["y"]}
        attack.append(rec)
        time.sleep(0.1)
        if len(attack) % 50 == 0:
            print(f"[t2:ai:attack] t={rec['t']} state={rec['state']} ehp={rec['hp']} "
                  f"php={rec['player_hp']} timer={rec['timer15']}")
    save_frame("enemy-attack")
    out["attack"] = attack
    json.dump(out, open(os.path.join(RES2, "ai-trace.json"), "w"), indent=1, default=str)
    return out


def phase_recon2(emu, jdwp, gid, gf, ff, cc, grid_names):
    """Кандидаты в миссионные объекты: L==10 с g.length>=9 (критерий f.c из g.java:17010)."""
    out = {"phase": "recon2"}
    ents = snap_entities(jdwp, gid, gf, grid_names, ff, cc)
    l10 = [e for e in ents if e["L"] == 10 and e["props"] and len(e["props"]) >= 9]
    pl = read_player(jdwp, gid, gf, ff, cc)
    pxy = (pl["x"], pl["y"]) if pl and pl["x"] else None
    cands = []
    for e in l10:
        rec = {"grid": e["grid"], "i": e["i"], "j": e["j"], "k": e["k"],
               "x": e["x"], "y": e["y"], "g0": e["props"][0], "g1": e["props"][1],
               "glen": len(e["props"]), "props": e["props"][:16]}
        if pxy:
            rec["dist_px"] = round((dist2((e["x"], e["y"]), pxy) ** 0.5) / 16384, 1)
        cands.append(rec)
    cands.sort(key=lambda r: r.get("dist_px", 1e9))
    out["candidates"] = cands
    out["count"] = len(cands)
    print(f"[t2:r2] L10 candidates (len>=9): {len(cands)}")
    for c in cands[:12]:
        print("   ", c["dist_px"], c["g0"], c["g1"], "len=", c["glen"], (c["x"], c["y"]), c["grid"], c["i"], c["j"], c["k"])
    # проверить ближайших 3 кандидатов подходом
    for idx, cand in enumerate(cands[:3]):
        print(f"[t2:r2] approach candidate {idx} at dist {cand.get('dist_px')}")
        t_end = time.time() + 15
        while time.time() < t_end:
            pl = read_player(jdwp, gid, gf, ff, cc)
            if not pl or not pl["x"]:
                break
            dx = cand["x"] - pl["x"]; dy = cand["y"] - pl["y"]
            if (dx*dx + dy*dy) ** 0.5 < 40000:
                break
            key = "RIGHT" if abs(dx) > abs(dy) and dx > 0 else "LEFT" if abs(dx) > abs(dy) else "DOWN" if dy > 0 else "UP"
            emu.key(key, hold=0.3)
            time.sleep(0.15)
        mo = snap_mo(jdwp, gid, gf)
        print(f"[t2:r2] after approach: i={mo['i']} cB={mo['cB']} cy={mo['cy']}")
        out[f"cand_{idx}"] = {"mo": mo}
        if mo["i"]:
            break
        # отойти (чтобы не застрять у объекта)
        t_end = time.time() + 4
        while time.time() < t_end:
            emu.key("LEFT", hold=0.3)
            time.sleep(0.15)
    json.dump(out, open(os.path.join(RES2, "recon2.json"), "w"), indent=1, default=str)
    return out


def phase_ai2(emu, jdwp, gid, gf, ff, cc, grid_names):
    """AI TRACE v2: зигзаг-обход к живому врагу, aggro, attack cycle, damage."""
    out = {"phase": "ai2"}
    en = [e for e in snap_entities(jdwp, gid, gf, grid_names, ff, cc)
          if e["L"] == 3 and e["x"]]
    pl = read_player(jdwp, gid, gf, ff, cc)
    pxy = (pl["x"], pl["y"])
    live = [e for e in en if (e["props"] or []) and len(e["props"]) > 16
            and (e["props"][7] or 0) > 0 and (e["props"][12] or 0) < 100]
    # все враги (HP=0 = не заспавнены, активируются при подходе);
    # приоритет: та же горизонталь (|dy| мал) — путь по прямой
    def score(e):
        dx = abs(e["x"]-pxy[0]); dy = abs(e["y"]-pxy[1])
        return dx + dy * 4
    enemy = min(en, key=score)
    out["enemy_selected"] = enemy
    print("[t2:ai2] enemy:", enemy["grid"], enemy["i"], enemy["j"], enemy["k"],
          (enemy["x"]>>14, enemy["y"]>>14), "hp=", (enemy["props"] or [None]*20)[7],
          "state=", (enemy["props"] or [None]*20)[12])
    # ждём свободного управления: sub==0 (сцена закрывается FIRE)
    t0 = time.time()
    while time.time() - t0 < 150:
        g = snap_global(jdwp, gid, gf)
        if g["sub"] == 0:
            break
        emu.key("FIRE", hold=0.25)
        time.sleep(8)
    print("[t2:ai2] control (sub=0) at t=", round(time.time()-t0, 1))
    trace = []
    t0 = time.time()
    def snap(tag):
        e = None
        ents = snap_entities(jdwp, gid, gf, grid_names, ff, cc)
        for ee in ents:
            if ee["L"] == 3 and ee["grid"] == enemy["grid"] and ee["i"] == enemy["i"] \
                    and ee["j"] == enemy["j"] and ee["k"] == enemy["k"] and ee["x"]:
                e = read_entity(jdwp, ff, cc, ee["fid"])
                break
        pl = read_player(jdwp, gid, gf, ff, cc)
        g = snap_global(jdwp, gid, gf)
        rec = {"t": round(time.time()-t0, 2), "tag": tag,
               "estate": (e["props"] or [None]*24)[12] if e else None,
               "ehp": (e["props"] or [None]*24)[7] if e else None,
               "ev13": (e["props"] or [None]*24)[13] if e else None,
               "ev14": (e["props"] or [None]*24)[14] if e else None,
               "etimer": (e["props"] or [None]*24)[15] if e else None,
               "eflags": (e["props"] or [None]*24)[16] if e else None,
               "esub": (e["props"] or [None]*24)[10] if e else None,
               "ex": e["x"] if e else None, "ey": e["y"] if e else None,
               "px": pl["x"] if pl else None, "py": pl["y"] if pl else None,
               "php": (pl["props"] or [None]*24)[7] if pl else None,
               "T": g["T"], "U": g["U"], "state": g["state"], "sub": g["sub"]}
        trace.append(rec)
        return rec
    # ---- движение зигзагом к цели (до 120с) ----
    t_end = time.time() + 120
    last_pos = None
    stuck = 0
    zig = 0
    while time.time() < t_end:
        r = snap("approach")
        if r["estate"] is None:
            break
        if r["estate"] != 0 and r["estate"] is not None and r["estate"] < 100:
            print(f"[t2:ai2] ENEMY STATE {r['estate']} at t={r['t']} dist=",
                  round(((r["ex"]-r["px"])**2 + (r["ey"]-r["py"])**2)**0.5 / 16384, 1))
            break
        if r["php"] is not None and r["php"] < 200:
            print(f"[t2:ai2] PLAYER DAMAGED php={r['php']} at t={r['t']} estate={r['estate']}")
        dx = r["ex"] - r["px"]; dy = r["ey"] - r["py"]
        d = (dx*dx + dy*dy) ** 0.5
        if d < 60000:
            print(f"[t2:ai2] REACHED enemy at t={r['t']} dist_px={round(d/16384,1)}")
            break
        # зигзаг: основное направление + периодический перпендикуляр
        if abs(dx) > abs(dy):
            main = "RIGHT" if dx > 0 else "LEFT"
        else:
            main = "DOWN" if dy > 0 else "UP"
        key = main
        if stuck >= 6:
            alt = {"UP": "RIGHT", "DOWN": "LEFT", "LEFT": "UP", "RIGHT": "DOWN"}[main] if zig % 2 == 0 \
                else {"UP": "LEFT", "DOWN": "RIGHT", "LEFT": "DOWN", "RIGHT": "UP"}[main]
            emu.key(alt, hold=1.5)
            zig += 1
            stuck = 0
        else:
            emu.key(key, hold=0.35)
        if last_pos == (r["px"], r["py"]):
            stuck += 1
        else:
            stuck = 0
        last_pos = (r["px"], r["py"])
        time.sleep(0.1)
    save_frame("enemy-approach")
    out["approach"] = trace
    # ---- рядом: ждём атаки врага (до 45с) ----
    atk = []
    t0 = time.time()
    t_end = time.time() + 45
    prev_php = None
    while time.time() < t_end:
        r = snap("attack")
        if r["estate"] is None:
            break
        atk.append(r)
        if prev_php is not None and r["php"] is not None and r["php"] < prev_php:
            print(f"[t2:ai2] DAMAGE: php {prev_php} -> {r['php']} at t={r['t']} estate={r['estate']}")
        prev_php = r["php"]
        if r["estate"] is not None and 0 < r["estate"] < 100:
            print(f"[t2:ai2] attack-state {r['estate']} t={r['t']} etimer={r['etimer']} ehp={r['ehp']}")
        time.sleep(0.12)
    save_frame("enemy-attack")
    out["attack"] = atk
    json.dump(out, open(os.path.join(RES2, "ai-trace.json"), "w"), indent=1, default=str)
    return out


def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    os.makedirs(RES2, exist_ok=True)
    os.makedirs(EVID2, exist_ok=True)
    emu = Emu()
    out = {}
    try:
        emu.start(os.path.join(RES2, "runtime-stdout.log"))
        gid = emu.classes["Lg;"][1]
        fid = emu.classes["Lf;"][1]
        cid = emu.classes["Lc;"][1]
        gf, ff, cc = build_maps2(emu.jdwp, gid, fid, cid)
        grid_names = sorted(k[5:] for k in gf if k.startswith("grid_"))
        print("[t2] reaching gameplay...")
        ok = reach_gameplay(emu, gf, gid)
        print("[t2] gameplay:", ok, snap_global(emu.jdwp, gid, gf)["state"])
        if not ok:
            out["status"] = "PARTIAL"
            json.dump(out, open(os.path.join(RES2, "summary.json"), "w"), indent=1)
            return
        time.sleep(3)
        if stage in ("recon2",):
            out["recon2"] = phase_recon2(emu, emu.jdwp, gid, gf, ff, cc, grid_names)
        if stage in ("mo", "all"):
            out["mo"] = phase_mo(emu, emu.jdwp, gid, gf, ff, cc, grid_names)
        if stage in ("ai", "all"):
            out["ai"] = phase_ai2(emu, emu.jdwp, gid, gf, ff, cc, grid_names)
        out["status"] = "done"
        json.dump(out, open(os.path.join(RES2, "summary.json"), "w"), indent=1, default=str)
    finally:
        emu.stop()

if __name__ == "__main__":
    main()
