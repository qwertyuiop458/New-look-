# Runtime Evidence Policy

1. Только реальные наблюдения (лог эмулятора, скриншоты реального рантайма) могут дать статус RUNTIME_CONFIRMED.
2. Сгенерированные/симулированные изображения и данные обозначаются SIMULATED и НЕ могут подтверждать runtime-факты.
3. Каждый runtime-факт: OBSERVED (лог+скриншот), MATCH/MISMATCH со static Bible, INCONCLUSIVE.
4. Вся evidence сохраняется в research/runtime/evidence/ с метаданными (эмулятор, дата, тест).
