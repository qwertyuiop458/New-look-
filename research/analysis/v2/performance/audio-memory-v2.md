# Audio Memory V2

- a[n] = ByteArrayInputStream (прелоад), b[n] = Player[2] (кэш).
- freeMemory < 100000 -> звук пропускается (g.java:4366/4421).
- Повторный createPlayer при ошибке; stop() освобождает.
- m13_2: 14 MIDI + 15 WAV (сегменты до 6.5 КБ).
- 2 канала: музыка + SFX.
