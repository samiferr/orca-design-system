# Forms

Whole form sections and specialised editors: sections, stacks, sign-in, schedules, zones, properties and rich text.

## Form section

`id: form-section` · level: pattern · source: Tangerine

A titled group of related fields with a short explanation beside them.

Built from: `form-field`, `section-heading`

### Why

Grouping long forms under descriptive headings makes them feel shorter and easier to scan (Practical UI R17, Miller's law); the explanation sits where it is needed (Tesler's law).

### When to use

- Settings pages and long single-page forms.

### How to use

- `<section class="orca-form-section">` with `.orca-form-section__intro` (section title + one-sentence description) and `.orca-form-section__fields` (form fields).
- The intro sits beside the fields from 1036px and above them below.

#### Example: Section

```django
<section class="orca-form-section" aria-labelledby="fs-t">
  <div class="orca-form-section__intro"><h2 class="orca-section-title" id="fs-t">Counting</h2><p>How often thumbnails are taken and how long videos are kept.</p></div>
  <div class="orca-form-section__fields">
    <div class="orca-field"><label class="orca-label" for="fs-int">Snapshot interval</label><div class="orca-input-group" style="max-width: 12rem"><input class="orca-input" id="fs-int" type="number" value="5" aria-describedby="fs-int-u"><span class="orca-addon" id="fs-int-u">minutes</span></div></div>
    <div class="orca-field"><label class="orca-label" for="fs-ret">Keep counts for</label><select class="orca-select" id="fs-ret" style="max-width: 16rem"><option>1 year</option><option selected>2 years</option></select></div>
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

### Why

One column gives one reading path and no zigzag (Practical UI R01); two columns are allowed only for short pairs people read together, such as start and end.

### When to use

- One column: almost every form.
- Two columns (compact): dense admin forms with many short fields.

### How to use

- `<div class="orca-form-stack">` of fields (24px apart, max 36rem).
- Compact: `orca-form-stack--two`; a field that needs the full width gets `.orca-span-2`. On phones it falls back to one column.

#### Example: One column and two columns

```django
<div class="orca-stack" style="gap: var(--orca-space-32)">
  <div class="orca-form-stack"><div class="orca-field"><label class="orca-label" for="fst-1">Video name</label><input class="orca-input" id="fst-1"></div><div class="orca-field"><label class="orca-label" for="fst-2">Stream address</label><input class="orca-input" id="fst-2"></div></div>
  <div class="orca-form-stack orca-form-stack--two"><div class="orca-field"><label class="orca-label" for="fst-3">Host</label><input class="orca-input" id="fst-3"></div><div class="orca-field"><label class="orca-label" for="fst-4">Port</label><input class="orca-input orca-input--w8" id="fst-4" inputmode="numeric"></div>
    <div class="orca-field orca-span-2"><label class="orca-label" for="fst-5">Notes <span class="orca-optional">(optional)</span></label><textarea class="orca-textarea" id="fst-5" rows="2"></textarea></div></div>
</div>
```

**Classes:** `.orca-form-stack`, `.orca-form-stack--two`, `.orca-span-2`

**Principles applied:** Practical UI R01: Keep the main form flow in one column; Practical UI R10: Keep labels close to their inputs; Miller's law: chunk information so working memory is not overloaded

**ORCA guide items covered:** Form stack (one column); Form stack (compact, two columns)

---

## Schedule editor

`id: schedule-editor` · level: pattern · source: Tangerine

A weekly schedule made of rows (day, start, end), with presets, add and remove, and overlap checks.

Built from: `add-row-button`, `overlap-warning`, `preset-buttons`

### Why

Schedules vary day by day; rows handle every shape without special fields (Tesler's law) and checking overlaps as people edit prevents a broken schedule (Peak–end rule, Practical UI R21).

### When to use

- Capture schedules, opening hours, alert quiet hours.

### How to use

- A form section containing preset buttons, the schedule rows (`<div class="orca-schedule" id=…>`), an add-row button with its `<template>`, and overlap warnings inside invalid rows.
- Django: a formset; the template uses `__prefix__` and `data-orca-total` points at TOTAL_FORMS.

#### Example: Capture schedule

```django
<fieldset class="orca-choice-group" style="max-width: 40rem"><legend class="orca-label">Capture schedule</legend>
  <div class="orca-presets" role="group" aria-label="Presets"><button class="orca-tag" type="button" aria-pressed="true">Opening hours</button><button class="orca-tag" type="button" aria-pressed="false">Around the clock</button></div>
  <div class="orca-schedule" id="se-rows">
    <div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day"><option>Weekdays</option><option>Saturday</option></select><input class="orca-input" type="time" value="08:00" aria-label="From"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="19:00" aria-label="To"><button class="orca-icon-button" type="button" aria-label="Remove weekdays 08:00 to 19:00" data-orca-remove-row>{% icon "delete" %}</button></div>
    <div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day"><option>Weekdays</option><option selected>Saturday</option></select><input class="orca-input" type="time" value="09:00" aria-label="From"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" value="18:00" aria-label="To"><button class="orca-icon-button" type="button" aria-label="Remove Saturday 09:00 to 18:00" data-orca-remove-row>{% icon "delete" %}</button></div>
  </div>
  <template id="se-tpl"><div class="orca-schedule-row" data-orca-row><select class="orca-select" aria-label="Day"><option>Weekdays</option><option>Saturday</option><option>Sunday</option></select><input class="orca-input" type="time" aria-label="From"><span class="orca-schedule-row__sep" aria-hidden="true">–</span><input class="orca-input" type="time" aria-label="To"><button class="orca-icon-button" type="button" aria-label="Remove row" data-orca-remove-row>{% icon "delete" %}</button></div></template>
  <div><button class="orca-button orca-button--ghost" type="button" data-orca-add-row="se-tpl" aria-controls="se-rows">{% icon "plus" %}Add hours</button></div>
</fieldset>
```

**Classes:** `.orca-schedule`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Peak–end rule: people judge an experience by its peak and its end; Practical UI R21: Validate after leaving a field when context matters

**ORCA guide items covered:** Schedule editor

---

## Zone/line editor

`id: zone-editor` · level: pattern · source: Tangerine

Draw a counting zone on the video image by clicking its corners, with a list of zones beside it.

Built from: `zone-row`, `captioned-media`

### Why

Zones are spatial, so they are drawn where they apply (Practical UI F03: direct manipulation); undo, clear and a status line make mistakes cheap, and coordinates are saved as plain data the server validates (Postel's law).

### When to use

- Defining counting zones, lines and excluded areas on a video view.

### How to use

- `<div class="orca-zone-editor" data-orca-zone-editor>` with `.orca-zone-editor__stage` (the snapshot image + an empty `<svg viewBox="0 0 100 100" preserveAspectRatio="none">`), a toolbar (`data-orca-zone-action="undo|clear|close"`), a status line (`data-orca-zone-status`, polite) and a hidden input receiving the points as JSON percentages.
- Beside it: the zone rows. Offer a coordinates form as the keyboard alternative.

### Accessibility

- Drawing needs a pointer; provide numeric corner fields for keyboard and screen-reader users.

#### Example: Draw a zone

```django
<div class="orca-zone-editor" data-orca-zone-editor>
  <div><div class="orca-zone-editor__stage" style="--orca-zone: var(--orca-teal-400)"><img src="{% static "orca/img/sample-street.svg" %}" alt="Entrance A video view"><svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"></svg></div>
    <input type="hidden" name="points" value="[[30,62],[62,60],[66,92],[26,94]]">
    <div class="orca-zone-editor__toolbar"><button class="orca-button orca-button--dense" type="button" data-orca-zone-action="close">Close shape</button><button class="orca-button orca-button--dense" type="button" data-orca-zone-action="undo">{% icon "rotate-left" %}Undo point</button><button class="orca-button orca-button--ghost orca-button--dense" type="button" data-orca-zone-action="clear">Clear</button></div>
    <p class="orca-zone-editor__hint" data-orca-zone-status aria-live="polite"></p></div>
  <div><p class="orca-panel-title">Zones</p><div class="orca-zone-row"><span class="orca-zone-swatch" style="--orca-zone: var(--orca-teal-400)"></span><span class="orca-zone-row__name">Door line</span><span class="orca-zone-row__count orca-num">4 points</span><span></span></div></div>
</div>
```

**Classes:** `.orca-zone-editor`, `.orca-zone-editor__stage`, `.orca-zone-editor__toolbar`, `.orca-zone-editor__hint`

**Principles applied:** Practical UI F03: Reduce the total effort of a task; Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end

**ORCA guide items covered:** Zone/line editor

---

## Login card

`id: login-card` · level: pattern · source: Tangerine

The sign-in form: logo, title, email, password, remember me, the sign-in button and recovery link.

Built from: `logo-link`, `form-field`, `toggle-field`, `form-actions`, `form-alert`

### Why

Sign-in is the first step every day; a familiar layout (Jakob's law), browser autofill and clear errors make it fast, and an error that never says which field was wrong protects accounts (Postel's law, security).

### When to use

- Sign-in pages (with the auth layout).

### How to use

- `<form class="orca-login" method="post">` with the logo, `h1.orca-login__title`, a form alert for failures, email (`autocomplete="username"`) and password (`autocomplete="current-password"`) fields, `.orca-login__row` (remember me + 'Forgot your password?'), a full-width primary button and `.orca-login__foot`.
- Error: 'Email or password is incorrect. Check both, or reset your password.'

#### Example: Sign in

```django
<form class="orca-login" method="post" action="#" onsubmit="return false">
  <div class="orca-login__head">{% orca_logo href="" %}<h1 class="orca-login__title">Sign in</h1></div>
  <div class="orca-callout orca-callout--negative" role="alert">{% icon "error" %}<p class="orca-callout__title">Email or password is incorrect</p><p class="orca-callout__body">Check both, or reset your password.</p></div>
  <div class="orca-field"><label class="orca-label" for="lg-email">Email</label><input class="orca-input" id="lg-email" type="email" autocomplete="username" value="ada@acme.com"></div>
  <div class="orca-field"><label class="orca-label" for="lg-pw">Password</label><input class="orca-input" id="lg-pw" type="password" autocomplete="current-password"></div>
  <div class="orca-login__row"><label class="orca-check"><input type="checkbox"><span class="orca-check__box"></span>Keep me signed in</label><a class="orca-link orca-small" href="#">Forgot your password?</a></div>
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

### Why

Free-form data needs structure without a fixed schema (Tesler's law); one row per pair, validated per row, keeps it forgiving and readable (Postel's law).

### When to use

- Custom properties, labels, headers, metadata on records.

### How to use

- A fieldset with a legend and help, the property rows, an add-row button and its template.
- Reject duplicate keys with an error on the second row; trim spaces silently.

#### Example: Properties

```django
<fieldset class="orca-choice-group" style="max-width: 40rem"><legend class="orca-label">Properties</legend><p class="orca-help">Extra details shown on reports. Keys must be unique.</p>
  <div class="orca-property-rows" id="pe-list">
    <div class="orca-property-row" data-orca-row><div><label class="orca-label" for="pe-k0">Key</label><input class="orca-input" id="pe-k0" value="cost-centre"></div><div><label class="orca-label" for="pe-v0">Value</label><input class="orca-input" id="pe-v0" value="NB-OPS"></div><button class="orca-icon-button" type="button" aria-label="Remove property cost-centre" data-orca-remove-row>{% icon "delete" %}</button></div>
  </div>
  <template id="pe-tpl"><div class="orca-property-row" data-orca-row><div><label class="orca-label" for="pe-k__prefix__">Key</label><input class="orca-input" id="pe-k__prefix__"></div><div><label class="orca-label" for="pe-v__prefix__">Value</label><input class="orca-input" id="pe-v__prefix__"></div><button class="orca-icon-button" type="button" aria-label="Remove property" data-orca-remove-row>{% icon "delete" %}</button></div></template>
  <div><button class="orca-button orca-button--ghost" type="button" data-orca-add-row="pe-tpl" aria-controls="pe-list">{% icon "plus" %}Add property</button></div>
</fieldset>
```

**Classes:** `.orca-property-rows`

**Principles applied:** Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Properties editor (key and value rows)

---

## Rich text editor

`id: rich-text-editor` · level: pattern · source: ORCA

A text area with a small formatting toolbar (bold, italic, lists, link) that saves HTML to a field.

Built from: `form-field`, `formatting-toolbar`

### Why

A few familiar formatting buttons cover most needs (Hick's law, Jakob's law); keeping a plain textarea underneath means the form still works without script (Postel's law).

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
<div class="orca-field" style="max-width: 36rem"><span class="orca-label" id="rt-label">Note</span>
<div class="orca-richtext" data-orca-richtext>
  <div class="orca-richtext__toolbar" role="toolbar" aria-label="Formatting"><button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="bold" aria-pressed="false" aria-label="Bold"><b>B</b></button><button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="italic" aria-pressed="false" aria-label="Italic"><i>I</i></button><span class="orca-divider orca-divider--vertical" role="separator"></span><button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="insertUnorderedList" aria-pressed="false" aria-label="Bulleted list">{% icon "list" %}</button><button class="orca-icon-button orca-icon-button--dense" type="button" data-orca-rt="createLink" aria-label="Add link">{% icon "get-link" %}</button></div>
  <div class="orca-richtext__area" contenteditable="true" role="textbox" aria-multiline="true" aria-labelledby="rt-label" data-placeholder="Write a note"><p>Video moved <strong>30 cm left</strong> on 3 March.</p></div>
  <textarea name="note" hidden></textarea>
</div></div>
```

**Classes:** `.orca-richtext`, `.orca-richtext__toolbar`, `.orca-richtext__area`

**Principles applied:** Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Rich text editor

---
