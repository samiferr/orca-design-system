# Forms

Form sections, stacks and sign-in, plus editors for schedules, zones, properties and rich text.

## Form section

`id: form-section` · level: pattern · source: Tangerine

A titled group of related fields with a short explanation beside them.

Built from: `form-field`, `section-heading`

### General description

A group of related fields under a heading, with a short note about what the group is for.

#### Use cases

- Splitting a long settings page into topics.
- Grouping billing, contact and account details separately.
- Making a long form feel shorter.

#### When not to use it

- For a short form with a handful of fields, headings only add clutter.
- For steps that must happen in order, use a multi-step form.

#### Best practices

- Give each section a clear, descriptive heading.
- Group only fields that belong together.
- Add a one-sentence description when the purpose is unclear.
- Keep the order logical, with the most important sections first.
- Use proper heading levels so screen readers can navigate.

### When to use

- Settings pages and long single-page forms.

### How to use

- `<section class="orca-form-section">` with `.orca-form-section__intro` (section title + one-sentence description) and `.orca-form-section__fields` (form fields).
- The intro sits beside the fields from 1036px and above them below.

#### Example: Section

```django
<section class="orca-form-section" aria-labelledby="fs-t">
  <div class="orca-form-section__intro">
    <h2 class="orca-section-title" id="fs-t">Counting</h2>
    <p>How often thumbnails are taken and how long videos are kept.</p>
  </div>
  <div class="orca-form-section__fields">
    <div class="orca-field">
      <label class="orca-label" for="fs-int">Snapshot interval</label>
      <div class="orca-input-group" style="max-width: 12rem">
        <input class="orca-input" id="fs-int" type="number" value="5" aria-describedby="fs-int-u">
        <span class="orca-addon" id="fs-int-u">minutes</span>
      </div>
    </div>
    <div class="orca-field">
      <label class="orca-label" for="fs-ret">Keep counts for</label>
      <select class="orca-select" id="fs-ret" style="max-width: 16rem">
        <option>1 year</option>
        <option selected>2 years</option>
      </select>
    </div>
  </div>
</section>
```

**Classes:** `.orca-form-section`, `.orca-form-section__intro`, `.orca-form-section__fields`

**Principles applied:** Practical UI R17: Group fields under headings; Miller's law: chunk information so working memory is not overloaded; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Form section

---

## Form stack

`id: form-stack` · level: pattern · source: Tangerine

Fields in one column (the default), or two columns for short, closely related fields.

Built from: `form-field`, `form-actions`

### General description

A layout that arranges form fields in one column, or in two columns when fields are short and closely related.

#### Use cases

- Laying out almost any form in one clear column.
- Placing start and end values side by side.
- Fitting many short fields into a compact admin form.

#### When not to use it

- Do not use many columns for long forms; people skip fields and lose their place.
- For unrelated fields, keep one column.

#### Best practices

- Prefer one column for a single reading path.
- Use two columns only for short, related pairs.
- Keep consistent spacing between fields.
- Limit the line width so inputs are not stretched too wide.
- Fall back to one column on phones.

### When to use

- One column: almost every form.
- Two columns (compact): dense admin forms with many short fields.

### How to use

- `<div class="orca-form-stack">` of fields (24px apart, max 36rem).
- Compact: `orca-form-stack--two`; a field that needs the full width gets `.orca-span-2`. On phones it falls back to one column.

#### Example: One column and two columns

```django
<div class="orca-stack" style="gap: var(--orca-space-32)">
  <div class="orca-form-stack">
    <div class="orca-field">
      <label class="orca-label" for="fst-1">Video name</label>
      <input class="orca-input" id="fst-1">
    </div>
    <div class="orca-field">
      <label class="orca-label" for="fst-2">Stream address</label>
      <input class="orca-input" id="fst-2">
    </div>
  </div>
  <div class="orca-form-stack orca-form-stack--two">
    <div class="orca-field">
      <label class="orca-label" for="fst-3">Host</label>
      <input class="orca-input" id="fst-3">
    </div>
    <div class="orca-field">
      <label class="orca-label" for="fst-4">Port</label>
      <input class="orca-input orca-input--w8" id="fst-4" inputmode="numeric">
    </div>
    <div class="orca-field orca-span-2">
      <label class="orca-label" for="fst-5">Notes <span class="orca-optional">(optional)</span></label>
      <textarea class="orca-textarea" id="fst-5" rows="2"></textarea>
    </div>
  </div>
</div>
```

**Classes:** `.orca-form-stack`, `.orca-form-stack--two`, `.orca-span-2`

**Principles applied:** Practical UI R01: Keep the main form flow in one column; Practical UI R10: Keep labels close to their inputs; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Form stack (one column); Form stack (compact, two columns)

---

## Schedule editor

`id: schedule-editor` · level: pattern · source: Tangerine

A weekly schedule of rows (day, start, end) with presets, add and remove, and overlap checks.

Built from: `add-row-button`, `overlap-warning`, `preset-buttons`

### General description

A form control for setting weekly times, built from rows of day, start and end time that can be added or removed.

#### Use cases

- Setting opening hours for a shop or service.
- Defining when a recording or alert is active.
- Choosing quiet hours for notifications.

#### When not to use it

- For a single date and time, use a date and time picker.
- For a repeating rule like every second Tuesday, use a recurrence form.

#### Best practices

- Offer presets such as business hours for common cases.
- Let people add and remove rows easily.
- Warn when rows overlap as soon as they are entered.
- Show a time format people recognise.
- Make each row's remove button describe which row it removes.

### When to use

- Capture schedules, opening hours, alert quiet hours.

### How to use

- A form section with preset buttons, the schedule rows (`<div class="orca-schedule" id=…>`), an add-row button with its `<template>`, and overlap warnings in invalid rows.
- Django: a formset; the template uses `__prefix__` and `data-orca-total` points at TOTAL_FORMS.

#### Example: Capture schedule

```django
<fieldset class="orca-choice-group" style="max-width: 40rem">
  <legend class="orca-label">Capture schedule</legend>
  <div class="orca-presets" role="group" aria-label="Presets">
    <button class="orca-tag" type="button" aria-pressed="true">Opening hours</button>
    <button class="orca-tag" type="button" aria-pressed="false">Around the clock</button>
  </div>
  <div class="orca-schedule" id="se-rows">
    <div class="orca-schedule-row" data-orca-row>
      <select class="orca-select" aria-label="Day">
        <option>Weekdays</option>
        <option>Saturday</option>
      </select>
      <input class="orca-input" type="time" value="08:00" aria-label="From">
      <span class="orca-schedule-row__sep" aria-hidden="true">–</span>
      <input class="orca-input" type="time" value="19:00" aria-label="To">
      <button class="orca-icon-button" type="button" aria-label="Remove weekdays 08:00 to 19:00" data-orca-remove-row>
        {% icon "delete" %}
      </button>
    </div>
    <div class="orca-schedule-row" data-orca-row>
      <select class="orca-select" aria-label="Day">
        <option>Weekdays</option>
        <option selected>Saturday</option>
      </select>
      <input class="orca-input" type="time" value="09:00" aria-label="From">
      <span class="orca-schedule-row__sep" aria-hidden="true">–</span>
      <input class="orca-input" type="time" value="18:00" aria-label="To">
      <button class="orca-icon-button" type="button" aria-label="Remove Saturday 09:00 to 18:00" data-orca-remove-row>
        {% icon "delete" %}
      </button>
    </div>
  </div>
  <template id="se-tpl">
    <div class="orca-schedule-row" data-orca-row>
      <select class="orca-select" aria-label="Day">
        <option>Weekdays</option>
        <option>Saturday</option>
        <option>Sunday</option>
      </select>
      <input class="orca-input" type="time" aria-label="From">
      <span class="orca-schedule-row__sep" aria-hidden="true">–</span>
      <input class="orca-input" type="time" aria-label="To">
      <button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>
        {% icon "delete" %}
      </button>
    </div>
  </template>
  <div>
    <button class="orca-button orca-button--ghost" type="button" data-orca-add-row="se-tpl" aria-controls="se-rows">
      {% icon "plus" %}
      Add hours
    </button>
  </div>
</fieldset>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Formset

```python
# videos/forms.py
from django import forms

from .models import OpeningHours, Video

OpeningHoursFormSet = forms.inlineformset_factory(
    Video, OpeningHours, fields=["weekday", "opens", "closes"], extra=0, can_delete=True,
)


# videos/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OpeningHoursFormSet
from .models import Video


def edit_hourss(request, pk):
    video = get_object_or_404(Video, pk=pk)
    formset = OpeningHoursFormSet(request.POST or None, instance=video, prefix="hourss")
    if request.method == "POST" and formset.is_valid():
        formset.save()
        return redirect("video-detail", pk=video.pk)
    # Template: {{ formset.management_form }}, one [data-orca-row] per form, and a <template id="hours-row">
    # holding {{ formset.empty_form }} (its names contain __prefix__). The add-row button points at it with
    # data-orca-add-row="hours-row" and data-orca-total="id_hourss-TOTAL_FORMS".
    return render(request, "videos/hourss.html", {"video": video, "formset": formset})
```

**Classes:** `.orca-schedule`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Peak–end rule: people judge an experience by its peak and its end; Practical UI R21: Validate after leaving a field when context matters

**ORCA guide items covered:** Schedule editor

---

## Zone/line editor

`id: zone-editor` · level: pattern · source: Tangerine

Draw a counting zone by clicking its corners on the video image, with the zone list beside it.

Built from: `zone-row`, `captioned-media`

### General description

A tool for drawing shapes or lines over an image or map by clicking points, next to a list of the shapes drawn.

#### Use cases

- Marking areas of interest on a camera image.
- Drawing a delivery or coverage area.
- Defining regions to include or exclude on a floor plan.

#### When not to use it

- For choosing from fixed areas, use a list or select instead of drawing.
- For precise measurements, offer typed coordinates instead of drawing only.

#### Best practices

- Offer undo and clear so mistakes cost little.
- Show a status line saying what to do next.
- Provide typed coordinate fields as an alternative to drawing.
- Show a label and colour for each shape.
- Store the shapes as simple data the server can check.

### When to use

- Defining counting zones, lines and excluded areas on a video view.

### How to use

- `<div class="orca-zone-editor" data-orca-zone-editor>` with `.orca-zone-editor__stage` (the snapshot image + an empty `<svg viewBox="0 0 100 100" preserveAspectRatio="none">`), a toolbar (`data-orca-zone-action="undo|clear|close"`), a status line (`data-orca-zone-status`, polite) and a hidden input receiving the points as JSON percentages.
- Beside it: the zone rows, plus a coordinates form as the keyboard alternative.

### Accessibility

- Drawing needs a pointer; provide numeric corner fields for keyboard and screen-reader users.

#### Example: Draw a zone

```django
<div class="orca-zone-editor" data-orca-zone-editor>
  <div>
    <div class="orca-zone-editor__stage" style="--orca-zone: var(--orca-teal-400)">
      <img src="{% static "orca/img/sample-street.svg" %}" alt="Entrance A video view">
      <svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"></svg>
    </div>
    <input type="hidden" name="points" value="[[30,62],[62,60],[66,92],[26,94]]">
    <div class="orca-zone-editor__toolbar">
      <button class="orca-button orca-button--dense" type="button" data-orca-zone-action="close">Close shape</button>
      <button class="orca-button orca-button--dense" type="button" data-orca-zone-action="undo">
        {% icon "rotate-left" %}
        Undo point
      </button>
      <button class="orca-button orca-button--ghost orca-button--dense" type="button" data-orca-zone-action="clear">Clear</button>
    </div>
    <p class="orca-zone-editor__hint" data-orca-zone-status aria-live="polite"></p>
  </div>
  <div>
    <p class="orca-panel-title">Zones</p>
    <div class="orca-zone-row">
      <span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-400)"></span>
      <span class="orca-zone-row__name">Door line</span>
      <span class="orca-zone-row__count orca-num">4 points</span>
      <span></span>
    </div>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form

```python
# videos/forms.py — the editor writes the points as JSON into a hidden field
import json

from django import forms


class RegionForm(forms.Form):
    name = forms.CharField()
    points = forms.CharField(widget=forms.HiddenInput)

    def clean_points(self):
        try:
            points = json.loads(self.cleaned_data["points"])
        except ValueError:
            raise forms.ValidationError("Draw the region again: its points could not be read.")
        if len(points) < 3 or not all(len(p) == 2 and all(0 <= v <= 100 for v in p) for p in points):
            raise forms.ValidationError("Draw at least three points inside the image.")
        return points   # [[x, y], …] in percent of the image; store it in a JSONField
```

**Classes:** `.orca-zone-editor`, `.orca-zone-editor__stage`, `.orca-zone-editor__toolbar`, `.orca-zone-editor__hint`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Zone/line editor

---

## Login card

`id: login-card` · level: pattern · source: Tangerine

The sign-in form: logo, title, email, password, remember me, sign-in button and recovery link.

Built from: `logo-link`, `form-field`, `toggle-field`, `form-actions`, `form-alert`

### General description

The sign-in form: a small panel with logo, email, password, a remember option, a sign-in button and a link to recover access.

#### Use cases

- Signing people in to an account or application.
- Starting a session in an admin area.
- Requesting access to a private site.

#### When not to use it

- For one-click access to a public site, avoid forcing a login.
- For sign-up, use a registration form with more fields.

#### Best practices

- Keep it short: only ask for what is needed to sign in.
- Allow browsers and password managers to fill in the fields.
- Use a general error message that does not say which field was wrong.
- Offer a clear password reset link.
- Let people show the password they typed.

### When to use

- Sign-in pages (with the auth layout).

### How to use

- `<form class="orca-login" method="post">` with the logo, `h1.orca-login__title`, a form alert for failures, email (`autocomplete="username"`) and password (`autocomplete="current-password"`) fields, `.orca-login__row` (remember me + 'Forgot your password?'), a full-width primary button and `.orca-login__foot`.
- Error: 'Email or password is incorrect. Check both, or reset your password.'

#### Example: Sign in

```django
<form class="orca-login" method="post" action="#" onsubmit="return false">
  <div class="orca-login__head">
    {% orca_logo href="" %}
    <h1 class="orca-login__title">Sign in</h1>
  </div>
  <div class="orca-callout orca-callout--negative" role="alert">
    {% icon "error" %}
    <p class="orca-callout__title">Email or password is incorrect</p>
    <p class="orca-callout__body">Check both, or reset your password.</p>
  </div>
  <div class="orca-field">
    <label class="orca-label" for="lg-email">Email</label>
    <input class="orca-input" id="lg-email" type="email" autocomplete="username" value="ada@acme.com">
  </div>
  <div class="orca-field">
    <label class="orca-label" for="lg-pw">Password</label>
    <input class="orca-input" id="lg-pw" type="password" autocomplete="current-password">
  </div>
  <div class="orca-login__row">
    <label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Keep me signed in</label>
    <a class="orca-link orca-small" href="#">Forgot your password?</a>
  </div>
  <button class="orca-button orca-button--primary orca-button--block" type="submit">Sign in</button>
  <p class="orca-login__foot">No account? Ask your administrator.</p>
</form>
```

**Classes:** `.orca-login`, `.orca-login__head`, `.orca-login__title`, `.orca-login__row`, `.orca-login__foot`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Practical UI W15: Help people recover from errors

**ORCA guide items covered:** Login card

---

## Properties editor

`id: properties-editor` · level: pattern · source: ORCA

A list of key and value rows with add and remove, for free-form metadata.

Built from: `property-row`, `add-row-button`

### General description

A list of key and value rows where people add their own details. It suits free-form data without a fixed structure.

#### Use cases

- Adding custom fields or labels to a record.
- Editing HTTP headers or settings pairs.
- Storing extra metadata that varies between items.

#### When not to use it

- For known fields, use normal form fields; they are clearer and easier to validate.
- For large structured data, use an import or a dedicated editor.

#### Best practices

- Provide clear Key and Value labels on every row.
- Reject duplicate keys with an error on the repeated row.
- Trim extra spaces without bothering the person.
- Make Add and Remove buttons easy to find and name.
- Keep focus on the new row after adding it.

### When to use

- Custom properties, labels, headers, metadata on records.

### How to use

- A fieldset with a legend and help, the property rows, an add-row button and its template.
- Reject duplicate keys with an error on the second row; trim spaces silently.

#### Example: Properties

```django
<fieldset class="orca-choice-group" style="max-width: 40rem">
  <legend class="orca-label">Properties</legend>
  <p class="orca-help">Extra details shown on reports. Keys must be unique.</p>
  <div class="orca-property-rows" id="pe-list">
    <div class="orca-property-row" data-orca-row>
      <div>
        <label class="orca-label" for="pe-k0">Key</label>
        <input class="orca-input" id="pe-k0" value="cost-centre">
      </div>
      <div>
        <label class="orca-label" for="pe-v0">Value</label>
        <input class="orca-input" id="pe-v0" value="NB-OPS">
      </div>
      <button class="orca-icon-button" type="button" aria-label="Remove property cost-centre" data-orca-remove-row>
        {% icon "delete" %}
      </button>
    </div>
  </div>
  <template id="pe-tpl">
    <div class="orca-property-row" data-orca-row>
      <div>
        <label class="orca-label" for="pe-k__prefix__">Key</label>
        <input class="orca-input" id="pe-k__prefix__">
      </div>
      <div>
        <label class="orca-label" for="pe-v__prefix__">Value</label>
        <input class="orca-input" id="pe-v__prefix__">
      </div>
      <button class="orca-icon-button" type="button" aria-label="Remove property" data-orca-remove-row>
        {% icon "delete" %}
      </button>
    </div>
  </template>
  <div>
    <button class="orca-button orca-button--ghost" type="button" data-orca-add-row="pe-tpl" aria-controls="pe-list">
      {% icon "plus" %}
      Add property
    </button>
  </div>
</fieldset>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Formset

```python
# videos/forms.py
from django import forms

from .models import Property, Video

PropertyFormSet = forms.inlineformset_factory(
    Video, Property, fields=["key", "value"], extra=0, can_delete=True,
)


# videos/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PropertyFormSet
from .models import Video


def edit_propertys(request, pk):
    video = get_object_or_404(Video, pk=pk)
    formset = PropertyFormSet(request.POST or None, instance=video, prefix="propertys")
    if request.method == "POST" and formset.is_valid():
        formset.save()
        return redirect("video-detail", pk=video.pk)
    # Template: {{ formset.management_form }}, one [data-orca-row] per form, and a <template id="property-row">
    # holding {{ formset.empty_form }} (its names contain __prefix__). The add-row button points at it with
    # data-orca-add-row="property-row" and data-orca-total="id_propertys-TOTAL_FORMS".
    return render(request, "videos/propertys.html", {"video": video, "formset": formset})
```

**Classes:** `.orca-property-rows`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Properties editor (key and value rows)

---

## Rich text editor

`id: rich-text-editor` · level: pattern · source: ORCA

A text area with a small formatting toolbar (bold, italic, lists, link) that saves HTML to a field.

Built from: `form-field`, `formatting-toolbar`

### General description

A text area with a small toolbar for formatting, such as bold, italic, lists and links. It produces formatted text.

#### Use cases

- Writing notes, comments or descriptions that need simple formatting.
- Composing messages with links and lists.
- Editing short content like a product description.

#### When not to use it

- For plain notes, use a normal text area.
- For long documents or code, use a dedicated editor.

#### Best practices

- Offer only the few formatting options people really need.
- Label every toolbar button and show its pressed state.
- Support common keyboard shortcuts such as Ctrl+B.
- Clean and sanitize the saved HTML on the server.
- Keep a plain text fallback when scripts do not run.

### When to use

- Notes, descriptions and messages that need simple formatting.

### When not to use

- Code or structured data; long documents (use a dedicated editor).

### How to use

- `<div class="orca-richtext" data-orca-richtext>` with `.orca-richtext__toolbar` (icon buttons `data-orca-rt="bold|italic|insertUnorderedList|insertOrderedList|createLink|removeFormat"` with `aria-pressed`), a `<div class="orca-richtext__area" contenteditable="true" role="textbox" aria-multiline="true" aria-labelledby=…>` and a hidden `<textarea name=…>` that receives the HTML.
- Always sanitize the HTML on the server (allow p, strong, em, ul, ol, li, a[href]).

### Accessibility

- The toolbar is a `role="toolbar"` with a label; buttons have names and pressed states.

#### Example: Editor

```django
<div class="orca-field" style="max-width: 36rem">
  <span class="orca-label" id="rt-label">Note</span>
  <div class="orca-richtext" data-orca-richtext>
    <div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting">
      <button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="bold" aria-pressed="false" aria-label="Bold">
        <b>B</b>
      </button>
      <button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="italic" aria-pressed="false" aria-label="Italic">
        <i>I</i>
      </button>
      <span class="orca-divider orca-divider--vertical" role="separator"></span>
      <button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="insertUnorderedList" aria-pressed="false" aria-label="Bulleted list">
        {% icon "list" %}
      </button>
      <button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="createLink" aria-label="Add link">
        {% icon "get-link" %}
      </button>
    </div>
    <div class="orca-richtext__area" contenteditable="true" role="textbox" aria-multiline="true" aria-labelledby="rt-label" data-placeholder="Write a note">
      <p>Video moved <strong>30 cm left</strong> on 3 March.</p>
    </div>
    <textarea name="note" hidden></textarea>
  </div>
</div>
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Form

```python
# videos/forms.py — the editor syncs its HTML into a hidden field; clean it before saving
import nh3   # pip install nh3

from django import forms

ALLOWED = {"p", "br", "strong", "b", "em", "i", "ul", "ol", "li", "a"}


class DescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_description(self):
        return nh3.clean(self.cleaned_data["description"], tags=ALLOWED, link_rel="noopener noreferrer")
```

**Classes:** `.orca-richtext`, `.orca-richtext__toolbar`, `.orca-richtext__area`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Rich text editor

---
