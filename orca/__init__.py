"""ORCA design system for Django: primitives with their why, when and how.

Quick start::

    pip install orca-design-system
    INSTALLED_APPS += ["orca"]
    # base template
    {% load orca %}<html {% orca_html_attrs %}><head>{% orca_head %}</head>

Look up any element from a terminal: ``python -m orca show button``.
"""

__version__ = "0.2.0"
