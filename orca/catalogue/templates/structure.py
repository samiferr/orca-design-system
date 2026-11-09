"""Level 4: structural layouts, the CSS grids templates are built with."""

from ..registry import add, category
from . import Template

C = category(
    "structural-layouts", "Structural layouts",
    "Layout classes that arrange sections inside a page: stacks, grids and splits. They hold patterns and never style them.",
    level="template",
)

PANEL = '<section class="orca-panel" aria-label="{0}"><p class="orca-panel-title">{0}</p><div class="orca-skeleton orca-skeleton--text"></div></section>'

add(Template(
    "vertical-stack", "Vertical stack", C,
    "Sections one under another with one spacing step between them; tight and loose variants.",
    why="Equal gaps between sections show they are siblings, and larger gaps than inside a section show where one ends (Practical UI L09).",
    when=["The main column of almost every page; the sections of a side panel."],
    how=["`<div class=\"orca-vstack\">` around the sections; `--tight` (12px) inside panels, `--loose` (40px) between page regions.",
         "Do not add margins to the children: the stack owns the spacing."],
    laws=["L09", "L08"], uses=["panel"], classes=[".orca-vstack", ".orca-vstack--tight", ".orca-vstack--loose"],
    examples=[("Stack", '<div class="orca-vstack">' + PANEL.format("Section one") + PANEL.format("Section two") + "</div>")],
    guide=["Vertical stack"],
))

add(Template(
    "stat-grid", "Stat grid", C,
    "Stat cards in equal columns that wrap, each at least 12rem wide.",
    why="Equal tiles in a row are compared at a glance (Miller's law); a minimum width keeps every number readable on any screen (Practical UI L11).",
    when=["Headline numbers at the top of a dashboard or a parent record."],
    how=["`<div class=\"orca-stat-grid\">` of stat cards; keep to 3–6 cards."],
    laws=["miller", "L11"], uses=["kpi-grid"], classes=[".orca-stat-grid"],
    examples=[("Stats", '<div class="orca-stat-grid">' + "".join(f'<div class="orca-stat-card"><div class="orca-stat-card__head"><span class="orca-stat-card__icon" aria-hidden="true">{{% icon "statistics" %}}</span><p class="orca-stat-label">Metric {i}</p></div><p class="orca-stat-value">{v}</p></div>' for i, v in ((1, "1,234"), (2, "56"), (3, "98%"))) + "</div>")],
    guide=["Stat grid"],
))

add(Template(
    "card-grid-layout", "Card grid", C,
    "Cards in as many equal columns as fit, at least 15rem wide.",
    why="A regular grid lets people scan many similar items by position (Practical UI L11); auto-fill adapts from one column on phones to four on wide screens without breakpoints.",
    when=["Collections browsed by picture or title: videos, products, people, plans."],
    avoid=["Items compared on several attributes: use a table."],
    how=["`<ul class=\"orca-card-grid\">` of `<li class=\"orca-card\">`; override the minimum with `grid-template-columns` only for a different card type."],
    laws=["L11", "jakob"], uses=["card-grid"], classes=[".orca-card-grid"],
    examples=[("Cards", '<ul class="orca-card-grid">' + "".join(f'<li class="orca-card"><div class="orca-card__body"><h3 class="orca-card-title">Card {i}</h3><p class="orca-card-meta">Meta line</p></div></li>' for i in range(1, 5)) + "</ul>")],
    guide=["Card grid"],
))

add(Template(
    "two-column-grid", "Two-column grid", C,
    "Two equal columns from 1036px, one column below.",
    why="Two equal columns pair related panels (two charts, two lists) for comparison (Practical UI L01) while staying readable; on narrow screens they stack in reading order.",
    when=["Pairs of charts or panels of the same importance."],
    how=["`<div class=\"orca-two-col\">` with exactly two children (more wrap into rows of two)."],
    laws=["L01", "L11"], uses=["panel"], classes=[".orca-two-col"],
    examples=[("Two columns", '<div class="orca-two-col">' + PANEL.format("Left") + PANEL.format("Right") + "</div>")],
    guide=["Two-column grid"],
))

add(Template(
    "split-layout", "Split (main + aside)", C,
    "A main column and a 20rem aside (end by default, start or wider as variants); the aside drops below on narrow screens.",
    why="Primary content gets the width and secondary context sits beside it, not in the way (Practical UI L03); below 1036px the aside follows the main content so reading order holds.",
    when=["A form with help or conflicts beside it, a record with related items, a booking with its summary."],
    how=["`<div class=\"orca-split\">` with the main element first, then `<aside>`; `--aside-start` puts the aside first on wide screens, `--wide-aside` makes it 26rem."],
    laws=["L03", "L01"], uses=["panel"], classes=[".orca-split", ".orca-split--aside-start", ".orca-split--wide-aside"],
    examples=[("Split", '<div class="orca-split">' + PANEL.format("Main") + '<aside>' + PANEL.format("Aside") + "</aside></div>")],
    guide=["Split (main + aside)"],
))

add(Template(
    "media-split", "Media split", C,
    "The live picture in two thirds, details and actions in one third; the picture stays in view while the details scroll.",
    why="When watching and adjusting at the same time (zones, settings), the picture must stay visible next to the controls (Practical UI L14: less travel between related things).",
    when=["Video, zone and recording pages; any media with its settings."],
    how=["`<div class=\"orca-media-split\">` with `.orca-media-split__media` (the player or snapshot) and `.orca-media-split__side` (panels)."],
    laws=["L14", "L01"], uses=["recording-player", "panel"], classes=[".orca-media-split", ".orca-media-split__media", ".orca-media-split__side"], source="Tangerine",
    examples=[("Media split", '<div class="orca-media-split"><div class="orca-media-split__media"><div class="orca-skeleton orca-aspect-16x9"></div></div><div class="orca-media-split__side">' + PANEL.format("Status") + PANEL.format("Settings") + "</div></div>")],
    guide=["Media split"],
))

add(Template(
    "form-grid", "Form grid", C,
    "Short fields side by side in as many 16rem columns as fit; long fields span the full width.",
    why="Short related fields (host and port, from and to) read as one unit side by side (Practical UI L01); long answers keep the full width. Use only for short, related fields: one column is still the default (R01).",
    when=["Settings pages with many short fields; address and connection details."],
    avoid=["Ordinary forms: use one column (narrow form)."],
    how=["`<div class=\"orca-form-grid\">` of fields; add `.orca-form-grid__full` to textareas and anything long."],
    laws=["L01", "R01", "R06"], uses=["form-section"], classes=[".orca-form-grid", ".orca-form-grid__full"],
    examples=[("Connection", '<div class="orca-form-grid"><div class="orca-field"><label class="orca-label" for="fg-h">Host</label><input class="orca-input" id="fg-h"></div><div class="orca-field"><label class="orca-label" for="fg-p">Port</label><input class="orca-input orca-input--w8" id="fg-p" inputmode="numeric"></div><div class="orca-field orca-form-grid__full"><label class="orca-label" for="fg-n">Notes <span class="orca-optional">(optional)</span></label><textarea class="orca-textarea" id="fg-n" rows="2"></textarea></div></div>')],
    guide=["Form grid"],
))

add(Template(
    "narrow-form", "Narrow form", C,
    "One column of fields at most 36rem wide.",
    why="A single, narrow column is read and filled top to bottom without missing fields (Practical UI R01), and short line lengths keep labels and help readable (T09).",
    when=["Every ordinary form: create, edit, settings, sign-up."],
    how=["`<div class=\"orca-narrow-form\">` around the form; the generic form templates use it."],
    laws=["R01", "T09"], uses=["form-stack"], classes=[".orca-narrow-form"],
    examples=[("Form", '<div class="orca-narrow-form"><div class="orca-form-stack"><div class="orca-field"><label class="orca-label" for="nf-a">Name</label><input class="orca-input" id="nf-a"></div><div class="orca-field"><label class="orca-label" for="nf-b">Email</label><input class="orca-input" id="nf-b" type="email"></div><div class="orca-form-actions"><button class="orca-button orca-button--primary" type="button">Save</button></div></div></div>')],
    guide=["Narrow form"],
))
