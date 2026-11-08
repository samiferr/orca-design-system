from functools import partial

from ..registry import Element

Template = partial(Element, source="ORCA")
