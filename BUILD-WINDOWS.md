# Сборка документации на Windows 10/11

Пошаговая инструкция: как скачать перевод и собрать из него сайт на своём компьютере. Сайт откроется в браузере,
интернет для просмотра не нужен.

Проверено на Windows 10, Python 3.10.6, Git 2.54.

## 1. Установите программы (один раз)

* **Python 3.10 или новее** — <https://www.python.org/downloads/windows/>.
  При установке отметьте галочку **«Add python.exe to PATH»**.
* **Git** — <https://git-scm.com/download/win> (все параметры по умолчанию).

Откройте **PowerShell** (Пуск → «PowerShell») и проверьте:

```powershell
python --version
git --version
```

Обе команды должны вывести номер версии.

## 2. Скачайте репозиторий

```powershell
cd $HOME\Documents
git clone https://github.com/LurkMuar/rtx-remix-docs-ru.git
cd rtx-remix-docs-ru
dir
```

Скачивается около 50 МБ. После `dir` в папке должны быть `1.7.0`, `README.md`, `requirements.txt` и `index.html`.

> Не создавайте папку `rtx-remix-docs-ru` вручную: `git clone` создаёт её сам. Если папка уже есть и в ней нет
> этих файлов, удалите её (`cd ..`, затем `Remove-Item -Recurse -Force rtx-remix-docs-ru`) и повторите `git clone`.

## 3. Создайте виртуальное окружение и установите Sphinx (один раз)

Виртуальное окружение — это папка `.venv` внутри проекта, куда ставятся нужные библиотеки. Системный Python
не затрагивается, удалить всё можно, просто стерев `.venv`.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Если появилась ошибка **«выполнение сценариев отключено в этой системе»**, разрешите запуск локальных сценариев
для своей учётной записи (один раз) и повторите активацию:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

После активации в начале строки появится `(.venv)`. Установите зависимости:

```powershell
pip install -r requirements.txt
```

Сообщение `[notice] A new release of pip available` — просто уведомление, на сборку оно не влияет. Убрать его можно
командой `python -m pip install --upgrade pip`.

## 4. Соберите и откройте сайт

```powershell
sphinx-build -b html 1.7.0 _site\1.7.0
start _site\1.7.0\index.html
```

В конце сборки должно быть `build succeeded.`

> [!IMPORTANT]
> **`sphinx-build` только собирает сайт, но не открывает его.** Готовый сайт — это файл **`index.html`** в папке
> **`_site\1.7.0`** внутри папки репозитория:
>
> **`Документы\rtx-remix-docs-ru\_site\1.7.0\index.html`**
>
> Откройте его командой `start _site\1.7.0\index.html` или двойным щелчком в Проводнике.

> [!WARNING]
> Файл `index.html` в **корне** папки репозитория (рядом с `README.md`) — это только перенаправление для сайта на
> GitHub Pages. Локально он сайт не откроет. Открывайте именно `_site\1.7.0\index.html`.

Пересобирать сайт каждый раз не нужно: если перевод не менялся, просто открывайте этот же `index.html`. Сообщение
`no targets are out of date` означает, что изменений нет и сайт уже актуален.

## Повторная сборка

В новом окне PowerShell окружение неактивно — активируйте его, создавать заново не нужно:

```powershell
cd $HOME\Documents\rtx-remix-docs-ru
.\.venv\Scripts\Activate.ps1
git pull
sphinx-build -b html 1.7.0 _site\1.7.0
start _site\1.7.0\index.html
```

`git pull` подтягивает свежие изменения перевода. Если меню или поиск показывают устаревшие данные, удалите папку
`_site` и соберите заново.

Выключать окружение командой `deactivate` не обязательно: достаточно закрыть окно PowerShell (или набрать `exit`).

## Частые ошибки

| Сообщение | Причина и решение |
|---|---|
| `выполнение сценариев отключено в этой системе` | Выполните `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. |
| `Could not open requirements file: requirements.txt` | Вы не в папке репозитория или репозиторий не склонирован. Проверьте `dir` (шаг 2). |
| `fatal: not a git repository` | Папка создана вручную, а не через `git clone`. Удалите её и склонируйте заново. |
| `"sphinx-build" не распознано` | Не активировано окружение (нет `(.venv)` в начале строки) или не выполнен `pip install -r requirements.txt`. |
| `"python" не распознано` | При установке Python не была отмечена «Add python.exe to PATH». Переустановите Python с этой галочкой. |
