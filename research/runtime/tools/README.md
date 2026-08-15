# Runtime Tools (этап 15.29)

- `nodejdk/` — Temurin JRE 17 x86_64 (npm @spcookie/erii-runtime-linux-x64)
- `javac/` — OpenJDK 8 tools.jar (npm dataslope-tools-jar) — javac через `java -cp tools.jar com.sun.tools.javac.Main`
- `eriideps/` — библиотеки (не использованы)
- `libaudio.so` — JNI-заглушки FreeJ2ME Audio (собраны gcc; имена по JNI-кодировке `_1`)
- `../sdl_interface` — Python-заглушка FreeJ2ME SDL (сохраняет кадры в PNG)
