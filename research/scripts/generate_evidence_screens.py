#!/usr/bin/env python3
# THIS SCRIPT DOES NOT EXECUTE THE ORIGINAL GAME.
# IT GENERATES SIMULATED/RECONSTRUCTED VISUAL EVIDENCE.
import os
from PIL import Image, ImageDraw, ImageFont

EVIDENCE_DIR = "/home/user/New-look-/research/runtime/simulated-evidence"

def create_screen(title, background_color, filename):
    # Standard vertical 240x320 screen size
    img = Image.new("RGBA", (240, 320), background_color)
    draw = ImageDraw.Draw(img)
    
    # Retro frame / border
    draw.rectangle([0, 0, 239, 319], outline=(0, 0, 0, 255), width=2)
    
    # Bottom softkey bar (HUD style)
    draw.rectangle([0, 290, 240, 320], fill=(20, 20, 20, 255), outline=(40, 40, 40, 255))
    draw.text((10, 298), "Меню", fill=(200, 200, 200, 255))
    draw.text((190, 298), "Назад", fill=(200, 200, 200, 255))
    
    # Top Status Bar
    draw.rectangle([0, 0, 240, 24], fill=(20, 20, 20, 255), outline=(40, 40, 40, 255))
    draw.text((10, 6), "12:00", fill=(150, 150, 150, 255))
    draw.text((180, 6), "[||||]", fill=(0, 255, 0, 255)) # Battery
    
    # Draw specified title inside the screen body
    draw.text((40, 40), title, fill=(255, 255, 255, 255))
    
    img.save(os.path.join(EVIDENCE_DIR, filename))
    print(f"Generated simulated screen: {filename}")

def main():
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    
    # 01 Boot Screen
    create_screen("GAMELOFT\n\n© 2008 Gameloft SA.", (180, 0, 0, 255), "01_boot.png")
    
    # 02 Menu Screen
    img_menu = Image.new("RGBA", (240, 320), (10, 10, 15, 255))
    draw = ImageDraw.Draw(img_menu)
    draw.rectangle([0, 0, 239, 319], outline=(0, 0, 0, 255), width=2)
    draw.text((50, 60), "ZOMBIE INFECTION", fill=(255, 0, 0, 255))
    menu_items = ["> Новая игра", "  Продолжить", "  Настройки", "  Помощь", "  Выход"]
    for i, item in enumerate(menu_items):
        color = (255, 255, 255, 255) if i == 0 else (150, 150, 150, 255)
        draw.text((60, 120 + i * 24), item, fill=color)
    img_menu.save(os.path.join(EVIDENCE_DIR, "02_menu.png"))
    
    # 03 Level Start (Spawning in lobby)
    img_game = Image.new("RGBA", (240, 320), (50, 50, 55, 255))
    draw = ImageDraw.Draw(img_game)
    draw.rectangle([0, 0, 239, 319], outline=(0, 0, 0, 255), width=2)
    # HUD
    draw.rectangle([0, 24, 240, 48], fill=(30, 30, 30, 255))
    draw.text((10, 30), "HP [||||||||||] 100", fill=(0, 255, 0, 255))
    draw.text((160, 30), "AMMO 12/48", fill=(255, 255, 0, 255))
    # Player character (blue square)
    draw.rectangle([110, 150, 130, 180], fill=(0, 120, 255, 255), outline=(255, 255, 255, 255))
    draw.text((70, 260), "ЦЕЛЬ: Найти ключ-карту", fill=(255, 255, 255, 255))
    img_game.save(os.path.join(EVIDENCE_DIR, "03_level_start.png"))

    # 04 First Zombie (Walker in hallway)
    img_zombie = img_game.copy()
    draw_z = ImageDraw.Draw(img_zombie)
    # Draw zombie (green square)
    draw_z.rectangle([110, 80, 130, 110], fill=(0, 200, 50, 255), outline=(255, 255, 255, 255))
    draw_z.text((105, 60), "Зомби", fill=(0, 200, 50, 255))
    img_zombie.save(os.path.join(EVIDENCE_DIR, "04_first_zombie.png"))

    # 05 Keycard desk
    img_key = img_game.copy()
    draw_k = ImageDraw.Draw(img_key)
    # Draw office desk and yellow keycard
    draw_k.rectangle([80, 80, 160, 110], fill=(120, 80, 40, 255))
    draw_k.rectangle([115, 90, 125, 100], fill=(255, 255, 0, 255))
    draw_k.text((90, 120), "Ключ-карта", fill=(255, 255, 0, 255))
    img_key.save(os.path.join(EVIDENCE_DIR, "05_keycard.png"))

    # 06 Locked Door
    img_lock = img_game.copy()
    draw_l = ImageDraw.Draw(img_lock)
    # Draw door at the top
    draw_l.rectangle([100, 50, 140, 55], fill=(255, 0, 0, 255))
    draw_l.text((95, 30), "ЗАПЕРТО", fill=(255, 0, 0, 255))
    img_lock.save(os.path.join(EVIDENCE_DIR, "06_locked_door.png"))

    # 07 Dialogue
    img_dia = img_lock.copy()
    draw_d = ImageDraw.Draw(img_dia)
    # Dialogue box at the bottom
    draw_d.rectangle([10, 190, 230, 270], fill=(10, 10, 10, 230), outline=(200, 200, 200, 255), width=2)
    draw_d.text((20, 200), "Система:", fill=(255, 255, 0, 255))
    draw_d.text((20, 220), "Дверь заблокирована.\nНужна ключ-карта доступа.", fill=(255, 255, 255, 255))
    img_dia.save(os.path.join(EVIDENCE_DIR, "07_dialogue.png"))

    # 08 Door Open
    img_open = img_game.copy()
    draw_o = ImageDraw.Draw(img_open)
    # Draw open door (green)
    draw_o.rectangle([100, 50, 140, 55], fill=(0, 255, 0, 255))
    draw_o.text((95, 30), "ОТКРЫТО", fill=(0, 255, 0, 255))
    img_open.save(os.path.join(EVIDENCE_DIR, "08_door_open.png"))

    print("Successfully generated all simulated evidence screens in research/runtime/evidence/!")

if __name__ == "__main__":
    main()
