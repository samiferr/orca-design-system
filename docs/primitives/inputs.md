# Inputs

Native form controls styled by ORCA. Native first: they work with keyboards, screen readers, autofill and phones for free.

## Text input

`id: text-input` · level: primitive · source: Tangerine

A single-line field: filled, square, with a 1.5px bottom border.

### Why

Native inputs with a visible boundary and a persistent label are instantly recognisable (Jakob's law, Practical UI R07, R18). The right `type`, `inputmode` and `autocomplete` let phones and browsers do the typing (Tesler's law).

### When to use

- Short free text: names, addresses, numbers with units, codes.

### When not to use

- Choosing from fewer than ~10 known options: use radios or a select (R11).
- Long text: use a textarea.

### How to use

- `<input class="orca-input" id=… name=… type="text">` under an `orca-label`.
- Set `type` (email, tel, url, number, password, search), `inputmode`, and `autocomplete` (name, email, one-time-code…).
- Space fields 24px apart and keep each label 8px above its own field, so a label never looks like the caption of the field before it (R10).
- Match width to the answer with `--w4`, `--w8`, `--w12`, `--w20`, `--w30` (R06); default is full width.
- Sizes: `--sm`, `--dense`, `--lg` (dense input), all reaching 44px on touch.
- States: hover fill, inside focus ring, `aria-invalid="true"` (red tint + bottom border), `disabled`, `readonly` (dashed, no fill).
- Accept liberal input and normalise it on the server: trim spaces, accept any case, strip separators (Postel's law).

### Accessibility

- Field text is 16px on touch so iOS does not zoom.
- Never put essential instructions in `placeholder`.

#### Example: States: default, read-only, disabled

```django
<div class="orca-stack" style="max-width: 24rem; gap: var(--orca-space-24)">
  <div><label class="orca-label" for="ti-1">Image name</label>
    <input class="orca-input" id="ti-1" value="Entrance A"></div>
  <div><label class="orca-label" for="ti-2">Serial number</label>
    <input class="orca-input orca-input--w20" id="ti-2" value="DS-2CD2143G2" readonly></div>
  <div><label class="orca-label" for="ti-3">Port</label>
    <input class="orca-input orca-input--w8" id="ti-3" inputmode="numeric" value="554" disabled></div>
</div>
```

#### Example: Sizes

```django
<div class="orca-stack" style="max-width: 24rem">
  <input class="orca-input orca-input--sm" aria-label="Small input" placeholder="Small">
  <input class="orca-input orca-input--dense" aria-label="Dense input" placeholder="Dense">
  <input class="orca-input orca-input--lg" aria-label="Large input" placeholder="Large">
</div>
```

**Classes:** `.orca-input`, `.orca-input--sm`, `.orca-input--dense`, `.orca-input--lg`, `.orca-input--w8`, `.orca-input--w30`

**Tokens:** `--orca-bg-input`, `--orca-border-strong`, `--orca-focus`, `--orca-negative-bg`, `--orca-control-md`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Tesler's law: move unavoidable complexity from the user to the system; Practical UI R06: Match input width to the expected answer; Practical UI R07: Keep recognisable control features; Practical UI R18: Keep control boundaries visible

**Related:** `label`, `help-text`, `error-text`

**ORCA guide items covered:** Text input; Dense text input; Small input; Large input

---

## Textarea

`id: textarea` · level: primitive · source: Tangerine

A multi-line field that grows vertically.

### Why

A taller box tells people a longer answer is expected (Practical UI R06).

### When to use

- Notes, descriptions, messages: anything that may run past one line.

### How to use

- `<textarea class="orca-textarea" rows="4">`. Resizable vertically by default; `.orca-textarea--fixed` stops resizing where layout depends on it.
- If there is a limit, say it in the help text and show the count (`maxlength` plus a live count, phase 2).

#### Example: Textarea

```django
<label class="orca-label" for="ta-1">Note <span class="orca-optional">(optional)</span></label>
<textarea class="orca-textarea" id="ta-1" rows="3">Mounted 3 m above the door, facing inward.</textarea>
<label class="orca-label" for="ta-2" style="margin-top: var(--orca-space-16)">Fixed size</label>
<textarea class="orca-textarea orca-textarea--fixed" id="ta-2" rows="2"></textarea>
```

**Classes:** `.orca-textarea`, `.orca-textarea--fixed`

**Tokens:** `--orca-bg-input`, `--orca-border-strong`

**Principles applied:** Practical UI R06: Match input width to the expected answer; Practical UI R08: Put essential help before the input

**ORCA guide items covered:** Textarea; Fixed-size textarea

---

## Select (native)

`id: select` · level: primitive · source: Tangerine

The browser's dropdown, styled with an ORCA chevron.

### Why

The native select works with every input method and opens the platform picker on phones (Postel's law, Jakob's law).

### When to use

- Choosing one of 7–15 options where space is short; options people know by name (country, timezone).

### When not to use

- Fewer than about 7 options: radios show the choices without a click (R11).
- Long lists people type rather than scroll: autocomplete (R12, phase 2).
- A pre-selected value that looks like an answer: start with an empty 'Choose…' option when no default is right.

### How to use

- `<select class="orca-select" id=… name=…>`. Sizes `--sm`, `--dense`, `--lg`.
- Group long lists with `<optgroup>`.
- Sort options in a meaningful order (frequency, alphabet, time).

#### Example: Select

```django
<label class="orca-label" for="sel-1">Album</label>
<select class="orca-select" id="sel-1" style="max-width: 20rem">
  <option value="">Choose an album</option>
  <option>Summer 2026</option>
  <option>Product shots</option>
</select>
```

**Classes:** `.orca-select`, `.orca-select--dense`

**Tokens:** `--orca-bg-input`, `--orca-border-strong`

**Principles applied:** Jakob's law: work the way products people already know work; Postel's law: accept varied input, output reliable and accessible UI; Practical UI R11: Visible choices for small sets; Practical UI R12: Autocomplete for long lists

**Related:** `listbox`, `timezone-select`

**ORCA guide items covered:** Select; Native select

---

## Multiple select (listbox)

`id: listbox` · level: primitive · source: Tangerine

A native `<select multiple>` showing several options at once.

### Why

A visible list keeps options in view (recognition over recall, Miller's law) and works with the keyboard natively.

### When to use

- Selecting several items from a short-to-medium list in a dense admin form.

### When not to use

- Most end-user forms: checkboxes are easier (ctrl-click is not discoverable); use a checkbox group or multi-picker.

### How to use

- `<select class="orca-select orca-listbox" multiple size="6">`.
- Say in the help text how to pick several: 'Hold Ctrl (Cmd on Mac) to choose more than one.'

#### Example: Listbox

```django
<label class="orca-label" for="lb-1">Albums</label>
<p class="orca-help" id="lb-1-help">Hold Ctrl (Cmd on Mac) to choose more than one.</p>
<select class="orca-select orca-listbox" id="lb-1" multiple size="4" aria-describedby="lb-1-help" style="max-width: 20rem">
  <option selected>Entrance A</option><option>Entrance B</option><option selected>Loading dock</option><option>Car park</option>
</select>
```

**Classes:** `.orca-listbox`

**Tokens:** `--orca-bg-input`, `--orca-bg-active`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** Multiple select (listbox)

---

## Search input

`id: search-input` · level: primitive · source: Tangerine

A text field with a magnifier and a clear button.

### Why

The magnifier is one of the few universally understood icons (Jakob's law); a clear button saves selecting and deleting text (Fitts's law).

### When to use

- Filtering a list or table; searching the app.

### How to use

- Wrap: `<div class="orca-search">{% icon "search" %}<input class="orca-input" type="search" placeholder=" " aria-label=…><button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>{% icon "close" %}</button></div>`.
- Keep `placeholder` non-empty (a space is fine): the clear button hides while the placeholder shows.
- A single search field may use placeholder text as its visible hint if it also has an accessible label (R09 exception).

### Accessibility

- Give the input an `aria-label` or a visually hidden label; wrap in `<form role="search">` for the main site search.

#### Example: Search with clear

```django
<form role="search" class="orca-search" style="max-width: 22rem" onsubmit="return false">
  {% icon "search" %}
  <input class="orca-input" type="search" name="q" placeholder="Search images" aria-label="Search images" value="Entrance">
  <button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>{% icon "close" %}</button>
</form>
```

**Classes:** `.orca-search`, `.orca-search__clear`

**Tokens:** `--orca-bg-input`, `--orca-text-muted`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI R09: Persistent labels, not placeholders

**ORCA guide items covered:** Search input; Search clear button

---

## Checkbox

`id: checkbox` · level: primitive · source: Tangerine

A square tick for an on/off choice that takes effect when the form is saved, or one of several choices.

### Why

The square box is the convention for 'any number of these' (Practical UI R07), and the whole label row is the target (Fitts's law). Checkboxes apply on submit; switches apply at once (R14).

### When to use

- Agreeing, opting in, or picking several options in a form that is submitted.

### When not to use

- Settings that apply immediately: use a switch.
- One of several mutually exclusive options: radios.

### How to use

- `<label class="orca-check"><input type="checkbox" name=…><span class="orca-check__box"></span>Email me a daily report</label>`.
- Description under the label: wrap text in `.orca-check__text` and add `.orca-check__desc`.
- Indeterminate (some children checked): set `input.indeterminate = true` in script.
- Phrase the label positively, so 'Yes' makes sense in front of it (R15).

### Accessibility

- The native input stays focusable; the ring is drawn outside the box with a gap.
- Groups use `<fieldset>` + `<legend>`.

#### Example: Checkboxes

```django
<fieldset style="border: 0; margin: 0; padding: 0" class="orca-stack">
  <legend class="orca-label">Daily report</legend>
  <label class="orca-check"><input type="checkbox" name="r" checked><span class="orca-check__box"></span>Email me a daily report</label>
  <label class="orca-check"><input type="checkbox" name="r2"><span class="orca-check__box"></span><span class="orca-check__text">Include thumbnails<span class="orca-check__desc">Adds one image per video, about 2 MB.</span></span></label>
  <label class="orca-check"><input type="checkbox" disabled><span class="orca-check__box"></span>Attach videos</label>
</fieldset>
```

**Classes:** `.orca-check`, `.orca-check__box`, `.orca-check__text`, `.orca-check__desc`

**Tokens:** `--orca-accent`, `--orca-border-strong`, `--orca-focus`

**Principles applied:** Practical UI R07: Keep recognisable control features; Practical UI R14: Checkbox or switch according to timing; Practical UI R15: Phrase binary labels positively; Fitts's law: big, close, well-spaced targets are faster and safer

**Related:** `switch`, `radio`

**ORCA guide items covered:** Checkbox

---

## Radio

`id: radio` · level: primitive · source: Tangerine

A round mark for choosing exactly one option from a small visible set.

### Why

Showing every option lets people compare without opening anything (Practical UI R11); the round mark signals 'only one' by convention (R07, Jakob's law).

### When to use

- 2 to about 10 mutually exclusive options, especially when the differences need a description.

### When not to use

- Two options that are really on/off: a checkbox or switch.
- Long lists: a select or autocomplete.

### How to use

- `<label class="orca-radio"><input type="radio" name="grp" value=…><span class="orca-radio__dot"></span>Label</label>` inside a fieldset.
- Stack vertically (R01). Pre-select the recommended option only when it is genuinely the right default (Hick's law; ethics of defaults).

### Accessibility

- Arrow keys move between radios of the same `name`.

#### Example: Radio group

```django
<fieldset style="border: 0; margin: 0; padding: 0" class="orca-stack">
  <legend class="orca-label">Thumbnail interval</legend>
  <label class="orca-radio"><input type="radio" name="interval" value="1"><span class="orca-radio__dot"></span>Every minute</label>
  <label class="orca-radio"><input type="radio" name="interval" value="5" checked><span class="orca-radio__dot"></span>Every 5 minutes (recommended)</label>
  <label class="orca-radio"><input type="radio" name="interval" value="15"><span class="orca-radio__dot"></span>Every 15 minutes</label>
</fieldset>
```

**Classes:** `.orca-radio`, `.orca-radio__dot`

**Tokens:** `--orca-accent`, `--orca-border-strong`

**Principles applied:** Practical UI R11: Visible choices for small sets; Practical UI R07: Keep recognisable control features; Hick's law: fewer, clearer choices mean faster decisions; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Radio

---

## Switch

`id: switch` · level: primitive · source: Tangerine

An on/off control that takes effect immediately.

### Why

A switch mirrors a physical switch: flipping it changes something now (Jakob's law, Practical UI R14). Immediate effect needs immediate feedback (Doherty threshold).

### When to use

- Settings saved at once: play videos automatically, turn notifications on.

### When not to use

- Inside forms that need a Save button: use a checkbox.

### How to use

- `<label class="orca-switch"><input type="checkbox" role="switch" checked><span class="orca-switch__track"></span><span>Autoplay videos</span></label>`.
- Save on change (htmx `hx-trigger="change"`) and confirm with a status message; revert and explain on failure.
- Label states what is on, not the action ('Notifications', not 'Turn on notifications').

### Accessibility

- `role="switch"` announces on/off.

#### Example: Switches

```django
<div class="orca-stack">
  <label class="orca-switch"><input type="checkbox" role="switch" checked><span class="orca-switch__track"></span><span>Autoplay videos</span></label>
  <label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>Email alerts</span></label>
  <label class="orca-switch"><input type="checkbox" role="switch" disabled><span class="orca-switch__track"></span><span>Record audio</span></label>
</div>
```

**Classes:** `.orca-switch`, `.orca-switch__track`

**Tokens:** `--orca-accent`, `--orca-border-strong`, `--orca-duration-brisk`

**Principles applied:** Practical UI R14: Checkbox or switch according to timing; Doherty threshold: respond within 400 ms; show progress for anything slower; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Switch

---

## Number input

`id: number-input` · level: primitive · source: Tangerine

A numeric field with large minus and plus buttons for small adjustments.

### Why

For small changes a stepper is faster than typing or a dropdown, and the field still accepts typing (Practical UI R13, Postel's law).

### When to use

- Small counts and limits: capacity, retries, minutes between shots.

### When not to use

- Values that change by large amounts or are identifiers (phone, card, postcode): use a text input with `inputmode="numeric"`.

### How to use

- `<div class="orca-number">` with a minus `orca-icon-button` (`data-orca-step="-1"`), the `<input type="number" class="orca-input" min max step>`, and a plus button (`data-orca-step="1"`).
- Show the unit in the label or an addon ('Minutes').

### Accessibility

- Buttons need `aria-label` naming the field ('Decrease capacity'); the input keeps its own label.

#### Example: Stepper

```django
<label class="orca-label" for="cap">Zone capacity</label>
<div class="orca-number">
  <button class="orca-icon-button" type="button" aria-label="Decrease zone capacity" data-orca-step="-1">{% icon "minus" %}</button>
  <input class="orca-input" id="cap" type="number" min="0" max="999" step="1" value="40">
  <button class="orca-icon-button" type="button" aria-label="Increase zone capacity" data-orca-step="1">{% icon "plus" %}</button>
</div>
```

**Classes:** `.orca-number`

**Tokens:** `--orca-control-md`

**Principles applied:** Practical UI R13: Steppers for small numeric changes; Postel's law: accept varied input, output reliable and accessible UI; Fitts's law: big, close, well-spaced targets are faster and safer

**ORCA guide items covered:** Number input

---

## Colour input

`id: color-input` · level: primitive · source: ORCA

A native colour picker paired with its hex value.

### Why

The swatch gives a quick visual pick; the hex field lets people paste an exact brand value (Postel's law).

### When to use

- Choosing a zone colour, a calendar colour, a brand colour in settings.

### How to use

- `<div class="orca-color"><input type="color" id=… value="#0f95a1"><input class="orca-input" value="#0f95a1" aria-label="Hex value" pattern="#?[0-9a-fA-F]{3,6}"></div>`.
- Accept 3 or 6 digits, with or without #, any case; normalise on the server (`orca.color.normalize`).
- Warn if the colour will carry text and falls below 4.5:1 (`orca.color.contrast`).

#### Example: Colour

```django
<label class="orca-label" for="zc">Zone colour</label>
<div class="orca-color"><input type="color" id="zc" value="#0f95a1"><input class="orca-input" value="#0f95a1" aria-label="Zone colour hex value"></div>
```

**Classes:** `.orca-color`

**Tokens:** `--orca-border-strong`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI C01: Check contrast for meaningful content

**ORCA guide items covered:** Colour input

---

## File input

`id: file-input` · level: primitive · source: Tangerine

The native file picker with an ORCA-styled button.

### Why

The native control works with drag-and-drop, taking a photo on phones and assistive technology (Postel's law).

### When to use

- Uploading images, CSV files, licences.

### How to use

- `<input class="orca-file" type="file" id=… accept="image/*">`.
- State accepted types and the size limit in help text before the field; validate again on the server.
- Multiple: add `multiple`.

#### Example: File

```django
<label class="orca-label" for="fi">Floor plan</label>
<p class="orca-help" id="fi-help">PNG or JPG, up to 10 MB.</p>
<input class="orca-file" type="file" id="fi" accept="image/png,image/jpeg" aria-describedby="fi-help">
```

**Classes:** `.orca-file`

**Tokens:** `--orca-border-strong`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI R08: Put essential help before the input

**ORCA guide items covered:** File input

---

## OTP digit box

`id: otp-digit` · level: primitive · source: ORCA

One box per digit of a one-time code, with auto-advance and paste.

### Why

Separate boxes chunk the code (Miller's law) and show its length; accepting a pasted code and the SMS autofill removes typing entirely (Tesler's law, Postel's law).

### When to use

- Two-factor codes and email verification codes of 4–8 digits.

### When not to use

- Codes with letters, or longer than 8 characters: use one text input.

### How to use

- Group: `<div class="orca-row" data-orca-otp role="group" aria-labelledby=…>` with one `<input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit 1 of 6">` per digit.
- Put `autocomplete="one-time-code"` on the first box.
- orca.js advances on input, goes back on Backspace and spreads a pasted code across the boxes.
- Alternative with zero script: a single `<input class="orca-input orca-input--w8" autocomplete="one-time-code" inputmode="numeric">`.

### Accessibility

- Each box names its position ('Digit 3 of 6').

#### Example: Six-digit code

```django
<p class="orca-label" id="otp-label">Verification code</p>
<div class="orca-row" data-orca-otp role="group" aria-labelledby="otp-label">
  {% for i in "123456" %}<input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit {{ i }} of 6"{% if forloop.first %} autocomplete="one-time-code"{% endif %}>{% endfor %}
</div>
```

**Classes:** `.orca-otp-digit`

**Tokens:** `--orca-font-mono`

**Principles applied:** Miller's law: chunk information so working memory is not overloaded; Tesler's law: move unavoidable complexity from the user to the system; Postel's law: accept varied input, output reliable and accessible UI

**ORCA guide items covered:** OTP digit box

---

## Input addon (prefix, suffix)

`id: input-addon` · level: primitive · source: Tangerine

A fixed unit, prefix or button joined to an input.

### Why

Showing the unit beside the value removes guessing ('minutes or seconds?') and stops people typing the unit (Postel's law, Practical UI F03).

### When to use

- Units (min, %, m²), protocols (https://), currency, an attached action (Copy, Test).

### How to use

- `<div class="orca-input-group"><span class="orca-addon">https://</span><input class="orca-input" …><span class="orca-addon">.mp4</span></div>`.
- A button suffix uses `.orca-button` inside the group.
- Link the addon text to the input with `aria-describedby` if it changes the meaning.

#### Example: Prefix and suffix

```django
<label class="orca-label" for="ig1">Thumbnail interval</label>
<div class="orca-input-group" style="max-width: 14rem"><input class="orca-input" id="ig1" type="number" value="5" aria-describedby="ig1-unit"><span class="orca-addon" id="ig1-unit">minutes</span></div>
<label class="orca-label" for="ig2" style="margin-top: var(--orca-space-16)">Video address</label>
<div class="orca-input-group" style="max-width: 28rem"><span class="orca-addon">https://</span><input class="orca-input" id="ig2" value="media.example.com/v/4821"><button class="orca-button" type="button">Test</button></div>
```

**Classes:** `.orca-input-group`, `.orca-addon`

**Tokens:** `--orca-bg-alt`, `--orca-border-strong`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI F03: Reduce the total effort of a task

**ORCA guide items covered:** Input addon (prefix, suffix)

---
