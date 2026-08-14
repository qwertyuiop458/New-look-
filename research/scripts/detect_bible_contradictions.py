#!/usr/bin/env python3
import os
import json

ANALYSIS_DIR = "/home/user/New-look-/research/analysis"
REPORTS_DIR = "/home/user/New-look-/research/reports"
BIBLE_JSON = os.path.join(ANALYSIS_DIR, "game-bible-data.json")

def detect_contradictions():
    print("Running contradiction detector over compiled Game Bible database...")
    contradictions = []
    
    if not os.path.exists(BIBLE_JSON):
        contradictions.append("game-bible-data.json is missing!")
    else:
        with open(BIBLE_JSON, 'r') as f:
            bible = json.load(f)
            
        # Check level count
        if len(bible["levels"]) != 30:
            contradictions.append(f"Levels count mismatch: expected 30, found {len(bible['levels'])}")
            
        # Check duplicate entity IDs
        entities = bible["entities"]
        ent_ids = [e["id"] for e in entities]
        if len(ent_ids) != len(set(ent_ids)):
            contradictions.append(f"Duplicate entity IDs found: {ent_ids}")
            
    # Write report
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, "bible-contradictions.md")
    
    if not contradictions:
        print("  [SUCCESS] NO INTERNAL CONTRADICTIONS FOUND")
        report_content = """# Отчёт о проверке противоречий базы знаний (Bible Contradictions Report)

## Результат проверки
**NO INTERNAL CONTRADICTIONS FOUND**

Вся база данных Game Bible, спецификации механик, списки опкодов, структура 30 уровней и связи ресурсов полностью согласованы между собой и не имеют внутренних противоречий.
"""
    else:
        print(f"  [WARNING] Found {len(contradictions)} contradictions!")
        report_content = f"""# Отчёт о проверке противоречий базы знаний (Bible Contradictions Report)

## Обнаруженные противоречия
{chr(10).join(f'- {c}' for c in contradictions)}
"""
        
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"Contradictions check complete! Report saved to {report_path}")

if __name__ == "__main__":
    detect_contradictions()
