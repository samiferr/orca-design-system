from ..registry import add, category
from . import Component

C = category(
    "component-actions", "Actions",
    "Button groups, menus, and the action sets on records and rows.",
    level="component",
)

add(Component(
    "button-group", "Button group", C,
    "Related buttons joined into one control, or spaced as a set.",
    why="Joining buttons shows they act on the same thing (Practical UI L01: common region); spacing keeps dangerous neighbours apart (Fitts's law).",
    when=["Joined: alternatives on one object (Zoom in, Zoom out, Reset).", "Spaced: a set of independent actions (Export, Print)."],
    avoid=["Choosing a mode: use a segmented control or toggle buttons with aria-pressed."],
    how=["`<div class=\"orca-button-group\" role=\"group\" aria-label=…>` of `.orca-button`; `--spaced` for 8px gaps.",
         "Keep the same variant within a joined group; never join a destructive button."],
    classes=[".orca-button-group", ".orca-button-group--spaced"],
    laws=["L01", "fitts"],
    uses=["button"],
    examples=[("Joined and spaced", """<div class="orca-row orca-row--16">
  <div class="orca-button-group" role="group" aria-label="Zoom"><button class="orca-button orca-button--dense" type="button" aria-label="Zoom out">{% icon "minus" %}</button><button class="orca-button orca-button--dense" type="button">100%</button><button class="orca-button orca-button--dense" type="button" aria-label="Zoom in">{% icon "plus" %}</button></div>
  <div class="orca-button-group orca-button-group--spaced" role="group" aria-label="Report"><button class="orca-button" type="button">Export CSV</button><button class="orca-button" type="button">Schedule</button></div>
</div>""")],
    guide=["Button group"],
))

add(Component(
    "dropdown-menu", "Dropdown menu", C,
    "A button that opens a list of actions.",
    why="Rare or secondary actions go behind one button so the screen keeps one clear priority (Hick's law, Practical UI S04), while staying one click away.",
    when=["More than two secondary actions on an object; account menus; 'Add' menus with several kinds."],
    avoid=["Choosing a value: use a select or dropdown select.", "The one main action: show it as a button."],
    how=["`<div class=\"orca-anchor\">` with `<button class=\"orca-button\" type=\"button\" aria-haspopup=\"menu\" aria-expanded=\"false\" aria-controls=\"m1\" data-orca-menu>` and `<ul class=\"orca-popover\" role=\"menu\" id=\"m1\" hidden>`.",
         "Items are dropdown items. Group with `.orca-menu__separator` and `.orca-menu__group` labels; put destructive items last.",
         "`orca-popover--end` aligns it to the button's end edge; `--up` opens upwards near the bottom of the screen."],
    a11y=["orca.js: Enter/Space/Down open on the first item, Up on the last; arrows move; Escape closes and returns focus."],
    classes=[".orca-anchor", ".orca-popover", ".orca-popover--end", ".orca-popover--up", ".orca-menu__separator", ".orca-menu__group"],
    laws=["hick", "S04", "jakob"],
    uses=["button", "dropdown-item"],
    examples=[("Actions menu", """<div class="orca-anchor">
  <button class="orca-button" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="dm-1" data-orca-menu>Actions{% icon "chevron-down" %}</button>
  <ul class="orca-popover" role="menu" id="dm-1" hidden>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "edit" %}Rename</button></li>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "copy" %}Duplicate</button></li>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "external-link" %}Open stream</a></li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none"><button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">{% icon "delete" %}Delete</button></li>
  </ul>
</div>""")],
    guide=["Dropdown menu"], source="Tangerine",
))

add(Component(
    "dropdown-item", "Dropdown item", C,
    "One action in a menu: icon, label, optional description or shortcut; danger and disabled variants.",
    why="Consistent rows with a leading icon and a verb are scanned fast (Miller's law); a description removes doubt about what an item does (Practical UI W04).",
    when=["Every row of a dropdown menu."],
    how=["`<li role=\"none\"><button class=\"orca-menu__item\" role=\"menuitem\" type=\"button\">` or an `<a>` for navigation.",
         "Description: wrap text in `.orca-menu__text` with `.orca-menu__desc`. Shortcut: a `.orca-kbd` at the end.",
         "`--danger` for destructive items (confirm them); `aria-disabled=\"true\"` with the reason in the description."],
    classes=[".orca-menu__item", ".orca-menu__item--danger", ".orca-menu__text", ".orca-menu__desc"],
    laws=["miller", "W04", "B07"],
    uses=["icon", "kbd"],
    examples=[("Items", """<ul class="orca-popover" role="menu" style="position: static; display: block" aria-label="Example items">
  <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "copy" %}Copy link<kbd class="orca-kbd">Ctrl C</kbd></button></li>
  <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "upload" %}<span class="orca-menu__text">Export<span class="orca-menu__desc">CSV with one row per hour</span></span></button></li>
  <li role="none"><button class="orca-menu__item" role="menuitem" type="button" aria-disabled="true">{% icon "archive" %}<span class="orca-menu__text">Archive<span class="orca-menu__desc">Stop the run first</span></span></button></li>
  <li role="none"><button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">{% icon "delete" %}Delete</button></li>
</ul>""")],
    guide=["Dropdown item"], source="Tangerine",
))

add(Component(
    "copy-button", "Copy button", C,
    "A value with a Copy button that confirms 'Copied' in place and for screen readers.",
    why="Copying exact values (keys, addresses) by hand causes errors; one click with visible confirmation is faster and certain (Doherty threshold, Tesler's law).",
    when=["IDs, API keys, addresses, links, commands."],
    how=["`<div class=\"orca-copy\"><code class=\"orca-copy__value\" id=\"v1\">…</code><button class=\"orca-button\" type=\"button\" data-orca-copy=\"v1\">{% templatetag openblock %} icon \"copy\" class=\"orca-icon--copy\" {% templatetag closeblock %}{% templatetag openblock %} icon \"check\" class=\"orca-icon--copied\" {% templatetag closeblock %}<span data-orca-copy-label>Copy</span></button></div>`.",
         "For 1.5 s the label reads 'Copied', the copy icon becomes a check mark and the change is announced. Where the clipboard is blocked, the value is selected instead."],
    classes=[".orca-copy", ".orca-copy__value", ".orca-icon--copy", ".orca-icon--copied"],
    laws=["doherty", "tesler"],
    uses=["button", "code-text"],
    examples=[("Copy a stream address", """<div class="orca-copy"><code class="orca-copy__value" id="cp-1">https://media.example.com/v/4821</code><button class="orca-button" type="button" data-orca-copy="cp-1">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy</span></button></div>""")],
    guide=["Copy button (copied confirmation)"],
))

add(Component(
    "record-actions", "Record actions", C,
    "On a record's page: one visible main action and a 'More actions' menu for the rest.",
    why="One visible action keeps the decision simple (Hick's law, Practical UI B03); the overflow menu keeps the rest reachable without crowding the header.",
    when=["The header of detail pages and cards with several actions."],
    how=["`<div class=\"orca-record-actions\">` with the main action as a button and an icon button (`aria-label=\"More actions for Entrance A\"`) opening a dropdown menu.",
         "Destructive actions go last in the menu and ask for confirmation."],
    classes=[".orca-record-actions"],
    laws=["hick", "B03", "B13"],
    uses=["icon-button", "dropdown-menu"],
    examples=[("Record actions", """<div class="orca-record-actions orca-anchor">
  <a class="orca-button" href="#">{% icon "edit" %}Edit video</a>
  <button class="orca-icon-button orca-icon-button--outlined" type="button" aria-label="More actions for Entrance A" aria-haspopup="menu" aria-expanded="false" aria-controls="ra-menu" data-orca-menu>{% icon "more" %}</button>
  <ul class="orca-popover orca-popover--end" role="menu" id="ra-menu" hidden>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "pin" %}Pin to dashboard</button></li>
    <li role="none"><button class="orca-menu__item" role="menuitem" type="button">{% icon "restart" %}Restart stream</button></li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none"><button class="orca-menu__item orca-menu__item--danger" role="menuitem" type="button">{% icon "delete" %}Delete video</button></li>
  </ul>
</div>""")],
    guide=["Record actions (one button + overflow menu)"], source="Tangerine",
))

add(Component(
    "row-actions", "Row actions", C,
    "Small actions at the end of a table row: one or two ghost buttons and an overflow menu.",
    why="Actions next to the row they affect shorten travel (Practical UI L14); quiet styling keeps many rows from shouting (B05). They are always visible, never hover-only, so touch and keyboard users find them.",
    when=["The last column of data tables."],
    how=["`<td><div class=\"orca-row-actions\">` with `orca-button--ghost orca-button--sm` buttons or icon buttons whose `aria-label` names the row ('Edit Entrance A').",
         "At most two visible actions; the rest in a menu."],
    classes=[".orca-row-actions"],
    laws=["L14", "B05", "fitts"],
    uses=["icon-button", "dropdown-menu"],
    examples=[("In a row", """<table class="orca-table" style="max-width: 32rem"><tbody><tr><td>Entrance A</td><td><span class="orca-status"><span class="orca-dot orca-dot--positive"></span>Online</span></td>
  <td><div class="orca-row-actions"><a class="orca-button orca-button--ghost orca-button--sm" href="#">Edit</a><button class="orca-icon-button orca-icon-button--sm" type="button" aria-label="More actions for Entrance A">{% icon "more" %}</button></div></td></tr></tbody></table>""")],
    guide=["Row actions"],
))
