from .registry import Element, add, category

C = category(
    "status", "Status marks and labels",
    "Small marks that state a condition or categorise an item. Status always pairs colour with a word and, where it matters, a shape.",
)

add(Element(
    "status-dot", "Status dot", C,
    "A 12px round mark before a word, showing the live state of a thing.",
    why="A dot plus a word is the lightest way to show state in dense lists (Miller's law); the word makes it readable "
        "without colour (Practical UI C03).",
    when=["Online/offline, running/stopped, enabled/disabled in tables and lists."],
    avoid=["The dot alone.", "More than five distinct dot colours on one screen."],
    how=["`<span class=\"orca-status\"><span class=\"orca-dot orca-dot--positive\"></span>Online</span>`.",
         "Tones: info, positive, caution, negative, neutral (default), purple, brand. Small: `.orca-dot--sm`.",
         "Live (recording, streaming): add `.orca-dot--pulse` to a negative dot; it stops for reduced motion."],
    classes=[".orca-status", ".orca-dot", ".orca-dot--positive", ".orca-dot--negative", ".orca-dot--caution", ".orca-dot--info", ".orca-dot--pulse"],
    tokens=["positive", "caution", "negative", "info", "neutral"],
    laws=["C03", "miller"],
    examples=[("Dots", """<div class="orca-stack">
  <span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online</span>
  <span class="orca-status"><span class="orca-dot orca-dot--negative orca-dot--pulse"></span>Recording</span>
  <span class="orca-status"><span class="orca-dot"></span>Disabled</span>
</div>""")],
    guide=["Status dot"],
    related=["badge"],
))

add(Element(
    "badge", "Badge", C,
    "A compact square label with a status or category word, solid or subtle.",
    why="A filled label stands out in a row of plain text so the state is found by scanning (Von Restorff), and its word "
        "keeps it meaningful without colour (C03, C04).",
    when=["Status of a record (Approved, Failed, Draft) in tables, cards and headers.", "Category labels (Beta, New)."],
    avoid=["Long text (more than three words).", "Interactive filters: use tags.", "Several solid badges in one row: use `--subtle`."],
    how=["`<span class=\"orca-badge orca-badge--positive\">Approved</span>`.",
         "Tones: `--info` (informative, action), `--positive`, `--caution`, `--negative`, default neutral grey fill, `--grey` (light neutral), `--purple` (tertiary), `--accent`, `--brand`.",
         "Subtle tint with dark text: add `--subtle` (info, positive, caution, negative); add a status icon inside.",
         "Uppercase is not applied: write sentence case; badges use the 12px label style."],
    a11y=["Text in solid badges holds 4.5:1 (caution uses black text)."],
    classes=[".orca-badge", ".orca-badge--info", ".orca-badge--positive", ".orca-badge--caution", ".orca-badge--negative",
             ".orca-badge--grey", ".orca-badge--purple", ".orca-badge--accent", ".orca-badge--brand", ".orca-badge--subtle"],
    tokens=["info-fill", "positive-fill", "caution-fill", "negative-fill", "neutral-fill", "on-fill", "on-caution"],
    laws=["restorff", "C03", "C04"],
    examples=[
        ("Solid", """<div class="orca-row">
  <span class="orca-badge orca-badge--info">Informative</span>
  <span class="orca-badge orca-badge--positive">Approved</span>
  <span class="orca-badge orca-badge--caution">Pending</span>
  <span class="orca-badge orca-badge--negative">Failed</span>
  <span class="orca-badge">Draft</span>
  <span class="orca-badge orca-badge--grey">Archived</span>
  <span class="orca-badge orca-badge--purple">Beta</span>
  <span class="orca-badge orca-badge--accent">New</span>
  <span class="orca-badge orca-badge--brand">Pro</span>
</div>"""),
        ("Subtle with icon", """<div class="orca-row">
  <span class="orca-badge orca-badge--subtle orca-badge--positive">{% icon "success" %}Online</span>
  <span class="orca-badge orca-badge--subtle orca-badge--caution">{% icon "warning" %}Degraded</span>
  <span class="orca-badge orca-badge--subtle orca-badge--negative">{% icon "error" %}Offline</span>
  <span class="orca-badge orca-badge--subtle orca-badge--info">{% icon "info" %}Updating</span>
</div>"""),
    ],
    guide=["Badge (information, positive, negative, caution)", "Badge (neutral, grey)", "Badge (accent, brand)",
           "Badge (action, informative)", "Badge (tertiary, purple)"],
    related=["status-dot", "tag", "count-badge"],
))

add(Element(
    "alert-icon", "Alert icon", C,
    "The status glyph that leads an alert, callout or field message, placed in the alert's left inset.",
    why="The same glyph in the same place on every message lets people classify it before reading (Jakob's law, C03).",
    when=["First element of every alert, callout, toast and error summary."],
    how=["`{% status_icon \"negative\" %}` with `.orca-alert-icon` when placed in a flex row.",
         "Match the glyph to the alert tone; never change a glyph's meaning."],
    classes=[".orca-alert-icon"], tokens=["negative", "caution", "positive", "info"],
    laws=["jakob", "C03"],
    examples=[("Leading an alert", """<div class="orca-row" style="align-items: flex-start; gap: var(--orca-space-16); max-width: 30rem; padding: var(--orca-space-16); border: var(--orca-border-width) solid var(--orca-border); border-inline-start: var(--orca-bar) solid var(--orca-caution)">
  <span class="orca-alert-icon">{% status_icon "caution" %}</span>
  <div><p class="orca-alert-title">Disk almost full</p><p class="orca-p">Videos older than 20 days will be deleted tonight.</p></div>
</div>""")],
    guide=["Alert icon"],
    related=["status-icon"],
))

add(Element(
    "count-badge", "Count badge", C,
    "A small pill with a number: unread items, pending tasks.",
    why="A count tells people whether something needs attention and how much, without opening it (Peak–end: prevent missed events).",
    when=["On a notifications button, a navigation item or a tab."],
    avoid=["Counts that are always non-zero (people learn to ignore them: banner blindness)."],
    how=["`<span class=\"orca-count\">3</span>`; red by default for 'needs attention'; `--neutral` for plain totals; `--accent`.",
         "On an icon button: add `.orca-has-count` to the button and put the count inside it.",
         "Cap at 99+: `{% if n > 99 %}99+{% else %}{{ n }}{% endif %}`.",
         "Include the meaning for screen readers: `aria-label=\"Notifications, 3 unread\"` on the button."],
    classes=[".orca-count", ".orca-count--neutral", ".orca-count--accent", ".orca-has-count"],
    tokens=["negative-fill", "radius-pill"],
    laws=["peak-end", "restorff"],
    examples=[("Count on a button", """<div class="orca-row orca-row--16">
  <button class="orca-icon-button orca-has-count" type="button" aria-label="Notifications, 3 unread">{% icon "notifications" %}<span class="orca-count" aria-hidden="true">3</span></button>
  <span>Videos <span class="orca-count orca-count--neutral">12</span></span>
</div>""")],
    guide=["Count badge"], source="ORCA",
))

add(Element(
    "tag", "Tag", C,
    "A label for a keyword or category; static, selectable (filter) or removable (chosen value).",
    why="Tags make applied filters and chosen values visible and reversible (Practical UI S06, Postel's law); the selected "
        "state adds a tick and an outline, not only colour (C03).",
    when=["Keywords on a record; filter chips; values chosen in a multi-picker."],
    avoid=["Status (use a badge).", "Tags as navigation."],
    how=["Static: `<span class=\"orca-tag\">North building</span>`.",
         "Selectable filter: `<button class=\"orca-tag\" type=\"button\" aria-pressed=\"false\" data-orca-toggle>Weekdays</button>`.",
         "Removable: `<span class=\"orca-tag\"><span class=\"orca-tag__text\">Entrance A</span><button class=\"orca-tag__remove\" type=\"button\" aria-label=\"Remove Entrance A\">{% icon \"close\" %}</button></span>`.",
         "Long values truncate inside the tag; give the full value in `title`."],
    a11y=["Remove buttons name the value they remove. Selected filter tags use `aria-pressed`."],
    classes=[".orca-tag", ".orca-tag--selected", ".orca-tag__remove", ".orca-tag__text"],
    tokens=["neutral-bg", "accent"],
    laws=["S06", "postel", "C03"],
    examples=[("Tags", """<div class="orca-row">
  <span class="orca-tag">North building</span>
  <button class="orca-tag" type="button" aria-pressed="true" data-orca-toggle>Weekdays</button>
  <button class="orca-tag" type="button" aria-pressed="false" data-orca-toggle>Weekends</button>
  <span class="orca-tag"><span class="orca-tag__text">Entrance A</span><button class="orca-tag__remove" type="button" aria-label="Remove Entrance A">{% icon "close" %}</button></span>
</div>""")],
    guide=["Tag", "Selected tag", "Removable tag"],
    related=["badge"],
))
