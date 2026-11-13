from .registry import Element, add, category

C = category(
    "foundations", "Base styles",
    "The tokens all other elements are built from: colour, type, space, shape, elevation, layers, size and motion. "
    "Use the names, never raw values. Projects may change only brand tokens.",
)

add(Element(
    "color-palette", "Colour palette", C,
    "Raw colours: a 13-step gray scale and eleven hues with nine numbered steps each.",
    why="A small, named palette keeps colour consistent and lets semantic tokens point at known values "
        "(Practical UI C18: name raw colours separately from their uses). Generating the hues in OKLCH gives every "
        "step the same perceived lightness across hues, so a chart's series read as equally important.",
    when=["Charts, zones, calendars and illustrations that need several distinct categories.",
          "Defining a new semantic token inside ORCA itself."],
    avoid=["Text, controls, backgrounds and status: use `semantic-colors`.",
           "Separating series by hue alone: also vary lightness or add a shape, label or pattern."],
    how=["Gray: `--orca-gray-0` (white) to `--orca-gray-1000` (black).",
         "Hues: `--orca-{red|orange|amber|yellow|green|teal|cyan|blue|indigo|purple|pink}-{100..900}`; 100 is lightest.",
         "For data series use `--orca-chart-1`…`--orca-chart-8`, which pick contrasting steps for each theme.",
         "Text on a hue step: steps 100–400 take `--orca-text` in light themes; 600–900 take white."],
    tokens=["gray-500", "blue-600", "chart-1", "heat-3"],
    laws=["C18", "C03", "aesthetic"],
    examples=[("Gray and one hue", """<div class="orca-row">
  <span class="orca-swatch" style="--orca-swatch: var(--orca-gray-200)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-gray-500)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-gray-900)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-teal-200)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-teal-500)"></span>
  <span class="orca-swatch" style="--orca-swatch: var(--orca-teal-800)"></span>
</div>""")],
    guide=["Colour palette", "Neutral scale (gray)", "Hue scales (eleven hues, numbered steps)"],
    related=["semantic-colors", "swatch"], source="ORCA",
))

add(Element(
    "semantic-colors", "Semantic colour tokens", C,
    "Colours named by their job: text, backgrounds, lines, interaction, status, actions, planning and data.",
    why="Components written against roles (`--orca-text-muted`, `--orca-border-strong`) work in every theme without "
        "change, and every role carries a tested contrast promise (Practical UI C09, C01).",
    when=["Every colour in every element and page."],
    avoid=["Picking a token for its look instead of its job (a muted heading is still `--orca-text`).",
           "`--orca-border` (decorative, 1.6:1) on a control: controls need `--orca-border-strong` (3:1)."],
    how=["Text: `text` (body, labels, headings), `text-muted` (help, meta), `text-inactive` (unselected nav).",
         "Backgrounds: `bg` page, `bg-alt` separate region, `bg-input` fields, `bg-hover`, `bg-active` (pressed, selected), `bg-elevated` floating.",
         "Lines: `border` decorative, `border-strong` controls, `border-weak` row separators.",
         "Status families `info`, `positive`, `caution`, `negative`, `neutral`: the bare name for marks and text, `-bg` for tints, `-fill` for solid badges.",
         "Actions: `primary*` (main action, green), `danger*` (confirmed destruction), `brand-strong*` (brand fill).",
         "Pair every status colour with an icon and a word."],
    a11y=["`text` and `text-muted` hold 4.5:1 on `bg`, `bg-alt` and `bg-input` in every theme.",
          "Known exception from Vanilla: `caution` text is 3.0:1 in light themes, so never use it alone."],
    tokens=["text", "text-muted", "bg", "bg-alt", "border-strong", "positive", "negative-bg", "primary"],
    laws=["C09", "C18", "C01", "C04"],
    examples=[("Roles in use", """<div style="background: var(--orca-bg-alt); padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border)">
  <p class="orca-p">Body text uses <code class="orca-code">--orca-text</code>.</p>
  <p class="orca-p orca-muted">Secondary text uses <code class="orca-code">--orca-text-muted</code>.</p>
  <span class="orca-badge orca-badge--subtle orca-badge--positive">{% icon "success" %} Approved</span>
</div>""")],
    guide=["Semantic colour tokens"],
    related=["color-palette", "themes"],
))

add(Element(
    "brand-color", "Brand colour and surfaces", C,
    "The one brand colour, the fills derived from it, and the page surfaces it sits on.",
    why="One brand colour plus neutrals is usually enough (Practical UI C07). Deriving the text-carrying fill "
        "automatically keeps any brand colour readable, moving the contrast work from the developer to the system "
        "(Tesler's law).",
    when=["One brand moment per page: the top bar, brand button, logo mark or a highlight rule.",
          "Re-branding: set `ORCA['BRAND']['color']` and nothing else."],
    avoid=["More than one brand-filled element per screen (Von Restorff: emphasis loses power when repeated).",
           "Showing status: brand never means success, warning or error.",
           "Links and checked controls: use the accent colour."],
    how=["`--orca-brand`: the colour as given, for decorative marks and 3px bars (needs only 3:1).",
         "`--orca-brand-strong`: fills that carry text, darkened until `--orca-brand-on` reads at 4.5:1.",
         "`--orca-brand-strong-hover` / `-active`: derived hover and pressed fills.",
         "Surfaces: page `--orca-bg`, set-apart regions `--orca-bg-alt`, floating `--orca-bg-elevated`.",
         "Set it in settings; any adjustment ORCA makes is reported as a system-check warning (`orca.W001`)."],
    a11y=["Never show state by brand colour alone; selection uses the accent and a shape."],
    tokens=["brand", "brand-strong", "brand-strong-hover", "brand-on", "bg", "bg-alt", "bg-elevated"],
    laws=["C07", "C08", "restorff", "tesler"],
    examples=[("Brand moments", """<div class="orca-stack">
  <span class="orca-row">{% orca_logo href="" %}</span>
  <hr class="orca-divider orca-divider--brand">
  <button class="orca-button orca-button--brand" type="button">Start free trial</button>
</div>""")],
    guide=["Brand colour and surfaces"],
    related=["accent-color", "button", "logo"], source="ORCA",
))

add(Element(
    "accent-color", "Accent colour", C,
    "The single interactive colour: links, checked ticks, radios, switches, progress, selected days.",
    why="One consistent action colour teaches people what they can act on (Practical UI C07); using it for every "
        "'on' state makes selection recognisable at a glance.",
    when=["Links, checked ticks, radios and switches, progress fills, selected calendar days, "
          "accent outlines and badges."],
    avoid=["Static headings or decorative icons: action colour on non-interactive things misleads (C07).",
           "Large fills behind long text."],
    how=["Use `var(--orca-accent)`; hover is `var(--orca-accent-hover)`.",
         "Set `ORCA['BRAND']['accent']` (light and paper) and optionally `accent_dark`; ORCA adjusts it to 4.5:1.",
         "Text on an accent fill is `var(--orca-bg)`."],
    a11y=["Holds 4.5:1 on `bg` and `bg-alt` in every theme, so it works for link text."],
    tokens=["accent", "accent-hover"],
    laws=["C07", "jakob"],
    examples=[("Accent in use", """<p class="orca-p">Read the <a class="orca-link" href="#">retention policy</a>.</p>
<label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Email me a daily report</label>""")],
    guide=["Accent colour"],
    related=["text-link", "checkbox"], source="ORCA",
))

add(Element(
    "themes", "Themes", C,
    "Light, dark and paper share every token name. ORCA has one appearance, named ORCA.",
    why="Writing components once against shared names means a theme can never break a component (Postel's law: "
        "reliable output in every context). Users with light sensitivity or bright surroundings choose what suits them.",
    when=["Always: every page gets all three themes for free.",
          "Set `ORCA['THEME']` to `light`, `dark` or `paper` to force one. `auto` (default) follows the OS and the user's saved choice."],
    avoid=["Theme-specific CSS: if you need it, a token is missing, so report it.",
           "Pure black backgrounds: dark uses #262626 and #202020."],
    how=["Put `{% orca_html_attrs %}` on `<html>` and `{% orca_head %}` in `<head>`.",
         "A theme toggle is a button with `data-orca-theme-toggle`; it cycles light → dark → paper and remembers the choice.",
         "Appearance: ORCA only (square corners, 1.5px borders, filled fields with a bottom border, inside focus ring)."],
    a11y=["Contrast holds in every theme; dark lifts floating surfaces one step so elevation shows without shadows."],
    tokens=["bg", "text"],
    laws=["postel", "C11", "C12"],
    examples=[("Theme toggle", """<button class="orca-icon-button orca-icon-button--outlined" type="button" data-orca-theme-toggle aria-label="Change theme">{% icon "sun" %}</button>""")],
    guide=["Themes (light, dark, paper)", "Appearances (Lumen, Tangerine)"],
    related=["toggle-button"],
))

add(Element(
    "typography", "Fonts and type styles", C,
    "Ubuntu Sans (variable) for everything, JetBrains Mono for code, on a fixed type scale.",
    why="One legible sans serif with two working weights keeps the interface calm and readable (Practical UI T01, T04); "
        "a fixed scale makes hierarchy predictable (T05).",
    when=["Every piece of text; pick the style by role: heading, title, body, detail, label or code."],
    avoid=["New sizes or weights in page CSS.", "Weights other than 400 and 550 for interface text (thin 180/275 only for the large h2/h4 styles).",
           "All caps for anything longer than a short label (W07)."],
    how=["Heading: `--orca-type-h1`…`h6`, `--orca-type-page-title`, `--orca-type-display`.",
         "Title: `--orca-type-title` (panel and card titles, 18/24 550).",
         "Body: `--orca-type-body` (16/24) and `--orca-type-body-strong` (550). Bold is 550, not 700.",
         "Detail: `--orca-type-detail` (14/20) for help, meta and timestamps; `--orca-type-label` (12/16 550) for table headers, badges, kickers and stat card labels.",
         "Figure: `--orca-type-figure` (28/36 550) for a stat card's number.",
         "Code: `--orca-type-code` with `--orca-font-mono` (JetBrains Mono, self-hosted; it keeps 0/O and 1/l/I distinct). Code blocks use the `--orca-code-*` tokens.",
         "Numbers in tables and stats get `font-variant-numeric: tabular-nums` (`.orca-num`).",
         "Apply as `font: var(--orca-type-body)`. Brand tokens `font_sans` / `font_mono` swap the families."],
    a11y=["Sizes are in rem so they follow the user's font-size setting; the root grows to 18px above 1681px.",
          "Running text is capped at `--orca-measure` (70ch)."],
    tokens=["type-h1", "type-title", "type-body", "type-detail", "type-label", "type-code", "font-sans", "font-mono"],
    laws=["T01", "T04", "T05", "T07", "T09", "aesthetic"],
    examples=[("The scale", """<div class="orca-stack">
  <p class="orca-h3">Heading 3 · 24/32 550</p>
  <p class="orca-panel-title">Title · 18/24 550</p>
  <p class="orca-p">Body · 16/24 400</p>
  <p class="orca-small orca-muted">Detail · 14/20 400</p>
  <p class="orca-card-kicker">Label · 12/16 550</p>
  <code class="orca-code">Code · JetBrains Mono</code>
</div>""")],
    guide=["Fonts", "Type scale", "Type styles (heading, title, body, detail)", "Monospace font"],
    related=["heading", "paragraph"],
))

add(Element(
    "spacing", "Spacing scale", C,
    "Eleven spacing steps on the 8px unit, named by their pixel value.",
    why="A small set of spacing options removes guesswork and makes grouping visible: related things sit closer "
        "than unrelated things (Miller's law, Practical UI L08, L09).",
    when=["Every margin, padding and gap."],
    avoid=["Values off the scale (6px, 10px, 18px).", "Using the same gap at every nesting level: it flattens grouping."],
    how=["`--orca-space-4` menu rows · `-8` icon to label, related controls, label to field · `-12` field to help text · "
         "`-16` button and input side padding, card padding, between fields · `-24` between sections · `-32` between page regions · `-48` alert text inset.",
         "Work from the inside out: the innermost gap is smallest.",
         "Utilities: `.orca-stack` (column, 8px), `.orca-row` (wrapping row, 8px; `.orca-row--16`)."],
    tokens=["space-4", "space-8", "space-12", "space-16", "space-24", "space-32"],
    laws=["miller", "L08", "L09", "L01"],
    examples=[("Nested spacing", """<div style="padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border); display: grid; gap: var(--orca-space-24)">
  <div style="display: grid; gap: var(--orca-space-4)"><p class="orca-panel-title">Section one</p><p class="orca-small orca-muted">8px and under inside a group</p></div>
  <div style="display: grid; gap: var(--orca-space-4)"><p class="orca-panel-title">Section two</p><p class="orca-small orca-muted">24px between groups</p></div>
</div>""")],
    guide=["Spacing scale (8 px)"],
    related=["divider"],
))

add(Element(
    "borders", "Borders", C,
    "Three line weights: 1px hairline, 1.5px outline, 3px emphasis bar.",
    why="Consistent line weights make structure readable without decoration (Practical UI S02); the 3px bar is "
        "reserved for emphasis so it keeps its meaning.",
    when=["Hairline: rules, table header line, row separators.", "1.5px: outlines of buttons, cards, alerts, tick boxes; the field bottom border.",
          "3px: the selected tab, an alert's side bar, the focus ring, a highlight rule."],
    avoid=["Borders that box every group (Practical UI L01): use space first."],
    how=["Width tokens: `--orca-hairline`, `--orca-border-width`, `--orca-bar`.",
         "Colour tokens: `--orca-border` (decorative), `--orca-border-strong` (controls, 3:1), `--orca-border-weak` (rows)."],
    tokens=["hairline", "border-width", "bar", "border", "border-strong", "border-weak"],
    laws=["R18", "S02"],
    examples=[("Three weights", """<div class="orca-stack">
  <hr class="orca-divider orca-divider--flush">
  <div style="height: 2rem; border: var(--orca-border-width) solid var(--orca-border-strong)"></div>
  <hr class="orca-divider orca-divider--highlight orca-divider--flush">
</div>""")],
    guide=["Borders"],
    related=["divider"],
))

add(Element(
    "radii", "Corner radii", C,
    "ORCA is square; only round marks and bar ends are rounded.",
    why="One consistent shape language is part of the system's recognisable look (Aesthetic–usability effect); "
        "rounding reserved for round marks (radios, dots, avatars) keeps those marks distinct from boxes (checkboxes).",
    when=["`--orca-radius-none` for every box: buttons, fields, cards, menus, dialogs, badges, tags.",
          "`--orca-radius-round` for radios, status dots, avatars, step markers, the switch handle.",
          "`--orca-radius-pill` for the switch track and count badges; `--orca-radius-bar` for progress tracks."],
    avoid=["Rounding a checkbox: square means pick many, round means pick one (Practical UI R07)."],
    how=["Use the tokens even for 0, so a later rounding change only edits a token."],
    tokens=["radius-none", "radius-round", "radius-pill", "radius-bar"],
    laws=["aesthetic", "R07"],
    examples=[("Shapes", """<div class="orca-row orca-row--16">
  <button class="orca-button" type="button">Square button</button>
  <span class="orca-avatar orca-avatar--s">AL</span>
  <span class="orca-dot orca-dot--positive"></span>
  <span class="orca-count">3</span>
</div>""")],
    guide=["Corner radii (rounding)"],
))

add(Element(
    "shadows", "Shadows and elevation", C,
    "Three shadows (card, elevated, dragged) and elevation utilities. Only floating things cast a shadow.",
    why="Depth signals what sits above the page and what can be moved (Practical UI C12, L05). Reserving shadows "
        "for floating things keeps them meaningful.",
    when=["`shadow-card`: the hover lift of an interactive card.", "`shadow-elevated`: menus, dropdown lists, popovers, toasts, drawers.",
          "`shadow-dragged`: a dragged item, a dialog, a sidebar opened over content."],
    avoid=["Shadows on resting cards, panels or page sections: use a border or `bg-alt`."],
    how=["Utilities: `.orca-elevation-0` … `.orca-elevation-3` (2 and 3 also set `--orca-bg-elevated`).",
         "In dark themes elevation also comes from the lighter `--orca-bg-elevated` surface."],
    tokens=["shadow-card", "shadow-elevated", "shadow-dragged", "bg-elevated"],
    classes=[".orca-elevation-0", ".orca-elevation-1", ".orca-elevation-2", ".orca-elevation-3"],
    laws=["C12", "L05"],
    examples=[("Elevation levels", """<div class="orca-row orca-row--16">
  <div class="orca-elevation-1" style="padding: var(--orca-space-16)">Card</div>
  <div class="orca-elevation-2" style="padding: var(--orca-space-16)">Elevated</div>
  <div class="orca-elevation-3" style="padding: var(--orca-space-16)">Dragged</div>
</div>""")],
    guide=["Shadows (card, elevated, dragged)", "Elevation utilities"],
))

add(Element(
    "layers", "Layers (z-index)", C,
    "A fixed stacking order from page content to the skip link.",
    why="A named stacking order prevents the 'z-index: 9999' arms race and guarantees, for example, that a save "
        "toast is never hidden behind a dialog (Peak–end rule: the end of an action must be seen).",
    when=["Any positioned element that must sit above or below another."],
    avoid=["Raw z-index numbers."],
    how=["Order: `layer-base` 0 < `raised` 1 < `sticky` 10 < `sidebar` 20 < `dropdown` 100 < `drawer` 150 < `dialog` 200 < `toast` 300 < `tooltip` 400 < `skip` 1000.",
         "Use `z-index: var(--orca-layer-dropdown)`."],
    tokens=["layer-sticky", "layer-dropdown", "layer-drawer", "layer-dialog", "layer-toast", "layer-tooltip"],
    laws=["peak-end"],
    examples=[("Using a layer", """<div style="position: relative; height: 4rem; background: var(--orca-bg-alt)">
  <div class="orca-elevation-2" style="position: absolute; z-index: var(--orca-layer-dropdown); top: var(--orca-space-8); left: var(--orca-space-8); padding: var(--orca-space-8)">Dropdown layer</div>
</div>""")],
    guide=["Layers"], source="ORCA",
))

add(Element(
    "control-heights", "Control heights", C,
    "Five heights shared by buttons, fields, selects and toggles: sm, dense, md, lg, xl.",
    why="Controls that share a height line up in rows and toolbars (alignment), and the 44px touch minimum is applied "
        "in one place for every control (Fitts's law, Practical UI B11).",
    when=["md (37px) by default; dense (29px) in top bars and filter bars; sm (22.5px) inside table rows; "
          "lg (44px) for touch-first screens; xl (48px) for phone primary actions."],
    avoid=["Mixing heights in one row of controls."],
    how=["Modifiers: `--sm`, `--dense`, `--lg`, `--xl` on `.orca-button`, `.orca-input`, `.orca-select`, `.orca-icon-button`.",
         "On coarse pointers and below 620px every control grows to `--orca-control-lg` (44px) automatically."],
    tokens=["control-sm", "control-dense", "control-md", "control-lg", "control-xl"],
    laws=["fitts", "B11"],
    examples=[("Heights side by side", """<div class="orca-row">
  <button class="orca-button orca-button--sm" type="button">Small</button>
  <button class="orca-button orca-button--dense" type="button">Dense</button>
  <button class="orca-button" type="button">Default</button>
  <button class="orca-button orca-button--lg" type="button">Large</button>
  <button class="orca-button orca-button--xl" type="button">Extra large</button>
</div>""")],
    guide=["Control heights (sm, md, lg, xl)"],
))

add(Element(
    "motion", "Motion", C,
    "Four durations and two easings, all under the 400 ms Doherty threshold.",
    why="Fast, consistent feedback keeps people in flow (Doherty threshold). Motion explains change; it never "
        "decorates. Reduced-motion users get the end state immediately (Von Restorff accessibility note).",
    when=["snap 0.1s: hover on buttons, tabs, rows.", "fast 0.165s: field fills, chevrons, card lift.",
          "brisk 0.333s: ticks, switches, accordions, drawers, progress."],
    avoid=["Animations longer than 0.333s on interface feedback.", "Looping motion except spinners, skeletons and indeterminate progress."],
    how=["`transition: background-color var(--orca-duration-snap) var(--orca-ease-in)` for hover.",
         "`var(--orca-ease-out)` for anything arriving.",
         "The base layer stops animations for `prefers-reduced-motion: reduce`."],
    tokens=["duration-snap", "duration-fast", "duration-brisk", "ease-out", "ease-in"],
    laws=["doherty", "restorff"],
    examples=[("Hover speed", """<button class="orca-button" type="button">Hover me: 0.1s</button>""")],
    guide=["Animation", "Motion"],
))

add(Element(
    "aspect-ratio", "Aspect-ratio utilities", C,
    "Reserve the space of images and video before they load.",
    why="Reserving space stops the page jumping when media arrives, which feels faster and avoids mis-taps "
        "(Doherty threshold: perceived performance; Fitts's law).",
    when=["Any image, video, snapshot or chart whose size is unknown until it loads."],
    how=["Wrapper: `.orca-ratio.orca-ratio--16x9` (also 1x1, 4x3, 3x2, 21x9, 3x4) with the media inside.",
         "Single element: `.orca-aspect-16x9` etc. Custom ratio: `style=\"--orca-ratio: 5 / 4\"` on `.orca-ratio`."],
    classes=[".orca-ratio", ".orca-ratio--16x9", ".orca-aspect-16x9"],
    laws=["doherty"],
    examples=[("16:9 frame", """<div class="orca-ratio orca-ratio--16x9" style="max-width: 20rem">
  <img src="{% static "orca/img/sample-street.svg" %}" alt="City street at dusk" loading="lazy">
</div>""")],
    guide=["Aspect-ratio utilities"], source="ORCA",
))

add(Element(
    "scrollbar", "Scrollbar style", C,
    "A thin, token-coloured scrollbar for inner scrolling regions.",
    why="Inner scroll areas need a visible cue that there is more content (Practical UI S06); a thin bar in "
        "`border-strong` stays visible without competing with content.",
    when=["Scrolling panels, menus, code blocks, sidebars."],
    avoid=["Styling the page's main scrollbar: leave the OS default."],
    how=["Add `.orca-scroll` to the element that scrolls; it sets `overflow: auto`."],
    classes=[".orca-scroll"], tokens=["border-strong"],
    laws=["S06"],
    examples=[("Scrolling region", """<div class="orca-scroll" style="max-height: 6rem; border: var(--orca-border-width) solid var(--orca-border); padding: var(--orca-space-8)">
  {% for i in "123456789" %}<p class="orca-p">Row {{ i }}</p>{% endfor %}
</div>""")],
    guide=["Scrollbar style"], source="ORCA",
))
