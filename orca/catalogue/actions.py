from .registry import Element, add, category

C = category(
    "actions", "Actions",
    "Things people press. One primary action per screen; everything else is quieter.",
)

add(Element(
    "button", "Button", C,
    "A command. Variants express importance: primary, secondary (default), ghost, link, plus brand, danger, neutral, elevated and outlines.",
    why="Three clearly different weights (filled, outlined, text) let people find the main action instantly and make "
        "the hierarchy survive colour-blindness (Practical UI B01, B02; Von Restorff effect). One primary action per screen "
        "keeps decisions fast (Hick's law, B03).",
    when=["`orca-button--primary`: the one main action of the screen or form (Save, Add image).",
          "default (no modifier): secondary actions and equal alternatives (Cancel, Export).",
          "`--ghost`: low-priority or repeated actions in toolbars and rows.",
          "`--danger`: only to confirm a destructive action inside a confirm dialog.",
          "`--brand`: the single brand moment on a marketing or onboarding screen.",
          "`--neutral`: filled grey for toggles and filter chips in toolbars.",
          "`--elevated`: a button floating over media or maps.",
          "`--outline-accent` / `--outline-danger`: a secondary action that needs a colour cue (a quiet first step of a delete)."],
    avoid=["Navigation: use a link.", "Two primary buttons on one screen.", "A red button as the first step of a delete (B13): use the default or `--outline-danger`, confirm with `--danger`.",
           "'OK', 'Submit', 'Yes': name the action."],
    how=["`<button class=\"orca-button orca-button--primary\" type=\"submit\">Save image</button>`. Always set `type`.",
         "Label: verb + object, one to three words, sentence case (B10).",
         "Order: most important first, left to right; stack full width on phones (B08).",
         "Icon + label: put `{% icon %}` before the text; the icon is decorative.",
         "Busy: set `aria-busy=\"true\"`, disable, and prepend `<span class=\"orca-spinner orca-spinner--sm\"></span>`.",
         "Aliases kept from earlier systems: positive = primary, negative = danger, base = ghost, secondary = default."],
    a11y=["Focus ring is drawn inside the button; on filled variants it uses the on-fill colour so it shows.",
          "Disabled buttons cannot be focused: explain why nearby or keep the button enabled and validate on press (B06, B07)."],
    classes=[".orca-button", ".orca-button--primary", ".orca-button--brand", ".orca-button--danger", ".orca-button--neutral",
             ".orca-button--ghost", ".orca-button--elevated", ".orca-button--outline-accent", ".orca-button--outline-danger"],
    tokens=["primary", "primary-hover", "danger", "brand-strong", "border-strong", "control-md"],
    laws=["B01", "B03", "B10", "B13", "hick", "restorff", "fitts"],
    examples=[
        ("Weights", """<div class="orca-row">
  <button class="orca-button orca-button--primary" type="button">Save image</button>
  <button class="orca-button" type="button">Cancel</button>
  <button class="orca-button orca-button--ghost" type="button">{% icon "copy" %}Duplicate</button>
</div>"""),
        ("Other variants", """<div class="orca-row">
  <button class="orca-button orca-button--brand" type="button">Start free trial</button>
  <button class="orca-button orca-button--danger" type="button">Delete image</button>
  <button class="orca-button orca-button--neutral" type="button">Neutral</button>
  <button class="orca-button orca-button--elevated" type="button">Elevated</button>
  <button class="orca-button orca-button--outline-accent" type="button">Outline accent</button>
  <button class="orca-button orca-button--outline-danger" type="button">Delete</button>
</div>"""),
        ("Busy and disabled", """<div class="orca-row">
  <button class="orca-button orca-button--primary" type="button" aria-busy="true" disabled><span class="orca-spinner orca-spinner--sm" style="color: inherit"></span>Saving</button>
  <button class="orca-button" type="button" disabled>Export</button>
  <span class="orca-small orca-muted">Export is available once the run has finished.</span>
</div>"""),
    ],
    guide=["Button (base, positive, negative, brand)", "Button (primary, brand, secondary, neutral, ghost, elevated, danger)",
           "Button outlines (accent, neutral, danger)", "Disabled button"],
    related=["button-size", "icon-button", "link-action"],
))

add(Element(
    "button-size", "Button sizes", C,
    "Size modifiers: sm, dense, default, lg, xl, plus block (full width) and icon-only.",
    why="Size follows context, not importance: dense toolbars need compact controls, phones need 44–48px targets "
        "(Fitts's law, Practical UI B11). Heights match fields so rows align.",
    when=["`--sm` inside table rows; `--dense` in top bars and filter bars; default elsewhere; `--lg`/`--xl` for touch-first and phone primary actions.",
          "`--block` for the primary action at the bottom of a phone form.", "`--icon-only` for a square button with just an icon (prefer `icon-button`)."],
    avoid=["Using size to signal importance: use the variant.", "Mixing sizes in one row."],
    how=["Add one size modifier to `.orca-button`. On coarse pointers every size grows to 44px automatically.",
         "Icon-only buttons need `aria-label`."],
    classes=[".orca-button--sm", ".orca-button--dense", ".orca-button--lg", ".orca-button--xl", ".orca-button--block", ".orca-button--icon-only"],
    tokens=["control-sm", "control-dense", "control-md", "control-lg", "control-xl"],
    laws=["fitts", "B11"],
    examples=[("Sizes", """<div class="orca-row">
  <button class="orca-button orca-button--sm" type="button">Small</button>
  <button class="orca-button orca-button--dense" type="button">Dense</button>
  <button class="orca-button" type="button">Default</button>
  <button class="orca-button orca-button--lg" type="button">Large</button>
  <button class="orca-button orca-button--icon-only" type="button" aria-label="Refresh">{% icon "restart" %}</button>
</div>
<div style="max-width: 20rem; margin-top: var(--orca-space-16)"><button class="orca-button orca-button--primary orca-button--block orca-button--xl" type="button">Save image</button></div>""")],
    guide=["Button sizes (small, dense, block, icon-only)", "Button sizes (sm, lg, xl)"],
    related=["button", "control-heights"],
))

add(Element(
    "link-action", "Link (tertiary action)", C,
    "A text-styled button or link for the least important actions.",
    why="The tertiary weight keeps rare or repeated actions available without competing with the primary one (Practical UI B01, B05); "
        "the underline keeps it recognisably interactive.",
    when=["'Show more', 'Clear filters', 'Edit' inside a sentence or summary; secondary navigation like 'Back to images'."],
    avoid=["The main action of a screen."],
    how=["Command: `<button class=\"orca-button orca-button--link\" type=\"button\">Clear filters</button>`.",
         "Navigation: `<a class=\"orca-link\">`.", "Name the destination or result, never 'Click here'."],
    classes=[".orca-button--link"], tokens=["accent"],
    laws=["B01", "B05", "W14"],
    examples=[("Tertiary", """<p class="orca-p">3 filters applied. <button class="orca-button orca-button--link" type="button">Clear filters</button></p>""")],
    guide=["Link"],
    related=["text-link", "button"],
))

add(Element(
    "pin-button", "Pin button", C,
    "A toggle that pins an item to the top of a list or to the dashboard.",
    why="Letting people keep their most-used items close reduces search effort on every visit (Fitts's law: shorter distance; Practical UI F03).",
    when=["Lists where a few items are used much more than others (albums, reports)."],
    how=["`<button class=\"orca-icon-button orca-pin\" type=\"button\" aria-pressed=\"false\" aria-label=\"Pin Entrance A\" data-orca-toggle data-orca-label-on=\"Unpin Entrance A\" data-orca-label-off=\"Pin Entrance A\">{% icon \"pin\" %}</button>`.",
         "Persist the state on the server; `data-orca-toggle` only flips the pressed state in the page."],
    a11y=["`aria-pressed` announces pinned/not pinned; the label names the item."],
    classes=[".orca-pin"], tokens=["accent", "bg-active"],
    laws=["fitts", "F03"],
    examples=[("Pin toggle", """<button class="orca-icon-button orca-pin" type="button" aria-pressed="true" aria-label="Unpin Entrance A" data-orca-toggle data-orca-label-on="Unpin Entrance A" data-orca-label-off="Pin Entrance A">{% icon "pin" %}</button>""")],
    guide=["Pin button"],
    related=["toggle-button"],
))

add(Element(
    "email-button", "Email button", C,
    "A mailto link styled as a button, with the address shown as a fallback.",
    why="mailto fails silently when no mail app is set up; showing the address lets people copy it instead "
        "(Postel's law: tolerate every setup).",
    when=["Contact support, send a report link, reply to an alert."],
    how=["`<a class=\"orca-button\" href=\"mailto:…?subject=…\">{% icon \"mail\" %}Email support</a>` followed by "
         "`<span class=\"orca-email-button__fallback\">support@example.com</span>`.", "URL-encode subject and body with `urlencode`."],
    classes=[".orca-email-button__fallback"],
    laws=["postel"],
    examples=[("Email with fallback", """<div>
  <a class="orca-button" href="mailto:support@example.com?subject=Video%20will%20not%20play">{% icon "mail" %}Email support</a>
  <span class="orca-email-button__fallback">support@example.com</span>
</div>""")],
    guide=["Email button"],
))

add(Element(
    "toggle-button", "Toggle button (pressed)", C,
    "A button that stays pressed to show an on state.",
    why="A pressed button is a familiar way to switch a view or a mode in toolbars (Jakob's law), and its pressed fill "
        "plus `aria-pressed` makes the state visible and announced (C03).",
    when=["Toolbar modes: show grid, bold, live view on/off, mute."],
    avoid=["Settings that are saved: use a switch.", "Choosing one of several views: use a view toggle group (segmented, phase 2)."],
    how=["`<button class=\"orca-button\" type=\"button\" aria-pressed=\"false\" data-orca-toggle>`.",
         "Keep the label constant ('Show grid'); the pressed state says whether it is on."],
    a11y=["Do not change the label when pressed unless you remove aria-pressed (the two together are confusing)."],
    classes=[".orca-button[aria-pressed]"], tokens=["bg-active"],
    laws=["jakob", "C03", "R14"],
    examples=[("Toggle", """<button class="orca-button orca-button--dense" type="button" aria-pressed="true" data-orca-toggle>{% icon "grid" %}Show grid</button>""")],
    guide=["Toggle button (pressed)"],
))

add(Element(
    "icon-button", "Icon button", C,
    "A square button with a single 16px icon and an accessible name. Quiet, outlined, accent and neutral-fill variants.",
    why="Icon buttons save space for frequent, well-known actions (close, more, refresh) while keeping a full "
        "control-height target (Fitts's law). Few icons are universal, so each needs a name (Hick's law: icons without labels).",
    when=["Close, more actions, refresh, pin, previous/next, toolbar actions people use often."],
    avoid=["Actions whose icon is not well known: use a button with a label.", "Destructive actions without confirmation."],
    how=["`<button class=\"orca-icon-button\" type=\"button\" aria-label=\"Close\">{% icon \"close\" %}</button>`.",
         "Variants: default quiet, `--outlined`, `--accent`, `--neutral`. Sizes: `--sm`, `--dense`, `--lg`.",
         "Add a visible tooltip with the same text when the meaning might be unclear (tooltip: phase 2)."],
    a11y=["`aria-label` is required. The icon is decorative.", "Target grows to 44px on touch."],
    classes=[".orca-icon-button", ".orca-icon-button--outlined", ".orca-icon-button--accent", ".orca-icon-button--neutral"],
    tokens=["icon", "bg-hover", "control-md"],
    laws=["fitts", "hick", "B11", "B12"],
    examples=[("Variants", """<div class="orca-row">
  <button class="orca-icon-button" type="button" aria-label="Close">{% icon "close" %}</button>
  <button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="More actions">{% icon "more" %}</button>
  <button class="orca-icon-button orca-icon-button--accent" type="button" aria-label="Refresh">{% icon "restart" %}</button>
  <button class="orca-icon-button orca-icon-button--neutral" type="button" aria-label="Settings">{% icon "settings" %}</button>
</div>""")],
    guide=["Icon button (quiet, outlined, accent, neutral fill)"],
    related=["button", "icon"],
))

add(Element(
    "fab", "Floating action button (FAB)", C,
    "A large floating button for the one creation action of a phone screen.",
    why="On phones the primary action floats within thumb reach at the bottom (Fitts's law, Practical UI F03) and its "
        "distinct shape makes it the one thing that stands out (Von Restorff). Familiar from mobile platforms (Jakob's law).",
    when=["Phone layouts (below 620px) of list pages with one create action."],
    avoid=["Desktop layouts: put the action in the page head.", "More than one FAB, or for anything other than the primary action."],
    how=["Icon-only: `<a class=\"orca-fab\" href=\"…\" aria-label=\"Add image\">{% icon \"plus\" %}</a>`.",
         "Extended (preferred: icon + label): add `.orca-fab--extended` and visible text.",
         "Leave 5rem of bottom padding on the page so the FAB never covers the last row."],
    a11y=["Icon-only FABs need `aria-label`. The FAB is 56px."],
    classes=[".orca-fab", ".orca-fab--extended", ".orca-fab--static"],
    tokens=["primary", "shadow-dragged", "layer-sticky"],
    laws=["fitts", "restorff", "jakob"],
    examples=[("FAB (shown in place)", """<div class="orca-row orca-row--16">
  <a class="orca-fab orca-fab--static" href="#" aria-label="Add image">{% icon "plus" %}</a>
  <a class="orca-fab orca-fab--static orca-fab--extended" href="#">{% icon "plus" %}Add image</a>
</div>""")],
    guide=["Floating action button (FAB)", "Extended FAB"],
    source="ORCA",
))
