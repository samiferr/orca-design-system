"""The ORCA documentation website.

Everything on it is generated from the package itself (catalogue, tokens, icons), so the site can never drift from
the code. Serve it with ``path("orca/", include("orca.urls"))``; export it as static HTML with
``python manage.py orca_site <folder>``. Disable with ``ORCA['DOCS_ENABLED'] = False``.
"""

from __future__ import annotations

from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.template import Context, Template, TemplateSyntaxError
from django.utils.safestring import mark_safe

from . import __version__, icons, tokens
from .catalogue import registry
from .catalogue.guide import LEVELS
from .conf import compute_brand, docs_enabled

PRELUDE = "{% load orca static %}"

# Guide pages, in reading order: (slug, title, one-line summary)
GUIDE = [
    ("installation", "Installation", "Install the package, add the app and load ORCA in your base template."),
    ("usage", "Usage", "Template tags, filters, the page skeleton and the optional script behaviours."),
    ("brand-and-themes", "Brand and themes", "The brand tokens a project may change, and the light, dark and paper themes."),
    ("ai-agents", "For AI agents", "How coding agents look elements up, the hard rules they follow and how their output is checked."),
    ("principles", "Principles", "The Practical UI and Laws of UX rules ORCA applies, and the elements that apply each one."),
    ("accessibility", "Accessibility", "Contrast, focus, touch targets, motion and markup commitments, and how they are tested."),
    ("localization", "Localization", "Translation, right-to-left layouts, text expansion, dates, times and numbers."),
    ("tooling", "Tooling", "Command line, lint, system checks, the build and the static documentation export."),
    ("roadmap", "Levels and roadmap", "The five ORCA levels and what each release delivers."),
]
GUIDE_TITLES = {slug: title for slug, title, _ in GUIDE}


def render_snippet(html: str) -> str:
    """Render an example snippet with ORCA's template tags available."""
    try:
        return Template(PRELUDE + html).render(Context({}))
    except TemplateSyntaxError as exc:  # surfaced by the test suite
        return f'<p class="orca-error">Example failed to render: {exc}</p>'


def _guard():
    if not docs_enabled():
        raise Http404("The ORCA documentation is disabled (ORCA['DOCS_ENABLED'] = False).")


LEVEL_URLS = {"primitive": "orca:index", "component": "orca:components"}


def _levels() -> list[dict]:
    return [{"key": lvl, "title": registry.LEVEL_TITLES[lvl], "url": LEVEL_URLS[lvl],
             "nav": [(c, registry.by_category(c.key)) for c in registry.categories(lvl)]}
            for lvl in registry.RELEASED_LEVELS]


def _ctx(page: str, **extra) -> dict:
    return {
        "levels": _levels(), "nav": [(c, registry.by_category(c.key)) for c in registry.categories()],
        "guide": GUIDE, "page": page, "version": __version__, **extra,
    }


def _stats() -> dict:
    els = registry.all_elements()
    return {
        "elements": len(els),
        "primitives": len(registry.all_elements("primitive")),
        "components": len(registry.all_elements("component")),
        "guide_items": sum(len(v) for lvl in LEVELS.values() for v in lvl.values()),
        "categories": len(registry.categories()),
        "icons": len(icons.names()),
        "tokens": len(tokens.semantic_tokens()) + len(tokens.ALL_SCALES),
        "brand_keys": len(tokens.BRAND_TOKENS),
    }


def home(request):
    _guard()
    hero = mark_safe(render_snippet("""<div class="orca-row orca-row--16">
  <button class="orca-button orca-button--primary" type="button">Save camera</button>
  <button class="orca-button" type="button">Cancel</button>
  <span class="orca-badge orca-badge--subtle orca-badge--positive">{% icon "success" %}Online</span>
  <label class="orca-switch"><input type="checkbox" role="switch" checked><span class="orca-switch__track"></span><span>Email alerts</span></label>
</div>"""))
    return render(request, "orca/docs/home.html", _ctx("home", stats=_stats(), hero=hero))


LEVEL_INTROS = {
    "primitive": "The smallest building blocks and the base styles every other level uses. Each one cannot be broken down further without ceasing to be useful.",
    "component": "Simple groups of primitives that work together as one unit and do one job. Each is reusable on its own and sits inside many patterns.",
}


def level_index(request, level="primitive"):
    _guard()
    return render(request, "orca/docs/index.html", _ctx(
        registry.LEVEL_TITLES[level].lower(), level=level, level_title=registry.LEVEL_TITLES[level],
        level_intro=LEVEL_INTROS[level], elements=registry.all_elements(level), brand_tokens=tokens.BRAND_TOKENS,
        level_nav=[(c, registry.by_category(c.key)) for c in registry.categories(level)],
    ))


def primitives(request):
    return level_index(request, "primitive")


def components(request):
    return level_index(request, "component")


def _principles() -> list[dict]:
    used: dict[str, list] = {}
    for el in registry.all_elements():
        for key in el.laws:
            used.setdefault(key, []).append(el)
    laws = [{"key": k, "name": registry.LAWS[k], "elements": used.get(k, []), "kind": "Laws of UX"} for k in registry.LAWS]
    pui = [{"key": k, "name": registry.PRACTICAL_UI[k], "elements": used[k], "kind": "Practical UI"}
           for k in sorted(registry.PRACTICAL_UI) if k in used]
    return laws + pui


def guide(request, slug):
    _guard()
    if slug not in GUIDE_TITLES:
        raise Http404(f"No guide page {slug!r}")
    extra = {"title": GUIDE_TITLES[slug], "slug": slug}
    if slug == "brand-and-themes":
        extra.update(brand_tokens=tokens.BRAND_TOKENS, brand=compute_brand())
    if slug == "principles":
        extra.update(principles=_principles())
    if slug == "roadmap":
        extra.update(stats=_stats(), coverage=[(registry.LEVEL_TITLES[lvl], [(s, len(items)) for s, items in LEVELS[lvl].items()])
                                             for lvl in registry.RELEASED_LEVELS])
    if slug == "tooling":
        extra.update(stats=_stats())
    index = [s for s, _, _ in GUIDE].index(slug)
    extra["prev"] = GUIDE[index - 1] if index > 0 else None
    extra["next"] = GUIDE[index + 1] if index + 1 < len(GUIDE) else None
    return render(request, f"orca/docs/guide/{slug}.html", _ctx(f"guide-{slug}", **extra))


def element(request, element_id):
    _guard()
    el = registry.get(element_id)
    if el is None:
        raise Http404(f"No ORCA element {element_id!r}")
    examples = [{"title": t, "html": h.strip(), "rendered": mark_safe(render_snippet(h))} for t, h in el.examples]
    related = [registry.get(r) for r in el.related if registry.get(r)]
    uses = [registry.get(u) for u in el.uses if registry.get(u)]
    used_by = [e for e in registry.all_elements() if el.id in e.uses]
    return render(request, "orca/docs/element.html", _ctx(
        el.id, el=el, examples=examples, related=related, uses=uses, used_by=used_by,
        level_url=LEVEL_URLS.get(el.level, "orca:index"), level_title=registry.LEVEL_TITLES[el.level],
        category=next(c for c in registry.categories() if c.key == el.category),
    ))


def token_list(request):
    _guard()
    brand = compute_brand()
    return render(request, "orca/docs/tokens.html", _ctx(
        "tokens", semantic=tokens.semantic_tokens(), scales=tokens.ALL_SCALES, brand=brand,
        brand_rows=[(k, v, brand.css["dark"][k]) for k, v in brand.css["light"].items()],
        brand_tokens=tokens.BRAND_TOKENS, neutral=tokens.NEUTRAL, hues=tokens.HUES, steps=list(tokens.STEPS),
    ))


def icon_list(request):
    _guard()
    items = [(name, mark_safe(icons.svg(name, size="m"))) for name in icons.names()]
    return render(request, "orca/docs/icons.html", _ctx("icons", items=items, aliases=sorted(icons.ALIASES.items())))


def catalogue_json(request):
    _guard()
    return JsonResponse(registry.as_json(), json_dumps_params={"ensure_ascii": False, "indent": 1})
