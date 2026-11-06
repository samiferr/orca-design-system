from .registry import Element, add, category

C = category(
    "form-text", "Form text",
    "The words around a field: its label, requirement marker, help and errors. They decide whether a form is completed.",
)

add(Element(
    "label", "Label", C,
    "A visible, persistent name above every field.",
    why="Labels above inputs give one straight downward reading path (Practical UI R01) and stay visible while typing, "
        "unlike placeholders (R09). A `<label>` also enlarges the click target to its text (Fitts's law).",
    when=["Every input, select, textarea and group of ticks (use `<legend>` for groups)."],
    avoid=["Placeholder text as the only label.", "'My' or 'Your' in labels (W09): 'Email', not 'Your email'.",
           "Labels to the left of fields in a separate column."],
    how=["`<label class=\"orca-label\" for=\"id\">` directly above the control; 8px gap (`--orca-space-8`).",
         "Short noun phrase, sentence case, no colon.",
         "Group of ticks or radios: `<fieldset>` with `<legend class=\"orca-label\">`."],
    a11y=["`for` must match the input `id`; the accessible name of the field is the label text."],
    classes=[".orca-label"], tokens=["type-body", "space-8"],
    laws=["R01", "R09", "R10", "fitts"],
    examples=[("Label and input", """<label class="orca-label" for="cam-name">Camera name</label>
<input class="orca-input orca-input--w30" id="cam-name" name="name" autocomplete="off">""")],
    guide=["Label"],
    related=["text-input", "required-marker", "help-text"],
))

add(Element(
    "required-marker", "Required marker", C,
    "The word 'required' or 'optional' after a label.",
    why="People cannot guess which fields they may skip; marking status at the field is the safest pattern "
        "(Practical UI R03, R05). Words are clearer than a red asterisk, which reads as an error.",
    when=["Mark optional fields when most are required; mark required ones when most are optional. Mark both in long or unfamiliar forms."],
    avoid=["A red asterisk.", "'All fields are required' notices people skip."],
    how=["Inside the label: `<span class=\"orca-optional\">(optional)</span>` or `<span class=\"orca-required\">(required)</span>`.",
         "Always also set the `required` attribute on required controls."],
    a11y=["`required` exposes the status to assistive technology; the word makes it visible."],
    classes=[".orca-required", ".orca-optional"], tokens=["text-muted"],
    laws=["R03", "R05", "postel"],
    examples=[("Optional field", """<label class="orca-label" for="cam-note">Note <span class="orca-optional">(optional)</span></label>
<input class="orca-input" id="cam-note" name="note">""")],
    guide=["Required marker"],
))

add(Element(
    "help-text", "Help text", C,
    "A hint between the label and the field that helps people answer correctly.",
    why="Guidance placed before the input is read before answering and is never covered by autofill or the "
        "on-screen keyboard (Practical UI R08). It prevents errors instead of reporting them (Peak–end rule).",
    when=["Format expectations ('Use the address printed on the recorder'), consequences, or where to find a value."],
    avoid=["Repeating the label.", "Essential information hidden in a tooltip.", "More than two short sentences."],
    how=["`<p class=\"orca-help\" id=\"x-help\">` after the label, before the field.",
         "Link it: `aria-describedby=\"x-help\"` on the input."],
    a11y=["`aria-describedby` makes screen readers read the hint after the label."],
    classes=[".orca-help"], tokens=["type-detail", "text-muted"],
    laws=["R08", "peak-end", "tesler"],
    examples=[("Hint before the field", """<label class="orca-label" for="rtsp">Stream address</label>
<p class="orca-help" id="rtsp-help">Starts with rtsp://. Find it in the camera's network settings.</p>
<input class="orca-input" id="rtsp" name="rtsp" inputmode="url" aria-describedby="rtsp-help">""")],
    guide=["Help text"],
))

add(Element(
    "error-text", "Error text", C,
    "A message above the field that says what is wrong and how to fix it.",
    why="Errors stated next to the field, with an icon and in words, are found and fixed fastest; colour alone is "
        "missed (Practical UI R20, C03). Telling people how to fix it avoids blame (W15, Postel's law).",
    when=["After submit or after leaving a field with an invalid value."],
    avoid=["'Invalid input', 'Error', or technical codes.", "Showing errors while the person is still typing a first answer (R22)."],
    how=["`<p class=\"orca-error\" id=\"x-error\">{% icon \"error\" %}<span>Enter a stream address that starts with rtsp://</span></p>` above the input, after the help text.",
         "Mark the field `aria-invalid=\"true\"` and add the error id to `aria-describedby` (first).",
         "Pattern: what is wrong + how to fix, in one sentence."],
    a11y=["The icon is decorative; the text carries the meaning.", "Move focus to the error summary or first invalid field after submit."],
    classes=[".orca-error"], tokens=["negative", "type-detail"],
    laws=["R20", "W15", "C03", "postel"],
    examples=[("Invalid field", """<label class="orca-label" for="rtsp2">Stream address</label>
<p class="orca-error" id="rtsp2-error">{% icon "error" %}<span>Enter an address that starts with rtsp://, for example rtsp://192.168.1.40/stream1.</span></p>
<input class="orca-input" id="rtsp2" name="rtsp" value="192.168.1.40" aria-invalid="true" aria-describedby="rtsp2-error">""")],
    guide=["Error text"],
    related=["error-list"],
))

add(Element(
    "help-icon", "Help icon", C,
    "A question-mark button that reveals optional, extra explanation in place.",
    why="Secondary explanations stay out of the way until wanted (Practical UI S04, Tesler's law), while essential help stays visible as help text.",
    when=["Background for experts: how a KPI is computed, what a technical term means."],
    avoid=["Essential instructions: use help text (R08).", "Hover-only tooltips: they fail on touch and keyboard (B07)."],
    how=["Use a native disclosure: `<details class=\"orca-help-toggle\"><summary aria-label=\"About dwell time\">{% icon \"help\" %}</summary><span class=\"orca-help-toggle__text\">…</span></details>`.",
         "Place it right after the label text."],
    a11y=["`<summary>` is keyboard reachable and announces expanded/collapsed; the aria-label names the topic."],
    classes=[".orca-help-toggle", ".orca-help-toggle__text"],
    laws=["S04", "tesler", "B07"],
    examples=[("Help disclosure", """<div>
  <span class="orca-label" style="display: inline">Dwell time</span>
  <details class="orca-help-toggle">
    <summary aria-label="About dwell time">{% icon "help" %}</summary>
    <span class="orca-help-toggle__text">The average time between a person entering and leaving the zone, in minutes.</span>
  </details>
</div>""")],
    guide=["Help icon"], source="ORCA",
))

add(Element(
    "error-list", "Error list", C,
    "An error summary at the top of a form, linking to each invalid field.",
    why="With several errors, a counted list of links lets people fix them in order without hunting (Practical UI R20) "
        "and gives screen-reader users one place to start.",
    when=["After a submit that failed on two or more fields, or on a non-field (form-wide) error."],
    how=["Render above the form: `<div class=\"orca-error-list\" role=\"alert\" tabindex=\"-1\">` with the error icon, a title "
         "stating the count ('2 fields need attention'), and a `<ul>` of links to `#field-id`.",
         "Move focus to it after the failed submit.", "Repeat each message at its field (error-text)."],
    a11y=["`role=\"alert\"` announces it; `tabindex=\"-1\"` lets you focus it programmatically."],
    classes=[".orca-error-list", ".orca-error-list__title"], tokens=["negative"],
    laws=["R20", "W15", "peak-end"],
    examples=[("Error summary", """<div class="orca-error-list" role="alert" tabindex="-1">
  {% icon "error" %}
  <p class="orca-error-list__title">2 fields need attention</p>
  <ul>
    <li><a href="#rtsp2">Enter an address that starts with rtsp://</a></li>
    <li><a href="#cam-name">Enter a camera name</a></li>
  </ul>
</div>""")],
    guide=["Error list"],
    related=["error-text"],
))
