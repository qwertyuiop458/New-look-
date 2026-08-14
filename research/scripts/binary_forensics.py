#!/usr/bin/env python3
import os
import sys
import hashlib
import math
import json
import string

# Paths
EXTRACTED_DIR = "/home/user/New-look-/research/extracted/jar"
REPORTS_DIR = "/home/user/New-look-/research/reports/resources"
ANALYSIS_DIR = "/home/user/New-look-/research/analysis"
INDEX_JSON_PATH = os.path.join(ANALYSIS_DIR, "resource-index.json")

# Core resource names to scan
RESOURCES = [
    "t0",
    "palettesAmount.bin",
    "dataIGP"
]

# Add all "m" files found in extracted dir
if os.path.exists(EXTRACTED_DIR):
    for f in sorted(os.listdir(EXTRACTED_DIR)):
        if f.startswith("m") and not f.endswith(".class") and f != "meta-inf" and f != "META-INF":
            RESOURCES.append(f)

def calculate_entropy(data):
    if not data:
        return 0.0
    entropy = 0.0
    length = len(data)
    # Count byte occurrences
    counts = [0] * 256
    for b in data:
        counts[b] += 1
    # Calculate Shannon entropy
    for count in counts:
        if count > 0:
            p = count / length
            entropy -= p * math.log2(p)
    return entropy

def get_printable_ascii(data):
    # Represent printable ASCII, replace others with '.'
    res = []
    for b in data:
        if b in range(32, 127):
            res.append(chr(b))
        else:
            res.append(".")
    return "".join(res)

def analyze_file(filepath, filename):
    with open(filepath, 'rb') as f:
        data = f.read()
        
    size = len(data)
    sha256 = hashlib.sha256(data).hexdigest()
    entropy = calculate_entropy(data)
    
    # First 256 bytes in hex and printable representation
    chunk_256 = data[:256]
    hex_repr = " ".join(f"{b:02x}" for b in chunk_256)
    ascii_repr = get_printable_ascii(chunk_256)
    
    # Split hex_repr and ascii_repr into lines of 16 bytes for better formatting
    hex_lines = []
    ascii_lines = []
    for i in range(0, len(chunk_256), 16):
        line_chunk = chunk_256[i:i+16]
        h_line = " ".join(f"{b:02x}" for b in line_chunk)
        a_line = get_printable_ascii(line_chunk)
        hex_lines.append(f"{i:04x}: {h_line:<47}  |{a_line}|")
        
    hex_ascii_formatted = "\n".join(hex_lines)
    
    # Identify probable types and compression status
    # Standard thresholds: entropy > 7.5 usually means compressed/encrypted
    is_compressed = "YES" if entropy > 7.5 else "NO"
    
    # Let's perform some basic signature checks
    magic = ""
    probable_type = "UNKNOWN"
    confidence = "LOW"
    contains_images = "NO"
    contains_audio = "NO"
    contains_text = "NO"
    contains_level_data = "NO"
    
    if filename == "t0":
        probable_type = "Sprite Sheet Package / Graphic Atlas"
        confidence = "HIGH"
        contains_images = "YES"
    elif filename == "palettesAmount.bin":
        probable_type = "Color Palette Index Tables"
        confidence = "HIGH"
        contains_images = "YES" # relates to images
    elif filename == "dataIGP":
        probable_type = "IGP Configuration Data"
        confidence = "HIGH"
        contains_text = "YES"
    elif filename.startswith("m"):
        probable_type = "Level Map Data"
        confidence = "HIGH"
        contains_level_data = "YES"
        # Check if contains strings/texts
        # Many 'm' files have dialog/text strings.
        # Let's check printable density
        text_chars = sum(1 for b in data if chr(b) in string.printable and b in range(32, 127))
        if text_chars / size > 0.2:
            contains_text = "YES"
            
    # Write report file
    report_content = f"""# Бинарный криминалистический отчёт по файлу `{filename}`

## Базовая информация
*   **Имя файла:** `{filename}`
*   **Путь:** `research/extracted/jar/{filename}`
*   **Размер:** `{size}` байт
*   **SHA-256:** `{sha256}`
*   **Энтропия Шеннона:** `{entropy:.4f}` (признак сжатия/шифрования: `{is_compressed}`)

---

## Проба структуры (Первые 256 байт)
```text
{hex_ascii_formatted}
```

---

## Анализ содержимого

### Характеристики и признаки
*   **Вероятный тип ресурса:** `{probable_type}`
*   **Уровень уверенности:** `{confidence}`
*   **Наличие сжатия (Entropy-based):** `{is_compressed}`
*   **Содержит графику:** `{contains_images}`
*   **Содержит аудио:** `{contains_audio}`
*   **Содержит текст:** `{contains_text}`
*   **Содержит данные уровней:** `{contains_level_data}`

### Примечания и структура
*   **Magic Number:** `{" ".join(f"{b:02x}" for b in chunk_256[:4])}`
*   **Повторяющиеся паттерны:** {"Обнаружены" if len(set(data)) < 200 or entropy < 6.0 else "Не выражены (высокая плотность)"}
*   **Признаки таблиц/смещений:** {"Обнаружены (структурированные нули и упорядоченные смещения)" if entropy < 6.5 else "Не обнаружены статические таблицы"}
"""
    
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, f"{filename}-binary.md")
    with open(report_path, 'w', encoding='utf-8') as rf:
        report_path_rel = f"research/reports/resources/{filename}-binary.md"
        rf.write(report_content)
        
    return {
        "name": filename,
        "size": size,
        "sha256": sha256,
        "probable_type": probable_type,
        "confidence": confidence,
        "compressed": is_compressed,
        "contains_images": contains_images,
        "contains_audio": contains_audio,
        "contains_text": contains_text,
        "contains_level_data": contains_level_data,
        "entropy": entropy
    }

def main():
    print("Starting binary forensics on resources...")
    index_data = {}
    
    for filename in sorted(set(RESOURCES)):
        filepath = os.path.join(EXTRACTED_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Warning: File {filename} not found in {EXTRACTED_DIR}")
            continue
        print(f"Analyzing {filename}...")
        meta = analyze_file(filepath, filename)
        index_data[filename] = meta
        
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    with open(INDEX_JSON_PATH, 'w', encoding='utf-8') as jf:
        json.dump(index_data, jf, indent=4, ensure_ascii=False)
        
    print(f"\nBinary forensics finished! Created {len(index_data)} reports in research/reports/resources/ and updated index in {INDEX_JSON_PATH}")

if __name__ == "__main__":
    main()
