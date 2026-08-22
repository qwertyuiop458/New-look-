#!/usr/bin/env python3
"""TEST-003: подход к тайлу 31 (триггер opcode 147) в mission 03."""
import sys, time, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_003_driver import (Emu, build_maps3, snap_global, set_bB, snap_mo,
                             RES3, read_player)
from test_001_driver import snap_entities

def main():
    emu = Emu()
    try:
        emu.start(os.path.join(RES3, "tile31.log"))
        gid = emu.classes['Lg;'][1]
        gf, ff, cc = build_maps3(emu.jdwp, gid, emu.classes['Lf;'][1], emu.classes['Lc;'][1])
        grid_names = sorted(k[5:] for k in gf if k.startswith('grid_'))
        # скриптовые поля
        bof = bqf = None
        for fid_, name, sig, mod in emu.jdwp.fields(gid):
            if name == 'bO' and sig == 'I': bof = fid_
            if name == 'bQ' and sig == 'I': bqf = fid_
        time.sleep(6)
        for _ in range(8):
            if snap_global(emu.jdwp, gid, gf)['u'] == 0:
                break
            emu.key('FIRE', hold=0.15); time.sleep(2.5)
        emu.key('FIRE', hold=0.15); time.sleep(2)
        emu.key('FIRE', hold=0.15); time.sleep(3)
        for _ in range(4):
            if snap_global(emu.jdwp, gid, gf)['u'] == 9:
                break
            emu.key('FIRE', hold=0.15); time.sleep(2.5)
        emu.key('FIRE', hold=0.15); time.sleep(3)
        set_bB(emu.jdwp, gid, gf, 3)
        t0 = time.time()
        while time.time() - t0 < 120:
            g = snap_global(emu.jdwp, gid, gf)
            if g['bB'] == 0 and g['state'] in (16, 4, 2):
                set_bB(emu.jdwp, gid, gf, 3)
            if g['state'] == 6:
                break
            if g['state'] == 2 and g['sub'] == 1:
                emu.key('FIRE', hold=0.2); time.sleep(0.5)
            else:
                time.sleep(0.005)
        print('mission 3: state', g['state'], 'bB', g['bB'], 'by', g['by'], 'bz', g['bz'])
        # сцена sub 1 -> sub 0 (FIRE)
        t1 = time.time()
        while time.time() - t1 < 120:
            g = snap_global(emu.jdwp, gid, gf)
            if g['sub'] == 0:
                break
            emu.key('FIRE', hold=0.25)
            time.sleep(3)
            mo = snap_mo(emu.jdwp, gid, gf)
            if mo['i'] or mo['cB']:
                print(f'MO во время сцены: i={mo["i"]} cB={mo["cB"]}')
        g = snap_global(emu.jdwp, gid, gf)
        print('sub=', g['sub'])
        def snap():
            g = snap_global(emu.jdwp, gid, gf)
            mo = snap_mo(emu.jdwp, gid, gf)
            bq = emu.jdwp.get_static(gid, [bqf])[0][1] if bqf else None
            bo = emu.jdwp.get_static(gid, [bof])[0][1] if bof else None
            return g, mo, bq, bo
        g, mo, bq, bo = snap()
        print(f'start: sub={g["sub"]} i={mo["i"]} cB={mo["cB"]} bQ={bq} bO={bo}')
        # цель: тайл 31 -> (x=2, y=7)*16 = (32, 112) — и вариации
        targets = [(32, 112), (32, 128), (48, 112), (16, 112), (32, 96)]
        for tx, ty in targets:
            pl = read_player(emu.jdwp, gid, gf, ff, cc)
            if not pl or not pl['x']:
                print('player lost'); break
            print(f'--- moving to ({tx},{ty}) from ({pl["x"]>>14},{pl["y"]>>14})')
            t_end = time.time() + 40
            last_pos = None
            stuck = 0
            while time.time() < t_end:
                g, mo, bq, bo = snap()
                if mo['i'] or mo['cB']:
                    print(f'  MO ACTIVATED: i={mo["i"]} cB={mo["cB"]} cy={mo["cy"]} cz={mo["cz"]} Q={mo["Q"]}')
                    return
                pl = read_player(emu.jdwp, gid, gf, ff, cc)
                if not pl or not pl['x']:
                    break
                dx = tx*16384 - pl['x']; dy = ty*16384 - pl['y']
                d = (dx*dx + dy*dy) ** 0.5
                if d < 12000:
                    print(f'  arrived ({tx},{ty}); waiting...')
                    time.sleep(3)
                    g, mo, bq, bo = snap()
                    print(f'  after wait: i={mo["i"]} cB={mo["cB"]} bQ={bq} bO={bo}')
                    if mo['i']:
                        return
                    break
                key = None
                if abs(dx) > abs(dy):
                    key = 'RIGHT' if dx > 0 else 'LEFT'
                else:
                    key = 'DOWN' if dy > 0 else 'UP'
                emu.key(key, hold=0.3)
                if last_pos == (pl['x']>>14, pl['y']>>14):
                    stuck += 1
                    if stuck >= 6:
                        alt = {'UP':'LEFT','DOWN':'RIGHT','LEFT':'UP','RIGHT':'DOWN'}[key]
                        emu.key(alt, hold=1.0)
                        stuck = 0
                else:
                    stuck = 0
                last_pos = (pl['x']>>14, pl['y']>>14)
                time.sleep(0.15)
        g, mo, bq, bo = snap()
        print(f'FINAL: i={mo["i"]} cB={mo["cB"]} bQ={bq} bO={bo} sub={g["sub"]}')
        # обзор: L10 объекты с необычными props (g[0]!=5 или len>8)
        ents = snap_entities(emu.jdwp, gid, gf, grid_names, ff, cc)
        odd = [e for e in ents if e['L'] == 10 and e['props'] and (e['props'][0] != 5 or len(e['props']) > 10)]
        print('odd L10 (g0!=5 or len>10):', len(odd))
        for e in odd[:10]:
            print('  ', e['grid'], e['i'], e['j'], e['k'], (e['x']>>14, e['y']>>14), (e['props'] or [])[:12])
    finally:
        emu.stop()

if __name__ == '__main__':
    main()
