from ..registry import add, category
from . import Component

C = category(
    "identity-controls", "Identity and controls",
    "Who is signed in, panel headers, and small controls that personalise the interface.",
    level="component",
)

add(Component(
    "user-chip", "User chip", C,
    "Avatar, name and role of the signed-in person; opens the account menu.",
    why="Showing who is signed in, in the familiar top-right place, prevents acting under the wrong account (Jakob's law, Peak–end rule).",
    when=["The end of the top bar."],
    how=["`<button class=\"orca-user-chip\" type=\"button\" aria-haspopup=\"menu\" aria-expanded=\"false\" data-orca-menu aria-controls=…>` with a small avatar and `.orca-user-chip__text` (`__name`, `__role`), inside an `.orca-anchor` with the menu.",
         "Menu: Profile, Settings, separator, Sign out. Below 620px only the avatar shows; the button keeps the name as its accessible name."],
    classes=[".orca-user-chip", ".orca-user-chip__text", ".orca-user-chip__name", ".orca-user-chip__role"],
    laws=["jakob", "peak-end"],
    uses=["avatar", "dropdown-menu"],
    examples=[("User chip", """<div class="orca-anchor">
  <button class="orca-user-chip" type="button" aria-haspopup="menu" aria-expanded="false" aria-controls="uc-menu" data-orca-menu><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><span class="orca-user-chip__text"><span class="orca-user-chip__name">Ada Lovelace</span><span class="orca-user-chip__role">Administrator</span></span>{% icon "chevron-down" size="xs" %}</button>
  <ul class="orca-popover orca-popover--end" role="menu" id="uc-menu" hidden>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "user" %}Profile</a></li>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "settings" %}Settings</a></li>
    <li role="separator" class="orca-menu__separator"></li>
    <li role="none"><a class="orca-menu__item" role="menuitem" href="#">{% icon "log-out" %}Sign out</a></li>
  </ul>
</div>""")],
    guide=["User chip"], source="Tangerine",
))

add(Component(
    "panel-header", "Panel header", C,
    "A panel's top: title, short description and actions.",
    why="Each panel answers one question; naming it and placing its actions beside the name keeps controls next to what they change (Practical UI L14, Miller's law).",
    when=["Every panel, table card and chart frame."],
    how=["`<div class=\"orca-panel-header\">` with `.orca-panel-header__text` (`h2.orca-panel-title` + `.orca-panel-header__desc`) and `.orca-panel-header__actions` (ghost or dense buttons).",
         "Actions wrap under the title on narrow panels."],
    classes=[".orca-panel-header", ".orca-panel-header__text", ".orca-panel-header__desc", ".orca-panel-header__actions"],
    laws=["L14", "miller"],
    uses=["panel-title", "button"],
    examples=[("Panel header", """<div class="orca-panel-header" style="max-width: 36rem"><div class="orca-panel-header__text"><h2 class="orca-panel-title">People inside</h2><p class="orca-panel-header__desc">All entrances, updated every minute</p></div>
  <div class="orca-panel-header__actions"><button class="orca-button orca-button--ghost orca-button--dense" type="button">{% icon "restart" %}Refresh</button><a class="orca-button orca-button--dense" href="#">Open report</a></div></div>""")],
    guide=["Panel header"], source="Tangerine",
))

add(Component(
    "pin-control", "Pin control", C,
    "A pin toggle that shows 'Pinned' in words and announces changes.",
    why="Pinning changes where an item appears; saying so in words and announcing it confirms the action for everyone (Doherty threshold, C03).",
    when=["Detail pages and cards of items that can be pinned to a dashboard or list top."],
    how=["`<span class=\"orca-pin-control\">` with a pin button (`id`, `aria-pressed`, `data-orca-toggle`, `data-orca-state-on=\"Pinned\"`, `data-orca-state-off=\"Not pinned\"`) and `<span class=\"orca-pin-control__state\" data-orca-state-for=\"button-id\">`.",
         "Save on the server (htmx `hx-post`); revert and show an alert if it fails."],
    classes=[".orca-pin-control", ".orca-pin-control__state"],
    laws=["doherty", "C03"],
    uses=["pin-button"],
    examples=[("Pin control", """<span class="orca-pin-control"><button class="orca-icon-button orca-pin" id="pc-pin" type="button" aria-pressed="true" aria-label="Pin Entrance A to the dashboard" data-orca-toggle data-orca-state-on="Pinned" data-orca-state-off="Not pinned">{% icon "pin" %}</button><span class="orca-pin-control__state" data-orca-state-for="pc-pin">Pinned</span></span>""")],
    guide=["Pin control"], source="Tangerine",
))

add(Component(
    "theme-toggle", "Theme toggle", C,
    "A segmented choice of Auto, Light, Dark and Paper themes, remembered per browser.",
    why="People choose a theme for their eyes and surroundings; showing all options at once is clearer than a cycling button (Practical UI R11), and Auto respects the system setting by default (Tesler's law).",
    when=["Settings panels and account settings."],
    how=["`<fieldset class=\"orca-segmented\" data-orca-theme-choice>` with a legend and four radio labels `.orca-segmented__item` (values auto, light, dark, paper).",
         "orca.js applies and remembers the theme; ORCA's head script restores it before the page paints.",
         "A compact top-bar alternative is the theme toggle button (`data-orca-theme-toggle`, see Themes)."],
    classes=[".orca-segmented", ".orca-segmented__item"],
    laws=["R11", "tesler", "postel"],
    uses=["radio"],
    related=["themes"],
    examples=[("Theme choice", """<fieldset class="orca-segmented" data-orca-theme-choice><legend class="orca-label">Theme</legend>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="auto" checked>Auto</label>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="light">{% icon "sun" %}Light</label>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="dark">{% icon "moon" %}Dark</label>
  <label class="orca-segmented__item"><input type="radio" name="tt-theme" value="paper">Paper</label>
</fieldset>""")],
    guide=["Theme toggle"], source="Tangerine",
))

add(Component(
    "email-fallback", "Email button (with fallback link)", C,
    "An email button with the address shown and a Copy button, for when no mail app opens.",
    why="mailto links fail silently on many setups; showing the address with a Copy button guarantees a way through (Postel's law, Peak–end rule).",
    when=["Contact and support actions, sharing a report by email."],
    how=["`<div class=\"orca-stack\">` with the mailto button, then a copy button component holding the address.",
         "Prefill the subject with `?subject=` (URL-encoded); never put personal data in the URL."],
    classes=[".orca-copy"],
    laws=["postel", "peak-end"],
    uses=["email-button", "copy-button"],
    examples=[("Email support", """<div class="orca-stack" style="align-items: flex-start">
  <a class="orca-button" href="mailto:support@example.com?subject=Video%20offline">{% icon "mail" %}Email support</a>
  <div class="orca-copy"><code class="orca-copy__value" id="ef-addr">support@example.com</code><button class="orca-button orca-button--dense" type="button" data-orca-copy="ef-addr">{% icon "copy" class="orca-icon--copy" %}{% icon "check" class="orca-icon--copied" %}<span data-orca-copy-label>Copy address</span></button></div>
</div>""")],
    guide=["Email button (with fallback link)"], source="Tangerine",
))
