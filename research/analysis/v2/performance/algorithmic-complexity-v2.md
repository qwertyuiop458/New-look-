# Algorithmic Complexity V2

- Entity update: O(E) — цикл по активным сущностям.
- Collision: O(E*C) — E сущностей x C объектов зонда (5 точек + AABB).
- AI (f.b): O(E) с AABB-проверками (дистанция 1600).
- Rendering: O(entities * frames) + O(pixels) при декоде; кэш Image снижает.
- Script: O(S) на скрипт (bQ опкодов).
- Sprite decode: O(w*h) пикселей, lazy + кэш.
- Только статические оценки; реальные замеры — RUNTIME.
