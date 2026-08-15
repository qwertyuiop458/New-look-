# Emulator Comparison V2

## Окружение (аудит 15.28)
- java/javac/javap: НЕТ; X11/Xvfb: НЕТ; DISPLAY пуст.
- python 3.11, node 22, npm, pip доступны.
- apt: нет прав на установку (root недоступен).
- Сеть: GitHub доступен (200); Adoptium API недоступен.

## Кандидаты
| Эмулятор | Java | X11 | Headless | Пригодность в этом env |
| :--- | :-: | :-: | :-: | :--- |
| FreeJ2ME (Java) | нужен | да | частично | требует JRE (недоступен без root) |
| freej2me-web (WASM) | нет | нет | да (headless browser) | **НАИБОЛЕЕ ПРИГОДЕН** (Node есть) |
| J2ME-Loader (Android) | нет | нет | нет | требует Android |
| wie (Java) | нужен | да | частично | требует JRE |
| MicroEmulator | нужен | да | нет | deprecated |

## Выбор кандидата
1. **freej2me-web** (WASM через headless Chromium) — единственный путь без Java/X11;
   требует установки headless Chrome (npm puppeteer) — проверка доступности ниже.
2. FreeJ2ME (Java) — запасной, если появится portable JRE (без root: tar.gz JDK в workspace).

## Блокеры
- Установка JRE без root: возможно через portable JDK (распаковка tar.gz в workspace) — не блокер.
- Headless browser: нужен Chrome/Chromium — установка через npm puppeteer (скачивание Chromium).
- X11: НЕ обязателен для freej2me-web.
