"""The ORCA catalogue site: every element with its why, when, how and a live example.

Include it in your project with ``path("orca/", include("orca.urls"))``. Disable with ``ORCA['DOCS_ENABLED'] = False``.
"""

from __future__ import annotations

from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.template import Context, Template, TemplateSyntaxError
from django.utils.safestring import mark_safe

from . import icons, tokens
from .catalogue import registry
from .conf import compute_brand, docs_enabled

PRELUDE = "{% load orca static %}"


def render_snippet(html: str) -> str:
    """Render an example snippet with ORCA's template tags available."""
    try:
        return Template(PRELUDE + html).render(Context({}))
    except TemplateSyntaxError as exc:  # surfaced by the test suite
        return f'<p class="orca-error">Example failed to render: {exc}</p>'


def _guard():
    if not docs_enabled():
        raise Http404("The ORCA catalogue is disabled (ORCA['DOCS_ENABLED'] = False).")


def _nav():
    return [(c, registry.by_category(c.key)) for c in registry.categories()]


def index(request):
    _guard()
    return render(request, "orca/docs/index.html", {
        "nav": _nav(), "elements": registry.all_elements(), "brand_tokens": tokens.BRAND_TOKENS, "page": "index",
    })


def element(request, element_id):
    _guard()
    el = registry.get(element_id)
    if el is None:
        raise Http404(f"No ORCA element {element_id!r}")
    examples = [{"title": t, "html": h.strip(), "rendered": mark_safe(render_snippet(h))} for t, h in el.examples]
    related = [registry.get(r) for r in el.related if registry.get(r)]
    return render(request, "orca/docs/element.html", {
        "nav": _nav(), "el": el, "examples": examples, "related": related,
        "category": next(c for c in registry.categories() if c.key == el.category), "page": el.id,
    })


def token_list(request):
    _guard()
    brand = compute_brand()
    return render(request, "orca/docs/tokens.html", {
        "nav": _nav(), "semantic": tokens.semantic_tokens(), "scales": tokens.ALL_SCALES, "brand": brand,
        "brand_rows": [(k, v, brand.css["dark"][k]) for k, v in brand.css["light"].items()],
        "brand_tokens": tokens.BRAND_TOKENS, "neutral": tokens.NEUTRAL, "hues": tokens.HUES, "steps": list(tokens.STEPS),
        "page": "tokens",
    })


def icon_list(request):
    _guard()
    items = [(name, mark_safe(icons.svg(name, size="m"))) for name in icons.names()]
    return render(request, "orca/docs/icons.html", {
        "nav": _nav(), "items": items, "aliases": sorted(icons.ALIASES.items()), "page": "icons",
    })


def catalogue_json(request):
    _guard()
    return JsonResponse(registry.as_json(), json_dumps_params={"ensure_ascii": False, "indent": 1})
