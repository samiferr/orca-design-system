"""Command line for humans and AI agents. No Django project needed.

    python -m orca list [category]     every element id, grouped by category
    python -m orca show <id>           why / when / how / example of one element
    python -m orca search <words>      find elements by name, guide item or class
    python -m orca icons               all icon names and aliases
    python -m orca tokens              brand tokens and every CSS token name
    python -m orca json                the whole catalogue as JSON
    python -m orca build               regenerate tokens.css and docs/ (maintainers)
"""

from __future__ import annotations

import json
import sys

from . import build, icons, tokens
from .catalogue import registry
from .catalogue.render import element_text


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    cmd = args.pop(0) if args else "help"

    if cmd == "list":
        for cat in registry.categories():
            if args and args[0] not in (cat.key, cat.title):
                continue
            print(f"\n{cat.title} ({cat.key})")
            for el in registry.by_category(cat.key):
                print(f"  {el.id:<24} {el.summary}")
        return 0
    if cmd == "show" and args:
        el = registry.get(args[0])
        if el is None:
            hits = registry.search(" ".join(args))
            if len(hits) == 1:
                el = hits[0]
            else:
                print(f"No element {args[0]!r}." + (f" Did you mean: {', '.join(h.id for h in hits[:8])}?" if hits else ""))
                return 1
        print(element_text(el))
        return 0
    if cmd == "search" and args:
        for el in registry.search(" ".join(args)):
            print(f"{el.id:<24} {el.name}: {el.summary}")
        return 0
    if cmd == "icons":
        print(" ".join(icons.names()))
        print("\nAliases: " + ", ".join(f"{a} -> {t}" for a, t in sorted(icons.ALIASES.items())))
        return 0
    if cmd == "tokens":
        print("Brand tokens (settings.ORCA['BRAND']):")
        for t in tokens.BRAND_TOKENS:
            print(f"  {t.key:<12} {', '.join(t.css) or '(template)':<28} {t.usage}")
        print("\nSemantic colours:")
        for t in tokens.semantic_tokens():
            print(f"  --orca-{t.name:<22} {t.usage}")
        print("\nScales:")
        for s in tokens.ALL_SCALES:
            print(f"  --orca-{s.name:<22} {s.value:<12} {s.usage}")
        return 0
    if cmd == "json":
        print(json.dumps(registry.as_json(), indent=1, ensure_ascii=False))
        return 0
    if cmd == "build":
        changed = build.write()
        print("\n".join(f"wrote {p}" for p in changed) or "Everything up to date.")
        return 0
    print(__doc__)
    return 0 if cmd in ("help", "-h", "--help") else 1


if __name__ == "__main__":
    raise SystemExit(main())
