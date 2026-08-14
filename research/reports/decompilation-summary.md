# Сводный отчёт по декомпиляции Java-кода J2ME-игры (Zombie Infection)

## Общая статистика декомпиляции
*   **Всего обнаружено .class файлов:** `8`
*   **Успешно декомпилировано в .java:** `8` (100.0%)
*   **Ошибок декомпиляции:** `0` (0.0%)
*   **Общее количество декомпилированных строк кода:** `47787` строк
*   **Суммарное количество методов:** `1739`
*   **Суммарное количество полей:** `935`

---

## Таблица результатов декомпиляции
| Имя класса | Размер .class | Статус CFR | Кол-во методов | Кол-во полей | Кол-во строк .java | Ссылка на код | Ссылка на отчёт |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GloftMASS.class` | 561 B (0.55 KB) | Успешно | 4 | 2 | 38 | [Смотреть](research/decompiled/GloftMASS.java) | [Отчёт](research/reports/decompilation/GloftMASS.md) |
| `a.class` | 13163 B (12.85 KB) | Успешно | 28 | 51 | 944 | [Смотреть](research/decompiled/a.java) | [Отчёт](research/reports/decompilation/a.md) |
| `b.class` | 33176 B (32.40 KB) | Успешно | 60 | 142 | 2420 | [Смотреть](research/decompiled/b.java) | [Отчёт](research/reports/decompilation/b.md) |
| `c.class` | 2608 B (2.55 KB) | Успешно | 18 | 15 | 227 | [Смотреть](research/decompiled/c.java) | [Отчёт](research/reports/decompilation/c.md) |
| `d.class` | 536 B (0.52 KB) | Успешно | 0 | 15 | 26 | [Смотреть](research/decompiled/d.java) | [Отчёт](research/reports/decompilation/d.md) |
| `e.class` | 2934 B (2.87 KB) | Успешно | 7 | 12 | 158 | [Смотреть](research/decompiled/e.java) | [Отчёт](research/reports/decompilation/e.md) |
| `f.class` | 100180 B (97.83 KB) | Успешно | 288 | 64 | 8524 | [Смотреть](research/decompiled/f.java) | [Отчёт](research/reports/decompilation/f.md) |
| `g.class` | 422699 B (412.79 KB) | Успешно | 1334 | 634 | 35450 | [Смотреть](research/decompiled/g.java) | [Отчёт](research/reports/decompilation/g.md) |

---

## Выводы
*   Все исходные `.class` файлы были обработаны автоматически и воспроизводимо с помощью скрипта `research/scripts/decompile_all.py`.
*   Полнота декомпиляции составляет **100%** (все 8 классов успешно декомпилированы без падений и критических сбоев).
*   В декомпилированном коде отсутствуют ручные правки; он полностью отражает структуру оригинального байт-кода, воссозданную утилитой CFR 0.152.
