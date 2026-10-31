# Конфигурация Sphinx для русского перевода документации RTX Remix 1.7.0
import shutil
from pathlib import Path

project = "RTX Remix 1.7.0 — документация на русском"
author = "NVIDIA (оригинал); перевод сообщества"
language = "ru"
master_doc = "index"

extensions = [
    "myst_parser",
    "sphinxcontrib.video",
]

myst_heading_anchors = 4
myst_enable_extensions = ["colon_fence"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["myst.header"]

html_theme = "furo"
html_title = "RTX Remix 1.7.0 — документация на русском"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "announcement": (
        "Неофициальный перевод документации NVIDIA RTX Remix, версия <b>1.7.0-dev</b>. "
        "<a href=\"https://docs.omniverse.nvidia.com/kit/docs/rtx_remix/1.7.0-dev/\">Оригинал на английском</a>"
    ),
}


def _copy_icons(app, exception):
    """Значки интерфейса вставлены в текст через <img>, поэтому Sphinx сам их не копирует."""
    if exception or app.builder.format != "html":
        return
    src = Path(app.srcdir) / "data" / "icons"
    dst = Path(app.outdir) / "data" / "icons"
    shutil.copytree(src, dst, dirs_exist_ok=True)


def setup(app):
    app.connect("build-finished", _copy_icons)
