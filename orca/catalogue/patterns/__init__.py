"""Level 3 of the ORCA guide: patterns, distinct sections of a screen made of components and primitives."""

from functools import partial

from ..registry import Element

# Patterns default to source "ORCA"; pass source="Tangerine" for ones taken from wise_people_analyzer.
Pattern = partial(Element, source="ORCA")
