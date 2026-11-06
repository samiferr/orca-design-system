from .registry import Element, add, category

C = category(
    "icons", "Icons",
    "One icon set, 16px, single ink in currentColor. Icons support words; they never replace them.",
)

GUIDE_GLYPHS = ["menu", "notifications", "snapshot", "statistics", "plus", "search", "play", "arrow-right", "chevron-left",
                "chevron-right", "chevron-down", "close", "delete", "archive", "restart", "location", "edit", "filter", "star",
                "more", "sort", "grid", "chat", "sliders", "home", "help", "unlock", "success", "error", "settings"]

add(Element(
    "icon", "Icon", C,
    "An inline SVG glyph from the ORCA set, sized by token and coloured by its text.",
    why="Familiar icons speed recognition (Jakob's law) but few are universal, so ORCA icons always sit beside a word or "
        "carry an accessible name (Hick's law: oversimplification). One set with one line weight keeps the interface coherent (Practical UI F09).",
    when=["Beside a label in buttons, menus, navigation and status messages.", "Alone only in icon buttons with an `aria-label`."],
    avoid=["Icons from another set on the same screen.", "Icons as the only carrier of meaning.", "Decorative icons that compete with content (B12)."],
    how=["`{% icon \"search\" %}` renders decorative inline SVG (`aria-hidden`).",
         "`{% icon \"close\" label=\"Close\" %}` only when the icon stands alone without a labelled control.",
         "Sizes: `size=\"xs\"` 12px (inside 12–14px text), `s` 16px default (every control), `m` 20px, `l` 24px (heading icons), `xl` 36px (empty states). Aliases: small=xs, default=s, large=l.",
         "Colour comes from `currentColor`; set `color` on the parent, never on the path.",
         "List all names: `python -m orca icons`."],
    a11y=["Decorative by default. Interactive icon-only controls put the name on the control, not the svg."],
    classes=[".orca-icon", ".orca-icon--xs", ".orca-icon--m", ".orca-icon--l", ".orca-icon--xl", ".orca-with-icon"],
    tokens=["icon-xs", "icon-s", "icon-m", "icon-l", "icon-xl", "icon"],
    laws=["jakob", "hick", "F09", "B12"],
    examples=[("Sizes", """<div class="orca-row orca-row--16">
  {% icon "statistics" size="xs" %}{% icon "statistics" %}{% icon "statistics" size="m" %}{% icon "statistics" size="l" %}{% icon "statistics" size="xl" %}
</div>"""),
              ("Icon with a word", """<span class="orca-with-icon">{% icon "location" %}North building</span>""")],
    guide=["Icon (small, default, large)", "Icon sizes (xs, s, m, l, xl)"],
    related=["icon-set", "icon-button"],
))

add(Element(
    "status-icon", "Status icon", C,
    "The four status glyphs (success, warning, error, info), each a distinct shape in its status colour.",
    why="Status must survive colour-blindness: four different shapes plus a word carry the meaning, colour confirms it "
        "(Practical UI C03, C04; Von Restorff accessibility).",
    when=["Alerts, field errors, validation summaries, status badges, run results."],
    avoid=["Using a status glyph decoratively, or in another colour."],
    how=["`{% status_icon \"positive\" %}` · `\"caution\"` · `\"negative\"` · `\"info\"` · `\"neutral\"`.",
         "Always followed by a word: 'Online', 'Needs attention', 'Failed'."],
    a11y=["Decorative unless `label=` is given; prefer the visible word."],
    classes=[".orca-status-icon--positive", ".orca-status-icon--caution", ".orca-status-icon--negative", ".orca-status-icon--info"],
    tokens=["positive", "caution", "negative", "info"],
    laws=["C03", "C04", "restorff"],
    examples=[("Four statuses", """<div class="orca-stack">
  <span class="orca-with-icon">{% status_icon "positive" %}Online</span>
  <span class="orca-with-icon">{% status_icon "caution" %}Disk 90% full</span>
  <span class="orca-with-icon">{% status_icon "negative" %}Offline since 08:14</span>
  <span class="orca-with-icon">{% status_icon "info" %}Firmware update available</span>
</div>""")],
    guide=["Status icon (four status glyphs)", "Success", "Error"],
    related=["badge", "alert-icon"],
))

add(Element(
    "icon-set", "Icon set", C,
    "The named glyphs: 106 from Vanilla (via Tangerine) plus ORCA glyphs for ideas Vanilla lacks.",
    why="A single set with one line weight looks intentional (Aesthetic–usability effect, Practical UI F09). ORCA draws the "
        "missing glyphs (home, edit, filter, star, calendar…) on Vanilla's 16px grid instead of mixing in a second set.",
    when=["Pick a name from the set; use aliases when the guide's word differs (bell → notifications, refresh → restart, pencil → edit)."],
    avoid=["Adding SVGs from other sets (Lucide, Material) to an ORCA screen. If a glyph is missing, use a word and ask for it to be added."],
    how=["Guide icons: " + ", ".join(GUIDE_GLYPHS) + ".",
         "Full list with previews: the docs site's Icons page, or `python -m orca icons`.",
         "Arrows: arrow-up/down/left/right and diagonals. Chevrons: chevron-up/down/left/right (mirror left/right in RTL)."],
    tokens=["icon"],
    laws=["F09", "aesthetic", "jakob"],
    examples=[("Guide icons", "<div class=\"orca-row orca-row--16\" style=\"max-width: 30rem\">\n  "
               + "".join(f'<span title="{g}">{{% icon "{g}" size="m" %}}</span>' for g in GUIDE_GLYPHS)
               + "\n</div>")],
    guide=["Menu (hamburger)", "Notifications", "Snapshot", "Statistics", "Plus", "Search (magnifier)", "Play", "Arrows",
           "Chevrons (left, right, down)", "Close", "Delete", "Archive", "Restart", "Location", "Lucide icon set", "Edit (pencil)",
           "Filter", "Star", "More (ellipsis)", "Sort", "Grid", "Chat", "Sliders", "Home", "Help", "Unlock", "Refresh", "Settings"],
    related=["icon", "planning-icons"],
))
