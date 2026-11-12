"""ORCA design system for Django: primitives with their why, when and how.

Quick start::

    pip install orca-design-system
    INSTALLED_APPS += ["orca"]
    # base template
    {% load orca %}<html {% orca_html_attrs %}><head>{% orca_head %}</head>

Look up any element from a terminal: ``python -m orca show button``.
"""

import datetime as _datetime

__version__ = "0.4.0"
__released__ = _datetime.date(2026, 11, 12)  # shown as "Last updated" on the documentation pages; set it when you release
