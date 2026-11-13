# Form text

The words around a field: its label, requirement marker, help and errors. They decide whether a form is completed.

## Label

`id: label` · level: primitive · source: Tangerine

A visible, persistent name above every field.

### When to use

- Every input, select, textarea and group of ticks (use `<legend>` for groups).

### When not to use

- Placeholder text as the only label.
- 'My' or 'Your' in labels (W09): 'Email', not 'Your email'.
- Labels to the left of fields in a separate column.

### How to use

- `<label class="orca-label" for="id">` directly above the control; 8px gap (`--orca-space-8`).
- Short noun phrase, sentence case, no colon.
- Group of ticks or radios: `<fieldset>` with `<legend class="orca-label">`.

### Accessibility

- `for` must match the input `id`; the accessible name of the field is the label text.

#### Example: Label and input

```django
<label class="orca-label" for="image-name">Image name</label>
<input class="orca-input orca-input--w30" id="image-name" name="name" autocomplete="off">
```

**Classes:** `.orca-label`

**Tokens:** `--orca-type-body`, `--orca-space-8`

**Principles applied:** Practical UI R01: Keep the main form flow in one column; Practical UI R09: Persistent labels, not placeholders; Practical UI R10: Keep labels close to their inputs; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `text-input`, `required-marker`, `help-text`

**ORCA guide items covered:** Label

---

## Required marker

`id: required-marker` · level: primitive · source: Tangerine

The word 'required' or 'optional' after a label.

### When to use

- Mark optional fields when most are required; mark required ones when most are optional. Mark both in long or unfamiliar forms.

### When not to use

- A red asterisk.
- 'All fields are required' notices people skip.

### How to use

- Inside the label: `<span class="orca-optional">(optional)</span>` or `<span class="orca-required">(required)</span>`.
- Always also set the `required` attribute on required controls.

### Accessibility

- `required` exposes the status to assistive technology; the word makes it visible.

#### Example: Optional field

```django
<label class="orca-label" for="image-note">Note <span class="orca-optional">(optional)</span></label>
<input class="orca-input" id="image-note" name="note">
```

**Classes:** `.orca-required`, `.orca-optional`

**Tokens:** `--orca-text-muted`

**Principles applied:** Practical UI R03: Label optional information; Practical UI R05: Make requirement status clear; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Required marker

---

## Help text

`id: help-text` · level: primitive · source: Tangerine

A hint between the label and the field that helps people answer correctly.

### When to use

- Format expectations ('Use the address from the video's Share menu'), consequences, or where to find a value.

### When not to use

- Repeating the label.
- Essential information hidden in a tooltip.
- More than two short sentences.

### How to use

- `<p class="orca-help" id="x-help">` after the label, before the field.
- Link it: `aria-describedby="x-help"` on the input.

### Accessibility

- `aria-describedby` makes screen readers read the hint after the label.

#### Example: Hint before the field

```django
<label class="orca-label" for="video-url">Video address</label>
<p class="orca-help" id="video-url-help">Starts with https://. Copy it from the video's Share menu.</p>
<input class="orca-input" id="video-url" name="video_url" inputmode="url" aria-describedby="video-url-help">
```

**Classes:** `.orca-help`

**Tokens:** `--orca-type-detail`, `--orca-text-muted`

**Principles applied:** Practical UI R08: Put essential help before the input; Peak–end rule: people judge an experience by its peak and its end; Tesler's law: move unavoidable complexity from the user to the system

**ORCA guide items covered:** Help text

---

## Error text

`id: error-text` · level: primitive · source: Tangerine

A message above the field that says what is wrong and how to fix it.

### When to use

- After submit or after leaving a field with an invalid value.

### When not to use

- 'Invalid input', 'Error', or technical codes.
- Showing errors while the person is still typing a first answer (R22).

### How to use

- `<p class="orca-error" id="x-error">{% icon "error" %}<span>Enter a video address that starts with https://</span></p>` above the input, after the help text.
- Mark the field `aria-invalid="true"` and add the error id to `aria-describedby` (first).
- Pattern: what is wrong + how to fix, in one sentence.

### Accessibility

- The icon is decorative; the text carries the meaning.
- Move focus to the error summary or first invalid field after submit.

#### Example: Invalid field

```django
<label class="orca-label" for="video-url2">Video address</label>
<p class="orca-error" id="video-url2-error">
  {% icon "error" %}
  <span>Enter an address that starts with https://, for example https://media.example.com/v/4821.</span>
</p>
<input class="orca-input" id="video-url2" name="video_url" value="media.example.com/v/4821" aria-invalid="true" aria-describedby="video-url2-error">
```

**Classes:** `.orca-error`

**Tokens:** `--orca-negative`, `--orca-type-detail`

**Principles applied:** Practical UI R20: Submit-time validation with an error summary; Practical UI W15: Help people recover from errors; Practical UI C03: Communicate meaning beyond colour; Postel's law: accept varied input, output reliable and accessible UI

**Related:** `error-list`

**ORCA guide items covered:** Error text

---

## Help icon

`id: help-icon` · level: primitive · source: ORCA

A question-mark button that reveals optional, extra explanation in place.

### When to use

- Background for experts: how a KPI is computed, what a technical term means.

### When not to use

- Essential instructions: use help text (R08).
- Hover-only tooltips: they fail on touch and keyboard (B07).

### How to use

- Use a native disclosure: `<details class="orca-help-toggle"><summary aria-label="About dwell time">{% icon "help" %}</summary><span class="orca-help-toggle__text">…</span></details>`.
- Place it right after the label text.

### Accessibility

- `<summary>` is keyboard reachable and announces expanded/collapsed; the aria-label names the topic.

#### Example: Help disclosure

```django
<div>
  <span class="orca-label" style="display: inline">Dwell time</span>
  <details class="orca-help-toggle">
    <summary aria-label="About dwell time">
      {% icon "help" %}
    </summary>
    <span class="orca-help-toggle__text">The average time between a person entering and leaving the zone, in minutes.</span>
  </details>
</div>
```

**Classes:** `.orca-help-toggle`, `.orca-help-toggle__text`

**Principles applied:** Practical UI S04: Reveal secondary information when needed; Tesler's law: move unavoidable complexity from the user to the system; Practical UI B07: Explain necessary disabled states

**ORCA guide items covered:** Help icon

---

## Error list

`id: error-list` · level: primitive · source: Tangerine

An error summary at the top of a form, linking to each invalid field.

### When to use

- After a submit that failed on two or more fields, or on a non-field (form-wide) error.

### How to use

- Render above the form: `<div class="orca-error-list" role="alert" tabindex="-1">` with the error icon, a title stating the count ('2 fields need attention'), and a `<ul>` of links to `#field-id`.
- Move focus to it after the failed submit.
- Repeat each message at its field (error-text).

### Accessibility

- `role="alert"` announces it; `tabindex="-1"` lets you focus it programmatically.

#### Example: Error summary

```django
<div class="orca-error-list" role="alert" tabindex="-1">
  {% icon "error" %}
  <p class="orca-error-list__title">2 fields need attention</p>
  <ul>
    <li>
      <a href="#video-url2">Enter a video address that starts with https://</a>
    </li>
    <li>
      <a href="#image-name">Enter an image name</a>
    </li>
  </ul>
</div>
```

**Classes:** `.orca-error-list`, `.orca-error-list__title`

**Tokens:** `--orca-negative`

**Principles applied:** Practical UI R20: Submit-time validation with an error summary; Practical UI W15: Help people recover from errors; Peak–end rule: people judge an experience by its peak and its end

**Related:** `error-text`

**ORCA guide items covered:** Error list

---
