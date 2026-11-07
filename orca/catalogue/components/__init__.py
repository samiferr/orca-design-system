"""Level 2 of the ORCA guide: components, simple groups of primitives that do one job."""

from functools import partial

from ..registry import Element

# Components default to source "ORCA"; pass source="Tangerine" for ones taken from Tangerine.
Component = partial(Element, source="ORCA")
