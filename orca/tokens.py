"""ORCA design tokens: the single source of truth.

``python -m orca build`` turns this module into ``orca/static/orca/css/tokens.css``. Never edit
the generated CSS by hand. Values come from the Tangerine system (built from Canonical's Vanilla
framework 4.59), as used in ``wise_people_analyzer``; departures are marked ``ORCA:`` in the usage note.

Only the tokens in ``BRAND_TOKENS`` may be changed by a project (through ``settings.ORCA``). Every
other token is locked so that every ORCA screen keeps the same, tested contrast and rhythm.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from . import color

THEMES = ("light", "dark", "paper")
APPEARANCE = "tangerine"  # ORCA has one appearance: Tangerine.


@dataclass(frozen=True)
class Token:
    name: str
    light: str
    dark: str | None = None  # None: same as light
    paper: str | None = None  # None: same as light
    usage: str = ""
    group: str = ""

    def value(self, theme: str) -> str:
        if theme == "dark" and self.dark is not None:
            return self.dark
        if theme == "paper" and self.paper is not None:
            return self.paper
        return self.light


@dataclass(frozen=True)
class Scale:
    """A theme-independent token (space, size, motion, type...)."""

    name: str
    value: str
    usage: str = ""
    group: str = ""


@dataclass(frozen=True)
class BrandToken:
    key: str  # key in settings.ORCA["BRAND"]
    css: list[str] = field(default_factory=list)
    default: str = ""
    usage: str = ""


# ----------------------------------------------------------------------------------------------
# Brand tokens: the ONLY values a project may change.
# ----------------------------------------------------------------------------------------------

BRAND_TOKENS = [
    BrandToken(
        "name", [], "ORCA",
        "Product name. Used by the Logo primitive as the wordmark and as the logo's alt text.",
    ),
    BrandToken(
        "logo", [], "",
        "Static path of the logo image (SVG preferred), e.g. 'brand/logo.svg'. Empty: the Logo shows the name as a wordmark.",
    ),
    BrandToken(
        "favicon", [], "",
        "Static path of a 32px PNG or an SVG favicon. Empty: no favicon tags are written.",
    ),
    BrandToken(
        "color", ["--orca-brand"], "#0f95a1",
        "The brand colour. Decorative brand marks and the 3px brand bars use it as given. "
        "ORCA derives --orca-brand-strong (fills that carry text, darkened until --orca-brand-on reads at 4.5:1), "
        "--orca-brand-strong-hover and --orca-brand-strong-active from it, and the top bar ground --orca-brand-bar "
        "(the colour mixed with 30% black, as in wise_people_analyzer) with --orca-brand-bar-on, -hover and -active.",
    ),
    BrandToken(
        "on_color", ["--orca-brand-on"], "",
        "Text and icons on brand fills. Empty: ORCA picks black or white, whichever reads better.",
    ),
    BrandToken(
        "accent", ["--orca-accent"], "#0066cc",
        "The interactive colour of the light and paper themes: links, checked ticks and radios, switches that are on, "
        "progress fills, selected days. ORCA darkens it if it falls below 4.5:1 on the page grounds.",
    ),
    BrandToken(
        "accent_dark", ["--orca-accent"], "#6699cc",
        "The interactive colour in the dark theme. Empty: derived from 'accent', lightened until it reads at 4.5:1 on #262626.",
    ),
    BrandToken(
        "font_sans", ["--orca-font-sans"],
        '"Ubuntu Sans", -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        "Font stack for all interface text. ORCA self-hosts Ubuntu Sans (variable, 100–800). "
        "A replacement face must have regular (400) and semibold (550 or 600) weights and you must load it yourself.",
    ),
    BrandToken(
        "font_mono", ["--orca-font-mono"],
        '"Ubuntu Sans Mono", ui-monospace, Consolas, Menlo, monospace',
        "Font stack for code, keyboard keys and tabular identifiers.",
    ),
]

BRAND_KEYS = {t.key for t in BRAND_TOKENS}
BRAND_CSS_NAMES = {
    "--orca-brand", "--orca-brand-strong", "--orca-brand-strong-hover", "--orca-brand-strong-active",
    "--orca-brand-bar", "--orca-brand-bar-hover", "--orca-brand-bar-active", "--orca-brand-bar-on",
    "--orca-brand-on", "--orca-accent", "--orca-accent-hover", "--orca-font-sans", "--orca-font-mono",
}


# ----------------------------------------------------------------------------------------------
# Raw palette (primitive colour tokens). Use them only through semantic tokens, or for charts.
# ----------------------------------------------------------------------------------------------

NEUTRAL = [
    ("0", "#ffffff"), ("50", "#f7f7f7"), ("100", "#f2f2f2"), ("150", "#ebebeb"), ("200", "#e5e5e5"),
    ("300", "#d9d9d9"), ("400", "#999999"), ("500", "#707070"), ("600", "#666666"), ("700", "#373737"),
    ("800", "#262626"), ("900", "#111111"), ("1000", "#000000"),
]

# Eleven hues, nine numbered steps each (100 lightest, 900 darkest), generated in OKLCH so that the
# same step has the same perceived lightness across hues. Use them for charts, zones and calendars.
HUES = {
    "red": 25, "orange": 50, "amber": 75, "yellow": 100, "green": 145, "teal": 185,
    "cyan": 215, "blue": 255, "indigo": 278, "purple": 305, "pink": 350,
}
STEPS = {
    100: (0.965, 0.030), 200: (0.915, 0.060), 300: (0.840, 0.100), 400: (0.750, 0.135),
    500: (0.660, 0.160), 600: (0.570, 0.160), 700: (0.480, 0.140), 800: (0.400, 0.110), 900: (0.310, 0.080),
}


def hue_scale() -> list[tuple[str, str]]:
    out = []
    for hue, angle in HUES.items():
        for step, (lightness, chroma) in STEPS.items():
            out.append((f"{hue}-{step}", color.oklch_in_gamut(lightness, chroma, angle)))
    return out


# ----------------------------------------------------------------------------------------------
# Semantic colour tokens (themed). Components use only these.
# ----------------------------------------------------------------------------------------------

T = Token
SEMANTIC = [
    # Text
    T("text", "#000000", "#ffffff", group="Text", usage="All body text, labels and headings. 21:1 on --orca-bg."),
    T("text-muted", "rgba(0,0,0,0.6)", "rgba(255,255,255,0.6)", group="Text",
      usage="Secondary text: help text, meta, timestamps, placeholders. Holds 4.5:1 on --orca-bg, --orca-bg-alt and --orca-bg-input."),
    T("text-inactive", "rgba(0,0,0,0.75)", "rgba(255,255,255,0.75)", group="Text",
      usage="Unselected navigation items. Brightens to --orca-text on hover and selection."),
    T("icon", "#000000", "#ffffff", group="Text", usage="Icons that are not status marks."),
    T("link-visited", "#7d42b8", "#a679d2", group="Text", usage="Visited links in running text only."),
    # Grounds
    T("bg", "#ffffff", "#262626", "#f3f3f3", group="Grounds",
      usage="The default fill of controls and surfaces that have no ground of their own: buttons, tags, tooltips, swatch wells."),
    T("bg-page", "#f7f7f7", "#202020", "#f3f3f3", group="Grounds",
      usage="ORCA: the page ground behind the panels, as in wise_people_analyzer (surface-page). The <body> uses it."),
    T("bg-panel", "#ffffff", "#262626", "#ffffff", group="Grounds",
      usage="ORCA: panels, cards, side navigation and drawers' content set on the page ground (wise_people_analyzer surface-panel). "
            "White in light and paper, the raised grey in dark."),
    T("bg-stat", "#fff8d6", "#3a3318", group="Grounds",
      usage="ORCA: the pale yellow of stat cards (wise_people_analyzer surface-stat); a muted amber tint in dark. Pair with --orca-border-stat."),
    T("bg-alt", "#f7f7f7", "#202020", "#ebebeb", group="Grounds", usage="A region set apart from the page: a side panel, a card preview, an image well."),
    T("bg-input", "#f5f5f5", "#2f2f2f", "#eaeaea", group="Grounds", usage="Fill of text fields, selects and dropdown buttons."),
    T("bg-hover", "#f2f2f2", "#313131", "#e7e7e7", group="Grounds", usage="Hover fill of anything interactive that has no fill of its own."),
    T("bg-active", "#ebebeb", "#373737", "#e0e0e0", group="Grounds", usage="Pressed, selected and current states."),
    T("bg-elevated", "#ffffff", "#2c2c2c", "#ffffff", group="Grounds",
      usage="ORCA: floating surfaces (menus, dialogs, drawers, toasts). Dark lifts one step so elevation shows without a shadow (Practical UI C12)."),
    T("bg-code", "rgba(0,0,0,0.03)", "rgba(255,255,255,0.15)", group="Grounds", usage="Inline code and keyboard keys."),
    T("bg-overlay", "rgba(17,17,17,0.85)", group="Grounds", usage="The scrim behind dialogs and drawers."),
    # Lines
    T("border", "rgba(0,0,0,0.2)", "rgba(255,255,255,0.2)", group="Lines",
      usage="Decorative outlines: cards, panels, rules, tab base line. Not for controls."),
    T("border-strong", "#707070", "#939393", group="Lines",
      usage="Control boundaries that must be seen: button outlines, the field bottom border, tick boxes. 3:1 or more on every ground."),
    T("border-weak", "rgba(0,0,0,0.1)", "rgba(255,255,255,0.1)", group="Lines", usage="Row separators in tables and lists."),
    T("border-stat", "#ecd97a", "#6b5d22", group="Lines", usage="ORCA: the outline of a stat card on --orca-bg-stat."),
    # Interaction
    T("focus", "#0f6dcc", "#99ccff", group="Interaction",
      usage="ORCA: the 3px keyboard focus outline. Light and paper use #0f6dcc instead of Vanilla's #2e96ff so the ring holds 3:1 on every ground."),
    T("focus-on-fill", "#003008", "#ffffff", group="Interaction",
      usage="Focus outline drawn on a filled primary button, where --orca-focus would not show."),
    # Status: information
    T("info", "#24598f", "#5ea6ed", group="Status", usage="Information marks and text: icons, side bars, dots."),
    T("info-bg", "rgba(0,99,199,0.1)", "rgba(0,127,255,0.2)", group="Status", usage="Tint behind information messages."),
    T("info-bg-hover", "rgba(0,99,199,0.15)", "rgba(0,127,255,0.3)", group="Status", usage="Hover on an information tint."),
    T("info-fill", "#24598f", group="Status", usage="Solid information badge fill. Text on it: --orca-on-fill."),
    # Status: positive
    T("positive", "#0e8420", "#62a36c", group="Status", usage="Success marks and text."),
    T("positive-bg", "rgba(10,189,37,0.1)", "rgba(10,189,37,0.2)", group="Status", usage="Tint behind success messages."),
    T("positive-bg-hover", "rgba(0,199,30,0.15)", "rgba(0,199,30,0.3)", group="Status", usage="Hover on a success tint."),
    T("positive-fill", "#0e8420", group="Status", usage="Solid success badge fill."),
    # Status: caution
    T("caution", "#cc7900", "#c48831", group="Status",
      usage="Warning marks. As text in light and paper it is 3.0:1 (Vanilla's value, kept): never set caution text on its own, always with an icon and at 16px or more."),
    T("caution-bg", "rgba(199,90,0,0.1)", "rgba(255,115,0,0.2)", group="Status", usage="Tint behind warnings."),
    T("caution-bg-hover", "rgba(199,90,0,0.15)", "rgba(255,143,51,0.3)", group="Status", usage="Hover on a warning tint."),
    T("caution-fill", "#cc7900", group="Status", usage="Solid warning badge fill. Text on it is black: --orca-on-caution."),
    # Status: negative
    T("negative", "#c7162b", "#d17b85", group="Status", usage="Error marks and error text."),
    T("negative-bg", "rgba(199,0,20,0.1)", "rgba(255,102,120,0.2)", group="Status", usage="Tint behind errors and invalid fields."),
    T("negative-bg-hover", "rgba(199,0,20,0.15)", "rgba(255,102,120,0.3)", group="Status", usage="Hover on an error tint."),
    T("negative-fill", "#c7162b", group="Status", usage="Solid error badge fill."),
    # Status: neutral
    T("neutral", "#707070", "#a6a6a6", group="Status", usage="Neutral status marks (draft, unknown, off)."),
    T("neutral-bg", "#f2f2f2", "rgba(255,255,255,0.15)", group="Status", usage="Neutral tint: tags, avatars, neutral buttons."),
    T("neutral-bg-hover", "#e5e5e5", "rgba(255,255,255,0.2)", group="Status", usage="Hover on the neutral tint."),
    T("neutral-bg-active", "#dedede", "rgba(255,255,255,0.25)", group="Status", usage="Pressed neutral tint."),
    T("neutral-fill", "#666666", group="Status", usage="Solid neutral badge fill."),
    T("purple", "#7d42b8", "#a679d2", group="Status", usage="A fifth, non-status category colour (badges, dots). Never a status."),
    T("on-fill", "#ffffff", group="Status", usage="Text on the solid info, positive, negative, neutral and purple fills."),
    T("on-caution", "#000000", group="Status", usage="Text on the caution fill."),
    # Action fills
    T("primary", "#0e8420", "#008013", group="Actions", usage="Fill of the one main action on a screen (Tangerine: green)."),
    T("primary-hover", "#0c6d1a", "#00660f", group="Actions", usage="Hover fill of the primary button."),
    T("primary-active", "#0a5f17", "#00570d", group="Actions", usage="Pressed fill of the primary button."),
    T("primary-on", "#ffffff", group="Actions", usage="Text on the primary fill. 4.8:1 light, 5.0:1 dark."),
    T("danger", "#c7162b", "#a11223", group="Actions", usage="Fill of a confirmed destructive action (in a confirm dialog)."),
    T("danger-hover", "#b01326", "#8a0f1e", group="Actions", usage="Hover fill of the danger button."),
    T("danger-active", "#a21223", "#7c0e1b", group="Actions", usage="Pressed fill of the danger button."),
    T("danger-on", "#ffffff", group="Actions", usage="Text on the danger fill."),
    # Planning
    T("today", "#c7162b", "#ff8a95", group="Planning", usage="ORCA: the today marker and the now line on calendars."),
    T("weekend-bg", "rgba(0,0,0,0.03)", "rgba(255,255,255,0.04)", group="Planning", usage="Tint behind weekend columns and cells."),
    T("holiday-bg", "rgba(125,66,184,0.08)", "rgba(166,121,210,0.15)", group="Planning", usage="Tint behind holidays and closed days."),
    T("gridline", "rgba(0,0,0,0.1)", "rgba(255,255,255,0.1)", group="Planning", usage="Hour and half-hour lines in day and week views."),
]


def chart_tokens() -> list[Token]:
    """Categorical and sequential data colours, referencing the hue scales."""
    cat = ["blue-600", "orange-500", "teal-600", "purple-600", "amber-500", "pink-600", "green-600", "indigo-400"]
    cat_dark = ["blue-400", "orange-400", "teal-400", "purple-400", "amber-300", "pink-400", "green-400", "indigo-300"]
    out = [
        T(f"chart-{i + 1}", f"var(--orca-{c})", f"var(--orca-{d})", group="Data",
          usage=f"Categorical series {i + 1}. Use in order; pair every series with a legend label.")
        for i, (c, d) in enumerate(zip(cat, cat_dark))
    ]
    heat = ["blue-100", "blue-200", "blue-300", "blue-500", "blue-700", "blue-900"]
    heat_dark = ["blue-900", "blue-800", "blue-700", "blue-500", "blue-300", "blue-100"]
    out += [
        T(f"heat-{i}", f"var(--orca-{c})", f"var(--orca-{d})", group="Data",
          usage=f"Sequential level {i} of 5 (heat maps, capacity). Always print the value in the cell or a tooltip.")
        for i, (c, d) in enumerate(zip(heat, heat_dark))
    ]
    return out


# ----------------------------------------------------------------------------------------------
# Scales (theme independent)
# ----------------------------------------------------------------------------------------------

S = Scale
SPACE = [
    S("space-2", "0.125rem", "Hairline gaps: a tag's inner icon nudge, stacked meta lines.", "Spacing"),
    S("space-4", "0.25rem", "Vertical padding of menu items and navigation rows; gap inside a text stack.", "Spacing"),
    S("space-8", "0.5rem", "The unit. Icon to label, related controls, label to field.", "Spacing"),
    S("space-12", "0.75rem", "Field to its help text; inside tabs.", "Spacing"),
    S("space-16", "1rem", "Side padding of buttons and inputs; card padding; between form fields.", "Spacing"),
    S("space-24", "1.5rem", "Between sections inside a panel.", "Spacing"),
    S("space-32", "2rem", "Between page regions.", "Spacing"),
    S("space-40", "2.5rem", "Large section padding.", "Spacing"),
    S("space-48", "3rem", "Text inset of alerts and accordions; empty-state padding.", "Spacing"),
    S("space-64", "4rem", "Page sections on wide screens.", "Spacing"),
    S("space-96", "6rem", "Marketing-page section padding.", "Spacing"),
]

RADII = [
    S("radius-none", "0", "Tangerine is square: buttons, fields, cards, menus, dialogs, tables, badges.", "Shape"),
    S("radius-bar", "0.1875rem", "The 3px ends of progress tracks and event bars.", "Shape"),
    S("radius-pill", "1rem", "Switch track and count badges.", "Shape"),
    S("radius-round", "50%", "Round marks: radios, switch handle, status dots, avatars, step markers.", "Shape"),
]

BORDERS = [
    S("hairline", "1px", "Rules, tab base line, table header line, row separators.", "Lines"),
    S("border-width", "1.5px", "Every outline: buttons, cards, alerts, tick boxes, the field bottom border.", "Lines"),
    S("bar", "0.1875rem", "3px emphasis: selected tab, alert side bar, focus outline, highlight rule.", "Lines"),
    S("focus-width", "0.1875rem", "Width of the focus outline (3px).", "Lines"),
]

SHADOWS = [
    S("shadow-card", "0 1px 1px 0 rgba(0,0,0,0.15), 0 2px 2px -1px rgba(0,0,0,0.15), 0 0 3px 0 rgba(0,0,0,0.2)",
      "Hover lift of interactive cards. Cards at rest have no shadow.", "Elevation"),
    S("shadow-elevated", "0 1px 1px 0 rgba(0,0,0,0.15), 0 2px 2px -1px rgba(0,0,0,0.15), 0 0 3px 0 rgba(0,0,0,0.2)",
      "Floating surfaces: menus, dropdown lists, popovers, toasts, drawers.", "Elevation"),
    S("shadow-dragged", "0 0 2rem 0 rgba(0,0,0,0.2)",
      "Something lifted over the page: a dragged item, a collapsed sidebar opened over content.", "Elevation"),
]

LAYERS = [
    S("layer-base", "0", "Page content.", "Layers"),
    S("layer-raised", "1", "Selected tab bar, sticky table header.", "Layers"),
    S("layer-sticky", "10", "Top bar and sticky toolbars.", "Layers"),
    S("layer-sidebar", "20", "The sidebar while it opens over content.", "Layers"),
    S("layer-dropdown", "100", "Menus, dropdown lists, popovers.", "Layers"),
    S("layer-drawer", "150", "Drawers and their scrim.", "Layers"),
    S("layer-dialog", "200", "Modal dialogs and their backdrop.", "Layers"),
    S("layer-toast", "300", "Toasts: above dialogs so a save result is never hidden.", "Layers"),
    S("layer-tooltip", "400", "Tooltips.", "Layers"),
    S("layer-skip", "1000", "The skip link, above everything when focused.", "Layers"),
]

SIZES = [
    S("control-sm", "1.405rem", "Small controls (22.5px), 14/20 text. Toolbars inside tables.", "Control heights"),
    S("control-dense", "1.82rem", "Dense controls (29px): top bar, filter bars.", "Control heights"),
    S("control-md", "2.32rem", "The default height (37px) of buttons, fields, selects.", "Control heights"),
    S("control-lg", "2.75rem", "44px: the touch minimum. Every control grows to it on coarse pointers.", "Control heights"),
    S("control-xl", "3rem", "48px: phone primary actions and the FAB.", "Control heights"),
    S("tab-height", "3rem", "Tabs.", "Control heights"),
    S("icon-xs", "0.75rem", "12px icons inside 12–14px text.", "Icon sizes"),
    S("icon-s", "1rem", "16px: every icon inside a control. The default.", "Icon sizes"),
    S("icon-m", "1.25rem", "20px: standalone icons in lists and toolbars.", "Icon sizes"),
    S("icon-l", "1.5rem", "24px: heading icons, empty states inside panels.", "Icon sizes"),
    S("icon-xl", "2.25rem", "36px: page-level heading icons and empty states.", "Icon sizes"),
    S("avatar-xs", "1.5rem", "Avatar in dense rows.", "Avatar sizes"),
    S("avatar-s", "2rem", "Avatar in lists and chips.", "Avatar sizes"),
    S("avatar-m", "2.5rem", "Default avatar.", "Avatar sizes"),
    S("avatar-l", "3rem", "Profile headers.", "Avatar sizes"),
    S("avatar-xl", "6rem", "Profile pages.", "Avatar sizes"),
    S("thumb", "3rem", "Thumbnail images in lists.", "Media sizes"),
    S("thumb-lg", "6rem", "Thumbnail images in cards.", "Media sizes"),
    S("measure", "70ch", "Maximum width of running text (40–80 characters per line).", "Layout"),
    S("nav-height", "3.5rem", "Top bar height.", "Layout"),
    S("sidebar-width", "15rem", "Expanded sidebar.", "Layout"),
    S("sidebar-width-collapsed", "4rem", "Collapsed sidebar icon rail.", "Layout"),
    S("grid-max-width", "80rem", "Maximum content width.", "Layout"),
    S("grid-gutter", "2rem", "Column gutter from 1036px.", "Layout"),
    S("grid-gutter-small", "1.5rem", "Column gutter below 1036px.", "Layout"),
    S("grid-margin", "1.5rem", "Page side margin from 620px.", "Layout"),
    S("grid-margin-small", "1rem", "Page side margin below 620px.", "Layout"),
]

MOTION = [
    S("duration-snap", "0.1s", "Button, tab and row hover.", "Motion"),
    S("duration-fast", "0.165s", "Field fills, chevrons, card lift.", "Motion"),
    S("duration-brisk", "0.333s", "Ticks, switches, accordions, drawers, progress.", "Motion"),
    S("duration-slow", "0.5s", "Reserved. ORCA moved the switch handle to brisk to stay under the 400 ms Doherty threshold.", "Motion"),
    S("ease-out", "cubic-bezier(.215,.61,.355,1)", "Things arriving or changing state.", "Motion"),
    S("ease-in", "cubic-bezier(.55,.055,.675,.19)", "Hover fades on buttons and tabs.", "Motion"),
    S("opacity-disabled", "0.33", "Disabled controls keep their colours and drop to 33%.", "States"),
]

TYPE = [
    S("type-display", "100 5.25rem/6rem var(--orca-font-sans)", "Marketing display line.", "Type"),
    S("type-h1", "550 2.625rem/3rem var(--orca-font-sans)", "Heading 1 from 1036px; 2rem/2.5rem below.", "Type"),
    S("type-h2", "180 2.625rem/3rem var(--orca-font-sans)", "Heading 2: the thin Ubuntu signature; 2rem/2.5rem below 1036px.", "Type"),
    S("type-h3", "550 1.5rem/2rem var(--orca-font-sans)", "Heading 3.", "Type"),
    S("type-h4", "275 1.5rem/2rem var(--orca-font-sans)", "Heading 4: dialog, drawer and empty-state titles.", "Type"),
    S("type-h5", "550 1rem/1.5rem var(--orca-font-sans)", "Heading 5: bold body size.", "Type"),
    S("type-h6", "italic 400 1rem/1.5rem var(--orca-font-sans)", "Heading 6.", "Type"),
    S("type-page-title", "700 1.75rem/2.25rem var(--orca-font-sans)", "The one page title (wise_people_analyzer's dense title).", "Type"),
    S("type-title", "550 1.125rem/1.5rem var(--orca-font-sans)", "Panel and card titles.", "Type"),
    S("type-body", "400 1rem/1.5rem var(--orca-font-sans)", "Everything by default: body, labels, controls.", "Type"),
    S("type-body-strong", "550 1rem/1.5rem var(--orca-font-sans)", "Bold body. Vanilla's bold is 550, not 700.", "Type"),
    S("type-detail", "400 0.875rem/1.25rem var(--orca-font-sans)", "Help text, validation messages, meta, timestamps.", "Type"),
    S("type-label", "550 0.75rem/1rem var(--orca-font-sans)", "Table headers, badges, kickers, stat labels (uppercase allowed).", "Type"),
    S("type-stat", "550 1.25rem/1.75rem var(--orca-font-sans)", "Stat values.", "Type"),
    S("type-figure", "550 1.75rem/2.25rem var(--orca-font-sans)", "ORCA: the number of a stat card, larger than its label so it is read first.", "Type"),
    S("type-code", "400 0.9375rem/1.5rem var(--orca-font-mono)", "Code and keyboard keys.", "Type"),
    S("weight-regular", "400", "Body text.", "Type"),
    S("weight-strong", "550", "Bold text and headings.", "Type"),
]

ALL_SCALES = SPACE + RADII + BORDERS + SHADOWS + LAYERS + SIZES + MOTION + TYPE

# Density. "comfortable" is the default scale above. "dense" (data-density="dense" on <html> or on any region)
# tightens type, control heights and the larger spacing steps for data-heavy screens: dashboards, admin tools,
# documentation. Body text stays at 14px or more, labels at 12px, and every control still grows to the 44px touch
# minimum (control-lg) on coarse pointers, so density never costs accessibility.
DENSITIES = ("comfortable", "dense")
DENSE = {
    "space-16": "0.75rem", "space-24": "1rem", "space-32": "1.5rem", "space-40": "2rem", "space-48": "2rem",
    "space-64": "3rem", "space-96": "4rem",
    "control-sm": "1.25rem", "control-dense": "1.625rem", "control-md": "2rem", "tab-height": "2.5rem",
    "nav-height": "3rem", "grid-gutter": "1.5rem", "grid-gutter-small": "1rem", "grid-margin": "1rem",
    "type-display": "100 3.5rem/4rem var(--orca-font-sans)",
    "type-h1": "550 2rem/2.5rem var(--orca-font-sans)",
    "type-h2": "180 2rem/2.5rem var(--orca-font-sans)",
    "type-h3": "550 1.25rem/1.75rem var(--orca-font-sans)",
    "type-h4": "275 1.25rem/1.75rem var(--orca-font-sans)",
    "type-h5": "550 0.875rem/1.25rem var(--orca-font-sans)",
    "type-h6": "italic 400 0.875rem/1.25rem var(--orca-font-sans)",
    "type-page-title": "700 1.5rem/2rem var(--orca-font-sans)",
    "type-title": "550 1rem/1.5rem var(--orca-font-sans)",
    "type-body": "400 0.875rem/1.25rem var(--orca-font-sans)",
    "type-body-strong": "550 0.875rem/1.25rem var(--orca-font-sans)",
    "type-detail": "400 0.8125rem/1.125rem var(--orca-font-sans)",
    "type-stat": "550 1.125rem/1.5rem var(--orca-font-sans)",
    "type-figure": "550 1.5rem/2rem var(--orca-font-sans)",
    "type-code": "400 0.8125rem/1.25rem var(--orca-font-mono)",
}

BREAKPOINTS = [("x-small", 460), ("small", 620), ("large", 1036), ("x-large", 1681)]


def semantic_tokens() -> list[Token]:
    return SEMANTIC + chart_tokens()
