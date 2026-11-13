# Inputs

Native form controls, styled. They work with keyboards, screen readers, autofill and phones for free.

## Text input

`id: text-input` · level: primitive · source: Tangerine

A single-line field: filled, square, with a 1.5px bottom border.

### General description

A single-line box where people type short text such as a name, email address or code.

#### Use cases

- Collecting names, email addresses and phone numbers.
- Entering short codes, usernames or search terms.
- Capturing numbers with units, such as a port or a postcode.

#### When not to use it

- Long answers: use a multi-line text area instead.
- A small set of known options: use radio buttons or a select.

#### Best practices

- Give every field a visible label, not just placeholder text.
- Set the right input type so phones show a suitable keyboard.
- Turn on autofill hints for common details like name and email.
- Size the box to the expected answer length.
- Explain errors next to the field and say how to fix them.

### When to use

- Short free text: names, addresses, numbers with units, codes.

### When not to use

- Fewer than ~10 known options: use radios or a select (R11).
- Long text: use a textarea.

### How to use

- `<input class="orca-input" id=… name=… type="text">` under an `orca-label`.
- Set `type` (email, tel, url, number, password, search), `inputmode`, and `autocomplete` (name, email, one-time-code…).
- Space fields 24px apart and put each label 8px above its field, so it never looks like the previous field's caption (R10).
- Match width to the answer with `--w4`, `--w8`, `--w12`, `--w20`, `--w30` (R06); default is full width.
- Sizes: `--sm`, `--dense`, `--lg`; all reach 44px on touch.
- States: hover fill, inside focus ring, `aria-invalid="true"` (red tint + bottom border), `disabled`, `readonly` (dashed, no fill).
- Accept loose input and clean it on the server: trim spaces, ignore case, strip separators (Postel's law).

### Accessibility

- Field text is 16px on touch so iOS does not zoom.
- Never put essential instructions in `placeholder`.

#### Example: States: default, read-only, disabled

```django
<div class="orca-stack" style="max-width: 24rem; gap: var(--orca-space-24)">
  <div>
    <label class="orca-label" for="ti-1">Image name</label>
    <input class="orca-input" id="ti-1" value="Entrance A">
  </div>
  <div>
    <label class="orca-label" for="ti-2">Serial number</label>
    <input class="orca-input orca-input--w20" id="ti-2" value="DS-2CD2143G2" readonly>
  </div>
  <div>
    <label class="orca-label" for="ti-3">Port</label>
    <input class="orca-input orca-input--w8" id="ti-3" inputmode="numeric" value="554" disabled>
  </div>
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

### General description

A multi-line box for longer free text such as notes, messages or descriptions. It grows or scrolls as people type.

#### Use cases

- Comments, feedback and support messages.
- Descriptions and notes on a record.
- Pasting in longer text, such as an address list.

#### When not to use it

- Short one-line answers: use a text input.
- Rich formatting needs: use a rich text editor.

#### Best practices

- Make the box tall enough to show that a longer answer is expected.
- State any character limit and show a live count.
- Keep a visible label above the box.
- Let people resize it vertically when the layout allows.

### When to use

- Notes, descriptions, messages: anything longer than one line.

### How to use

- `<textarea class="orca-textarea" rows="4">`. Resizes vertically by default; `.orca-textarea--fixed` stops that where layout depends on it.
- For a limit, say so in the help text and show a count (`maxlength` plus a live count, phase 2).

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

### General description

A dropdown menu that lets people pick one option from a list. It saves space when the list is fairly long.

#### Use cases

- Choosing a country, state or time zone.
- Picking one value from a medium list where space is tight.
- Sorting or filtering by a single category.

#### When not to use it

- Very few options: radio buttons show all choices without a click.
- Long lists people know by name: use a search field with suggestions.

#### Best practices

- Keep options in a meaningful order, such as alphabetical or by frequency.
- Start with a clear prompt like 'Choose an option' when no default fits.
- Group long lists under headings.
- Prefer the browser's own dropdown, especially on phones.

### When to use

- One choice from 7–15 options when space is short, or options people know by name (country, timezone).

### When not to use

- Fewer than about 7 options: radios show them without a click (R11).
- Long lists people type rather than scroll: autocomplete (R12, phase 2).
- A pre-selected value that looks like an answer: start with an empty 'Choose…' option unless a default is right.

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

### General description

A list that shows several options at once and lets people select one or more. It is a plain form control with a visible list.

#### Use cases

- Picking several items from a short list in a dense admin screen.
- Assigning multiple tags or roles to a record.
- Choosing items where seeing all options at once helps.

#### When not to use it

- Most public forms: a group of checkboxes is easier to understand.
- Long lists: use a search field with multi-select suggestions.

#### Best practices

- Tell people how to select more than one item.
- Show enough rows to see most options without scrolling.
- Label the list clearly and keep options short.
- Make sure it works with the keyboard alone.

### When to use

- Picking several items from a short or medium list in a dense admin form.

### When not to use

- Most end-user forms: use a checkbox group or multi-picker, since ctrl-click is hard to discover.

### How to use

- `<select class="orca-select orca-listbox" multiple size="6">`.
- Say in the help text how to pick several: 'Hold Ctrl (Cmd on Mac) to choose more than one.'

#### Example: Listbox

```django
<label class="orca-label" for="lb-1">Albums</label>
<p class="orca-help" id="lb-1-help">Hold Ctrl (Cmd on Mac) to choose more than one.</p>
<select class="orca-select orca-listbox" id="lb-1" multiple size="4" aria-describedby="lb-1-help" style="max-width: 20rem">
  <option selected>Entrance A</option>
  <option>Entrance B</option>
  <option selected>Loading dock</option>
  <option>Car park</option>
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

### General description

A text field made for searching, usually with a magnifier icon and a button to clear what was typed.

#### Use cases

- Searching a whole site or app.
- Filtering a long list or table.
- Finding a person, product or document by name.

#### When not to use it

- Choosing from a short, fixed list: use a select or radio buttons.
- Browsing by category: use navigation or filters.

#### Best practices

- Use the familiar magnifier icon.
- Give the field an accessible name even when there is no visible label.
- Let people clear the text in one tap.
- Show results quickly and say clearly when nothing matches.

### When to use

- Filtering a list or table; searching the app.

### How to use

- Wrap: `<div class="orca-search">{% icon "search" %}<input class="orca-input" type="search" placeholder=" " aria-label=…><button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>{% icon "close" %}</button></div>`.
- Keep `placeholder` non-empty (a space is fine): the clear button hides while the placeholder shows.
- A lone search field may use placeholder text as its hint if it also has an accessible label (R09 exception).

### Accessibility

- Give the input an `aria-label` or a visually hidden label; wrap in `<form role="search">` for the main site search.

#### Example: Search with clear

```django
<form role="search" class="orca-search" style="max-width: 22rem" onsubmit="return false">
  {% icon "search" %}
  <input class="orca-input" type="search" name="q" placeholder="Search images" aria-label="Search images" value="Entrance">
  <button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>
    {% icon "close" %}
  </button>
</form>
```

**Classes:** `.orca-search`, `.orca-search__clear`

**Tokens:** `--orca-bg-input`, `--orca-text-muted`

**Principles applied:** Jakob's law: work the way products people already know work; Fitts's law: big, close, well-spaced targets are faster and safer; Practical UI R09: Persistent labels, not placeholders

**ORCA guide items covered:** Search input; Search clear button

---

## Checkbox

`id: checkbox` · level: primitive · source: Tangerine

A square tick for an on/off choice applied when the form is saved, or for one of several choices.

### General description

A small box that people tick or untick. It records a yes or no, or lets people pick any number of options.

#### Use cases

- Agreeing to terms or opting in to emails.
- Selecting several options in a form that is submitted.
- Selecting rows in a list or table.

#### When not to use it

- Settings that apply instantly: use a switch.
- Choosing exactly one option: use radio buttons.

#### Best practices

- Make the whole label clickable, not just the box.
- Word labels positively so ticking means yes.
- Group related checkboxes under a clear heading.
- Never pre-tick boxes that help the business more than the user.

### When to use

- Agreeing, opting in or picking several options in a submitted form.

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
  <label class="orca-check">
    <input type="checkbox" name="r2">
    <span class="orca-check__box"></span>
    <span class="orca-check__text">Include thumbnails<span class="orca-check__desc">Adds one image per video, about 2 MB.</span></span>
  </label>
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

A round mark for choosing exactly one of a few visible options.

### General description

A round button used in a group where only one option can be chosen at a time.

#### Use cases

- Choosing one plan, shipping method or payment type.
- Answering a question with a few clear options.
- Options that need a short description each.

#### When not to use it

- Many options: use a select or a search field.
- A single yes or no: use a checkbox or switch.

#### Best practices

- List the options vertically so they are easy to compare.
- Put the group under a clear question or heading.
- Pre-select an option only if it is a sensible default.
- Make the whole label clickable.

### When to use

- 2 to about 10 mutually exclusive options, especially when the differences need a description.

### When not to use

- Two options that are really on/off: a checkbox or switch.
- Long lists: a select or autocomplete.

### How to use

- `<label class="orca-radio"><input type="radio" name="grp" value=…><span class="orca-radio__dot"></span>Label</label>` inside a fieldset.
- Stack vertically (R01). Pre-select an option only when it is truly the right default (Hick's law; ethics of defaults).

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

### General description

A toggle that turns a setting on or off and takes effect right away, like a physical light switch.

#### Use cases

- Turning notifications or autoplay on and off.
- Enabling a feature in a settings page.
- Settings that save immediately without a Save button.

#### When not to use it

- Forms that are submitted with a button: use a checkbox.
- Choosing between more than two options: use radio buttons.

#### Best practices

- Apply the change immediately and confirm it happened.
- Label the setting itself, not the action.
- Show the on and off states with more than colour alone.
- Undo the change and explain if saving fails.

### When to use

- Settings saved at once: play videos automatically, turn notifications on.

### When not to use

- Inside forms that need a Save button: use a checkbox.

### How to use

- `<label class="orca-switch"><input type="checkbox" role="switch" checked><span class="orca-switch__track"></span><span>Autoplay videos</span></label>`.
- Save on change (htmx `hx-trigger="change"`) and confirm with a status message; revert and explain on failure.
- Name the setting, not the action ('Notifications', not 'Turn on notifications').

### Accessibility

- `role="switch"` announces on/off.

#### Example: Switches

```django
<div class="orca-stack">
  <label class="orca-switch">
    <input type="checkbox" role="switch" checked>
    <span class="orca-switch__track"></span>
    <span>Autoplay videos</span>
  </label>
  <label class="orca-switch">
    <input type="checkbox" role="switch">
    <span class="orca-switch__track"></span>
    <span>Email alerts</span>
  </label>
  <label class="orca-switch">
    <input type="checkbox" role="switch" disabled>
    <span class="orca-switch__track"></span>
    <span>Record audio</span>
  </label>
</div>
```

**Classes:** `.orca-switch`, `.orca-switch__track`

**Tokens:** `--orca-accent`, `--orca-border-strong`, `--orca-duration-brisk`

**Principles applied:** Practical UI R14: Checkbox or switch according to timing; Doherty threshold: respond within 400 ms; show progress for anything slower; Jakob's law: work the way products people already know work

**ORCA guide items covered:** Switch

---

## Number input

`id: number-input` · level: primitive · source: Tangerine

A number field with large minus and plus buttons for small adjustments.

### General description

A field for entering a number, often with plus and minus buttons for small changes.

#### Use cases

- Setting quantities, counts or limits.
- Adjusting a value up or down by small steps.
- Entering amounts with a minimum and maximum.

#### When not to use it

- Identifiers like phone, card or postcode numbers: use a text input with a numeric keyboard.
- Wide ranges: use a slider or plain typing.

#### Best practices

- Set sensible minimum, maximum and step values.
- Show the unit in the label or beside the field.
- Let people type as well as use the buttons.
- Name the buttons so screen readers say what they change.

### When to use

- Small counts and limits: capacity, retries, minutes between shots.

### When not to use

- Large changes or identifiers (phone, card, postcode): use a text input with `inputmode="numeric"`.

### How to use

- `<div class="orca-number">` with a minus `orca-icon-button` (`data-orca-step="-1"`), the `<input type="number" class="orca-input" min max step>`, and a plus button (`data-orca-step="1"`).
- Show the unit in the label or an addon ('Minutes').

### Accessibility

- Buttons need `aria-label` naming the field ('Decrease capacity'); the input keeps its own label.

#### Example: Stepper

```django
<label class="orca-label" for="cap">Zone capacity</label>
<div class="orca-number">
  <button class="orca-icon-button" type="button" aria-label="Decrease zone capacity" data-orca-step="-1">
    {% icon "minus" %}
  </button>
  <input class="orca-input" id="cap" type="number" min="0" max="999" step="1" value="40">
  <button class="orca-icon-button" type="button" aria-label="Increase zone capacity" data-orca-step="1">
    {% icon "plus" %}
  </button>
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

### General description

A control for picking a colour, usually a swatch that opens a picker plus a text box for the exact colour code.

#### Use cases

- Choosing a theme or brand colour.
- Labelling categories, calendars or zones with a colour.
- Setting a colour in a drawing or design tool.

#### When not to use it

- Picking from a few set colours: use radio buttons with swatches.
- Colour is the only way to tell options apart: add text or icons.

#### Best practices

- Show the current colour and its code together.
- Accept codes with or without the hash and in any case.
- Warn when a colour is hard to read against text.
- Offer a few preset colours for quick picks.

### When to use

- Choosing a zone, calendar or brand colour in settings.

### How to use

- `<div class="orca-color"><input type="color" id=… value="#0f95a1"><input class="orca-input" value="#0f95a1" aria-label="Hex value" pattern="#?[0-9a-fA-F]{3,6}"></div>`.
- Accept 3 or 6 digits, with or without #, any case; normalise on the server (`orca.color.normalize`).
- Warn if the colour will carry text and falls below 4.5:1 (`orca.color.contrast`).

#### Example: Colour

```django
<label class="orca-label" for="zc">Zone colour</label>
<div class="orca-color">
  <input type="color" id="zc" value="#0f95a1">
  <input class="orca-input" value="#0f95a1" aria-label="Zone colour hex value">
</div>
```

**Classes:** `.orca-color`

**Tokens:** `--orca-border-strong`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI C01: Check contrast for meaningful content

**ORCA guide items covered:** Colour input

---

## File input

`id: file-input` · level: primitive · source: Tangerine

The native file picker with an ORCA-styled button.

### General description

A control that lets people choose a file from their device to upload, such as a photo or document.

#### Use cases

- Uploading photos, avatars or scans.
- Attaching documents to a form or message.
- Importing a data file such as a spreadsheet.

#### When not to use it

- Files already stored online: let people paste a link or pick from a library.
- Typing short text: use a text input.

#### Best practices

- Say which file types and sizes are allowed before people choose.
- Check the file again on the server.
- Show the chosen file name and a way to remove it.
- Allow several files only when you can handle them.

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

### General description

A row of single-digit boxes for entering a one-time code, such as a text-message or email verification code.

#### Use cases

- Two-step sign-in codes.
- Email or phone number verification.
- Confirming a sensitive action with a short code.

#### When not to use it

- Codes with letters or more than 8 characters: use one text field.
- Long-term passwords: use a password field.

#### Best practices

- Move to the next box automatically after each digit.
- Let people paste the whole code at once.
- Allow phones to fill the code from a text message.
- Use a numeric keyboard on phones.
- Offer a way to resend the code.

### When to use

- Two-factor codes and email verification codes of 4–8 digits.

### When not to use

- Codes with letters, or longer than 8 characters: use one text input.

### How to use

- Group: `<div class="orca-row" data-orca-otp role="group" aria-labelledby=…>` with one `<input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit 1 of 6">` per digit.
- Put `autocomplete="one-time-code"` on the first box.
- orca.js moves forward on input, back on Backspace, and spreads a pasted code across the boxes.
- No-script option: a single `<input class="orca-input orca-input--w8" autocomplete="one-time-code" inputmode="numeric">`.

### Accessibility

- Each box names its position ('Digit 3 of 6').

#### Example: Six-digit code

```django
<p class="orca-label" id="otp-label">Verification code</p>
<div class="orca-row" data-orca-otp role="group" aria-labelledby="otp-label">
  {% for i in "123456" %}
    <input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit {{ i }} of 6"{% if forloop.first %} autocomplete="one-time-code"{% endif %}>
  {% endfor %}
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

### General description

A fixed piece of text or a button attached to the side of an input, such as a unit, a currency sign or a Copy button.

#### Use cases

- Showing a unit like minutes, percent or metres.
- Adding a fixed prefix like https:// or a currency sign.
- Attaching an action such as Copy or Test.

#### When not to use it

- Long explanations: put them in help text under the field.
- Actions unrelated to the field: use a separate button.

#### Best practices

- Keep the addon text very short.
- Make clear the addon is not part of what people type.
- Connect the addon text to the input for screen readers.
- Make sure attached buttons are large enough to tap.

### When to use

- Units (min, %, m²), protocols (https://), currency, an attached action (Copy, Test).

### How to use

- `<div class="orca-input-group"><span class="orca-addon">https://</span><input class="orca-input" …><span class="orca-addon">.mp4</span></div>`.
- A button suffix uses `.orca-button` inside the group.
- Link the addon text to the input with `aria-describedby` if it changes the meaning.

#### Example: Prefix and suffix

```django
<label class="orca-label" for="ig1">Thumbnail interval</label>
<div class="orca-input-group" style="max-width: 14rem">
  <input class="orca-input" id="ig1" type="number" value="5" aria-describedby="ig1-unit">
  <span class="orca-addon" id="ig1-unit">minutes</span>
</div>
<label class="orca-label" for="ig2" style="margin-top: var(--orca-space-16)">Video address</label>
<div class="orca-input-group" style="max-width: 28rem">
  <span class="orca-addon">https://</span>
  <input class="orca-input" id="ig2" value="media.example.com/v/4821">
  <button class="orca-button" type="button">Test</button>
</div>
```

**Classes:** `.orca-input-group`, `.orca-addon`

**Tokens:** `--orca-bg-alt`, `--orca-border-strong`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Practical UI F03: Reduce the total effort of a task

**ORCA guide items covered:** Input addon (prefix, suffix)

---
