"""Generators: tokens.css from tokens.py, and the Markdown/JSON catalogue for AI agents.

Run ``python -m orca build`` after changing ``tokens.py`` or anything in ``orca/catalogue/``.
The test suite fails when a generated file is out of date.
"""

from __future__ import annotations

import json
from pathlib import Path

from . import tokens as tk
from .conf import brand_style, compute_brand

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parent
TOKENS_CSS = PACKAGE / "static" / "orca" / "css" / "tokens.css"
DOCS_DIR = ROOT / "docs"

HEADER = "/* ORCA tokens: generated from orca/tokens.py by `python -m orca build`. Do not edit. */\n"


def _decls(pairs, indent="  ") -> str:
    return "\n".join(f"{indent}--orca-{name}: {value};" for name, value in pairs)


def tokens_css() -> str:
    sem = tk.semantic_tokens()
    root = [("gray-" + s, v) for s, v in tk.NEUTRAL] + tk.hue_scale()
    root += [(s.name, s.value) for s in tk.ALL_SCALES]
    out = [HEADER, "@layer orca.tokens {", ":root {", "  color-scheme: light;", _decls(root)]
    out.append(_decls([(t.name, t.value("light")) for t in sem]))
    out.append("}")
    dark = _decls([(t.name, t.value("dark")) for t in sem], "    ")
    out.append("@media (prefers-color-scheme: dark) {")
    out.append('  :root:not([data-theme="light"]):not([data-theme="paper"]) {\n    color-scheme: dark;')
    out.append(dark)
    out.append("  }\n}")
    out.append(':root[data-theme="dark"] {\n  color-scheme: dark;')
    out.append(_decls([(t.name, t.value("dark")) for t in sem]))
    out.append("}")
    paper = [(t.name, t.value("paper")) for t in sem if t.paper is not None]
    out.append(':root[data-theme="paper"] {\n  color-scheme: light;')
    out.append(_decls(paper))
    out.append("}")
    out.append('/* Dense density: on <html> (settings.ORCA["DENSITY"] = "dense") or on any region. */')
    out.append('[data-density="dense"] {')
    out.append(_decls(list(tk.DENSE.items())))
    out.append("}")
    defaults = {s.name: s.value for s in tk.ALL_SCALES}
    out.append('/* A comfortable region inside a dense page. */')
    out.append('[data-density="comfortable"] {')
    out.append(_decls([(name, defaults[name]) for name in tk.DENSE]))
    out.append("}")
    out.append("/* Brand tokens (defaults). {% orca_head %} re-emits them from settings.ORCA['BRAND']. */")
    out.append(brand_style(compute_brand({})))
    out.append("}\n")
    return "\n".join(out)


def catalogue_markdown() -> dict[Path, str]:
    from .catalogue import registry
    from .catalogue.render import element_markdown, index_markdown

    files = {}
    for level in registry.RELEASED_LEVELS:
        folder = DOCS_DIR / registry.LEVEL_TITLES[level].lower()
        files[folder / "README.md"] = index_markdown(level)
        for category in registry.categories(level):
            parts = [f"# {category.title}\n", category.intro + "\n"]
            for el in registry.by_category(category.key):
                parts.append(element_markdown(el))
            files[folder / f"{category.key}.md"] = "\n".join(parts)
    files[DOCS_DIR / "catalogue.json"] = json.dumps(registry.as_json(), indent=1, ensure_ascii=False) + "\n"
    return files


def outputs() -> dict[Path, str]:
    files = {TOKENS_CSS: tokens_css()}
    files.update(catalogue_markdown())
    return files


def write() -> list[Path]:
    changed = []
    for path, text in outputs().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
            changed.append(path)
    return changed
