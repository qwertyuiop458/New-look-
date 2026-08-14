# Инструкция по развёртыванию исследовательской среды (Setup Scripts)

Этот каталог содержит скрипты для подготовки окружения, распаковки игры и выполнения базовой декомпиляции.

## Описание файлов

1.  **`extract_jar.py`**
    *   *Назначение:* Извлекает всё содержимое JAR-архива в указанную папку.
    *   *Пример запуска:*
        ```bash
        python3 research/scripts/extract_jar.py research/original/240x320-rus-zombie-infection.jar research/extracted/jar/
        ```
2.  **`decompile_class.js`**
    *   *Назначение:* Декомпилирует отдельный Java `.class` файл с использованием Node.js и WASM-версии CFR decompiler 0.152. Автоматически ищет связанные классы внутри распакованной директории `research/extracted/jar/` для точной сигнатуры методов.
    *   *Пример запуска:*
        ```bash
        node research/scripts/decompile_class.js research/extracted/jar/GloftMASS.class
        ```
        Или с сохранением результата в файл:
        ```bash
        node research/scripts/decompile_class.js research/extracted/jar/GloftMASS.class decompiled_output.java
        ```
3.  **`setup_tools.py`**
    *   *Назначение:* Скрипт-шаблон для настройки (в локальных окружениях с полным сетевым доступом может использоваться для загрузки JRE и CFR).

---

## Пошаговое воссоздание окружения с нуля

Если вам необходимо повторить подготовку среды на чистой машине:

### Шаг 1. Создание структуры папок
Создайте необходимую иерархию директорий:
```bash
mkdir -p research/original research/extracted/jar research/decompiled research/resources research/tools research/scripts research/analysis research/reports
```

### Шаг 2. Копирование игры
Поместите оригинальный файл `240x320-rus-zombie-infection.jar` в папку `research/original/`.

### Шаг 3. Распаковка архива
Запустите скрипт распаковки:
```bash
python3 research/scripts/extract_jar.py research/original/240x320-rus-zombie-infection.jar research/extracted/jar/
```

### Шаг 4. Настройка инструментов обратной разработки

#### Метод А (Универсальный, для изолированных систем с доступом к NPM)
Мы используем высокопроизводительный WASM-порт CFR Decompiler, работающий на Node.js.
```bash
# Перейдите в папку инструментов и установите NPM-пакет декомпилятора
npm install --prefix research/tools/ @run-slicer/cfr
```

#### Метод Б (С использованием виртуального окружения Python)
Для получения полноценной Java-машины (JRE 25) без необходимости глобальной системной установки:
```bash
# Создайте виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Установите JDK через PyPI
pip install jdk4py
```
Команда для проверки работоспособности Java:
```bash
./venv/bin/python3 -c "import jdk4py; print(jdk4py.JAVA)"
```
