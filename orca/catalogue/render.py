"""Plain-text renderings of the catalogue (Markdown for docs/, text for the CLI)."""

from __future__ import annotations

from . import registry


def _bullets(items: list[str]) -> str:
    return "\n".join(f"- {i}" for i in items)


def element_markdown(el: registry.Element) -> str:
    out = [f"## {el.name}", "", f"`id: {el.id}` · level: {el.level} · source: {el.source}", "", el.summary, ""]
    if el.uses:
        out += ["Built from: " + ", ".join(f"`{u}`" for u in el.uses), ""]
    out += ["### Why", "", el.why, ""]
    out += ["### When to use", "", _bullets(el.when), ""]
    if el.avoid:
        out += ["### When not to use", "", _bullets(el.avoid), ""]
    out += ["### How to use", "", _bullets(el.how), ""]
    if el.a11y:
        out += ["### Accessibility", "", _bullets(el.a11y), ""]
    for title, html in el.examples:
        out += [f"#### Example: {title}", "", "```django", html.strip(), "```", ""]
    meta = []
    if el.classes:
        meta.append("**Classes:** " + ", ".join(f"`{c}`" for c in el.classes))
    if el.tokens:
        meta.append("**Tokens:** " + ", ".join(f"`--orca-{t}`" for t in el.tokens))
    if el.laws:
        meta.append("**Principles applied:** " + "; ".join(el.law_names()))
    if el.related:
        meta.append("**Related:** " + ", ".join(f"`{r}`" for r in el.related))
    if el.guide:
        meta.append("**ORCA guide items covered:** " + "; ".join(el.guide))
    out += ["\n\n".join(meta), "", "---", ""]
    return "\n".join(out)


def index_markdown(level: str = "primitive") -> str:
    title = registry.LEVEL_TITLES[level]
    out = [
        f"# ORCA {title.lower()}",
        "",
        "Generated from `orca/catalogue/` by `python -m orca build`. Do not edit by hand.",
        "",
        "Every element below has a **why**, **when**, **when not**, **how**, accessibility notes, the tokens and",
        "classes it uses, the UX principles it applies, and a copy-ready Django template example.",
        "Load the tags with `{% load orca %}` and put `{% orca_head %}` in `<head>`.",
        "",
    ]
    for cat in registry.categories(level):
        els = registry.by_category(cat.key)
        out.append(f"## [{cat.title}]({cat.key}.md) ({len(els)})")
        out.append("")
        out.append(cat.intro)
        out.append("")
        for el in els:
            out.append(f"- `{el.id}` **{el.name}**: {el.summary}")
        out.append("")
    return "\n".join(out)


def element_text(el: registry.Element) -> str:
    """Compact text for the terminal (`python -m orca show <id>`)."""
    return element_markdown(el)
