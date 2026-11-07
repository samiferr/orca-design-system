"""Export the ORCA documentation website as static HTML.

Every page is rendered through Django (so it carries the project's brand settings), written as a flat
``<name>.html`` file, and its links are rewritten to relative file names. Static files the pages use are
copied next to them. The folder then works on GitHub Pages, any static host, or opened from disk.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import Client
from django.urls import reverse

from . import views
from .catalogue import registry

_LINK = re.compile(r'(href|src)="(/[^"#?]*)([#?][^"]*)?"')
_PRE = re.compile(r"(<pre\b.*?</pre>)", re.S | re.I)
_DOC_TAGS = re.compile(r"<!doctype html>|</?html[^>]*>|</?head>|<body[^>]*>|</body>", re.I)
PACKAGE_STATIC = Path(__file__).resolve().parent / "static" / "orca"


def pages() -> dict[str, str]:
    """URL path → output file name, for every page of the site."""
    out = {
        reverse("orca:home"): "index.html",
        reverse("orca:index"): "primitives.html",
        reverse("orca:components"): "components.html",
        reverse("orca:patterns"): "patterns.html",
        reverse("orca:tokens"): "tokens.html",
        reverse("orca:icons"): "icons.html",
        reverse("orca:catalogue-json"): "catalogue.json",
    }
    for slug, _, _ in views.GUIDE:
        out[reverse("orca:guide", args=[slug])] = f"guide-{slug}.html"
    taken = set(out.values())
    for el in registry.all_elements():
        name = f"{el.id}.html"
        if name in taken:
            raise ValueError(f"Element id {el.id!r} collides with a site page; rename it.")
        out[reverse("orca:element", args=[el.id])] = name
    return out


def _rewrite(html: str, mapping: dict[str, str], static_url: str, used_static: set[str]) -> str:
    def repl(m: re.Match) -> str:
        attr, path, tail = m.group(1), m.group(2), m.group(3) or ""
        if path == "/":
            return f'{attr}="index.html"'
        if path in mapping:
            return f'{attr}="{mapping[path]}{tail if tail.startswith("#") else ""}"'
        if path.startswith(static_url):
            rel = path[len(static_url):]
            used_static.add(rel)
            return f'{attr}="static/{rel}"'
        return m.group(0)

    # Code samples are text: leave their link-like content as written.
    return "".join(part if _PRE.fullmatch(part) else _LINK.sub(repl, part) for part in _PRE.split(html))


def export(out_dir: str | Path, fragment_index: bool = False) -> list[Path]:
    """Render every page into ``out_dir``. Returns the files written.

    ``fragment_index`` strips the document wrapper (doctype, html, head, body tags) from ``index.html`` only,
    for hosts that wrap the entry page in their own document.
    """
    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    mapping = pages()
    static_url = settings.STATIC_URL if settings.STATIC_URL.startswith("/") else "/" + settings.STATIC_URL
    client = Client()
    used_static: set[str] = set()
    written: list[Path] = []

    for url, name in mapping.items():
        res = client.get(url)
        if res.status_code != 200:
            raise RuntimeError(f"{url} answered {res.status_code}; the export stopped.")
        body = res.content.decode("utf-8")
        if name.endswith(".html"):
            body = _rewrite(body, mapping, static_url, used_static)
            if fragment_index and name == "index.html":
                body = _DOC_TAGS.sub("", body).strip() + "\n"
        path = out / name
        path.write_text(body, encoding="utf-8")
        written.append(path)

    # ORCA's own static files (CSS references fonts relatively), then anything else the pages linked to.
    shutil.copytree(PACKAGE_STATIC, out / "static" / "orca")
    for rel in sorted(used_static):
        target = out / "static" / rel
        if target.exists():
            continue
        found = finders.find(rel)
        if found:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(found, target)
    (out / ".nojekyll").write_text("", encoding="utf-8")
    written += [p for p in (out / "static").rglob("*") if p.is_file()]
    return written
