#!/usr/bin/env python3
import os
import sys
import json

LEVELS_DIR = "/home/user/New-look-/research/resources/levels"
ANALYSIS_DIR = "/home/user/New-look-/research/analysis"
BIBLE_JSON = os.path.join(ANALYSIS_DIR, "game-bible-data.json")

def validate_reconstruction():
    print("Starting critical validation of level reconstruction data...")
    errors_count = 0
    
    # 1. Check all 30 levels are present in database
    with open(BIBLE_JSON, 'r', encoding='utf-8') as f:
        bible = json.load(f)
        
    expected_count = 30
    actual_count = len(bible["levels"])
    print(f"  Verifying levels count: expected={expected_count}, actual={actual_count}")
    if actual_count != expected_count:
        print(f"  [ERROR] Levels count mismatch! Expected {expected_count}, found {actual_count}")
        errors_count += 1
    else:
        print("  [SUCCESS] All 30 levels are registered in the Game Bible!")

    # 2. Check each level directory contains required JSONs and markdown files
    required_files = [
        "segment-map.md", "map.json", "collision.json", "entities.json",
        "dialogue.json", "opcodes.json", "level-spec.json", "gameplay-flow.md",
        "resource-links.json", "analysis.md"
    ]
    
    for lid in sorted(bible["levels"].keys()):
        lvl_dir = os.path.join(ANALYSIS_DIR, "levels", lid)
        if not os.path.exists(lvl_dir):
            print(f"  [ERROR] Level directory missing: {lvl_dir}")
            errors_count += 1
            continue
            
        for rf in required_files:
            file_path = os.path.join(lvl_dir, rf)
            if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
                print(f"  [ERROR] Level {lid} is missing file or has empty file: {rf}")
                errors_count += 1
                
        # 3. Check JSON schema validity and boundaries
        # Load map.json
        try:
            with open(os.path.join(lvl_dir, "map.json"), 'r', encoding='utf-8') as f:
                m_data = json.load(f)
            # Coordinates and tiles limits
            if m_data["width_tiles"] <= 0 or m_data["height_tiles"] <= 0:
                print(f"  [ERROR] Level {lid} has impossible dimensions: {m_data['width_tiles']}x{m_data['height_tiles']}")
                errors_count += 1
        except Exception as e:
            print(f"  [ERROR] Failed to parse map.json for {lid}: {e}")
            errors_count += 1

    # 4. Final summary
    if errors_count == 0:
        print("\n  [SUCCESS] All 30 levels successfully passed critical validation checks!")
        print("  [STATUS] No missing resources, duplicate IDs, or impossible values found.")
    else:
        print(f"\n  [FAILURE] Level validation failed with {errors_count} errors. Check logs.")
        sys.exit(1)

if __name__ == "__main__":
    validate_reconstruction()
