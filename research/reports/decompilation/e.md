# Технический отчёт по декомпиляции класса `e`

## Базовая информация
*   **Имя класса:** `e.class`
*   **Размер исходного .class файла:** `2934` байт
*   **Статус декомпиляции:** `УСПЕШНО`
*   **Количество методов:** `7`
*   **Количество полей:** `12`
*   **Внутренние / анонимные классы:** `Нет`

---

## Зависимости
*   **Другие игровые классы:** `a`, `b`, `c`, `d`, `g`
*   **Библиотеки J2ME (javax.microedition.*):** `javax.microedition.io.Connector`, `javax.microedition.sensor.ChannelInfo`, `javax.microedition.sensor.Data`, `javax.microedition.sensor.DataListener`, `javax.microedition.sensor.SensorConnection`, `javax.microedition.sensor.SensorInfo`, `javax.microedition.sensor.SensorManager`

---

## Предупреждения и сообщения CFR Decompiler
> /* * Decompiled with CFR 0.152. * * Could not load the following classes: *  java.lang.Exception *  java.lang.Object *  java.lang.String *  java.lang.System *  javax.microedition.io.Connector *  javax.microedition.sensor.ChannelInfo *  javax.microedition.sensor.Data *  javax.microedition.sensor.DataListener *  javax.microedition.sensor.SensorConnection *  javax.microedition.sensor.SensorInfo *  javax.microedition.sensor.SensorManager */
> /* * Duplicate member names - consider using --renamedupmembers true */

---

## Список объявленных полей
- `public static boolean a = true`
- `public int[] a`
- `public String[] a`
- `public boolean b`
- `public String a`
- `public SensorConnection a`
- `public boolean c = false`
- `public int a = new String[3]`
- `public int b`
- `public int[] b = new int[]{0, 0, 0}`
- `public static int c`
- `public static int d`

---

## Список сигнатур методов
- `public final void a()`
- `public static boolean a()`
- `public static boolean b()`
- `public static void a(boolean bl)`
- `public final void dataReceived(SensorConnection sensorConnection, Data[] dataArray, boolean bl)`
- `private void b()`
- `public static boolean c()`
