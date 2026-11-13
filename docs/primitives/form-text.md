# Form text

The words around a field: label, requirement marker, help and errors. They decide whether people finish a form.

## Label

`id: label` · level: primitive · source: Tangerine

A name that stays visible above every field.

### General description

A short text above or beside a form field that names what to enter. It tells people and assistive technology what the field is for.

#### Use cases

- Naming every text field, select and text area.
- Titling a group of options with a legend.
- Giving a clear click target that focuses the field.

#### When not to use it

- Using placeholder text as the only name; it disappears while typing.
- Vague words like 'Info'; use specific names.

#### Best practices

- Place the label above the field and keep it visible.
- Use short nouns in sentence case.
- Connect the label to its field in the code.
- Avoid colons and unneeded words like 'Your'.

### When to use

- Every input, select, textarea and group of ticks (use `<legend>` for groups).

### When not to use

- Placeholder text as the only label.
- 'My' or 'Your' in labels (W09): 'Email', not 'Your email'.
- Labels in a separate column left of the field.

### How to use

- `<label class="orca-label" for="id">` directly above the control; 8px gap (`--orca-space-8`).
- Short noun phrase, sentence case, no colon.
- Group of ticks or radios: `<fieldset>` with `<legend class="orca-label">`.

### Accessibility

- `for` must match the input `id`, so the label text becomes the field's accessible name.

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

### General description

A short note beside a label, such as '(required)' or '(optional)', that tells people whether they must fill in a field.

#### Use cases

- Marking optional fields in a mostly required form.
- Marking required fields in a mostly optional form.
- Long or unfamiliar forms where both states help.

#### When not to use it

- Using only a red asterisk; it can look like an error and may be missed.
- A general 'all fields required' notice that people skip.

#### Best practices

- Use words rather than symbols alone.
- Mark whichever kind of field is rarer.
- Also set the required attribute so assistive technology knows.
- Keep the marker beside the label, not in the field.

### When to use

- Mark whichever kind is rarer; mark both in long or unfamiliar forms.

### When not to use

- A red asterisk.
- 'All fields are required' notices people skip.

### How to use

- Inside the label: `<span class="orca-optional">(optional)</span>` or `<span class="orca-required">(required)</span>`.
- Also set the `required` attribute on required controls.

### Accessibility

- `required` tells assistive technology; the word shows it to everyone.

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

A hint between label and field that helps people answer correctly.

### General description

A short hint placed with a field that explains what to enter, such as a format or where to find the value. It helps people get it right the first time.

#### Use cases

- Showing the expected format, such as a date or address.
- Explaining what a choice will cause.
- Telling people where to find a number or code.

#### When not to use it

- Repeating the label; cut it instead.
- Long instructions; link to a help page.
- Hiding essential information in a tooltip.

#### Best practices

- Keep it to one or two short sentences.
- Place it between the label and the field.
- Link it to the field so screen readers read it.
- Use it to prevent errors, not explain them afterwards.

### When to use

- Expected format ('Use the address from the video's Share menu'), consequences, or where to find a value.

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

### General description

A message beside a field that says what is wrong and how to fix it. It helps people correct a mistake and continue.

#### Use cases

- Telling someone a value has the wrong format.
- Pointing out a missing required answer.
- Explaining why a value was rejected, such as a duplicate.

#### When not to use it

- Vague messages like 'Invalid input'; say what is wrong.
- Showing errors while someone is still typing their first answer; wait until they leave the field.

#### Best practices

- Write one sentence: what is wrong and how to fix it.
- Place it next to the field it belongs to.
- Use an icon and words, not colour alone.
- Link it to the field and mark the field as invalid.

### When to use

- After submit or after leaving a field with an invalid value.

### When not to use

- 'Invalid input', 'Error', or technical codes.
- Errors while the person is still typing a first answer (R22).

### How to use

- `<p class="orca-error" id="x-error">{% icon "error" %}<span>Enter a video address that starts with https://</span></p>` above the input, after the help text.
- Mark the field `aria-invalid="true"` and add the error id to `aria-describedby` (first).
- One sentence: what is wrong and how to fix it.

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

A question-mark button that reveals extra explanation in place.

### General description

A small question-mark button that reveals extra explanation on demand. It keeps background information out of the way until someone wants it.

#### Use cases

- Explaining a technical term or how a figure is calculated.
- Giving extra context in a dense form or report.
- Offering background that experts may want.

#### When not to use it

- Essential instructions; show them as visible help text.
- Hover-only tooltips; they fail on touch and for keyboard users.

#### Best practices

- Open it with a click or tap, as well as the keyboard.
- Give the button a name that says the topic.
- Keep the explanation brief.
- Place it right after the text it explains.

### When to use

- Background for experts: how a KPI is computed, what a technical term means.

### When not to use

- Essential instructions: use help text (R08).
- Hover-only tooltips: they fail on touch and keyboard (B07).

### How to use

- Use a native disclosure: `<details class="orca-help-toggle"><summary aria-label="About dwell time">{% icon "help" %}</summary><span class="orca-help-toggle__text">…</span></details>`.
- Place it right after the label text.

### Accessibility

- `<summary>` works with the keyboard and announces expanded or collapsed; the aria-label names the topic.

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

### General description

A summary at the top of a form that lists every problem and links to each field. It gives people one place to start fixing things.

#### Use cases

- Showing several problems after a failed submit.
- Reporting an error that applies to the whole form.
- Helping screen reader users find all the problems.

#### When not to use it

- A single field error; show a message beside the field.
- Warnings or tips that do not block submitting; use inline messages.

#### Best practices

- State the number of problems in the title.
- Make each item a link to its field.
- Move focus to the summary after a failed submit.
- Repeat each message beside its field.

### When to use

- After a failed submit with two or more invalid fields, or a form-wide error.

### How to use

- Render above the form: `<div class="orca-error-list" role="alert" tabindex="-1">` with the error icon, a title with the count ('2 fields need attention') and a `<ul>` of links to `#field-id`.
- Move focus to it after the failed submit.
- Repeat each message at its field (error-text).

### Accessibility

- `role="alert"` announces it; `tabindex="-1"` lets code move focus to it.

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
