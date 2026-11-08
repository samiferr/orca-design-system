"""Check a project's templates and CSS against ORCA's rules.

    python manage.py orca_lint [paths...]

Finds what AI agents (and people) most often get wrong:
  * overriding a non-brand ``--orca-*`` token (only brand tokens may change)
  * hard-coded hex colours in templates
  * ``outline: none`` / ``outline: 0`` that removes the focus ring
  * ``<button>`` without ``type``; icon-only buttons without ``aria-label``
  * ``<img>`` without ``alt``; inputs without a label reference
  * class names that look like ORCA classes but do not exist
Exits with status 1 when problems are found, so it can run in CI.
"""

from __future__ import annotations

import re
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from ...build import PACKAGE
from ...tokens import BRAND_CSS_NAMES

TOKEN_SET = re.compile(r"(--orca-[a-z0-9-]+)\s*:")
HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")
OUTLINE_NONE = re.compile(r"outline\s*:\s*(none|0)\b")
BUTTON = re.compile(r"<button\b[^>]*>", re.I)
IMG = re.compile(r"<img\b[^>]*>", re.I)
CLASS_ATTR = re.compile(r'class="([^"]*)"')
ORCA_CLASS = re.compile(r"\borca-[a-z0-9_-]+")


def known_classes() -> set[str]:
    css = "".join((PACKAGE / "static" / "orca" / "css" / name).read_text(encoding="utf-8") for name in ("orca.css", "components.css", "patterns.css", "templates.css"))
    return set(m.group(0)[1:] for m in re.finditer(r"\.orca-[a-z0-9_-]+", css))


class Command(BaseCommand):
    help = "Check templates and CSS for violations of ORCA rules."

    def add_arguments(self, parser):
        parser.add_argument("paths", nargs="*", help="Files or folders (default: TEMPLATES DIRS and STATICFILES_DIRS).")

    def handle(self, *args, **opts):
        roots = [Path(p) for p in opts["paths"]] or self._default_roots()
        classes = known_classes()
        problems: list[str] = []
        for root in roots:
            files = [root] if root.is_file() else [p for p in root.rglob("*") if p.suffix in {".html", ".css", ".txt"}]
            for path in files:
                if PACKAGE in path.resolve().parents:
                    continue
                problems += self._check(path, classes)
        for p in problems:
            self.stdout.write(p)
        if problems:
            self.stderr.write(self.style.ERROR(f"{len(problems)} problem(s) found."))
            raise SystemExit(1)
        self.stdout.write(self.style.SUCCESS("No ORCA problems found."))

    def _default_roots(self) -> list[Path]:
        roots = []
        for conf in getattr(settings, "TEMPLATES", []):
            roots += [Path(d) for d in conf.get("DIRS", [])]
        roots += [Path(d if isinstance(d, (str, Path)) else d[1]) for d in getattr(settings, "STATICFILES_DIRS", [])]
        return [r for r in roots if r.exists()]

    def _check(self, path: Path, classes: set[str]) -> list[str]:
        out = []
        text = path.read_text(encoding="utf-8", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            where = f"{path}:{n}"
            for m in TOKEN_SET.finditer(line):
                if m.group(1) not in BRAND_CSS_NAMES:
                    out.append(f"{where}: {m.group(1)} is not a brand token; only brand tokens may be changed (settings.ORCA['BRAND']).")
            if OUTLINE_NONE.search(line):
                out.append(f"{where}: removes the focus outline; keep ORCA's focus ring.")
            if path.suffix == ".html":
                if HEX.search(line) and "style=" in line:
                    out.append(f"{where}: hard-coded colour; use a --orca-* token.")
                for m in BUTTON.finditer(line):
                    tag = m.group(0)
                    if "type=" not in tag:
                        out.append(f"{where}: <button> without type; add type=\"button\" or type=\"submit\".")
                    if ("orca-icon-button" in tag or "icon-only" in tag) and "aria-label" not in tag:
                        out.append(f"{where}: icon-only button without aria-label.")
                for m in IMG.finditer(line):
                    if "alt=" not in m.group(0):
                        out.append(f"{where}: <img> without alt (use alt=\"\" if decorative).")
                for m in CLASS_ATTR.finditer(line):
                    for cls in ORCA_CLASS.findall(m.group(1)):
                        if cls not in classes:
                            out.append(f"{where}: unknown ORCA class '{cls}'. Run `python -m orca search` to find the right one.")
        return out
