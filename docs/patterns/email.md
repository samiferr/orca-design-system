# Email

The frame every transactional email is written in: brand bar, title, text, one action, footer.

## Email frame

`id: email-frame` · level: pattern · source: ORCA

A table-based, inline-styled email layout in the brand's colours with one action and a copyable link.

Built from: `logo`, `button`, `brand-color`

### Why

Email clients ignore CSS variables and most stylesheets, so ORCA computes the colours and writes them inline (Postel's law: work everywhere). One clear action, with the link also printed, works even when buttons are blocked (Peak–end rule).

### When to use

- Every transactional email: welcome, password reset, alert, report.

### When not to use

- Marketing newsletters with many sections: use a dedicated email tool.

### How to use

- Write emails as `{% extends "orca/email/base.html" %}` and fill the blocks `title`, `preheader`, `heading`, `content`, `action` (or set `action_url` and `action_label`), `footer`.
- `{% orca_email_colors as c %}` gives the hex colours for any extra inline styles.
- Always send a plain-text alternative. Keep the width at 560px; the subject states the event ('Loading dock is offline').

#### Example: Alert email (preview)

```django
{% orca_email_preview title="Loading dock is offline" preheader="No stream since 08:14" paragraphs=sample.email_paragraphs action_url="https://example.com/cameras/12/" action_label="Open the camera" footer="You get this email because you are on the alert list for Warehouse." %}
```

**Classes:** `.orca-email-preview`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors

**ORCA guide items covered:** Email frame

---
