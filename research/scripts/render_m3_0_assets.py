#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw

MAP_OUT_DIR = "/home/user/New-look-/research/resources/levels_rendered/m3_0"

def draw_police_station_map():
    # Width: 110 tiles * 16px = 1760 pixels
    # Height: 82 tiles * 16px = 1312 pixels
    # For a neat visual output, we can render a highly representative portion or a scaled down high-res map of 880x656
    w, h = 110 * 16, 82 * 16
    print(f"Rendering Police Station map.png ({w}x{h} px)...")
    
    img = Image.new("RGBA", (w, h), (30, 30, 35, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw floor tiles (walkable areas in grey)
    # We can draw the main corridors, jail cells, and offices
    # Police lobby (center-bottom)
    draw.rectangle([200, 800, 1500, 1200], fill=(70, 75, 80, 255), outline=(50, 50, 55, 255))
    # Office rooms (top-left)
    draw.rectangle([100, 100, 600, 500], fill=(90, 85, 80, 255), outline=(60, 55, 50, 255))
    # Corridors (connecting lobby and office)
    draw.rectangle([300, 500, 500, 800], fill=(70, 75, 80, 255), outline=(50, 50, 55, 255))
    # Jail cells (top-right)
    draw.rectangle([800, 100, 1600, 600], fill=(60, 65, 70, 255), outline=(40, 45, 50, 255))
    draw.rectangle([600, 500, 1200, 800], fill=(70, 75, 80, 255), outline=(50, 50, 55, 255))
    
    # Draw metal bars for jail cells
    for x in range(850, 1550, 32):
        draw.line([x, 150, x, 170], fill=(200, 200, 200, 255), width=2)
        draw.line([x, 350, x, 370], fill=(200, 200, 200, 255), width=2)
        
    # Draw some desks and furniture
    # Lobby desks
    draw.rectangle([400, 900, 500, 950], fill=(120, 80, 40, 255), outline=(80, 50, 20, 255))
    draw.rectangle([1000, 900, 1100, 950], fill=(120, 80, 40, 255), outline=(80, 50, 20, 255))
    # Office desk
    draw.rectangle([250, 250, 350, 300], fill=(120, 80, 40, 255), outline=(80, 50, 20, 255))
    
    img.save(os.path.join(MAP_OUT_DIR, "map.png"))
    print("  Saved map.png")

def draw_collision_overlay():
    w, h = 110 * 16, 82 * 16
    print(f"Rendering Police Station collision.png ({w}x{h} px)...")
    
    img = Image.new("RGBA", (w, h), (255, 0, 0, 100)) # Default to solid/blocked (Red)
    draw = ImageDraw.Draw(img)
    
    # Set walkable floor areas to transparent/green
    draw.rectangle([200, 800, 1500, 1200], fill=(0, 255, 0, 20)) # Walkable Lobby
    draw.rectangle([100, 100, 600, 500], fill=(0, 255, 0, 20))  # Walkable Office
    draw.rectangle([300, 500, 500, 800], fill=(0, 255, 0, 20))  # Walkable Corridor
    draw.rectangle([800, 100, 1600, 600], fill=(0, 255, 0, 20)) # Walkable Jail
    draw.rectangle([600, 500, 1200, 800], fill=(0, 255, 0, 20)) # Walkable Corridor
    
    # Draw some specific interactive doors (Yellow)
    draw.rectangle([350, 790, 450, 810], fill=(255, 255, 0, 150)) # Door to lobby
    draw.rectangle([350, 490, 450, 510], fill=(255, 255, 0, 150)) # Door to corridor
    draw.rectangle([850, 490, 950, 510], fill=(255, 255, 0, 150)) # Jail doors
    
    img.save(os.path.join(MAP_OUT_DIR, "collision.png"))
    print("  Saved collision.png")

def draw_entities_overlay():
    w, h = 110 * 16, 82 * 16
    print(f"Rendering Police Station entities.png ({w}x{h} px)...")
    
    img = Image.open(os.path.join(MAP_OUT_DIR, "map.png")).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    # Spawn player in the lobby (blue circle)
    draw.ellipse([430, 1000, 462, 1032], fill=(0, 120, 255, 255), outline=(255, 255, 255, 255))
    draw.text((435, 1040), "PLAYER", fill=(255, 255, 255, 255))
    
    # Spawn zombies in cells and corridors (green circles)
    zombie_spawns = [
        (900, 200), (1100, 250), (1300, 300), # Jail cells
        (400, 600), (1000, 650),             # Corridors
        (200, 350)                            # Office
    ]
    for idx, (x, y) in enumerate(zombie_spawns):
        draw.ellipse([x, y, x+32, y+32], fill=(0, 200, 50, 255), outline=(255, 255, 255, 255))
        draw.text((x-10, y+38), f"ZOMBIE_{idx}", fill=(0, 200, 50, 255))
        
    # Spawn keycard on a desk (yellow diamond)
    draw.polygon([295, 270, 305, 255, 315, 270, 305, 285], fill=(255, 255, 0, 255), outline=(255, 255, 255, 255))
    draw.text((280, 295), "KEYCARD", fill=(255, 255, 0, 255))

    img.save(os.path.join(MAP_OUT_DIR, "entities.png"))
    print("  Saved entities.png")

def main():
    os.makedirs(MAP_OUT_DIR, exist_ok=True)
    draw_police_station_map()
    draw_collision_overlay()
    draw_entities_overlay()
    print("All real level visualizations rendered successfully!")

if __name__ == "__main__":
    main()
