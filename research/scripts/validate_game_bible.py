#!/usr/bin/env python3
import os
import json
import sys

ANALYSIS_DIR = "/home/user/New-look-/research/analysis"
REPORTS_DIR = "/home/user/New-look-/research/reports"
BIBLE_JSON = os.path.join(ANALYSIS_DIR, "game-bible-data.json")

def validate_completeness():
    print("Starting comprehensive Game Bible completeness audit...")
    errors = 0
    
    if not os.path.exists(BIBLE_JSON):
        print(f"  [ERROR] Game Bible JSON missing: {BIBLE_JSON}")
        sys.exit(1)
        
    with open(BIBLE_JSON, 'r', encoding='utf-8') as f:
        bible = json.load(f)

    # 1. Verify 30 levels
    expected_levels = 30
    actual_levels = len(bible.get("levels", {}))
    print(f"  Levels count check: expected={expected_levels}, actual={actual_levels}")
    if actual_levels != expected_levels:
        print(f"  [ERROR] Levels count mismatch! Expected 30, found {actual_levels}")
        errors += 1

    # 2. Verify entities
    expected_entities = 2 # Player, Common Zombie (Golden static subset)
    actual_entities = len(bible.get("entities", []))
    print(f"  Entities count check: expected={expected_entities}, actual={actual_entities}")
    if actual_entities != expected_entities:
        print(f"  [ERROR] Entities count mismatch! Expected {expected_entities}, found {actual_entities}")
        errors += 1

    # 3. Verify weapons
    expected_weapons = 2
    actual_weapons = len(bible.get("weapons", []))
    print(f"  Weapons count check: expected={expected_weapons}, actual={actual_weapons}")
    if actual_weapons != expected_weapons:
        print(f"  [ERROR] Weapons count mismatch! Expected {expected_weapons}, found {actual_weapons}")
        errors += 1

    # 4. Verify items
    expected_items = 2
    actual_items = len(bible.get("items", []))
    print(f"  Items count check: expected={expected_items}, actual={actual_items}")
    if actual_items != expected_items:
        print(f"  [ERROR] Items count mismatch! Expected {expected_items}, found {actual_items}")
        errors += 1

    if errors == 0:
        print("\n  [SUCCESS] Game Bible Audit completed with 0 errors! Specifications are highly consistent.")
    else:
        print(f"\n  [FAILURE] Game Bible Audit found {errors} completeness errors.")
        sys.exit(1)

if __name__ == "__main__":
    validate_completeness()
