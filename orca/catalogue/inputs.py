from .registry import Element, add, category

C = category(
    "inputs", "Inputs",
    "Native form controls styled by ORCA. Native first: they work with keyboards, screen readers, autofill and phones for free.",
)

add(Element(
    "text-input", "Text input", C,
    "A single-line field: filled, square, with a 1.5px bottom border.",
    why="Native inputs with a visible boundary and a persistent label are instantly recognisable (Jakob's law, "
        "Practical UI R07, R18). The right `type`, `inputmode` and `autocomplete` let phones and browsers do the typing (Tesler's law).",
    when=["Short free text: names, addresses, numbers with units, codes."],
    avoid=["Choosing from fewer than ~10 known options: use radios or a select (R11).", "Long text: use a textarea."],
    how=["`<input class=\"orca-input\" id=… name=… type=\"text\">` under an `orca-label`.",
         "Set `type` (email, tel, url, number, password, search), `inputmode`, and `autocomplete` (name, email, one-time-code…).",
         "Space fields 24px apart and keep each label 8px above its own field, so a label never looks like the caption of the field before it (R10).",
         "Match width to the answer with `--w4`, `--w8`, `--w12`, `--w20`, `--w30` (R06); default is full width.",
         "Sizes: `--sm`, `--dense`, `--lg` (dense input), all reaching 44px on touch.",
         "States: hover fill, inside focus ring, `aria-invalid=\"true\"` (red tint + bottom border), `disabled`, `readonly` (dashed, no fill).",
         "Accept liberal input and normalise it on the server: trim spaces, accept any case, strip separators (Postel's law)."],
    a11y=["Field text is 16px on touch so iOS does not zoom.", "Never put essential instructions in `placeholder`."],
    classes=[".orca-input", ".orca-input--sm", ".orca-input--dense", ".orca-input--lg", ".orca-input--w8", ".orca-input--w30"],
    tokens=["bg-input", "border-strong", "focus", "negative-bg", "control-md"],
    laws=["jakob", "postel", "tesler", "R06", "R07", "R18"],
    examples=[
        ("States: default, read-only, disabled", """<div class="orca-stack" style="max-width: 24rem; gap: var(--orca-space-24)">
  <div><label class="orca-label" for="ti-1">Image name</label>
    <input class="orca-input" id="ti-1" value="Entrance A"></div>
  <div><label class="orca-label" for="ti-2">Serial number</label>
    <input class="orca-input orca-input--w20" id="ti-2" value="DS-2CD2143G2" readonly></div>
  <div><label class="orca-label" for="ti-3">Port</label>
    <input class="orca-input orca-input--w8" id="ti-3" inputmode="numeric" value="554" disabled></div>
</div>"""),
        ("Sizes", """<div class="orca-stack" style="max-width: 24rem">
  <input class="orca-input orca-input--sm" aria-label="Small input" placeholder="Small">
  <input class="orca-input orca-input--dense" aria-label="Dense input" placeholder="Dense">
  <input class="orca-input orca-input--lg" aria-label="Large input" placeholder="Large">
</div>"""),
    ],
    guide=["Text input", "Dense text input", "Small input", "Large input"],
    related=["label", "help-text", "error-text"],
))

add(Element(
    "textarea", "Textarea", C,
    "A multi-line field that grows vertically.",
    why="A taller box tells people a longer answer is expected (Practical UI R06).",
    when=["Notes, descriptions, messages: anything that may run past one line."],
    how=["`<textarea class=\"orca-textarea\" rows=\"4\">`. Resizable vertically by default; `.orca-textarea--fixed` stops resizing where layout depends on it.",
         "If there is a limit, say it in the help text and show the count (`maxlength` plus a live count, phase 2)."],
    classes=[".orca-textarea", ".orca-textarea--fixed"], tokens=["bg-input", "border-strong"],
    laws=["R06", "R08"],
    examples=[("Textarea", """<label class="orca-label" for="ta-1">Note <span class="orca-optional">(optional)</span></label>
<textarea class="orca-textarea" id="ta-1" rows="3">Mounted 3 m above the door, facing inward.</textarea>
<label class="orca-label" for="ta-2" style="margin-top: var(--orca-space-16)">Fixed size</label>
<textarea class="orca-textarea orca-textarea--fixed" id="ta-2" rows="2"></textarea>""")],
    guide=["Textarea", "Fixed-size textarea"],
))

add(Element(
    "select", "Select (native)", C,
    "The browser's dropdown, styled with an ORCA chevron.",
    why="The native select works with every input method and opens the platform picker on phones (Postel's law, Jakob's law).",
    when=["Choosing one of 7–15 options where space is short; options people know by name (country, timezone)."],
    avoid=["Fewer than about 7 options: radios show the choices without a click (R11).",
           "Long lists people type rather than scroll: autocomplete (R12, phase 2).",
           "A pre-selected value that looks like an answer: start with an empty 'Choose…' option when no default is right."],
    how=["`<select class=\"orca-select\" id=… name=…>`. Sizes `--sm`, `--dense`, `--lg`.",
         "Group long lists with `<optgroup>`.", "Sort options in a meaningful order (frequency, alphabet, time)."],
    classes=[".orca-select", ".orca-select--dense"], tokens=["bg-input", "border-strong"],
    laws=["jakob", "postel", "R11", "R12"],
    examples=[("Select", """<label class="orca-label" for="sel-1">Album</label>
<select class="orca-select" id="sel-1" style="max-width: 20rem">
  <option value="">Choose an album</option>
  <option>Summer 2026</option>
  <option>Product shots</option>
</select>""")],
    guide=["Select", "Native select"],
    related=["listbox", "timezone-select"],
))

add(Element(
    "listbox", "Multiple select (listbox)", C,
    "A native `<select multiple>` showing several options at once.",
    why="A visible list keeps options in view (recognition over recall, Miller's law) and works with the keyboard natively.",
    when=["Selecting several items from a short-to-medium list in a dense admin form."],
    avoid=["Most end-user forms: checkboxes are easier (ctrl-click is not discoverable); use a checkbox group or multi-picker."],
    how=["`<select class=\"orca-select orca-listbox\" multiple size=\"6\">`.",
         "Say in the help text how to pick several: 'Hold Ctrl (Cmd on Mac) to choose more than one.'"],
    classes=[".orca-listbox"], tokens=["bg-input", "bg-active"],
    laws=["miller", "postel"],
    examples=[("Listbox", """<label class="orca-label" for="lb-1">Albums</label>
<p class="orca-help" id="lb-1-help">Hold Ctrl (Cmd on Mac) to choose more than one.</p>
<select class="orca-select orca-listbox" id="lb-1" multiple size="4" aria-describedby="lb-1-help" style="max-width: 20rem">
  <option selected>Entrance A</option><option>Entrance B</option><option selected>Loading dock</option><option>Car park</option>
</select>""")],
    guide=["Multiple select (listbox)"],
))

add(Element(
    "search-input", "Search input", C,
    "A text field with a magnifier and a clear button.",
    why="The magnifier is one of the few universally understood icons (Jakob's law); a clear button saves selecting "
        "and deleting text (Fitts's law).",
    when=["Filtering a list or table; searching the app."],
    how=["Wrap: `<div class=\"orca-search\">{% icon \"search\" %}<input class=\"orca-input\" type=\"search\" placeholder=\" \" aria-label=…><button class=\"orca-search__clear\" type=\"button\" aria-label=\"Clear search\" data-orca-clear>{% icon \"close\" %}</button></div>`.",
         "Keep `placeholder` non-empty (a space is fine): the clear button hides while the placeholder shows.",
         "A single search field may use placeholder text as its visible hint if it also has an accessible label (R09 exception)."],
    a11y=["Give the input an `aria-label` or a visually hidden label; wrap in `<form role=\"search\">` for the main site search."],
    classes=[".orca-search", ".orca-search__clear"], tokens=["bg-input", "text-muted"],
    laws=["jakob", "fitts", "R09"],
    examples=[("Search with clear", """<form role="search" class="orca-search" style="max-width: 22rem" onsubmit="return false">
  {% icon "search" %}
  <input class="orca-input" type="search" name="q" placeholder="Search images" aria-label="Search images" value="Entrance">
  <button class="orca-search__clear" type="button" aria-label="Clear search" data-orca-clear>{% icon "close" %}</button>
</form>""")],
    guide=["Search input", "Search clear button"],
))

add(Element(
    "checkbox", "Checkbox", C,
    "A square tick for an on/off choice that takes effect when the form is saved, or one of several choices.",
    why="The square box is the convention for 'any number of these' (Practical UI R07), and the whole label row is "
        "the target (Fitts's law). Checkboxes apply on submit; switches apply at once (R14).",
    when=["Agreeing, opting in, or picking several options in a form that is submitted."],
    avoid=["Settings that apply immediately: use a switch.", "One of several mutually exclusive options: radios."],
    how=["`<label class=\"orca-check\"><input type=\"checkbox\" name=…><span class=\"orca-check__box\"></span>Email me a daily report</label>`.",
         "Description under the label: wrap text in `.orca-check__text` and add `.orca-check__desc`.",
         "Indeterminate (some children checked): set `input.indeterminate = true` in script.",
         "Phrase the label positively, so 'Yes' makes sense in front of it (R15)."],
    a11y=["The native input stays focusable; the ring is drawn outside the box with a gap.", "Groups use `<fieldset>` + `<legend>`."],
    classes=[".orca-check", ".orca-check__box", ".orca-check__text", ".orca-check__desc"],
    tokens=["accent", "border-strong", "focus"],
    laws=["R07", "R14", "R15", "fitts"],
    examples=[("Checkboxes", """<fieldset style="border: 0; margin: 0; padding: 0" class="orca-stack">
  <legend class="orca-label">Daily report</legend>
  <label class="orca-check"><input type="checkbox" name="r" checked><span class="orca-check__box"></span>Email me a daily report</label>
  <label class="orca-check"><input type="checkbox" name="r2"><span class="orca-check__box"></span><span class="orca-check__text">Include thumbnails<span class="orca-check__desc">Adds one image per video, about 2 MB.</span></span></label>
  <label class="orca-check"><input type="checkbox" disabled><span class="orca-check__box"></span>Attach videos</label>
</fieldset>""")],
    guide=["Checkbox"],
    related=["switch", "radio"],
))

add(Element(
    "radio", "Radio", C,
    "A round mark for choosing exactly one option from a small visible set.",
    why="Showing every option lets people compare without opening anything (Practical UI R11); the round mark signals "
        "'only one' by convention (R07, Jakob's law).",
    when=["2 to about 10 mutually exclusive options, especially when the differences need a description."],
    avoid=["Two options that are really on/off: a checkbox or switch.", "Long lists: a select or autocomplete."],
    how=["`<label class=\"orca-radio\"><input type=\"radio\" name=\"grp\" value=…><span class=\"orca-radio__dot\"></span>Label</label>` inside a fieldset.",
         "Stack vertically (R01). Pre-select the recommended option only when it is genuinely the right default (Hick's law; ethics of defaults)."],
    a11y=["Arrow keys move between radios of the same `name`."],
    classes=[".orca-radio", ".orca-radio__dot"], tokens=["accent", "border-strong"],
    laws=["R11", "R07", "hick", "jakob"],
    examples=[("Radio group", """<fieldset style="border: 0; margin: 0; padding: 0" class="orca-stack">
  <legend class="orca-label">Thumbnail interval</legend>
  <label class="orca-radio"><input type="radio" name="interval" value="1"><span class="orca-radio__dot"></span>Every minute</label>
  <label class="orca-radio"><input type="radio" name="interval" value="5" checked><span class="orca-radio__dot"></span>Every 5 minutes (recommended)</label>
  <label class="orca-radio"><input type="radio" name="interval" value="15"><span class="orca-radio__dot"></span>Every 15 minutes</label>
</fieldset>""")],
    guide=["Radio"],
))

add(Element(
    "switch", "Switch", C,
    "An on/off control that takes effect immediately.",
    why="A switch mirrors a physical switch: flipping it changes something now (Jakob's law, Practical UI R14). "
        "Immediate effect needs immediate feedback (Doherty threshold).",
    when=["Settings saved at once: play videos automatically, turn notifications on."],
    avoid=["Inside forms that need a Save button: use a checkbox."],
    how=["`<label class=\"orca-switch\"><input type=\"checkbox\" role=\"switch\" checked><span class=\"orca-switch__track\"></span><span>Autoplay videos</span></label>`.",
         "Save on change (htmx `hx-trigger=\"change\"`) and confirm with a status message; revert and explain on failure.",
         "Label states what is on, not the action ('Notifications', not 'Turn on notifications')."],
    a11y=["`role=\"switch\"` announces on/off."],
    classes=[".orca-switch", ".orca-switch__track"], tokens=["accent", "border-strong", "duration-brisk"],
    laws=["R14", "doherty", "jakob"],
    examples=[("Switches", """<div class="orca-stack">
  <label class="orca-switch"><input type="checkbox" role="switch" checked><span class="orca-switch__track"></span><span>Autoplay videos</span></label>
  <label class="orca-switch"><input type="checkbox" role="switch"><span class="orca-switch__track"></span><span>Email alerts</span></label>
  <label class="orca-switch"><input type="checkbox" role="switch" disabled><span class="orca-switch__track"></span><span>Record audio</span></label>
</div>""")],
    guide=["Switch"],
))

add(Element(
    "number-input", "Number input", C,
    "A numeric field with large minus and plus buttons for small adjustments.",
    why="For small changes a stepper is faster than typing or a dropdown, and the field still accepts typing "
        "(Practical UI R13, Postel's law).",
    when=["Small counts and limits: capacity, retries, minutes between shots."],
    avoid=["Values that change by large amounts or are identifiers (phone, card, postcode): use a text input with `inputmode=\"numeric\"`."],
    how=["`<div class=\"orca-number\">` with a minus `orca-icon-button` (`data-orca-step=\"-1\"`), the `<input type=\"number\" class=\"orca-input\" min max step>`, and a plus button (`data-orca-step=\"1\"`).",
         "Show the unit in the label or an addon ('Minutes')."],
    a11y=["Buttons need `aria-label` naming the field ('Decrease capacity'); the input keeps its own label."],
    classes=[".orca-number"], tokens=["control-md"],
    laws=["R13", "postel", "fitts"],
    examples=[("Stepper", """<label class="orca-label" for="cap">Zone capacity</label>
<div class="orca-number">
  <button class="orca-icon-button" type="button" aria-label="Decrease zone capacity" data-orca-step="-1">{% icon "minus" %}</button>
  <input class="orca-input" id="cap" type="number" min="0" max="999" step="1" value="40">
  <button class="orca-icon-button" type="button" aria-label="Increase zone capacity" data-orca-step="1">{% icon "plus" %}</button>
</div>""")],
    guide=["Number input"],
))

add(Element(
    "color-input", "Colour input", C,
    "A native colour picker paired with its hex value.",
    why="The swatch gives a quick visual pick; the hex field lets people paste an exact brand value (Postel's law).",
    when=["Choosing a zone colour, a calendar colour, a brand colour in settings."],
    how=["`<div class=\"orca-color\"><input type=\"color\" id=… value=\"#0f95a1\"><input class=\"orca-input\" value=\"#0f95a1\" aria-label=\"Hex value\" pattern=\"#?[0-9a-fA-F]{3,6}\"></div>`.",
         "Accept 3 or 6 digits, with or without #, any case; normalise on the server (`orca.color.normalize`).",
         "Warn if the colour will carry text and falls below 4.5:1 (`orca.color.contrast`)."],
    classes=[".orca-color"], tokens=["border-strong"],
    laws=["postel", "C01"],
    examples=[("Colour", """<label class="orca-label" for="zc">Zone colour</label>
<div class="orca-color"><input type="color" id="zc" value="#0f95a1"><input class="orca-input" value="#0f95a1" aria-label="Zone colour hex value"></div>""")],
    guide=["Colour input"], source="ORCA",
))

add(Element(
    "file-input", "File input", C,
    "The native file picker with an ORCA-styled button.",
    why="The native control works with drag-and-drop, taking a photo on phones and assistive technology (Postel's law).",
    when=["Uploading images, CSV files, licences."],
    how=["`<input class=\"orca-file\" type=\"file\" id=… accept=\"image/*\">`.",
         "State accepted types and the size limit in help text before the field; validate again on the server.",
         "Multiple: add `multiple`."],
    classes=[".orca-file"], tokens=["border-strong"],
    laws=["postel", "R08"],
    examples=[("File", """<label class="orca-label" for="fi">Floor plan</label>
<p class="orca-help" id="fi-help">PNG or JPG, up to 10 MB.</p>
<input class="orca-file" type="file" id="fi" accept="image/png,image/jpeg" aria-describedby="fi-help">""")],
    guide=["File input"],
))

add(Element(
    "otp-digit", "OTP digit box", C,
    "One box per digit of a one-time code, with auto-advance and paste.",
    why="Separate boxes chunk the code (Miller's law) and show its length; accepting a pasted code and the SMS autofill "
        "removes typing entirely (Tesler's law, Postel's law).",
    when=["Two-factor codes and email verification codes of 4–8 digits."],
    avoid=["Codes with letters, or longer than 8 characters: use one text input."],
    how=["Group: `<div class=\"orca-row\" data-orca-otp role=\"group\" aria-labelledby=…>` with one `<input class=\"orca-input orca-otp-digit\" inputmode=\"numeric\" maxlength=\"1\" aria-label=\"Digit 1 of 6\">` per digit.",
         "Put `autocomplete=\"one-time-code\"` on the first box.",
         "orca.js advances on input, goes back on Backspace and spreads a pasted code across the boxes.",
         "Alternative with zero script: a single `<input class=\"orca-input orca-input--w8\" autocomplete=\"one-time-code\" inputmode=\"numeric\">`."],
    a11y=["Each box names its position ('Digit 3 of 6')."],
    classes=[".orca-otp-digit"], tokens=["font-mono"],
    laws=["miller", "tesler", "postel"],
    examples=[("Six-digit code", """<p class="orca-label" id="otp-label">Verification code</p>
<div class="orca-row" data-orca-otp role="group" aria-labelledby="otp-label">
  {% for i in "123456" %}<input class="orca-input orca-otp-digit" inputmode="numeric" maxlength="1" aria-label="Digit {{ i }} of 6"{% if forloop.first %} autocomplete="one-time-code"{% endif %}>{% endfor %}
</div>""")],
    guide=["OTP digit box"], source="ORCA",
))

add(Element(
    "input-addon", "Input addon (prefix, suffix)", C,
    "A fixed unit, prefix or button joined to an input.",
    why="Showing the unit beside the value removes guessing ('minutes or seconds?') and stops people typing the unit "
        "(Postel's law, Practical UI F03).",
    when=["Units (min, %, m²), protocols (https://), currency, an attached action (Copy, Test)."],
    how=["`<div class=\"orca-input-group\"><span class=\"orca-addon\">https://</span><input class=\"orca-input\" …><span class=\"orca-addon\">.mp4</span></div>`.",
         "A button suffix uses `.orca-button` inside the group.", "Link the addon text to the input with `aria-describedby` if it changes the meaning."],
    classes=[".orca-input-group", ".orca-addon"], tokens=["bg-alt", "border-strong"],
    laws=["postel", "F03"],
    examples=[("Prefix and suffix", """<label class="orca-label" for="ig1">Thumbnail interval</label>
<div class="orca-input-group" style="max-width: 14rem"><input class="orca-input" id="ig1" type="number" value="5" aria-describedby="ig1-unit"><span class="orca-addon" id="ig1-unit">minutes</span></div>
<label class="orca-label" for="ig2" style="margin-top: var(--orca-space-16)">Video address</label>
<div class="orca-input-group" style="max-width: 28rem"><span class="orca-addon">https://</span><input class="orca-input" id="ig2" value="media.example.com/v/4821"><button class="orca-button" type="button">Test</button></div>""")],
    guide=["Input addon (prefix, suffix)"],
))
