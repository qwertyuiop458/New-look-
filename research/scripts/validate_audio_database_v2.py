#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_audio_database_v2.py — валидация аудио (этап 15.23)."""
import json, sys
from pathlib import Path
AU = Path("research/analysis/v2/audio")
ERR = []
def err(m): ERR.append(m)
def load(p):
    f = AU / p
    if not f.exists(): err(f"нет {p}"); return None
    return json.loads(f.read_text(encoding="utf-8"))
def main():
    api = load("media-api-index-v2.json")
    res = load("audio-resource-inventory-v2.json")
    st = load("sound-table-v2.json")
    ea = load("event-audio-map-v2.json")
    if api and len(api["calls"]) < 5: err("API вызовов < 5")
    if res:
        if len(res["midi"]) < 10: err(f"MIDI < 10 ({len(res['midi'])})")
        if len(res["wav"]) < 10: err(f"WAV < 10 ({len(res['wav'])})")
    if st and len(st["sounds"]) < 8: err("звуков < 8")
    if ea and len(ea["events"]) < 8: err("событий < 8")
    print("=" * 60); print("VALIDATE AUDIO V2"); print("=" * 60)
    if ERR:
        for e in ERR: print("  x", e)
        print(f"РЕЗУЛЬТАТ: FAIL — {len(ERR)}"); return 1
    print("РЕЗУЛЬТАТ: PASS — структура согласована"); return 0
if __name__ == "__main__":
    sys.exit(main())
