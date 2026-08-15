#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_runtime_boot.py — валидация первого реального boot (этап 15.29)."""
import json, hashlib, sys
from pathlib import Path
RT = Path("research/runtime")
ERR = []
def err(m): ERR.append(m)
def main():
    # hash
    jar = RT / "jar" / "original.jar"
    if not jar.exists(): err("нет original.jar")
    else:
        h = hashlib.sha256(jar.read_bytes()).hexdigest()
        if h != "1111f12bd94e5693bbdd9acab4726e5b543730b9137504af1e8a8ecb09f00d4e":
            err(f"HASH MISMATCH: {h}")
    # runtime-info
    ri = json.loads((RT/"results/boot/runtime-info.json").read_text())
    if not ri["boot_results"]["status"].startswith("RUNTIME_CONFIRMED"): err("статус не RUNTIME_CONFIRMED")
    if "Zombie Infection" not in ri["boot_results"]["midlet_detected"]: err("MIDlet не найден")
    # boot.log
    log = RT/"results/boot/boot.log"
    if not log.exists(): err("нет boot.log")
    else:
        content = log.read_text()
        if "FRAME_SAVED" not in content: err("нет сохранённых кадров в boot.log")
    # screenshot
    shot = RT/"evidence/real/01_boot.png"
    if not shot.exists(): err("нет 01_boot.png")
    else:
        from PIL import Image
        im = Image.open(shot)
        if im.size != (240, 320): err(f"размер не 240x320: {im.size}")
    # startup-events
    se = json.loads((RT/"results/boot/startup-events.json").read_text())
    if not any(e["event"] == "MIDLET_FOUND" for e in se["events"]): err("нет MIDLET_FOUND")
    print("=" * 60); print("VALIDATE RUNTIME BOOT"); print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}"); return 1
    print("РЕЗУЛЬТАТ: PASS — реальный boot подтверждён (RUNTIME_CONFIRMED)"); return 0
if __name__ == "__main__":
    sys.exit(main())
