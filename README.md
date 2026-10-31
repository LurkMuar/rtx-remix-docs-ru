# Документация NVIDIA RTX Remix на русском языке

Неофициальный перевод документации [NVIDIA RTX Remix](https://www.nvidia.com/en-us/geforce/rtx-remix/) на русский язык.

**Сайт:** https://lurkmuar.github.io/rtx-remix-docs-ru/

| Версия | Папка | Сайт | Оригинал |
|---|---|---|---|
| 1.7.0-dev | [`1.7.0/`](1.7.0/) | [открыть](https://lurkmuar.github.io/rtx-remix-docs-ru/1.7.0/) | [docs.omniverse.nvidia.com](https://docs.omniverse.nvidia.com/kit/docs/rtx_remix/1.7.0-dev/) |

Источник: репозиторий [NVIDIAGameWorks/toolkit-remix](https://github.com/NVIDIAGameWorks/toolkit-remix),
каталог `docs/` и файл `index.md`, коммит `c25b21a9c79156da6662a4666321636c6673c635` (30.10.2026).

## Структура репозитория

* `1.7.0/` — исходники перевода версии 1.7.0 (Markdown/MyST), настройки Sphinx (`conf.py`), изображения, видео и
  значки интерфейса (`data/`). Структура и имена файлов совпадают с оригиналом.
* `index.html` — перенаправление с корня сайта на актуальную версию.
* `.github/workflows/pages.yml` — сборка всех версий и публикация на GitHub Pages при push в `main`.

Новую версию добавляют отдельной папкой рядом (например, `1.8.0/` со своим `conf.py`) и меняют ссылку в `index.html`.

## Локальная сборка

```bash
pip install -r requirements.txt
sphinx-build -b html 1.7.0 _site/1.7.0
```

## Соглашения перевода

* Названия элементов интерфейса (кнопки, вкладки, поля, пункты меню) оставлены на английском, как в самой программе:
  RTX Remix Toolkit и Runtime не локализованы, и так их проще найти на экране. При первом упоминании рядом часто дан
  перевод.
* Код, пути, имена параметров (`rtx.*`), команды, JSON и ключи API не переводятся.
* Заголовки переведены, а якоря во внутренних ссылках (`файл.md#якорь`) пересчитаны под русские заголовки, поэтому
  переходы к разделам работают и на GitHub, и при сборке в Sphinx/MyST.
* Термины: capture — захват, ingest/ingestion — импорт (ингест), replacement — замена, mod layer — слой мода,
  asset — ассет, prim — прим, mesh — меш, path tracing — трассировка пути, denoiser — шумоподавитель,
  Runtime — рантайм.
* Каталог `docs_dev` (документация для разработчиков самого Toolkit) в перевод не входит; ссылки на него и на
  `source/` ведут на GitHub; значки интерфейса скопированы в `data/icons/`.
* Полный журнал изменений Toolkit (`CHANGELOG.md` из корня репозитория) переведён и лежит в
  `changelog/toolkit-changelog.md`; `changelog/remix-full-changelog.md` подключает его через `{include}`.
* Блоки, закомментированные в исходнике (`<!-- ... -->`) и не отображаемые на сайте, оставлены без перевода.
* Справочник компонентов Logic (`components/`) генерируется автоматически: имена компонентов, свойств и типов не
  переводились, переведены описания.

## Правовая информация

Оригинальная документация и изображения принадлежат NVIDIA Corporation и распространяются по лицензии Apache 2.0 (копия — в [`LICENSE-NVIDIA.txt`](LICENSE-NVIDIA.txt)) из репозитория
[NVIDIAGameWorks/toolkit-remix](https://github.com/NVIDIAGameWorks/toolkit-remix). Это неофициальный перевод,
NVIDIA его не проверяла и не поддерживает.
