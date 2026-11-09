# Forms

Fields and the small groups around them. A form field is the unit people complete: label, hint, error and control in a fixed order.

## Form field

`id: form-field` · level: component · source: ORCA

Label, optional marker, help, error and one control, wired together. Text inputs and selects.

Built from: `label`, `required-marker`, `help-text`, `error-text`, `text-input`, `select`, `textarea`, `color-input`

### Why

Most form errors come from fields people misread. A fixed order (label, hint, error, control) means every field is read the same way, the hint is seen before answering and the error sits above the control where the keyboard cannot hide it (Practical UI R08, R10, R20). Generating the ARIA wiring removes the most common accessibility bug (Tesler's law).

### When to use

- Every single-value field of a form: text, number, email, date, select, textarea.

### When not to use

- One on/off option: use the toggle field.
- Choices from a short list: use a choice group.

### How to use

- Django forms: `{% orca_field form.name %}`. Options: `width="w8"` (input width), `label="…"`, `help_text="…"`, `hide_label=True` (search only).
- Manual markup: `<div class="orca-field">` with `orca-label`, `orca-help` (id), `orca-error` (id) and the control with `aria-describedby="error-id help-id"` and `aria-invalid` when invalid.
- Optional fields get “(optional)” automatically from `required=False`.
- Stack fields in `.orca-fields` (24px apart) so each label sits closer to its own control than to the field above.
- Date, time and date-time Django widgets render as native pickers with ISO values.

### Accessibility

- The error id comes first in `aria-describedby` so it is read before the hint.

#### Example: Text and select fields

```django
<div class="orca-fields" style="max-width: 24rem">
  <div class="orca-field">
    <label class="orca-label" for="ff-name">Video name</label>
    <p class="orca-help" id="ff-name-help">Shown on dashboards and in alert emails.</p>
    <input class="orca-input" id="ff-name" name="name" value="Entrance A" aria-describedby="ff-name-help">
  </div>
  <div class="orca-field">
    <label class="orca-label" for="ff-site">Site <span class="orca-optional">(optional)</span></label>
    <select class="orca-select" id="ff-site" name="site"><option value="">No site</option><option>North building</option><option>Warehouse</option></select>
  </div>
</div>
```

#### Example: Invalid field

```django
<div class="orca-field" style="max-width: 24rem">
  <label class="orca-label" for="ff-port">Port</label>
  <p class="orca-help" id="ff-port-help">Usually 554 for HTTPS.</p>
  <p class="orca-error" id="ff-port-error">{% icon "error" %}<span>Enter a port between 1 and 65535.</span></p>
  <input class="orca-input orca-input--w8" id="ff-port" name="port" value="70000" inputmode="numeric" aria-invalid="true" aria-describedby="ff-port-error ff-port-help">
</div>
```

#### Example: With Django

```django
<pre class="orca-code" style="display: block; white-space: pre-wrap">{% templatetag openblock %} orca_field form.name {% templatetag closeblock %}
{% templatetag openblock %} orca_field form.port width="w8" {% templatetag closeblock %}</pre>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form and view

```python
# videos/forms.py
from django import forms

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "album", "published", "recorded_on"]
        help_texts = {"title": "Shown under the player and in search."}


# videos/views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VideoForm
from .models import Video


def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST or None, instance=video)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Video “{video}” saved.")
        return redirect("video-detail", pk=video.pk)
    # Template: {% orca_form_errors form %} then {% orca_field form.title %} for each field.
    return render(request, "videos/edit.html", {"form": form, "video": video})
```

**Classes:** `.orca-field`, `.orca-fields`

**Principles applied:** Practical UI R08: Put essential help before the input; Practical UI R09: Persistent labels, not placeholders; Practical UI R10: Keep labels close to their inputs; Practical UI R20: Submit-time validation with an error summary; Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `toggle-field`, `choice-group`, `form-actions`

**ORCA guide items covered:** Form field (text); Form field (select)

---

## Toggle field

`id: toggle-field` · level: component · source: ORCA

One checkbox or switch with its label, description and error.

Built from: `checkbox`, `switch`, `help-text`, `error-text`

### Why

A single on/off question is clearest as one tick or switch whose label states the 'on' outcome (Practical UI R14, R15). The description sits inside the clickable label so the whole row is the target (Fitts's law).

### When to use

- Checkbox: an option saved with the form ('Email me a daily report').
- Switch: a setting that applies the moment it changes ('Video enabled').

### When not to use

- Negative labels ('Do not send emails').
- A switch inside a form that has a Save button.

### How to use

- Django: `{% orca_field form.daily_report %}` (checkbox) or `{% orca_field form.enabled switch=True %}`.
- Markup: `.orca-field` containing an `orca-check` (description in `.orca-check__desc`) or an `orca-switch` followed by `.orca-help`.
- Errors go above the control (for example a required agreement).

#### Example: Checkbox and switch

```django
<div class="orca-fields">
  <div class="orca-field"><label class="orca-check"><input type="checkbox" name="daily" checked><span class="orca-check__box"></span><span class="orca-check__text">Email me a daily report<span class="orca-check__desc">Sent at 07:00 with yesterday's counts.</span></span></label></div>
  <div class="orca-field"><label class="orca-switch"><input type="checkbox" role="switch" checked aria-describedby="tf-help"><span class="orca-switch__track"></span><span>Video enabled</span></label><p class="orca-help" id="tf-help">Turning it off stops counting immediately.</p></div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form

```python
# videos/forms.py
from django import forms


class NotificationForm(forms.Form):
    # A checkbox saved with the form: {% orca_field form.weekly_report %}
    weekly_report = forms.BooleanField(label="Send me the weekly report", required=False,
                                       help_text="Every Monday at 07:00.")
    # A setting applied at once: {% orca_field form.autoplay switch=True %} in a form with data-orca-autosubmit,
    # whose view saves it and redirects back.
    autoplay = forms.BooleanField(label="Play videos automatically", required=False)
```

**Classes:** `.orca-field`

**Principles applied:** Practical UI R14: Checkbox or switch according to timing; Practical UI R15: Phrase binary labels positively; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `form-field`

**ORCA guide items covered:** Form field (checkbox); Form field (switch)

---

## Choice group

`id: choice-group` · level: component · source: ORCA

A fieldset of radios (one answer) or checkboxes (several answers) with a legend, hint and error.

Built from: `radio`, `checkbox`, `label`

### Why

Visible options are compared without opening anything (Practical UI R11), and the fieldset's legend gives every option its question for screen-reader users (Postel's law).

### When to use

- Radios: 2 to about 7 mutually exclusive answers.
- Checkboxes: any number of answers from a short list.

### When not to use

- More than about 10 options: use a select, multi-picker or combobox.

### How to use

- Django: `{% orca_field form.interval %}` for RadioSelect and CheckboxSelectMultiple widgets; `horizontal=True` for 2–3 short options.
- Markup: `<fieldset class="orca-choice-group">`, `<legend class="orca-label">`, then `.orca-choice-group__items` with radios or checkboxes.
- Order options logically (frequency, size, time); mark a recommended option in its label only when it is truly recommended.

### Accessibility

- Put `aria-describedby` and `aria-invalid` on the fieldset.

#### Example: Radio group and checkbox group

```django
<div class="orca-fields">
  <fieldset class="orca-choice-group">
    <legend class="orca-label">Snapshot interval</legend>
    <div class="orca-choice-group__items">
      <label class="orca-radio"><input type="radio" name="cg-i" value="1"><span class="orca-radio__dot"></span>Every minute</label>
      <label class="orca-radio"><input type="radio" name="cg-i" value="5" checked><span class="orca-radio__dot"></span>Every 5 minutes (recommended)</label>
      <label class="orca-radio"><input type="radio" name="cg-i" value="15"><span class="orca-radio__dot"></span>Every 15 minutes</label>
    </div>
  </fieldset>
  <fieldset class="orca-choice-group orca-choice-group--horizontal" aria-describedby="cg-help">
    <legend class="orca-label">Send alerts by</legend>
    <p class="orca-help" id="cg-help">Choose at least one.</p>
    <div class="orca-choice-group__items">
      <label class="orca-check"><input type="checkbox" name="cg-c" checked><span class="orca-check__box"></span>Email</label>
      <label class="orca-check"><input type="checkbox" name="cg-c"><span class="orca-check__box"></span>Text message</label>
    </div>
  </fieldset>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form

```python
# videos/forms.py
from django import forms


class ExportForm(forms.Form):
    # One answer: radios. {% orca_field form.format %} renders the fieldset, legend and options.
    format = forms.ChoiceField(choices=[("mp4", "MP4"), ("webm", "WebM"), ("gif", "Animated GIF")],
                               widget=forms.RadioSelect, initial="mp4")
    # Several answers: checkboxes.
    include = forms.MultipleChoiceField(choices=[("captions", "Captions"), ("chapters", "Chapters")],
                                        widget=forms.CheckboxSelectMultiple, required=False)
```

**Classes:** `.orca-choice-group`, `.orca-choice-group__items`, `.orca-choice-group--horizontal`

**Principles applied:** Practical UI R11: Visible choices for small sets; Practical UI R01: Keep the main form flow in one column; Hick's law: fewer, clearer choices mean faster decisions; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Form field (radio group); Form field (checkbox group)

---

## Search field

`id: search-field` · level: component · source: ORCA

A labelled search input with magnifier, clear button and a live result count.

Built from: `search-input`

### Why

Filtering in place is faster than navigating (Doherty threshold); announcing the result count tells screen-reader users the list changed (Postel's law).

### When to use

- Filtering a list, table or menu already on the page.

### When not to use

- Searching the whole application: use the search bar.

### How to use

- `.orca-search-field` > `.orca-search` (icon, `input type=search`, clear button with `data-orca-clear`) + `<p class="orca-search-field__count" role="status">`.
- Filter as people type after a short pause (≈300 ms), or on submit for server searches.
- For a static list, add `data-orca-filter-list="list-id"` and `data-orca-status="count-id"` to the input.

#### Example: Filtering a list

```django
<div class="orca-search-field" style="max-width: 20rem">
  <div class="orca-search">{% icon "search" %}<input class="orca-input" type="search" placeholder=" " aria-label="Filter videos" data-orca-filter-list="sf-list" data-orca-status="sf-count"><button class="orca-search__clear" type="button" aria-label="Clear filter" data-orca-clear>{% icon "close" %}</button></div>
  <p class="orca-search-field__count" id="sf-count" role="status">4 shown</p>
</div>
<ul id="sf-list" class="orca-list" style="max-width: 20rem"><li><span class="orca-list-item">Entrance A</span></li><li><span class="orca-list-item">Entrance B</span></li><li><span class="orca-list-item">Loading dock</span></li><li><span class="orca-list-item">Car park</span></li></ul>
```

**Classes:** `.orca-search-field`, `.orca-search-field__count`

**Principles applied:** Doherty threshold: respond within 400 ms; show progress for anything slower; Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `search-bar`

**ORCA guide items covered:** Search field (icon + input + clear)

---

## Search bar

`id: search-bar` · level: component · source: ORCA

A search form: optional scope select, search field and a Search button.

Built from: `search-input`, `select`, `button`

### Why

An explicit form with a button works for every input method and lets people search on purpose (Postel's law); the scope narrows choices before results (Hick's law).

### When to use

- Searching the application or a large collection on the server.

### How to use

- `<form class="orca-search-bar" role="search" method="get">` with an optional `.orca-select` scope, an `.orca-search` and `<button class="orca-button" type="submit">Search</button>`.
- Keep the query in the field after submit; put it in the URL (`?q=`) so results can be shared.

#### Example: Search bar

```django
<form class="orca-search-bar" role="search" method="get" style="max-width: 40rem" onsubmit="return false">
  <select class="orca-select" name="scope" aria-label="Search in"><option>All</option><option>Videos</option><option>Events</option></select>
  <div class="orca-search">{% icon "search" %}<input class="orca-input" type="search" name="q" placeholder="Search" aria-label="Search" value="entrance"><button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>{% icon "close" %}</button></div>
  <button class="orca-button" type="submit">Search</button>
</form>
```

**Classes:** `.orca-search-bar`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Search form; Search bar

---

## Table toolbar

`id: table-toolbar` · level: component · source: ORCA

The row above a table: search, filters and view options on the left, actions on the right, and a bulk-action bar when rows are selected.

Built from: `search-input`, `button`, `count-badge`

### Why

Grouping everything that changes the table in one row keeps it near what it affects (Practical UI L14) and separates viewing from acting (Miller's law).

### When to use

- Above data tables and card lists with more than one page of items.

### How to use

- `<div class="orca-toolbar" role="toolbar" aria-label="Videos">`: search field, filter button, `.orca-toolbar__spacer`, then actions.
- When rows are selected, show `.orca-toolbar__selection` with the count and the bulk actions; hide the normal actions.
- Use dense controls (`--dense`) on desktop; they grow to 44px on touch.

#### Example: Toolbar and selection bar

```django
<div class="orca-stack" style="gap: var(--orca-space-8)">
  <div class="orca-toolbar" role="toolbar" aria-label="Videos">
    <div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Filter videos" aria-label="Filter videos"></div>
    <button class="orca-button orca-button--dense" type="button" aria-expanded="false">{% icon "filter" %}Filters<span class="orca-count orca-count--accent">2</span></button>
    <span class="orca-toolbar__spacer"></span>
    <button class="orca-button orca-button--dense" type="button">{% icon "upload" %}Export</button>
    <a class="orca-button orca-button--primary orca-button--dense" href="#">{% icon "plus" %}Add video</a>
  </div>
  <div class="orca-toolbar__selection" role="region" aria-label="Selection"><strong>3 selected</strong><button class="orca-button orca-button--dense" type="button">Disable</button><button class="orca-button orca-button--dense" type="button">Move to site</button><button class="orca-button orca-button--link" type="button">Clear selection</button></div>
</div>
```

**Classes:** `.orca-toolbar`, `.orca-toolbar__spacer`, `.orca-toolbar__selection`

**Principles applied:** Practical UI L14: Reduce travel between related actions; Miller's law: chunk information so working memory is not overloaded; Hick's law: fewer, clearer choices mean faster decisions

**Related:** `filter-button`

**ORCA guide items covered:** Table toolbar

---

## Multi-picker

`id: multi-picker` · level: component · source: Tangerine

A dropdown with a filter and a checkbox list, showing the chosen values as removable tags.

Built from: `checkbox`, `search-input`, `tag`

### Why

Picking several items from a long list needs search and visible choices (Practical UI R12, S06); tags keep the selection visible and reversible after the list closes.

### When to use

- Choosing several known items from 10 to a few hundred: videos, sites, people.

### When not to use

- A short list that fits on screen: use a checkbox group.

### How to use

- `<details class="orca-multipicker">` with `<summary class="orca-picker-btn">` (value text + chevron) and a panel `.orca-popover.orca-multipicker__panel`.
- Inside the panel: a filter input with `data-orca-filter-list`, a `.orca-multipicker__list` of checkboxes, and `.orca-multipicker__foot` with Clear and Done.
- Below: `.orca-multipicker__tags` with removable tags for the chosen values. Summary text: '3 videos' rather than a long list.

#### Example: Multi-picker

```django
<div style="max-width: 20rem">
  <p class="orca-label" id="mp-label">Videos</p>
  <details class="orca-multipicker" open>
    <summary class="orca-picker-btn" aria-labelledby="mp-label mp-value"><span class="orca-picker-btn__value" id="mp-value">2 videos</span>{% icon "chevron-down" %}</summary>
    <div class="orca-popover orca-multipicker__panel" style="position: static; box-shadow: var(--orca-shadow-elevated)">
      <div class="orca-search">{% icon "search" %}<input class="orca-input orca-input--dense" type="search" placeholder="Filter" aria-label="Filter videos" data-orca-filter-list="mp-list"></div>
      <ul class="orca-multipicker__list" id="mp-list">
        <li><label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Entrance A</label></li>
        <li><label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Entrance B</label></li>
        <li><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Loading dock</label></li>
      </ul>
      <div class="orca-multipicker__foot"><button class="orca-button orca-button--link" type="button">Clear</button><button class="orca-button orca-button--dense" type="button">Done</button></div>
    </div>
  </details>
  <div class="orca-multipicker__tags"><span class="orca-tag"><span class="orca-tag__text">Entrance A</span><button class="orca-tag__remove" type="button" aria-label="Remove Entrance A">{% icon "close" %}</button></span><span class="orca-tag"><span class="orca-tag__text">Entrance B</span><button class="orca-tag__remove" type="button" aria-label="Remove Entrance B">{% icon "close" %}</button></span></div>
</div>
```

**Classes:** `.orca-multipicker`, `.orca-multipicker__panel`, `.orca-multipicker__list`, `.orca-multipicker__foot`, `.orca-multipicker__tags`, `.orca-picker-btn`

**Principles applied:** Practical UI R12: Autocomplete for long lists; Practical UI S06: Make essential content visible or discoverable; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Multi-picker

---

## Language switcher

`id: language-switcher` · level: component · source: ORCA

A select of languages, each written in its own language, that posts to Django's set_language view.

Built from: `select`, `button`

### Why

People look for their language by its own name (Jakob's law), and a plain form works without script (Postel's law).

### When to use

- Products translated into two or more languages; in the user menu or footer.

### How to use

- `<form action="{% url 'set_language' %}" method="post">` with csrf, a `next` hidden input and a select of `LANGUAGES` showing `language.name_local`.
- Add `data-orca-autosubmit` to the select and keep a visible Change button inside `<noscript>`.
- Add `lang` on each option so screen readers pronounce the names correctly.

#### Example: Language switcher

```django
<form class="orca-row" method="post" action="#" onsubmit="return false">
  <label class="orca-label" for="lang" style="margin: 0">{% icon "website" %} <span class="orca-sr-only">Language</span></label>
  <select class="orca-select orca-select--dense" id="lang" name="language" style="width: auto" data-orca-autosubmit>
    <option value="en" lang="en" selected>English</option><option value="fr" lang="fr">Français</option><option value="de" lang="de">Deutsch</option><option value="ar" lang="ar">العربية</option>
  </select>
  <noscript><button class="orca-button orca-button--dense" type="submit">Change</button></noscript>
</form>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### URLs and settings

```python
# project/urls.py — Django's set_language view receives the switcher's form
from django.urls import include, path

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),   # the form posts to {% url 'set_language' %}
]

# project/settings.py
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",      # after sessions, before common
    "django.middleware.common.CommonMiddleware",
]
LANGUAGES = [("en", "English"), ("fr", "Français"), ("de", "Deutsch")]
```

**Classes:** `.orca-row`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Language switcher

---

## Input group

`id: input-group` · level: component · source: ORCA

An input joined to addons (unit, prefix) or a button that acts on it.

Built from: `input-addon`, `text-input`, `button`

### Why

Showing the unit and the action next to the value removes guessing and travel (Postel's law, Practical UI L14).

### When to use

- Values with a fixed unit or prefix; a field with one directly related action (Test, Copy, Generate).

### How to use

- `.orca-input-group` containing `.orca-addon` spans, the input, and optionally a `.orca-button` at the end.
- Reference the unit addon from the input with `aria-describedby`.

#### Example: Unit and action

```django
<div class="orca-fields" style="max-width: 28rem">
  <div class="orca-field"><label class="orca-label" for="ig-a">Retention</label><div class="orca-input-group" style="max-width: 12rem"><input class="orca-input" id="ig-a" type="number" value="30" aria-describedby="ig-a-u"><span class="orca-addon" id="ig-a-u">days</span></div></div>
  <div class="orca-field"><label class="orca-label" for="ig-b">Video address</label><div class="orca-input-group"><span class="orca-addon">https://</span><input class="orca-input" id="ig-b" value="media.example.com/v/4821"><button class="orca-button" type="button">Test</button></div></div>
</div>
```

**Classes:** `.orca-input-group`, `.orca-addon`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI L14: Reduce travel between related actions

**ORCA guide items covered:** Input group (addon + input)

---

## Filter button

`id: filter-button` · level: component · source: ORCA

A button that opens the filters, showing how many are active.

Built from: `button`, `count-badge`, `icon`

### Why

Hiding advanced filters until needed keeps the screen simple (Practical UI S04, Hick's law); the count keeps active filters visible so results are never mysteriously empty.

### When to use

- Lists with more filters than fit in the toolbar.

### How to use

- `<button class="orca-button" type="button" aria-expanded="false" aria-controls="filters" data-orca-disclose>{% icon "filter" %}Filters<span class="orca-count orca-count--accent">2</span></button>`.
- Give the count a hidden explanation: `<span class="orca-sr-only">, 2 active</span>`.
- When filters are active, also show them as removable tags with a Clear all link.

#### Example: Filter button with panel

```django
<button class="orca-button" type="button" aria-expanded="false" aria-controls="fb-panel" data-orca-disclose>{% icon "filter" %}Filters<span class="orca-count orca-count--accent" aria-hidden="true">2</span><span class="orca-sr-only">, 2 active</span></button>
<div id="fb-panel" hidden style="margin-top: var(--orca-space-8); padding: var(--orca-space-16); background: var(--orca-bg-alt)">
  <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Online only</label>
</div>
```

**Classes:** `.orca-button`, `.orca-count--accent`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Hick's law: fewer, clearer choices mean faster decisions; Practical UI S06: Make essential content visible or discoverable

**Related:** `table-toolbar`

**ORCA guide items covered:** Filter button

---

## Dropdown select (picker)

`id: dropdown-select` · level: component · source: Tangerine

A select-like button opening a listbox whose options can carry a description.

Built from: `select`

### Why

When options need a second line (a plan's limits, a role's permissions) a native select cannot show it; a listbox keeps the select convention (Jakob's law) while showing the difference that matters (Practical UI R12).

### When to use

- 5–15 options that need a description or an icon to tell them apart.

### When not to use

- Plain options: the native select is more robust.
- Choices people should compare side by side: radio cards or a choice group.

### How to use

- Wrapper `.orca-anchor.orca-anchor--block` with `data-orca-listbox-wrap`; button `.orca-picker-btn` with `data-orca-listbox`, `aria-haspopup="listbox"`, `aria-expanded`, `aria-controls`; a hidden input carrying the value.
- List: `<ul class="orca-popover" role="listbox" hidden>` with `<li class="orca-option" role="option" tabindex="-1" data-value=…>`.
- orca.js handles click, arrow keys, Home/End, Enter, Escape and returning focus.

### Accessibility

- Label the button with the visible label and the value: `aria-labelledby="label-id value-id"`.

#### Example: Role picker

```django
<div class="orca-anchor orca-anchor--block" data-orca-listbox-wrap style="max-width: 20rem">
  <span class="orca-label" id="dd-label">Role</span>
  <button class="orca-picker-btn" type="button" data-orca-listbox aria-haspopup="listbox" aria-expanded="false" aria-controls="dd-list" aria-labelledby="dd-label dd-value"><span class="orca-picker-btn__value" id="dd-value">Viewer</span>{% icon "chevron-down" %}</button>
  <input type="hidden" name="role" value="viewer">
  <ul class="orca-popover" id="dd-list" role="listbox" aria-labelledby="dd-label" hidden>
    <li class="orca-option" role="option" tabindex="-1" data-value="viewer" data-label="Viewer" aria-selected="true"><span class="orca-option__text">Viewer<span class="orca-option__desc">Sees dashboards and reports.</span></span></li>
    <li class="orca-option" role="option" tabindex="-1" data-value="operator" data-label="Operator" aria-selected="false"><span class="orca-option__text">Operator<span class="orca-option__desc">Also manages videos and runs.</span></span></li>
    <li class="orca-option" role="option" tabindex="-1" data-value="admin" data-label="Administrator" aria-selected="false"><span class="orca-option__text">Administrator<span class="orca-option__desc">Also manages users and settings.</span></span></li>
  </ul>
</div>
```

**Classes:** `.orca-picker-btn`, `.orca-picker-btn__value`, `.orca-popover`, `.orca-option`, `.orca-option__text`, `.orca-option__desc`, `.orca-anchor`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI R12: Autocomplete for long lists; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Dropdown select (picker)

---

## Combobox (autocomplete)

`id: combobox` · level: component · source: ORCA

A text input that suggests matching options as people type; the value must be one of the options.

Built from: `text-input`

### Why

When people know the name of what they want, typing a few letters beats scrolling a long list (Practical UI R12, Hick's law); highlighting the matched letters shows why each suggestion appears.

### When to use

- Choosing one item from a long known list: a country, a video, a person, a product.

### When not to use

- Free text with optional hints: use auto-suggest.
- Fewer than about 15 options: a select.

### How to use

- Wrapper `.orca-combobox` with `data-orca-combobox-wrap`; `<input class="orca-input" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="list-id" data-orca-combobox>` and a hidden input for the value.
- Options `<li class="orca-option" role="option" id=… data-value=…>` in a hidden `.orca-popover` listbox; show at most 10.
- Server results: swap the listbox content with htmx (`hx-get`, `hx-trigger="input changed delay:300ms"`, `hx-target`).
- Add a status element (`data-orca-status`) so the number of suggestions is announced.

### Accessibility

- Keyboard: Down opens and moves, Enter picks, Escape closes then clears; focus stays in the input (`aria-activedescendant`).

#### Example: Country

```django
<div class="orca-field orca-combobox" data-orca-combobox-wrap style="max-width: 20rem">
  <label class="orca-label" for="cb-in">Country</label>
  <input class="orca-input" id="cb-in" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="cb-list" autocomplete="off" data-orca-combobox data-orca-status="cb-status">
  <input type="hidden" name="country">
  <ul class="orca-popover" id="cb-list" role="listbox" aria-label="Countries" hidden style="top: 100%">
    <li class="orca-option" role="option" id="cb-1" data-value="DZ">Algeria</li><li class="orca-option" role="option" id="cb-2" data-value="BE">Belgium</li>
    <li class="orca-option" role="option" id="cb-3" data-value="CA">Canada</li><li class="orca-option" role="option" id="cb-4" data-value="FR">France</li>
    <li class="orca-option" role="option" id="cb-5" data-value="DE">Germany</li><li class="orca-option" role="option" id="cb-6" data-value="MA">Morocco</li>
    <li class="orca-option" role="option" id="cb-7" data-value="TN">Tunisia</li><li class="orca-popover__empty" hidden>No country matches. Check the spelling.</li>
  </ul>
  <span class="orca-sr-only" id="cb-status" role="status"></span>
</div>
```

**Classes:** `.orca-combobox`, `.orca-popover`, `.orca-option`, `.orca-popover__empty`

**Principles applied:** Practical UI R12: Autocomplete for long lists; Hick's law: fewer, clearer choices mean faster decisions; Doherty threshold: respond within 400 ms; show progress for anything slower

**Related:** `auto-suggest`

**ORCA guide items covered:** Combobox (input + suggestions); Autocomplete input

---

## Auto-suggest input

`id: auto-suggest` · level: component · source: ORCA

A free-text input with browser suggestions from a datalist.

Built from: `text-input`

### Why

Suggestions speed up common answers without forbidding new ones (Tesler's law, Postel's law), and the native datalist needs no script.

### When to use

- Free text where most answers repeat: a tag, a mounting location, a department.

### When not to use

- Answers that must match a list: use the combobox.

### How to use

- `<input class="orca-input" list="dl-id">` + `<datalist id="dl-id"><option value="…"></datalist>`.
- Order suggestions by how often they are used; keep the list under about 20.

#### Example: Mounting location

```django
<div class="orca-field" style="max-width: 20rem">
  <label class="orca-label" for="as-in">Mounting location</label>
  <input class="orca-input" id="as-in" list="as-dl" autocomplete="off">
  <datalist id="as-dl"><option value="Above the door"></option><option value="Ceiling, centre"></option><option value="Wall, facing in"></option></datalist>
</div>
```

**Classes:** `.orca-input`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Auto-suggest input

---

## OTP input

`id: otp-input` · level: component · source: ORCA

The full one-time-code question: label, digit boxes, hint, error and a resend link.

Built from: `otp-digit`, `help-text`, `countdown-label`

### Why

Codes are short-lived and copied from another app; accepting paste and autofill and offering a resend avoids a dead end at the most fragile step (Peak–end rule, Tesler's law).

### When to use

- Verification and two-factor steps.

### How to use

- `<fieldset class="orca-otp">` with the legend, help ('We sent a 6-digit code to …'), the OTP digit boxes (`data-orca-otp`), errors above the boxes and a 'Send a new code' button after the countdown.
- Submit automatically when the last digit is entered only if the server answers in under a second.

#### Example: Verification code

```django
<fieldset class="orca-choice-group" aria-describedby="otp-help">
  <legend class="orca-label">Verification code</legend>
  <p class="orca-help" id="otp-help">We sent a 6-digit code to a••••@acme.com. It expires in 10 minutes.</p>
  <div class="orca-row" data-orca-otp>{% for i in "123456" %}<input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit {{ i }} of 6"{% if forloop.first %} autocomplete="one-time-code"{% endif %}>{% endfor %}</div>
  <p class="orca-small">Didn't get it? <button class="orca-button orca-button--link" type="button">Send a new code</button></p>
</fieldset>
```

**Classes:** `.orca-choice-group`, `.orca-row`

**Principles applied:** Peak–end rule: people judge an experience by its peak and its end; Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** OTP input

---

## Rating input

`id: rating-input` · level: component · source: ORCA

One to five stars as a radio group, with the chosen value in words.

Built from: `radio`, `icon`

### Why

Stars are a familiar scale (Jakob's law); built on radios they work with arrow keys and screen readers, and the word ('4 of 5') removes doubt.

### When to use

- Feedback and review forms.

### How to use

- `<fieldset class="orca-rating-wrap">` with a legend and `.orca-rating`, which lists radios from 5 down to 1 (CSS reverses them) each followed by a label containing a star icon and hidden text '4 stars'.
- Show the value in words in `.orca-rating__value`.

#### Example: Rating

```django
<fieldset class="orca-rating-wrap">
  <legend class="orca-label">How easy was the setup?</legend>
  <div class="orca-rating">{% for n in "54321" %}<input type="radio" name="rate" id="rate-{{ n }}" value="{{ n }}"{% if n == "4" %} checked{% endif %}><label for="rate-{{ n }}">{% icon "star" %}<span class="orca-sr-only">{{ n }} star{% if n != "1" %}s{% endif %}</span></label>{% endfor %}</div>
  <span class="orca-rating__value">4 of 5</span>
</fieldset>
```

**Classes:** `.orca-rating`, `.orca-rating-wrap`, `.orca-rating__value`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI C03: Communicate meaning beyond colour

**ORCA guide items covered:** Rating input

---

## Split date input

`id: split-date` · level: component · source: ORCA

Day, month and year as three labelled numeric fields.

Built from: `text-input`, `label`

### Why

Dates people know by heart (birth dates, document dates) are faster to type than to pick from a calendar, and three labelled parts avoid day/month order confusion (Postel's law).

### When to use

- Known dates, far in the past or future: birth date, licence expiry, contract start.

### When not to use

- Dates chosen relative to today: use the date picker.

### How to use

- `<fieldset class="orca-split-date">` with legend, hint ('For example, 27 3 2024'), then `.orca-split-date__parts` with three `.orca-split-date__part` (label + `inputmode="numeric"` input); the year part adds `--year`.
- Order the parts as the locale writes dates; validate the whole date on the server and report one error for the group.

#### Example: Licence expiry

```django
<fieldset class="orca-split-date" aria-describedby="sd-help">
  <legend class="orca-label">Licence expiry date</legend>
  <p class="orca-help" id="sd-help">For example, 27 3 2027</p>
  <div class="orca-split-date__parts">
    <div class="orca-split-date__part"><label class="orca-label" for="sd-d">Day</label><input class="orca-input" id="sd-d" inputmode="numeric" maxlength="2"></div>
    <div class="orca-split-date__part"><label class="orca-label" for="sd-m">Month</label><input class="orca-input" id="sd-m" inputmode="numeric" maxlength="2"></div>
    <div class="orca-split-date__part orca-split-date__part--year"><label class="orca-label" for="sd-y">Year</label><input class="orca-input" id="sd-y" inputmode="numeric" maxlength="4"></div>
  </div>
</fieldset>
```

**Classes:** `.orca-split-date`, `.orca-split-date__parts`, `.orca-split-date__part`, `.orca-split-date__part--year`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI R06: Match input width to the expected answer

**ORCA guide items covered:** Split date input (day, month, year)

---

## File input field

`id: file-field` · level: component · source: ORCA

A labelled drop zone around a native file input, listing the chosen files.

Built from: `file-input`, `help-text`

### Why

A large target accepts both drag-and-drop and a click (Fitts's law); stating type and size limits up front prevents a failed upload (Peak–end rule).

### When to use

- Uploading documents, images or imports.

### How to use

- `.orca-field` with label and help (accepted types, size limit), then `<div class="orca-dropzone">` containing the icon, a title, a hint and the `<input type="file">` (it covers the zone).
- Add `data-orca-file-list="list-id"` to list chosen files in `.orca-file-list`.
- Validate type and size again on the server; show upload progress with progress-bar-with-counts.

#### Example: Drop zone

```django
<div class="orca-field" style="max-width: 28rem">
  <label class="orca-label" for="fz">Floor plan</label>
  <p class="orca-help" id="fz-help">PNG or JPG, up to 10 MB.</p>
  <div class="orca-dropzone">{% icon "upload" size="l" %}<span class="orca-dropzone__title">Drop a file here or choose one</span><span class="orca-dropzone__hint">One file</span>
    <input type="file" id="fz" accept="image/png,image/jpeg" aria-describedby="fz-help" data-orca-file-list="fz-list"></div>
  <ul class="orca-file-list" id="fz-list" aria-live="polite"></ul>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form and view

```python
# videos/forms.py
from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(label="Video file", help_text="MP4 or WebM, up to 2 GB.")


# videos/views.py
from django.shortcuts import redirect, render


def upload(request):
    # The form needs enctype="multipart/form-data" and the files come in request.FILES.
    form = UploadForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        handle_upload(form.cleaned_data["file"])
        return redirect("video-list")
    return render(request, "videos/upload.html", {"form": form})
```

**Classes:** `.orca-dropzone`, `.orca-dropzone__title`, `.orca-dropzone__hint`, `.orca-file-list`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Peak–end rule: people judge an experience by its peak and its end; Practical UI R08: Put essential help before the input

**ORCA guide items covered:** File input field

---

## Form alert

`id: form-alert` · level: component · source: ORCA

A message at the top of a form for errors that belong to no single field.

Built from: `error-list`, `callout`

### Why

Problems like 'These dates overlap an existing run' must be seen before the fields; a negative callout with the fix ends the dead end (Practical UI W15, Peak–end rule).

### When to use

- Non-field errors after submit; conflicts with other records; permission problems.

### How to use

- Django: `{% orca_form_errors form %}` renders non-field errors as a callout and, with two or more invalid fields, a linked error summary.
- Markup: `<div class="orca-callout orca-callout--negative" role="alert">` with the error icon, a title that states the problem and a body that says what to do.

#### Example: Non-field error

```django
<div class="orca-callout orca-callout--negative" role="alert">{% icon "error" %}<p class="orca-callout__title">This run overlaps “Morning check”</p><p class="orca-callout__body">Choose a start after 10:00 or stop the other run first.</p></div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form-wide errors

```python
# videos/forms.py
from django import forms


class ShareForm(forms.Form):
    email = forms.EmailField()
    expires_on = forms.DateField(required=False)

    def clean(self):
        data = super().clean()
        if not data.get("email", "").endswith("@example.com"):
            # Errors not tied to one field show in the alert: {% orca_form_errors form %}
            raise forms.ValidationError("Videos can only be shared inside your organisation.")
        return data
```

**Classes:** `.orca-callout`, `.orca-callout--negative`

**Principles applied:** Practical UI W15: Help people recover from errors; Peak–end rule: people judge an experience by its peak and its end; Practical UI R20: Submit-time validation with an error summary

**ORCA guide items covered:** Form alert (non-field errors)

---

## Form actions

`id: form-actions` · level: component · source: ORCA

The row of buttons that ends a form: the primary action first, then the alternatives.

Built from: `button`

### Why

Placing the submit action right after the last field shortens travel (Fitts's law); one primary action makes the next step obvious (Hick's law, Practical UI B03, B08).

### When to use

- The end of every form, dialog form and settings section with a Save.

### How to use

- `<div class="orca-form-actions">` after the last field: primary button first, then Cancel (default or link).
- A destructive action (Delete) goes to the far end in `.orca-form-actions__end`, styled default or outline-danger, and asks for confirmation.
- Long forms: `--sticky` keeps the actions visible at the bottom of the viewport. On phones the buttons stack full width.

#### Example: Save, cancel and delete

```django
<div class="orca-form-actions">
  <button class="orca-button orca-button--primary" type="submit">Save video</button>
  <a class="orca-button" href="#">Cancel</a>
  <span class="orca-form-actions__end"><button class="orca-button orca-button--outline-danger" type="button" data-orca-dialog-open="fa-confirm">Delete video</button></span>
</div>
<dialog class="orca-dialog" id="fa-confirm" aria-labelledby="fa-confirm-t"><form method="dialog"><div class="orca-dialog__header"><h2 class="orca-dialog-title" id="fa-confirm-t">Delete Entrance A?</h2></div><div class="orca-dialog__body"><p class="orca-p">Its counts are kept. Its zones and alert rules are deleted.</p></div><div class="orca-dialog__footer"><button class="orca-button orca-button--danger" type="submit" value="delete">Delete video</button><button class="orca-button" type="submit" value="cancel" autofocus>Cancel</button></div></form></dialog>
```

**Classes:** `.orca-form-actions`, `.orca-form-actions__end`, `.orca-form-actions--sticky`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B03: One primary action; Practical UI B08: Keep action order predictable; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Form actions

---

## Row selection

`id: row-select` · level: component · source: ORCA

A checkbox per table row and a select-all checkbox in the header.

Built from: `checkbox`

### Why

Selecting rows before choosing an action lets people act on many records at once (Practical UI F03); checkboxes are the familiar control for it (Jakob's law, R14).

### When to use

- Tables that offer bulk actions.

### How to use

- Header: `<th scope="col" class="orca-table__select"><label class="orca-check"><input type="checkbox" aria-label="Select all videos"><span class="orca-check__box"></span></label></th>`; one per row named after the row.
- When rows are selected, the table toolbar shows the count and the bulk actions.

### Accessibility

- Each checkbox is named after its row ('Select Entrance A').

#### Example: Select cells

```django
<table class="orca-table"><thead><tr><th scope="col" class="orca-table__select"><label class="orca-check"><input type="checkbox" aria-label="Select all videos"><span class="orca-check__box"></span></label></th><th scope="col">Video</th></tr></thead>
<tbody><tr><td class="orca-table__select"><label class="orca-check"><input type="checkbox" checked aria-label="Select Harbour at dusk"><span class="orca-check__box"></span></label></td><td>Harbour at dusk</td></tr></tbody></table>
```

**Classes:** `.orca-table__select`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Jakob's law: work the way products people already know work; Practical UI R14: Checkbox or switch according to timing

**Related:** `data-table`, `table-toolbar`

---

## Formatting toolbar

`id: formatting-toolbar` · level: component · source: ORCA

A row of pressed-state icon buttons for bold, italic, lists and links over a text area.

Built from: `icon-button`, `divider`

### Why

Formatting commands are recognised by their familiar glyphs (Jakob's law); pressed states show what applies to the selection (Practical UI F10).

### When to use

- Above a rich text field.

### How to use

- `<div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting">` with dense icon buttons using `aria-pressed`, groups separated by a vertical divider.

### Accessibility

- Arrow keys move between the buttons of the toolbar; each has an accessible name.

#### Example: Toolbar

```django
<div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting" style="max-width: 20rem"><button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="true" aria-label="Bold"><b>B</b></button><button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="false" aria-label="Italic"><i>I</i></button><span class="orca-divider orca-divider--vertical" role="separator"></span><button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="false" aria-label="Bulleted list">{% icon "list" %}</button></div>
```

**Classes:** `.orca-richtext__toolbar`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI F10: Specify every interaction state

**Related:** `rich-text-editor`

---

## Applied filters

`id: applied-filters` · level: component · source: ORCA

The filters in effect as removable tags, with Clear all and the number of results.

Built from: `tag`, `link-action`

### Why

Filters that are on must stay visible and reversible (Practical UI S06, Postel's law); the count confirms what they did (Doherty threshold).

### When to use

- Above results while at least one filter is applied; inside a no-results state.

### How to use

- `<div class="orca-filter-bar__applied"><span class="orca-small orca-muted">Filtered by</span>` then one removable tag per filter, a 'Clear all' link button and the count in `role="status"`.

### Accessibility

- Each remove button names the filter it removes.

#### Example: Applied filters

```django
<div class="orca-filter-bar__applied"><span class="orca-small orca-muted">Filtered by</span><span class="orca-tag"><span class="orca-tag__text">Type: Video</span><button class="orca-tag__remove" type="button" aria-label="Remove filter Type: Video">{% icon "close" %}</button></span><button class="orca-button orca-button--link" type="button">Clear all</button><span class="orca-small orca-muted" role="status">14 videos</span></div>
```

**Classes:** `.orca-filter-bar__applied`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Postel's law: accept varied input, output reliable and accessible UI; Doherty threshold: respond within 400 ms; show progress for anything slower

**Related:** `filter-bar`, `no-results`

---
