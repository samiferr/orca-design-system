# Email

The layout for every transactional email: brand bar, title, text, one action, footer.

## Email frame

`id: email-frame` · level: pattern · source: ORCA

A table-based email layout with inline styles in the brand's colours, one action and a copyable link.

Built from: `logo-link`, `call-to-action`, `fine-print`

### General description

The standard layout wrapped around an automatic email, with a header, message, one main button and a footer.

#### Use cases

- Welcome and sign-up emails.
- Password reset messages.
- Alerts and report notifications.

#### When not to use it

- Marketing newsletters with many sections: use an email tool.
- Long documents: link to a web page.

#### Best practices

- Keep the width around 600 pixels or less.
- Offer one clear action and print its link too.
- Always include a plain-text version.
- Say the event in the subject line.

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
{% orca_email_preview title="Loading dock is offline" preheader="No stream since 08:14" paragraphs=sample.email_paragraphs action_url="https://example.com/videos/12/" action_label="Open the video" footer="You get this email because you are on the alert list for Warehouse." %}
```

### Server code

What your views, forms, URLs or settings provide for this element.

#### Sending the email

```python
# videos/notifications.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_offline_alert(video, recipients):
    context = {
        "title": f"{video} is offline",
        "preheader": f"No video since {video.last_seen:%H:%M}",
        "paragraphs": [f"{video} has sent nothing since {video.last_seen:%H:%M} today.",
                       "Check the network connection; playback restarts on its own."],
        "action_url": f"https://example.com{video.get_absolute_url()}",
        "action_label": "Open the video",
        "footer": "You get this email because you are on the alert list.",
    }
    html = render_to_string("orca/email/base.html", context)   # colours are inlined: no CSS needed
    message = EmailMultiAlternatives(context["title"], strip_tags(html), to=recipients)
    message.attach_alternative(html, "text/html")
    message.send()
```

**Classes:** `.orca-email-preview`

**Principles applied:** Postel's law: accept varied input, output reliable and accessible UI; Peak–end rule: people judge an experience by its peak and its end; Practical UI W15: Help people recover from errors

**ORCA guide items covered:** Email frame

---
