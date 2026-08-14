# Система камеры и следования (Camera System)

В данном документе приведено математическое описание поведения виртуальной камеры.

---

## 1. Позиционирование (Centering)
*   Камера жестко центрируется на координатах главного героя (`Player`).
*   **Сглаживание (Smoothing):**
    `cam_x = cam_x + ((player_x - cam_x) * 1 / 4)` (плавное следование камеры с демпфированием). [INFERRED]

---

## 2. Границы карты (Bounds limits)
Камера ограничивается краями активного уровня:
*   `min_cam_x = 0`, `max_cam_x = (map_width * 16) - screen_width`. [CONFIRMED]
*   `min_cam_y = 0`, `max_cam_y = (map_height * 16) - screen_height`. [CONFIRMED]
