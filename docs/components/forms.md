# Forms

Fields and the small groups around them. A form field holds a label, hint, error and control in a fixed order.

## Form field

`id: form-field` · level: component · source: ORCA

One control with its label, optional marker, help and error, linked together. For text inputs and selects.

Built from: `label`, `required-marker`, `help-text`, `error-text`, `text-input`, `select`, `textarea`, `color-input`

### General description

A form field pairs one input with its label, hint and error message. It is the basic unit people fill in to give information.

#### Use cases

- Collecting a name, email address or number in a sign-up or settings form.
- Picking one option from a dropdown inside a form.
- Entering longer text, such as a message or description.

#### When not to use it

- For a single yes or no choice, use a checkbox or switch instead.
- For a short list of options, use radio buttons so all choices stay visible.

#### Best practices

- Put a visible label above every input; never rely on placeholder text alone.
- Show the hint before the input and the error next to it.
- Say what is wrong and how to fix it in error messages.
- Mark optional fields rather than required ones when most fields are required.
- Use the right input type so phones show a suitable keyboard.

### When to use

- Any single-value field: text, number, email, date, select, textarea.

### When not to use

- One on/off option: use the toggle field.
- Choices from a short list: use a choice group.

### How to use

- Django forms: `{% orca_field form.name %}`. Options: `width="w8"` (input width), `label="…"`, `help_text="…"`, `hide_label=True` (search only).
- Manual markup: `<div class="orca-field">` with `orca-label`, `orca-help` (id), `orca-error` (id) and the control with `aria-describedby="error-id help-id"` and `aria-invalid` when invalid.
- `required=False` adds “(optional)” automatically.
- Stack fields in `.orca-fields` (24px apart) so each label sits nearer its own control than the field above.
- Django date, time and date-time widgets render as native pickers with ISO values.

### Accessibility

- List the error id first in `aria-describedby` so it is read before the hint.

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
    <select class="orca-select" id="ff-site" name="site">
      <option value="">No site</option>
      <option>North building</option>
      <option>Warehouse</option>
    </select>
  </div>
</div>
```

#### Example: Invalid field

```django
<div class="orca-field" style="max-width: 24rem">
  <label class="orca-label" for="ff-port">Port</label>
  <p class="orca-help" id="ff-port-help">Usually 554 for HTTPS.</p>
  <p class="orca-error" id="ff-port-error">
    {% icon "error" %}
    <span>Enter a port between 1 and 65535.</span>
  </p>
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

### General description

A single checkbox or switch with its label and description. It lets people turn one option on or off.

#### Use cases

- Agreeing to terms or opting in to emails.
- Turning a feature on or off in settings.
- Marking one yes or no answer inside a longer form.

#### When not to use it

- For picking one answer from several, use radio buttons instead.
- For a choice that needs a Save button, use a checkbox rather than an instant switch.

#### Best practices

- Word the label as the result of turning it on, in positive terms.
- Use a switch only when the change takes effect immediately.
- Make the whole label clickable, not just the small box.
- Keep descriptions short and place them under the label.
- Show an error next to the control if a required box is left unticked.

### When to use

- Checkbox: an option saved with the form ('Email me a daily report').
- Switch: a setting that applies at once ('Video enabled').

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
  <div class="orca-field">
    <label class="orca-check">
      <input type="checkbox" name="daily" checked>
      <span class="orca-check__box"></span>
      <span class="orca-check__text">Email me a daily report<span class="orca-check__desc">Sent at 07:00 with yesterday's counts.</span></span>
    </label>
  </div>
  <div class="orca-field">
    <label class="orca-switch">
      <input type="checkbox" role="switch" checked aria-describedby="tf-help">
      <span class="orca-switch__track"></span>
      <span>Video enabled</span>
    </label>
    <p class="orca-help" id="tf-help">Turning it off stops counting immediately.</p>
  </div>
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

Radios (one answer) or checkboxes (several answers) in a fieldset with a legend, hint and error.

Built from: `radio`, `checkbox`, `label`

### General description

A set of radio buttons or checkboxes under one question. Radios allow one answer; checkboxes allow several.

#### Use cases

- Choosing a plan, delivery method or frequency from a few options.
- Selecting several interests or notification channels.
- Answering a survey question with a short list of answers.

#### When not to use it

- For a long list of options, use a dropdown or searchable picker instead.
- For one on or off setting, use a single checkbox or switch.

#### Best practices

- Wrap the options in a fieldset with a legend that states the question.
- Keep the list short, usually 2 to 7 options for radios.
- Order options in a logical way, not at random.
- Pre-select a safe default only when most people would choose it.
- Show an error message for the whole group, not each option.

### When to use

- Radios: 2 to about 7 mutually exclusive answers.
- Checkboxes: any number of answers from a short list.

### When not to use

- More than about 10 options: use a select, multi-picker or combobox.

### How to use

- Django: `{% orca_field form.interval %}` for RadioSelect and CheckboxSelectMultiple widgets; `horizontal=True` for 2–3 short options.
- Markup: `<fieldset class="orca-choice-group">`, `<legend class="orca-label">`, then `.orca-choice-group__items` with radios or checkboxes.
- Order options logically (frequency, size, time); mark one as recommended in its label only if it truly is.

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

### General description

A text box for typing a few words to narrow down what is already on the page, with a clear button and a result count.

#### Use cases

- Filtering a table, list or menu as the person types.
- Finding one item in a long settings or help list.
- Narrowing results on a page without reloading it.

#### When not to use it

- For searching a whole site or large collection, use a full search form with a button.
- For a short list of 5 or fewer items, no search is needed.

#### Best practices

- Label the field clearly, even when the label is visually hidden.
- Show the number of results and update it as people type.
- Provide a clear button to reset the filter in one click.
- Wait a moment after typing stops before filtering heavy lists.
- Show a helpful message when nothing matches.

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
  <div class="orca-search">
    {% icon "search" %}
    <input class="orca-input" type="search" placeholder=" " aria-label="Filter videos" data-orca-filter-list="sf-list" data-orca-status="sf-count">
    <button class="orca-search__clear" type="button" aria-label="Clear filter" data-orca-clear>
      {% icon "close" %}
    </button>
  </div>
  <p class="orca-search-field__count" id="sf-count" role="status">4 shown</p>
</div>
<ul id="sf-list" class="orca-list" style="max-width: 20rem">
  <li>
    <span class="orca-list-item">Entrance A</span>
  </li>
  <li>
    <span class="orca-list-item">Entrance B</span>
  </li>
  <li>
    <span class="orca-list-item">Loading dock</span>
  </li>
  <li>
    <span class="orca-list-item">Car park</span>
  </li>
</ul>
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

### General description

A search form with a text box and a button, sometimes with a menu to limit the search area. People submit it to see results.

#### Use cases

- Searching a whole website, shop or knowledge base.
- Finding records in a large database or archive.
- Searching within one category chosen from a menu.

#### When not to use it

- To narrow a list already on screen, use an instant filter field instead.
- For a few items, browsing or a menu is quicker than searching.

#### Best practices

- Place it where people expect it, usually the top of the page.
- Support the Enter key as well as the button.
- Keep the typed query visible on the results page.
- Put the query in the web address so results can be shared.
- Offer help when there are no results, such as spelling tips.

### When to use

- Searching the application or a large collection on the server.

### How to use

- `<form class="orca-search-bar" role="search" method="get">` with an optional `.orca-select` scope, an `.orca-search` and `<button class="orca-button" type="submit">Search</button>`.
- Keep the query in the field after submit and in the URL (`?q=`) so results can be shared.

#### Example: Search bar

```django
<form class="orca-search-bar" role="search" method="get" style="max-width: 40rem" onsubmit="return false">
  <select class="orca-select" name="scope" aria-label="Search in">
    <option>All</option>
    <option>Videos</option>
    <option>Events</option>
  </select>
  <div class="orca-search">
    {% icon "search" %}
    <input class="orca-input" type="search" name="q" placeholder="Search" aria-label="Search" value="entrance">
    <button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>
      {% icon "close" %}
    </button>
  </div>
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

### General description

A row of controls above a table or list that holds search, filters, view options and actions, plus bulk actions for selected rows.

#### Use cases

- Searching and filtering a large data table.
- Applying one action to many selected rows at once.
- Exporting or adding records from a list page.

#### When not to use it

- For short lists with no actions, a toolbar adds clutter; leave it out.
- For actions on a single row, use a row menu instead.

#### Best practices

- Group controls by purpose: finding on the left, acting on the right.
- Show the number of selected rows next to the bulk actions.
- Hide actions that do not apply to the current selection.
- Keep the toolbar in one row on wide screens and wrap it cleanly on small ones.
- Give the toolbar a label so screen readers can announce it.

### When to use

- Above tables and card lists that span more than one page.

### How to use

- `<div class="orca-toolbar" role="toolbar" aria-label="Videos">`: search field, filter button, `.orca-toolbar__spacer`, then actions.
- When rows are selected, show `.orca-toolbar__selection` with the count and the bulk actions; hide the normal actions.
- Use dense controls (`--dense`) on desktop; they grow to 44px on touch.

#### Example: Toolbar and selection bar

```django
<div class="orca-stack" style="gap: var(--orca-space-8)">
  <div class="orca-toolbar" role="toolbar" aria-label="Videos">
    <div class="orca-search">
      {% icon "search" %}
      <input class="orca-input orca-input--dense" type="search" placeholder="Filter videos" aria-label="Filter videos">
    </div>
    <button class="orca-button orca-button--dense" type="button" aria-expanded="false">
      {% icon "filter" %}
      Filters
      <span class="orca-count orca-count--accent">2</span>
    </button>
    <span class="orca-toolbar__spacer"></span>
    <button class="orca-button orca-button--dense" type="button">
      {% icon "upload" %}
      Export
    </button>
    <a class="orca-button orca-button--primary orca-button--dense" href="#">
      {% icon "plus" %}
      Add video
    </a>
  </div>
  <div class="orca-toolbar__selection" role="region" aria-label="Selection">
    <strong>3 selected</strong>
    <button class="orca-button orca-button--dense" type="button">Disable</button>
    <button class="orca-button orca-button--dense" type="button">Move to site</button>
    <button class="orca-button orca-button--link" type="button">Clear selection</button>
  </div>
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

### General description

A dropdown that lets people filter a long list and tick several items. The chosen items appear as tags that can be removed.

#### Use cases

- Assigning several people or teams to a task.
- Choosing multiple categories or tags for an item.
- Selecting several sites, devices or products from a long list.

#### When not to use it

- For a short list that fits on screen, use a checkbox group instead.
- For picking only one item, use a select or searchable dropdown.

#### Best practices

- Add a filter box when the list has more than about 10 items.
- Show chosen items as removable tags so they stay visible.
- Summarize the selection in the button, such as the number chosen.
- Provide Clear and Done buttons inside the list.
- Make every option reachable and selectable by keyboard.

### When to use

- Choosing several known items from 10 to a few hundred: videos, sites, people.

### When not to use

- A short list that fits on screen: use a checkbox group.

### How to use

- `<details class="orca-multipicker">` with `<summary class="orca-picker-btn">` (value text + chevron) and a panel `.orca-popover.orca-multipicker__panel`.
- Inside the panel: a filter input with `data-orca-filter-list`, a `.orca-multipicker__list` of checkboxes, and `.orca-multipicker__foot` with Clear and Done.
- Below: `.orca-multipicker__tags` with a removable tag per chosen value. Summary text: '3 videos', not a long list.

#### Example: Multi-picker

```django
<div style="max-width: 20rem">
  <p class="orca-label" id="mp-label">Videos</p>
  <details class="orca-multipicker" open>
    <summary class="orca-picker-btn" aria-labelledby="mp-label mp-value">
      <span class="orca-picker-btn__value" id="mp-value">2 videos</span>
      {% icon "chevron-down" %}
    </summary>
    <div class="orca-popover orca-multipicker__panel" style="position: static; box-shadow: var(--orca-shadow-elevated)">
      <div class="orca-search">
        {% icon "search" %}
        <input class="orca-input orca-input--dense" type="search" placeholder="Filter" aria-label="Filter videos" data-orca-filter-list="mp-list">
      </div>
      <ul class="orca-multipicker__list" id="mp-list">
        <li>
          <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Entrance A</label>
        </li>
        <li>
          <label class="orca-check"><input type="checkbox" checked><span class="orca-check__box"></span>Entrance B</label>
        </li>
        <li>
          <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Loading dock</label>
        </li>
      </ul>
      <div class="orca-multipicker__foot">
        <button class="orca-button orca-button--link" type="button">Clear</button>
        <button class="orca-button orca-button--dense" type="button">Done</button>
      </div>
    </div>
  </details>
  <div class="orca-multipicker__tags">
    <span class="orca-tag">
      <span class="orca-tag__text">Entrance A</span>
      <button class="orca-tag__remove" type="button" aria-label="Remove Entrance A">
        {% icon "close" %}
      </button>
    </span>
    <span class="orca-tag">
      <span class="orca-tag__text">Entrance B</span>
      <button class="orca-tag__remove" type="button" aria-label="Remove Entrance B">
        {% icon "close" %}
      </button>
    </span>
  </div>
</div>
```

**Classes:** `.orca-multipicker`, `.orca-multipicker__panel`, `.orca-multipicker__list`, `.orca-multipicker__foot`, `.orca-multipicker__tags`, `.orca-picker-btn`

**Principles applied:** Practical UI R12: Autocomplete for long lists; Practical UI S06: Make essential content visible or discoverable; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Multi-picker

---

## Language switcher

`id: language-switcher` · level: component · source: ORCA

A select of languages, each named in its own language, posting to Django's set_language view.

Built from: `select`, `button`

### General description

A control that lets people change the language of a site or app. Each language is shown in its own name.

#### Use cases

- Letting visitors switch a site between supported languages.
- Setting the interface language in an account menu.
- Offering translations in a footer of a public website.

#### When not to use it

- Do not guess language from location alone; offer a choice as well.
- For a site in one language, leave the switcher out.

#### Best practices

- Write each language in its own language, such as Deutsch or Français.
- Do not use flags, since one flag does not stand for one language.
- Place it in a predictable spot, such as the header or footer.
- Keep the person on the same page after switching.
- Mark each option with its language code so screen readers read it correctly.

### When to use

- Products in two or more languages; place it in the user menu or footer.

### How to use

- `<form action="{% url 'set_language' %}" method="post">` with csrf, a `next` hidden input and a select of `LANGUAGES` showing `language.name_local`.
- Add `data-orca-autosubmit` to the select and keep a visible Change button inside `<noscript>`.
- Add `lang` to each option so screen readers pronounce names correctly.

#### Example: Language switcher

```django
<form class="orca-row" method="post" action="#" onsubmit="return false">
  <label class="orca-label" for="lang" style="margin: 0">
    {% icon "website" %}
    <span class="orca-sr-only">Language</span>
  </label>
  <select class="orca-select orca-select--dense" id="lang" name="language" style="width: auto" data-orca-autosubmit>
    <option value="en" lang="en" selected>English</option>
    <option value="fr" lang="fr">Français</option>
    <option value="de" lang="de">Deutsch</option>
    <option value="ar" lang="ar">العربية</option>
  </select>
  <noscript>
    <button class="orca-button orca-button--dense" type="submit">Change</button>
  </noscript>
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

### General description

A text input joined to a fixed piece of text or a button, such as a unit, a currency sign or an action like Copy.

#### Use cases

- Entering an amount next to a currency or a unit like days or kg.
- Typing a web address with a fixed prefix.
- Adding a Copy or Test button right beside a value.

#### When not to use it

- For several unrelated actions, use separate buttons outside the field.
- For plain values with no unit, a normal input is enough.

#### Best practices

- Show the unit or prefix beside the value so people do not guess.
- Keep the attached text short.
- Link the addon to the input so screen readers read both.
- Use a button only for an action that directly relates to the input.
- Make sure the group stays readable on narrow screens.

### When to use

- Values with a fixed unit or prefix; a field with one related action (Test, Copy, Generate).

### How to use

- `.orca-input-group` containing `.orca-addon` spans, the input, and optionally a `.orca-button` at the end.
- Reference the unit addon from the input with `aria-describedby`.

#### Example: Unit and action

```django
<div class="orca-fields" style="max-width: 28rem">
  <div class="orca-field">
    <label class="orca-label" for="ig-a">Retention</label>
    <div class="orca-input-group" style="max-width: 12rem">
      <input class="orca-input" id="ig-a" type="number" value="30" aria-describedby="ig-a-u">
      <span class="orca-addon" id="ig-a-u">days</span>
    </div>
  </div>
  <div class="orca-field">
    <label class="orca-label" for="ig-b">Video address</label>
    <div class="orca-input-group">
      <span class="orca-addon">https://</span>
      <input class="orca-input" id="ig-b" value="media.example.com/v/4821">
      <button class="orca-button" type="button">Test</button>
    </div>
  </div>
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

### General description

A button that opens a panel of filters and shows how many are active. It keeps the page simple until filters are needed.

#### Use cases

- Narrowing a product or record list by many attributes.
- Showing advanced filters that do not fit in a toolbar.
- Telling people at a glance that a list is already filtered.

#### When not to use it

- For one or two simple filters, show them directly instead of hiding them.
- For free-text narrowing, use a search field.

#### Best practices

- Show the number of active filters on the button.
- Show active filters as removable tags outside the panel.
- Offer a clear all option.
- Tell the person how many results the filters give.
- Announce the open or closed state to assistive technology.

### When to use

- Lists with more filters than fit in the toolbar.

### How to use

- `<button class="orca-button" type="button" aria-expanded="false" aria-controls="filters" data-orca-disclose>{% icon "filter" %}Filters<span class="orca-count orca-count--accent">2</span></button>`.
- Explain the count to screen readers: `<span class="orca-sr-only">, 2 active</span>`.
- Also show active filters as removable tags with a Clear all link.

#### Example: Filter button with panel

```django
<button class="orca-button" type="button" aria-expanded="false" aria-controls="fb-panel" data-orca-disclose>
  {% icon "filter" %}
  Filters
  <span class="orca-count orca-count--accent" aria-hidden="true">2</span>
  <span class="orca-sr-only">, 2 active</span>
</button>
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

A select-style button that opens a listbox whose options can have a description.

Built from: `select`

### General description

A button that opens a list of options, where each option can include a short description or icon.

#### Use cases

- Choosing a role and seeing what each role can do.
- Picking a plan with a line explaining its limits.
- Selecting an option that needs a second line to tell it apart.

#### When not to use it

- When options are plain words, use the native select; it works better everywhere.
- When people must compare choices side by side, use radio buttons.

#### Best practices

- Keep the list to a manageable length, often 5 to 15 options.
- Show the current choice on the button.
- Support arrow keys, Enter and Escape.
- Return focus to the button when the list closes.
- Keep descriptions short and written in plain words.

### When to use

- 5–15 options that need a description or an icon to tell them apart.

### When not to use

- Plain options: the native select is more robust.
- Choices to compare side by side: use radio cards or a choice group.

### How to use

- Wrapper `.orca-anchor.orca-anchor--block` with `data-orca-listbox-wrap`; button `.orca-picker-btn` with `data-orca-listbox`, `aria-haspopup="listbox"`, `aria-expanded`, `aria-controls`; a hidden input carrying the value.
- List: `<ul class="orca-popover" role="listbox" hidden>` with `<li class="orca-option" role="option" tabindex="-1" data-value=…>`.
- orca.js handles click, arrow keys, Home/End, Enter, Escape and returning focus.

### Accessibility

- Name the button by its visible label and value: `aria-labelledby="label-id value-id"`.

#### Example: Role picker

```django
<div class="orca-anchor orca-anchor--block" data-orca-listbox-wrap style="max-width: 20rem">
  <span class="orca-label" id="dd-label">Role</span>
  <button class="orca-picker-btn" type="button" data-orca-listbox aria-haspopup="listbox" aria-expanded="false" aria-controls="dd-list" aria-labelledby="dd-label dd-value">
    <span class="orca-picker-btn__value" id="dd-value">Viewer</span>
    {% icon "chevron-down" %}
  </button>
  <input type="hidden" name="role" value="viewer">
  <ul class="orca-popover" id="dd-list" role="listbox" aria-labelledby="dd-label" hidden>
    <li class="orca-option" role="option" tabindex="-1" data-value="viewer" data-label="Viewer" aria-selected="true">
      <span class="orca-option__text">Viewer<span class="orca-option__desc">Sees dashboards and reports.</span></span>
    </li>
    <li class="orca-option" role="option" tabindex="-1" data-value="operator" data-label="Operator" aria-selected="false">
      <span class="orca-option__text">Operator<span class="orca-option__desc">Also manages videos and runs.</span></span>
    </li>
    <li class="orca-option" role="option" tabindex="-1" data-value="admin" data-label="Administrator" aria-selected="false">
      <span class="orca-option__text">Administrator<span class="orca-option__desc">Also manages users and settings.</span></span>
    </li>
  </ul>
</div>
```

**Classes:** `.orca-picker-btn`, `.orca-picker-btn__value`, `.orca-popover`, `.orca-option`, `.orca-option__text`, `.orca-option__desc`, `.orca-anchor`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI R12: Autocomplete for long lists; Hick's law: fewer, clearer choices mean faster decisions

**ORCA guide items covered:** Dropdown select (picker)

---

## Combobox (autocomplete)

`id: combobox` · level: component · source: ORCA

A text input that suggests matching options as people type. The value must be one of them.

Built from: `text-input`

### General description

A text box that suggests matching options as people type. The final value must be one of the suggestions.

#### Use cases

- Choosing a country, city or person from a long list.
- Finding a product or record by typing part of its name.
- Selecting an item when people know its name already.

#### When not to use it

- For short lists of about 15 items or fewer, use a normal select.
- When any text is allowed, use a plain input with optional suggestions.

#### Best practices

- Start suggesting after one or two typed letters.
- Highlight the part of each suggestion that matches the typed text.
- Show no more than about 10 suggestions at a time.
- Support arrow keys, Enter and Escape.
- Show a clear message when nothing matches.

### When to use

- Choosing one item from a long known list: a country, a video, a person, a product.

### When not to use

- Free text with optional hints: use auto-suggest.
- Fewer than about 15 options: a select.

### How to use

- Wrapper `.orca-combobox` with `data-orca-combobox-wrap`; `<input class="orca-input" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="list-id" data-orca-combobox>` and a hidden input for the value.
- Options `<li class="orca-option" role="option" id=… data-value=…>` in a hidden `.orca-popover` listbox; show at most 10.
- Server results: swap the listbox content with htmx (`hx-get`, `hx-trigger="input changed delay:300ms"`, `hx-target`).
- Add a status element (`data-orca-status`) to announce the number of suggestions.

### Accessibility

- Keyboard: Down opens and moves, Enter picks, Escape closes then clears; focus stays in the input (`aria-activedescendant`).

#### Example: Country

```django
<div class="orca-field orca-combobox" data-orca-combobox-wrap style="max-width: 20rem">
  <label class="orca-label" for="cb-in">Country</label>
  <input class="orca-input" id="cb-in" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="cb-list" autocomplete="off" data-orca-combobox data-orca-status="cb-status">
  <input type="hidden" name="country">
  <ul class="orca-popover" id="cb-list" role="listbox" aria-label="Countries" hidden style="top: 100%">
    <li class="orca-option" role="option" id="cb-1" data-value="DZ">Algeria</li>
    <li class="orca-option" role="option" id="cb-2" data-value="BE">Belgium</li>
    <li class="orca-option" role="option" id="cb-3" data-value="CA">Canada</li>
    <li class="orca-option" role="option" id="cb-4" data-value="FR">France</li>
    <li class="orca-option" role="option" id="cb-5" data-value="DE">Germany</li>
    <li class="orca-option" role="option" id="cb-6" data-value="MA">Morocco</li>
    <li class="orca-option" role="option" id="cb-7" data-value="TN">Tunisia</li>
    <li class="orca-popover__empty" hidden>No country matches. Check the spelling.</li>
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

### General description

A free text box that offers common answers from a list while still allowing anything to be typed.

#### Use cases

- Entering a tag, department or location where many answers repeat.
- Speeding up typing of common values without limiting them.
- Entering a job title or company name.

#### When not to use it

- When the answer must be from a fixed list, use a combobox or select.
- For answers that are always different, plain input is simpler.

#### Best practices

- Put the most common suggestions first.
- Keep the list reasonably short.
- Do not block answers that are not in the list.
- Still label the field clearly.
- Check typed values on the server, just as for any input.

### When to use

- Free text where most answers repeat: a tag, a mounting location, a department.

### When not to use

- Answers that must match a list: use the combobox.

### How to use

- `<input class="orca-input" list="dl-id">` + `<datalist id="dl-id"><option value="…"></datalist>`.
- Put the most used suggestions first; keep the list under about 20.

#### Example: Mounting location

```django
<div class="orca-field" style="max-width: 20rem">
  <label class="orca-label" for="as-in">Mounting location</label>
  <input class="orca-input" id="as-in" list="as-dl" autocomplete="off">
  <datalist id="as-dl">
    <option value="Above the door"></option>
    <option value="Ceiling, centre"></option>
    <option value="Wall, facing in"></option>
  </datalist>
</div>
```

**Classes:** `.orca-input`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Auto-suggest input

---

## OTP input

`id: otp-input` · level: component · source: ORCA

A one-time-code field: label, digit boxes, hint, error and a resend link.

Built from: `otp-digit`, `help-text`, `countdown-label`

### General description

A set of boxes for typing a one-time code, such as a six-digit number sent by text or email to confirm identity.

#### Use cases

- Confirming a login with two-step verification.
- Verifying a phone number or email address.
- Approving a sensitive action such as a payment.

#### When not to use it

- For long passwords, use a password field; codes are meant to be short and single-use.
- Do not use codes where a simpler check would do.

#### Best practices

- Tell people where the code was sent and how long it lasts.
- Allow pasting the whole code and browser autofill.
- Offer a Send a new code option after a short wait.
- Show errors that say whether the code was wrong or expired.
- Use a numeric keypad on phones.

### When to use

- Verification and two-factor steps.

### How to use

- `<fieldset class="orca-otp">` with the legend, help ('We sent a 6-digit code to …'), the OTP digit boxes (`data-orca-otp`), errors above the boxes and a 'Send a new code' button after the countdown.
- Auto-submit on the last digit only if the server answers in under a second.

#### Example: Verification code

```django
<fieldset class="orca-choice-group" aria-describedby="otp-help">
  <legend class="orca-label">Verification code</legend>
  <p class="orca-help" id="otp-help">We sent a 6-digit code to a••••@acme.com. It expires in 10 minutes.</p>
  <div class="orca-row" data-orca-otp>
    {% for i in "123456" %}
      <input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit {{ i }} of 6"{% if forloop.first %} autocomplete="one-time-code"{% endif %}>
    {% endfor %}
  </div>
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

### General description

A row of stars people select to give a score, usually from 1 to 5. It is a quick way to collect an opinion.

#### Use cases

- Rating a product, service or support conversation.
- Collecting quick feedback after a task.
- Letting people review a purchase or place.

#### When not to use it

- For detailed feedback, add a text box; stars alone say little.
- For measuring likelihood to recommend, use a 0 to 10 scale instead.

#### Best practices

- Show the chosen value in words, such as 4 of 5.
- Label each star so screen readers read the number.
- Make stars large enough to tap easily.
- Let people change their rating before submitting.
- Make clear what the lowest and highest ratings mean.

### When to use

- Feedback and review forms.

### How to use

- `<fieldset class="orca-rating-wrap">` with a legend and `.orca-rating`, which lists radios from 5 down to 1 (CSS reverses them), each followed by a label with a star icon and hidden text '4 stars'.
- Show the value in words in `.orca-rating__value`.

#### Example: Rating

```django
<fieldset class="orca-rating-wrap">
  <legend class="orca-label">How easy was the setup?</legend>
  <div class="orca-rating">
    {% for n in "54321" %}
      <input type="radio" name="rate" id="rate-{{ n }}" value="{{ n }}"{% if n == "4" %} checked{% endif %}>
      <label for="rate-{{ n }}">
        {% icon "star" %}
        <span class="orca-sr-only">
          {{ n }}
          star
          {% if n != "1" %}
            s
          {% endif %}
        </span>
      </label>
    {% endfor %}
  </div>
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

### General description

Three separate boxes for day, month and year. People type a date they already know instead of picking it in a calendar.

#### Use cases

- Entering a birth date.
- Entering a document date such as an expiry or issue date.
- Any date far in the past or future.

#### When not to use it

- For dates near today, such as a booking, use a calendar date picker.
- For relative dates like next week, offer shortcuts or a picker.

#### Best practices

- Label each box clearly as Day, Month and Year.
- Give an example, such as 27 3 2024.
- Order the boxes the way the reader's region writes dates.
- Use numeric keypads on phones.
- Show one error for the whole date, not three.

### When to use

- Dates people know, far in the past or future: birth date, licence expiry, contract start.

### When not to use

- Dates chosen relative to today: use the date picker.

### How to use

- `<fieldset class="orca-split-date">` with legend, hint ('For example, 27 3 2024'), then `.orca-split-date__parts` with three `.orca-split-date__part` (label + `inputmode="numeric"` input); the year part adds `--year`.
- Order the parts as the locale writes dates; validate the whole date on the server and give one error for the group.

#### Example: Licence expiry

```django
<fieldset class="orca-split-date" aria-describedby="sd-help">
  <legend class="orca-label">Licence expiry date</legend>
  <p class="orca-help" id="sd-help">For example, 27 3 2027</p>
  <div class="orca-split-date__parts">
    <div class="orca-split-date__part">
      <label class="orca-label" for="sd-d">Day</label>
      <input class="orca-input" id="sd-d" inputmode="numeric" maxlength="2">
    </div>
    <div class="orca-split-date__part">
      <label class="orca-label" for="sd-m">Month</label>
      <input class="orca-input" id="sd-m" inputmode="numeric" maxlength="2">
    </div>
    <div class="orca-split-date__part orca-split-date__part--year">
      <label class="orca-label" for="sd-y">Year</label>
      <input class="orca-input" id="sd-y" inputmode="numeric" maxlength="4">
    </div>
  </div>
</fieldset>
```

**Classes:** `.orca-split-date`, `.orca-split-date__parts`, `.orca-split-date__part`, `.orca-split-date__part--year`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI R06: Match input width to the expected answer

**ORCA guide items covered:** Split date input (day, month, year)

---

## File input field

`id: file-field` · level: component · source: ORCA

A labelled drop zone around a native file input that lists chosen files.

Built from: `file-input`, `help-text`

### General description

An area where people choose or drag files to upload. It lists the chosen files and states what is allowed.

#### Use cases

- Uploading documents, photos or a profile picture.
- Importing data from a spreadsheet file.
- Attaching files to a message or request.

#### When not to use it

- For tiny text, ask people to type it rather than upload a file.
- For many large files, use a dedicated uploader with progress and retry.

#### Best practices

- State accepted file types and the size limit before upload.
- Let people click or drag and drop.
- Show the chosen file names so they can be checked.
- Show progress for large uploads.
- Check file type and size again on the server.

### When to use

- Uploading documents, images or imports.

### How to use

- `.orca-field` with label and help (accepted types, size limit), then `<div class="orca-dropzone">` containing the icon, a title, a hint and the `<input type="file">` (it covers the zone).
- Add `data-orca-file-list="list-id"` to list chosen files in `.orca-file-list`.
- Check type and size again on the server; show upload progress with progress-bar-with-counts.

#### Example: Drop zone

```django
<div class="orca-field" style="max-width: 28rem">
  <label class="orca-label" for="fz">Floor plan</label>
  <p class="orca-help" id="fz-help">PNG or JPG, up to 10 MB.</p>
  <div class="orca-dropzone">
    {% icon "upload" size="l" %}
    <span class="orca-dropzone__title">Drop a file here or choose one</span>
    <span class="orca-dropzone__hint">One file</span>
    <input type="file" id="fz" accept="image/png,image/jpeg" aria-describedby="fz-help" data-orca-file-list="fz-list">
  </div>
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

### General description

A message at the top of a form that reports a problem not tied to one field, such as a conflict or permission error.

#### Use cases

- Showing that a save failed because of a server problem.
- Warning that chosen dates clash with another record.
- Explaining that the person lacks permission to submit.

#### When not to use it

- For a problem with one field, show the error next to that field.
- For good news or neutral tips, use an info or success message.

#### Best practices

- Place it above the fields so it is seen first.
- Say what went wrong and what to do next.
- Use an error icon as well as colour.
- Announce it to screen readers when it appears.
- Add a summary with links when several fields are invalid.

### When to use

- Non-field errors after submit; conflicts with other records; permission problems.

### How to use

- Django: `{% orca_form_errors form %}` renders non-field errors as a callout and, with two or more invalid fields, a linked error summary.
- Markup: `<div class="orca-callout orca-callout--negative" role="alert">` with the error icon, a title that states the problem and a body that says what to do.

#### Example: Non-field error

```django
<div class="orca-callout orca-callout--negative" role="alert">
  {% icon "error" %}
  <p class="orca-callout__title">This run overlaps “Morning check”</p>
  <p class="orca-callout__body">Choose a start after 10:00 or stop the other run first.</p>
</div>
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

### General description

The row of buttons at the end of a form, with the main action first and others such as Cancel after it.

#### Use cases

- Saving or submitting a form.
- Offering Cancel next to Save in a dialog.
- Placing a Delete action away from the main buttons.

#### When not to use it

- Do not scatter several equal buttons through the form; keep actions together at the end.
- For actions that apply instantly, such as switches, no button row is needed.

#### Best practices

- Make one primary action stand out, labelled with a verb.
- Place buttons directly after the last field.
- Put destructive actions apart and ask to confirm.
- Keep the Cancel option easy to reach.
- Stack buttons full width on small screens.

### When to use

- The end of every form, dialog form and settings section with a Save.

### How to use

- `<div class="orca-form-actions">` after the last field: primary button first, then Cancel (default or link).
- A destructive action (Delete) goes to the far end in `.orca-form-actions__end`, styled default or outline-danger, and asks for confirmation.
- Long forms: `--sticky` pins the actions to the bottom of the viewport. On phones the buttons stack full width.

#### Example: Save, cancel and delete

```django
<div class="orca-form-actions">
  <button class="orca-button orca-button--primary" type="submit">Save video</button>
  <a class="orca-button" href="#">Cancel</a>
  <span class="orca-form-actions__end">
    <button class="orca-button orca-button--outline-danger" type="button" data-orca-dialog-open="fa-confirm">Delete video</button>
  </span>
</div>
<dialog class="orca-dialog" id="fa-confirm" aria-labelledby="fa-confirm-t">
  <form method="dialog">
    <div class="orca-dialog__header">
      <h2 class="orca-dialog-title" id="fa-confirm-t">Delete Entrance A?</h2>
    </div>
    <div class="orca-dialog__body">
      <p class="orca-p">Its counts are kept. Its zones and alert rules are deleted.</p>
    </div>
    <div class="orca-dialog__footer">
      <button class="orca-button orca-button--danger" type="submit" value="delete">Delete video</button>
      <button class="orca-button" type="submit" value="cancel" autofocus>Cancel</button>
    </div>
  </form>
</dialog>
```

**Classes:** `.orca-form-actions`, `.orca-form-actions__end`, `.orca-form-actions--sticky`

**Principles applied:** Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI B03: One primary action; Practical UI B08: Keep action order predictable; Practical UI B13: Scale friction to the consequence

**ORCA guide items covered:** Form actions

---

## Row selection

`id: row-select` · level: component · source: ORCA

A checkbox per table row and a select-all checkbox in the header.

Built from: `checkbox`

### General description

Checkboxes at the start of table rows, with one at the top to select all. People pick several records and then act on them together.

#### Use cases

- Bulk delete, archive or export from a table.
- Moving or assigning many items at once.
- Comparing chosen rows.

#### When not to use it

- Tables where only a single action per row is needed; use row buttons.
- Choosing just one row from a few; use radio buttons.

#### Best practices

- Name each checkbox after its row for screen readers.
- Show how many rows are selected.
- Show the available bulk actions as soon as something is selected.
- Make select all clear about what it covers, such as this page or all results.

### When to use

- Tables that offer bulk actions.

### How to use

- Header: `<th scope="col" class="orca-table__select"><label class="orca-check"><input type="checkbox" aria-label="Select all videos"><span class="orca-check__box"></span></label></th>`; one per row named after the row.
- Selecting rows shows the count and the bulk actions in the table toolbar.

### Accessibility

- Each checkbox is named after its row ('Select Entrance A').

#### Example: Select cells

```django
<table class="orca-table">
  <thead>
    <tr>
      <th scope="col" class="orca-table__select">
        <label class="orca-check">
          <input type="checkbox" aria-label="Select all videos">
          <span class="orca-check__box"></span>
        </label>
      </th>
      <th scope="col">Video</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="orca-table__select">
        <label class="orca-check">
          <input type="checkbox" checked aria-label="Select Harbour at dusk">
          <span class="orca-check__box"></span>
        </label>
      </td>
      <td>Harbour at dusk</td>
    </tr>
  </tbody>
</table>
```

**Classes:** `.orca-table__select`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Jakob's law: work the way products people already know work; Practical UI R14: Checkbox or switch according to timing

**Related:** `data-table`, `table-toolbar`

---

## Formatting toolbar

`id: formatting-toolbar` · level: component · source: ORCA

A row of toggle icon buttons for bold, italic, lists and links above a text area.

Built from: `icon-button`, `divider`

### General description

A row of small buttons for formatting text, such as bold, italic, lists and links. It sits above a text area that supports rich text.

#### Use cases

- Writing comments or descriptions with formatting.
- Editing articles or emails.
- Rich notes fields.

#### When not to use it

- Plain text fields; leave the toolbar out.
- Very long documents needing many options; use a full editor with menus.

#### Best practices

- Use familiar icons with text names for assistive technology.
- Show which formats are on.
- Support keyboard shortcuts such as Ctrl+B.
- Group related buttons and keep the set small.

### When to use

- Above a rich text field.

### How to use

- `<div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting">` with dense icon buttons using `aria-pressed`, groups separated by a vertical divider.

### Accessibility

- Arrow keys move between buttons; each has an accessible name.

#### Example: Toolbar

```django
<div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting" style="max-width: 20rem">
  <button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="true" aria-label="Bold">
    <b>B</b>
  </button>
  <button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="false" aria-label="Italic">
    <i>I</i>
  </button>
  <span class="orca-divider orca-divider--vertical" role="separator"></span>
  <button class="orca-icon-button orca-icon-button--dense" type="button" aria-pressed="false" aria-label="Bulleted list">
    {% icon "list" %}
  </button>
</div>
```

**Classes:** `.orca-richtext__toolbar`

**Principles applied:** Jakob's law: work the way products people already know work; Practical UI F10: Specify every interaction state

**Related:** `rich-text-editor`

---

## Applied filters

`id: applied-filters` · level: component · source: ORCA

Active filters as removable tags, with Clear all and the result count.

Built from: `tag`, `link-action`

### General description

A row showing which filters are currently active, each as a tag that can be removed. It also gives a way to clear them all and the number of results.

#### Use cases

- Above search results or lists that have been filtered.
- Product listings with several filters.
- Empty results, to show what caused them.

#### When not to use it

- When no filter is active; show nothing.
- Choosing filters; use a filter panel or menu for that.

#### Best practices

- Show every active filter, never hide any.
- Let people remove one filter with one click.
- Offer Clear all when more than one is active.
- Show the result count and update it right away.

### When to use

- Above results while a filter is applied; inside a no-results state.

### How to use

- `<div class="orca-filter-bar__applied"><span class="orca-small orca-muted">Filtered by</span>` then one removable tag per filter, a 'Clear all' link button and the count in `role="status"`.

### Accessibility

- Each remove button names the filter it removes.

#### Example: Applied filters

```django
<div class="orca-filter-bar__applied">
  <span class="orca-small orca-muted">Filtered by</span>
  <span class="orca-tag">
    <span class="orca-tag__text">Type: Video</span>
    <button class="orca-tag__remove" type="button" aria-label="Remove filter Type: Video">
      {% icon "close" %}
    </button>
  </span>
  <button class="orca-button orca-button--link" type="button">Clear all</button>
  <span class="orca-small orca-muted" role="status">14 videos</span>
</div>
```

**Classes:** `.orca-filter-bar__applied`

**Principles applied:** Practical UI S06: Make essential content visible or discoverable; Postel's law: accept varied input, output reliable and accessible UI; Doherty threshold: respond within 400 ms; show progress for anything slower

**Related:** `filter-bar`, `no-results`

---
