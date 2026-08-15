# Протокол ввода FreeJ2ME SDL (Anbu) — верификация по байткоду

**Статус: RUNTIME_VERIFIED** — протокол восстановлен из байткода
`Anbu$SDL$SDLKeyTimerTask`, `Anbu$SDL`, `Anbu.getMobileKey` (freej2me-sdl.jar)
и подтверждён реальным тестом TEST-001 (input-smoke-test: KEY_RECEIVED).

## 1. Потоки процесса sdl_interface

| Поток | Направление | Назначение |
|---|---|---|
| stdin  | Anbu → sdl_interface | RGB-кадры 240×320×3 (по 230400 байт) |
| stdout | sdl_interface → Anbu | НЕ ИСПОЛЬЗУЕТСЯ для ввода |
| stderr | sdl_interface → Anbu | **пакеты клавиш** (читаются Anbu из `proc.getErrorStream()`) |

Из байткода `Anbu$SDL.start()`:
```
ldc './sdl_interface' → ProcessBuilder → proc.start()
proc.getErrorStream() → поле keys (InputStream)   // ВХОД КЛАВИШ
proc.getOutputStream() → поле frame (OutputStream) // КАДРЫ
new Timer → schedule(SDLKeyTimerTask, 5, 5)        // тик каждые 5 мс, 1 байт за тик
```

## 2. Формат пакета (5 байт)

`SDLKeyTimerTask.run()` (дизассемблер, байты 0x00–0x8B):

```
bin = keys.read(); if (bin == -1) return;
din[count++] = bin;
if (count != 5) return;            // ПАКЕТ = 5 байт (iconst_5 + if_icmpne)
count = 0;
switch (din[0] >>> 4) {            // lookupswitch: 0→KEY, 1→POINTER, default→loop
  case 0:  // KEY
    code = (din[1]&255)<<24 | (din[2]&255)<<16 | (din[3]&255)<<8 | (din[4]&255);
    mobikey = getMobileKey(code);
    break;
  case 1:  // POINTER
    x = (din[1]&255)<<8 | (din[2]&255);
    y = (din[3]&255)<<8 | (din[4]&255);
    if (din[0] % 2 != 0) pointerPressed(x,y) else pointerReleased(x,y);
    return;
}
if (mobikey == 0) return;                       // нераспознанный код — игнор
mobikeyN = (mobikey + 64) & 127;
if (din[0] % 2 != 0) {                          // бит нажатия
    if (pressedKeys[mobikeyN]) keyRepeated(mobikey);
    else keyPressed(mobikey);
    pressedKeys[mobikeyN] = true;
} else {
    keyReleased(mobikey);
    pressedKeys[mobikeyN] = false;
}
```

Итог для клавиш:

```
[0] = (type << 4) | pressed        type 0 = KEY, 1 = POINTER; pressed 1/0
[1..4] = code u32 BE               для KEY; для POINTER: [1..2]=x u16 BE, [3..4]=y u16 BE
```

## 3. Маппинг кодов (Anbu.getMobileKey, useFlag == 0 — конфигурация по умолчанию)

useFlag читается из конфигурации `phone` ('n'→1, 'e'→2, 's'→3, 'm'→4); при
отсутствии файла конфигурации (наш случай) useFlag = 0.

| Входящий код (SDL) | Возврат (Mobile) | Комментарий |
|---|---|---|
| 1073741906 (SDLK_UP) | 50 ('2') | |
| 1073741905 (SDLK_DOWN) | 56 ('8') | |
| 1073741904 (SDLK_LEFT) | 52 ('4') | |
| 1073741903 (SDLK_RIGHT) | 54 ('6') | |
| 13 (ENTER) | 53 ('5') | FIRE |
| 48–57 | 48–57 | цифры |
| 42 ('*'), 35 ('#') | 42, 35 | |
| 1073741913–1073741922 (KP_1..KP_0) | 55,56,57,52,53,54,49,50,51,48 | |
| 99 ('c') | переключение useFlag | |
| -1, 27, 1073741898 (SDLK_HOME) | выход из эмулятора | НЕ использовать |
| всё остальное (вкл. -6, -7) | 0 → игнор | SOFT_LEFT/SOFT_RIGHT недоставимы |

## 4. Игровая интерпретация (g.aa(int), класс g)

```
'0'..'9' → 1,2,4,8,16,32,64,128,256,512
'*' → 262144;  '#' → 524288
-1..-7 → 1024,2048,4096,8192,16384,32768,65536   (UP,DOWN,LEFT,RIGHT,FIRE,SOFT_LEFT,SOFT_RIGHT)
```

Меню (g.W): UP='2'/0x404, DOWN='8'/0x900, FIRE='5'/0x4020; SOFT_LEFT(0x8000) =
элемент len-2, SOFT_RIGHT(0x10000) = элемент len-1.

## 5. Эмпирические наблюдения TEST-001

1. Пакеты клавиш пишутся в **stderr** sdl_interface (не stdout).
2. Одно нажатие = ровно 2 разбора пакета в SDLKeyTimerTask (press + release),
   подтверждено брейкпоинтом JDWP на `putfield code` (0x89): 2 попадания.
3. В меню игры первое нажатие после активации (x 0→1, dm 0→4) даёт серию
   из 5 шагов курсора, последующие — по 1 шагу; серия повторяется ~каждые
   5 нажатий. Документировано как артефакт конвейера кадров эмулятора.
4. Код 27/ -1 завершают процесс эмулятора.
