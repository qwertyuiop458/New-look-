#!/usr/bin/env python3
import os
import re

LEVELS_DIR = "/home/user/New-look-/research/resources/levels"
TEXT_OUT_DIR = "/home/user/New-look-/research/resources/text"

# CP1251 Cyrillic characters plus some typical punctuation and whitespace
# Cyrillic uppercase/lowercase starts at 192 (\xc0) to 255 (\xff)
CYRILLIC_PATTERN = re.compile(b'[\xc0-\xff\x20-\x3f\x0a\x0d\x21-\x2f\x3a-\x40]{8,}')

def extract_strings_from_segment(seg_path):
    with open(seg_path, 'rb') as f:
        data = f.read()

    strings = []
    # Find Cyrillic runs
    for match in CYRILLIC_PATTERN.findall(data):
        try:
            text = match.decode('cp1251').strip()
            # Clean up and check if contains at least one actual Russian character
            if any(c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' for c in text):
                # Filter out strings with too many dots or garbage
                if len(text) >= 5 and text.count('.') / len(text) < 0.4:
                    strings.append(text)
        except:
            pass
    return strings

def main():
    print("Searching for dialogue and in-game texts in map segments...")
    os.makedirs(TEXT_OUT_DIR, exist_ok=True)
    all_extracted_texts = []

    if not os.path.exists(LEVELS_DIR):
        print(f"Error: levels directory not found at {LEVELS_DIR}")
        return

    for map_dir in sorted(os.listdir(LEVELS_DIR)):
        map_path = os.path.join(LEVELS_DIR, map_dir)
        if not os.path.isdir(map_path):
            continue
            
        map_strings = []
        for file in sorted(os.listdir(map_path)):
            if file.startswith("segment_") and file.endswith(".bin"):
                seg_path = os.path.join(map_path, file)
                strings = extract_strings_from_segment(seg_path)
                if strings:
                    map_strings.append(f"--- {file} ---")
                    for s in strings:
                        map_strings.append(s)

        if map_strings:
            out_file = os.path.join(TEXT_OUT_DIR, f"{map_dir}_texts.txt")
            with open(out_file, 'w', encoding='utf-8') as out_f:
                out_f.write("\n".join(map_strings))
            print(f"  Saved Russian texts of {map_dir} to {out_file}")
            all_extracted_texts.append(f"=== {map_dir} ===")
            all_extracted_texts.extend(map_strings)
            all_extracted_texts.append("\n")

    if all_extracted_texts:
        with open(os.path.join(TEXT_OUT_DIR, "all_texts.txt"), 'w', encoding='utf-8') as out_f:
            out_f.write("\n".join(all_extracted_texts))
        print(f"\nAll extracted texts compiled to {os.path.join(TEXT_OUT_DIR, 'all_texts.txt')}")
    else:
        print("No Russian texts were found.")

if __name__ == "__main__":
    main()
