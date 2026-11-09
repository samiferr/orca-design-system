from ..registry import add, category
from . import Pattern

C = category(
    "email", "Email",
    "The frame every transactional email is written in: brand bar, title, text, one action, footer.",
    level="pattern",
)

add(Pattern(
    "email-frame", "Email frame", C,
    "A table-based, inline-styled email layout in the brand's colours with one action and a copyable link.",
    why="Email clients ignore CSS variables and most stylesheets, so ORCA computes the colours and writes them inline (Postel's law: work everywhere). One clear action, with the link also printed, works even when buttons are blocked (Peak–end rule).",
    when=["Every transactional email: welcome, password reset, alert, report."],
    avoid=["Marketing newsletters with many sections: use a dedicated email tool."],
    how=["Write emails as `{% templatetag openblock %} extends \"orca/email/base.html\" {% templatetag closeblock %}` and fill the blocks `title`, `preheader`, `heading`, `content`, `action` (or set `action_url` and `action_label`), `footer`.",
         "`{% templatetag openblock %} orca_email_colors as c {% templatetag closeblock %}` gives the hex colours for any extra inline styles.",
         "Always send a plain-text alternative. Keep the width at 560px; the subject states the event ('Loading dock is offline')."],
    classes=[".orca-email-preview"],
    laws=["postel", "peak-end", "W15"],
    uses=["logo", "button", "brand-color"],
    examples=[("Alert email (preview)", """{% orca_email_preview title="Loading dock is offline" preheader="No stream since 08:14" paragraphs=sample.email_paragraphs action_url="https://example.com/videos/12/" action_label="Open the video" footer="You get this email because you are on the alert list for Warehouse." %}""")],
    guide=["Email frame"],
))
