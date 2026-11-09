"""The element registry: one record per ORCA element with its why, when and how.

Every record is written for an AI coding agent: specific, imperative, and tied to tokens and classes
that exist. The registry is pure Python (no Django needed) so ``python -m orca show button`` works
anywhere.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field



@dataclass(frozen=True)
class Level:
    key: str
    title: str
    built_from: str  # the level it groups ("" for primitives)
    definition: str
    examples: str


# The five ORCA levels. Each level is a group of the level before it, and only of that level:
# a component groups primitives, a pattern groups components, a template groups patterns,
# and a page is a template filled with real content. This is the one definition; docs read it from here.
LEVEL_DEFS = (
    Level("primitive", "Primitives", "",
          "The smallest working pieces and the base styles. A primitive contains no other ORCA element.",
          "button, input, icon, text style, status mark, token."),
    Level("component", "Components", "primitive",
          "A group of primitives with one job.",
          "form field, search bar, date picker, pagination, stat card, toast."),
    Level("pattern", "Patterns", "component",
          "A group of components that forms a recognisable section of a page.",
          "page head with page actions, filter drawer, sidebar, data table, month calendar."),
    Level("template", "Templates", "pattern",
          "A group of patterns arranged into a page layout, with placeholder content.",
          "app shell, list page, detail page, form page, calendar page."),
    Level("page", "Pages", "template",
          "A template filled with real content, including the variations that test it.",
          "a list page shown empty, overdue, right-to-left and dark."),
)
LEVELS = tuple(level.key for level in LEVEL_DEFS)

# Short keys used in Element.laws → full names (Laws of UX, Yablonski 2024; Practical UI, Dannaway 2024).
LAWS = {
    "jakob": "Jakob's law: work the way products people already know work",
    "fitts": "Fitts's law: big, close, well-spaced targets are faster and safer",
    "miller": "Miller's law: chunk information so working memory is not overloaded",
    "hick": "Hick's law: fewer, clearer choices mean faster decisions",
    "postel": "Postel's law: accept varied input, output reliable and accessible UI",
    "peak-end": "Peak–end rule: people judge an experience by its peak and its end",
    "aesthetic": "Aesthetic–usability effect: consistent, careful visuals earn trust",
    "restorff": "Von Restorff effect: the one thing that differs is noticed; use emphasis sparingly",
    "tesler": "Tesler's law: move unavoidable complexity from the user to the system",
    "doherty": "Doherty threshold: respond within 400 ms; show progress for anything slower",
}
PRACTICAL_UI = {
    "F01": "Design for a diverse audience", "F03": "Reduce the total effort of a task",
    "F05": "Build a design system with tokens and usage guidance", "F06": "Prefer established patterns",
    "F09": "Keep visual and functional behaviour consistent", "F10": "Specify every interaction state",
    "S03": "Use link styling with context", "S04": "Reveal secondary information when needed",
    "S05": "Preserve clarity when reducing elements", "C01": "Check contrast for meaningful content",
    "C03": "Communicate meaning beyond colour", "C04": "Reserve status colours for their meanings",
    "C07": "Prefer one purposeful action colour", "C09": "Give each palette token a role",
    "C12": "Use elevation consistently", "C18": "Name raw colours separately from their uses",
    "L01": "Group related information", "L03": "Establish an order of importance",
    "L08": "Define a limited spacing scale", "L09": "Set spacing by relationship",
    "L11": "Align the layout with a responsive grid", "L15": "Design for long and unusual content",
    "T01": "One legible sans serif family", "T04": "Limit the working set of weights",
    "T05": "Build sizes from a type scale", "T07": "Comfortable line spacing", "T09": "Limit reading measure",
    "T13": "Keep quieter text legible", "W02": "Use sentence case", "W07": "Reserve uppercase for short labels",
    "W11": "Make numbers scannable", "W14": "Give links meaningful destination names",
    "W15": "Help people recover from errors", "B01": "Three distinguishable action weights",
    "B03": "One primary action", "B05": "Keep low-priority actions quieter",
    "B06": "Prefer informative alternatives to disabled buttons", "B07": "Explain necessary disabled states",
    "B10": "Name the action clearly", "B11": "Make targets large and separated",
    "B12": "Balance icons and labels", "B13": "Scale friction to the consequence",
    "R03": "Label optional information", "R05": "Make requirement status clear",
    "R06": "Match input width to the expected answer", "R07": "Keep recognisable control features",
    "R08": "Put essential help before the input", "R09": "Persistent labels, not placeholders",
    "R10": "Keep labels close to their inputs", "R11": "Visible choices for small sets",
    "R12": "Autocomplete for long lists", "R13": "Steppers for small numeric changes",
    "R14": "Checkbox or switch according to timing", "R15": "Phrase binary labels positively",
    "R18": "Keep control boundaries visible", "R20": "Submit-time validation with an error summary",
    "R21": "Validate after leaving a field when context matters",
    "C08": "Choose and adapt the brand colour deliberately", "C11": "Build dark palettes independently",
    "L05": "Use depth to support navigation and priority", "R01": "Keep the main form flow in one column",
    "R17": "Group fields under headings", "S02": "Remove styles that compete without communicating",
    "S06": "Make essential content visible or discoverable", "T06": "Make long-form reading text large enough",
    "T12": "Make text over photos readable", "W01": "Make every word useful", "W04": "Lead with the information people seek",
    "W05": "Order explanations as an inverted pyramid", "W08": "Structure information for scanning",
    "W09": "Avoid unnecessary pronouns in labels", "W12": "Keep punctuation restrained", "R22": "Live feedback only when it helps",
    "B08": "Keep action order predictable", "B09": "Position multi-step navigation carefully",
    "L12": "Give text a stable alignment anchor", "L14": "Reduce travel between related actions",
    "R02": "Ask only for useful, necessary information", "R16": "Break long forms into sensible steps",
    "S08": "Simplify decisions: remove, group, stage, recommend", "W10": "Use one term for one concept",
}


@dataclass(frozen=True)
class Category:
    key: str
    title: str
    intro: str
    level: str = "primitive"


@dataclass
class Element:
    id: str
    name: str
    category: str
    summary: str
    why: str
    when: list[str]
    how: list[str]
    avoid: list[str] = field(default_factory=list)
    a11y: list[str] = field(default_factory=list)
    tokens: list[str] = field(default_factory=list)
    classes: list[str] = field(default_factory=list)
    laws: list[str] = field(default_factory=list)
    examples: list[tuple[str, str]] = field(default_factory=list)
    guide: list[str] = field(default_factory=list)  # ORCA guide items this element covers
    related: list[str] = field(default_factory=list)
    source: str = "Tangerine"  # Tangerine (from wise_people_analyzer) or ORCA (new in this system)
    level: str = "primitive"
    uses: list[str] = field(default_factory=list)  # lower-level elements this one is built from
    # Templates level: the Django template a project extends, the child template shown as its live preview
    # (orca/templates/orca/previews/<preview>.html), the blocks it offers and the context variables it reads.
    template: str = ""
    preview: str = ""
    blocks: list[str] = field(default_factory=list)
    context: list[str] = field(default_factory=list)

    def preview_template(self) -> str:
        return f"orca/previews/{self.preview}.html" if self.preview else ""

    def example_list(self) -> list[tuple[str, str]]:
        """Examples to show and export. A template's example is the child template of its preview."""
        if self.examples or not self.preview:
            return self.examples
        from pathlib import Path

        path = Path(__file__).resolve().parent.parent / "templates" / self.preview_template()
        return [("Child template", path.read_text(encoding="utf-8").strip())]

    def law_names(self) -> list[str]:
        out = []
        for key in self.laws:
            if key in LAWS:
                out.append(LAWS[key])
            elif key in PRACTICAL_UI:
                out.append(f"Practical UI {key}: {PRACTICAL_UI[key]}")
            else:
                out.append(key)
        return out


_CATEGORIES: list[Category] = []
_ELEMENTS: dict[str, Element] = {}


_CATEGORY_LEVEL: dict[str, str] = {}


def category(key: str, title: str, intro: str, level: str = "primitive") -> str:
    if key in _CATEGORY_LEVEL:
        raise ValueError(f"Duplicate ORCA category key {key!r}")
    _CATEGORIES.append(Category(key, title, intro, level))
    _CATEGORY_LEVEL[key] = level
    return key


_TEMPLATETAG = {"{% templatetag openblock %}": "{%", "{% templatetag closeblock %}": "%}",
                "{% templatetag openvariable %}": "{{", "{% templatetag closevariable %}": "}}"}


def _plain(text: str) -> str:
    """Catalogue prose may spell template syntax with templatetag (needed inside examples); prose shows it plainly."""
    for tag, out in _TEMPLATETAG.items():
        text = text.replace(tag, out)
    return text


def add(el: Element) -> Element:
    el.summary, el.why = _plain(el.summary), _plain(el.why)
    for name in ("when", "how", "avoid", "a11y", "context"):
        setattr(el, name, [_plain(t) for t in getattr(el, name)])
    if el.id in _ELEMENTS:
        raise ValueError(f"Duplicate ORCA element id {el.id!r}")
    el.level = _CATEGORY_LEVEL.get(el.category, el.level)
    _ELEMENTS[el.id] = el
    return el


def _load() -> None:
    if _CATEGORIES:
        return
    from . import (  # noqa: F401  (registration side effects, in catalogue order)
        foundations, text, form_text, actions, inputs, icons, status, identity, imagery,
        structure, progress, charts, planning,
    )
    from .components import (  # noqa: F401
        forms, navigation, feedback, actions as component_actions, data_display, content, identity_controls,
        pickers, planning_selectors, calendar_parts, schedule_parts, plan_items, docs_site,
    )
    from .patterns import (  # noqa: F401
        page_frame, grids, data_filtering, forms as pattern_forms, media, records, charts as pattern_charts,
        marketing, process, editorial, email, calendar_views, scheduler, event_editing, planning_boards,
    )
    from .templates import layouts, generic, page_types, structure as template_structure, slots  # noqa: F401


LEVEL_TITLES = {level.key: level.title for level in LEVEL_DEFS}
RELEASED_LEVELS = ("primitive", "component", "pattern", "template")


def categories(level: str | None = None) -> list[Category]:
    _load()
    return [c for c in _CATEGORIES if level is None or c.level == level]


def all_elements(level: str | None = None) -> list[Element]:
    _load()
    return [e for e in _ELEMENTS.values() if level is None or e.level == level]


def get(element_id: str) -> Element | None:
    _load()
    return _ELEMENTS.get(element_id)


def by_category(key: str) -> list[Element]:
    return [e for e in all_elements() if e.category == key]


def search(term: str) -> list[Element]:
    term = term.lower().strip()
    hits = []
    for el in all_elements():
        hay = " ".join([el.id, el.name, el.summary, " ".join(el.guide), " ".join(el.classes)]).lower()
        if term in hay:
            hits.append(el)
    return hits


def as_json() -> dict:
    from ..tokens import BRAND_TOKENS

    return {
        "system": "ORCA",
        "appearance": "tangerine",
        "themes": ["light", "dark", "paper"],
        "levels": [asdict(level) for level in LEVEL_DEFS],
        "released_levels": list(RELEASED_LEVELS),
        "brand_tokens": [{"key": t.key, "css": t.css, "default": t.default, "usage": t.usage} for t in BRAND_TOKENS],
        "categories": [asdict(c) for c in categories()],
        "elements": [
            dict(asdict(el), examples=[{"title": t, "html": h} for t, h in el.example_list()], law_names=el.law_names())
            for el in all_elements()
        ],
    }
