from ..registry import add, category
from . import Pattern

C = category(
    "records", "Record management",
    "Showing and changing one record and its children: detail panels, child tabs, activity, protected deletes and confirmations.",
    level="pattern",
)

add(Pattern(
    "detail-panel", "Detail panel", C,
    "One record's summary: title and status, its actions, and a table of its properties.",
    why="A record page answers 'what is it, what state is it in, what can I do' in that order (Practical UI L03); properties as aligned pairs are scanned fast (Miller's law).",
    when=["The main panel of a detail page; a side panel for the selected row."],
    how=["`<section class=\"orca-detail-panel\">` with `.orca-detail-panel__head` (`__title`: name + status light; record actions) and a key/value list or table card below."],
    classes=[".orca-detail-panel", ".orca-detail-panel__head", ".orca-detail-panel__title"],
    laws=["L03", "miller", "B03"],
    uses=["record-actions", "key-value-list", "status-light"],
    examples=[("Video", """<section class="orca-detail-panel" aria-labelledby="dp-t" style="max-width: 36rem">
  <div class="orca-detail-panel__head"><div class="orca-detail-panel__title"><h2 id="dp-t">Entrance A</h2><span class="orca-status orca-small"><span class="orca-dot orca-dot--positive"></span>Online <span class="orca-status__meta">for 12 days</span></span></div>
    <div class="orca-record-actions"><a class="orca-button orca-button--dense" href="#">{% icon "edit" %}Edit video</a><button class="orca-icon-button orca-icon-button--dense orca-icon-button--outlined" type="button" aria-label="More actions for Entrance A">{% icon "more" %}</button></div></div>
  <dl class="orca-kv"><div><dt>Site</dt><dd>North building</dd></div><div><dt>Format</dt><dd>MP4, 1080p</dd></div><div><dt>Address</dt><dd><code class="orca-code">media.example.com/v/4821</code></dd></div><div><dt>Views today</dt><dd class="orca-num">4,812</dd></div></dl>
</section>""")],
    guide=["Detail panel (header + actions + table)"], source="Tangerine",
))

add(Pattern(
    "parent-child-tabs", "Parent record with child tabs", C,
    "A parent record's summary followed by tabs, one per kind of child, each with its count.",
    why="Keeping the parent visible while browsing its children preserves context (Miller's law); counts on tabs say where the content is before clicking (Practical UI S06).",
    when=["Records that own lists of other records: a site's videos, zones and users."],
    how=["`<div class=\"orca-parent\">` with the page head, `.orca-parent__summary` (stat cards or key facts) and child tabs as page links; the active tab's panel holds the child list tab.",
         "Each tab is its own URL so it can be shared and survives a reload."],
    classes=[".orca-parent", ".orca-parent__summary"],
    laws=["miller", "S06", "jakob"],
    uses=["page-head", "child-tabs", "stat-card"],
    examples=[("Site", """<div class="orca-parent">
  <div class="orca-page-head" style="margin: 0"><div class="orca-page-head__text"><h1 class="orca-page-title">North building</h1><p class="orca-page-subtitle">12 Rue de la Gare, Lille</p></div><div class="orca-page-head__actions"><a class="orca-button" href="#">{% icon "edit" %}Edit site</a></div></div>
  <div class="orca-parent__summary"><div class="orca-stat-card"><p class="orca-stat-label">Visitors today</p><p class="orca-stat-value">9,530</p></div><div class="orca-stat-card"><p class="orca-stat-label">Videos online</p><p class="orca-stat-value">11 of 12</p></div></div>
  <nav class="orca-tabs__list" aria-label="North building"><a class="orca-tab" href="#">Overview</a><a class="orca-tab" href="#" aria-current="page">Videos <span class="orca-count orca-count--neutral">12</span></a><a class="orca-tab" href="#">Zones <span class="orca-count orca-count--neutral">5</span></a><a class="orca-tab" href="#">Users <span class="orca-count orca-count--neutral">3</span></a></nav>
</div>""")],
    guide=["Parent record with child tabs"],
))

add(Pattern(
    "child-list-tab", "Child list tab", C,
    "The content of one child tab: a list header scoped to the parent, the children's table and an empty state.",
    why="The same list tools as a top-level list make child lists familiar (Jakob's law); creating a child from here pre-fills the parent (Tesler's law).",
    when=["Inside parent-with-child-tabs pages."],
    how=["A list header ('Videos 12', search, 'Add video' that links to the form with `?site=…`), then a data table or card list; when empty, an empty state with the same create action."],
    classes=[".orca-list-header", ".orca-data-table"],
    laws=["jakob", "tesler"],
    uses=["list-header", "data-table", "empty-state"],
    examples=[("Empty child list", """<div><div class="orca-list-header"><h2 class="orca-list-header__title">Users <span class="orca-list-header__count">0</span></h2><div class="orca-list-header__tools"><a class="orca-button orca-button--primary orca-button--dense" href="#">{% icon "plus" %}Add user to North building</a></div></div>
  <div class="orca-empty">{% orca_illustration "empty" %}<h3 class="orca-empty-title">No users for this site</h3><p class="orca-empty-text">Add the people who should see North building's counts.</p></div></div>""")],
    guide=["Child list tab"],
))

add(Pattern(
    "activity-feed", "Activity feed", C,
    "Changes to a record or a site, grouped by day, each with who, what, when and the before and after values.",
    why="Seeing who changed what builds trust in shared data and answers 'why does this look different?' (Peak–end rule); grouping by day keeps a long history scannable (Miller's law).",
    when=["A history tab on records; an audit page for administrators."],
    how=["`<div class=\"orca-activity-feed\">` with `<h3 class=\"orca-activity-feed__day\">` headings and activity entries; 'Load older' at the end (never infinite scroll in an audit log)."],
    classes=[".orca-activity-feed", ".orca-activity-feed__day"],
    laws=["peak-end", "miller"],
    uses=["activity-entry"],
    examples=[("Feed", """<div class="orca-activity-feed" style="max-width: 36rem"><h3 class="orca-activity-feed__day">Today</h3>
  <div class="orca-activity"><span class="orca-avatar orca-avatar--s" aria-hidden="true">AL</span><div class="orca-activity__head"><span class="orca-badge orca-badge--subtle orca-badge--info">Updated</span><strong>Ada Lovelace</strong> changed Entrance A<time class="orca-activity__time" datetime="2026-11-06T08:14">08:14</time></div><dl class="orca-activity__change"><dt>Interval</dt><dd><del>15 min</del> → <ins>5 min</ins></dd></dl></div>
  <h3 class="orca-activity-feed__day">Yesterday</h3>
  <div class="orca-activity"><span class="orca-avatar orca-avatar--s" aria-hidden="true">GH</span><div class="orca-activity__head"><span class="orca-badge orca-badge--subtle orca-badge--positive">Created</span><strong>Grace Hopper</strong> added Gate 1<time class="orca-activity__time" datetime="2026-11-05T16:02">16:02</time></div></div>
  <div style="padding-top: var(--orca-space-12)"><button class="orca-button orca-button--ghost" type="button">Load older activity</button></div></div>""")],
    guide=["Activity feed"],
))

add(Pattern(
    "delete-blocked-notice", "Delete-blocked notice", C,
    "Why a record cannot be deleted yet, which records depend on it, and how to proceed.",
    why="A refusal without a reason is a dead end (Peak–end rule); listing the blockers with links turns it into a to-do list (Practical UI W15, Tesler's law).",
    when=["Deleting a record that protected relations still use (Django `ProtectedError`)."],
    how=["A negative callout titled 'Entrance A cannot be deleted yet', the reason, `<ul class=\"orca-blocked-list\">` of linked dependants with counts, and the alternative (disable or archive) as a button.",
         "Build it from `ProtectedError.protected_objects`, grouped by model."],
    classes=[".orca-blocked-list"],
    laws=["peak-end", "W15", "tesler"],
    uses=["callout", "list", "button-group"],
    examples=[("Blocked", """<div class="orca-callout orca-callout--negative" role="alert" style="max-width: 36rem">{% icon "error" %}<p class="orca-callout__title">Entrance A cannot be deleted yet</p>
  <div class="orca-callout__body"><p class="orca-p">These still use it. Remove or move them first.</p><ul class="orca-blocked-list"><li><a class="orca-link" href="#">2 zones</a> (Door line, Staff area)</li><li><a class="orca-link" href="#">1 alert rule</a> (Over capacity)</li></ul>
    <div class="orca-row"><button class="orca-button orca-button--dense" type="button">Disable video instead</button></div></div></div>""")],
    guide=["Delete-blocked notice (protected delete)"], source="Tangerine",
))

add(Pattern(
    "confirm-action-panel", "Confirm action panel", C,
    "A full-page confirmation for consequential actions: what will happen, what is kept, and the named action.",
    why="For actions too important for a small dialog, a page gives room to list consequences and needs a deliberate step (Practical UI B13; Doherty: useful friction), and works without script.",
    when=["Deleting a site, revoking a user, stopping all runs; the fallback of a confirm dialog."],
    how=["`<form class=\"orca-confirm-panel\" method=\"post\">` with a `.orca-confirm-panel__title` question, a list of what is removed and what is kept, an acknowledgement checkbox for irreversible cases, and form actions (danger button naming the action, Cancel link back).",
         "`--neutral` for non-destructive confirmations."],
    classes=[".orca-confirm-panel", ".orca-confirm-panel__title", ".orca-confirm-panel--neutral"],
    laws=["B13", "doherty", "peak-end"],
    uses=["confirm-dialog", "form-actions"],
    examples=[("Delete site", """<form class="orca-confirm-panel" method="post" onsubmit="return false"><h1 class="orca-confirm-panel__title">Delete North building?</h1>
  <div><p class="orca-p"><strong>Deleted:</strong></p><ul><li>12 videos and their zones</li><li>5 alert rules</li></ul></div>
  <div><p class="orca-p"><strong>Kept:</strong> counts in past reports.</p></div>
  <label class="orca-check"><input type="checkbox" required><span class="orca-check__box"></span>I understand this cannot be undone</label>
  <div class="orca-form-actions"><button class="orca-button orca-button--danger" type="submit">Delete site</button><a class="orca-button" href="#">Cancel</a></div></form>""")],
    guide=["Confirm action panel"], source="Tangerine",
))
