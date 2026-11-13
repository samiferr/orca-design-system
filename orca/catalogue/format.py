"""Readable layout for template examples: one element per line, indented, no blank lines.

Examples are written compactly in the catalogue. Shown on the site, in docs/ and in `python -m orca show`
they are laid out so they read well. The formatter only moves whitespace: it never changes a character that is
not whitespace, and when it cannot be sure of that (unbalanced tags, for instance) it returns the original text
with its blank lines removed.
"""

from __future__ import annotations

import re

_TOKEN = re.compile(
    r"""(?P<dcomment>\{\#.*?\#\})
      | (?P<tcomment><!--.*?-->)
      | (?P<ttag>\{%.*?%\})
      | (?P<var>\{\{.*?\}\})
      | (?P<tag><(?:[^<>"'{]|"[^"]*"|'[^']*'|\{%.*?%\}|\{\{.*?\}\}|\{)*>)""",
    re.S | re.X,
)
_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr", "!doctype"}
_RAW_ELEMENTS = {"pre", "textarea", "script", "style"}
_BLOCK = {"address", "article", "aside", "blockquote", "body", "dd", "details", "dialog", "div", "dl", "dt", "fieldset", "figure",
          "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html", "li", "main", "nav", "ol", "p",
          "pre", "section", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "ul"}
_TEMPLATE_BLOCKS = {"if", "ifchanged", "for", "block", "with", "spaceless", "autoescape", "filter", "language", "blocktranslate",
                    "blocktrans", "localize", "cache", "ifequal", "ifnotequal"}
_TEMPLATE_MID = {"else", "elif", "empty", "plural"}
_RAW_TEMPLATE = {"comment": "endcomment", "verbatim": "endverbatim"}


class _Unbalanced(Exception):
    pass


class _Node:
    __slots__ = ("kind", "open", "close", "name", "children", "mids")

    def __init__(self, kind, open="", close="", name=""):
        self.kind, self.open, self.close, self.name = kind, open, close, name
        self.children: list[_Node] = []
        self.mids: list[tuple[int, str]] = []  # (index into children, text of an else/elif/empty tag)


def _tag_name(tag: str) -> str:
    m = re.match(r"</?\s*([A-Za-z][\w:-]*|!doctype)", tag, re.I)
    return m.group(1).lower() if m else ""


def _tokens(src: str):
    pos = 0
    for m in _TOKEN.finditer(src):
        if m.start() > pos:
            yield "text", src[pos:m.start()]
        pos = m.end()
        yield m.lastgroup, m.group(0)
    if pos < len(src):
        yield "text", src[pos:]


def _parse(src: str) -> _Node:
    root = _Node("root")
    stack = [root]
    toks = list(_tokens(src))
    i = 0
    while i < len(toks):
        kind, text = toks[i]
        i += 1
        cur = stack[-1]
        if kind == "text":
            cur.children.append(_Node("text" if text.strip() else "ws", text))
        elif kind in ("dcomment", "tcomment", "var"):
            cur.children.append(_Node("var" if kind == "var" else "leaf", text))
        elif kind == "ttag":
            body = text[2:-2].strip().split(None, 1)
            word = body[0] if body else ""
            if word in _RAW_TEMPLATE:  # keep everything up to the end tag as it is
                end = _RAW_TEMPLATE[word]
                j = i
                while j < len(toks) and not (toks[j][0] == "ttag" and toks[j][1][2:-2].strip() == end):
                    j += 1
                if j >= len(toks):
                    raise _Unbalanced
                cur.children.append(_Node("raw", "".join(t for _, t in toks[i - 1:j + 1])))
                i = j + 1
            elif word in _TEMPLATE_BLOCKS:
                node = _Node("tblock", open=text, name=word)
                cur.children.append(node)
                stack.append(node)
            elif word.startswith("end") and word[3:] in _TEMPLATE_BLOCKS:
                if stack[-1].kind != "tblock" or stack[-1].name != word[3:]:
                    raise _Unbalanced
                stack[-1].close = text
                stack.pop()
            elif word in _TEMPLATE_MID:
                if cur.kind != "tblock":
                    raise _Unbalanced
                cur.mids.append((len(cur.children), text))
            else:
                cur.children.append(_Node("leaf", text))
        else:  # an HTML tag
            name = _tag_name(text)
            if text.startswith("</"):
                if stack[-1].kind != "element" or stack[-1].name != name:
                    raise _Unbalanced
                stack[-1].close = text
                stack.pop()
            elif name in _VOID or text.endswith("/>") or not name:
                cur.children.append(_Node("leaf", text))
            elif name in _RAW_ELEMENTS:
                j, depth = i, 1
                while j < len(toks):
                    if toks[j][0] == "tag" and _tag_name(toks[j][1]) == name:
                        depth += -1 if toks[j][1].startswith("</") else 1
                        if depth == 0:
                            break
                    j += 1
                if j >= len(toks):
                    raise _Unbalanced
                cur.children.append(_Node("raw", "".join(t for _, t in toks[i - 1:j + 1])))
                i = j + 1
            else:
                node = _Node("element", open=text, name=name)
                cur.children.append(node)
                stack.append(node)
    if len(stack) != 1:
        raise _Unbalanced
    return root


def _flat(node: _Node) -> str:
    """The node on one line. Spaces between inline items are kept; a line break plus indent becomes one space."""
    if node.kind in ("leaf", "var", "raw"):
        return node.open
    if node.kind in ("text", "ws"):
        return node.open
    mids: dict[int, list[str]] = {}
    for idx, tag in node.mids:
        mids.setdefault(idx, []).append(tag)
    parts: list[str] = []
    for idx, child in enumerate(node.children):
        parts.extend(mids.get(idx, []))
        parts.append(_flat(child))
    parts.extend(mids.get(len(node.children), []))
    inner = re.sub(r"^\s*\n\s*|\s*\n\s*$", "", "".join(parts))
    return node.open + re.sub(r"\s*\n\s*", " ", inner) + node.close


def _has_inline_content(node: _Node) -> bool:
    return any(c.kind in ("text", "var") for c in node.children)


def _has_template_tag(node: _Node) -> bool:
    """A Django tag ({% %} or {# #}) anywhere inside: a line always breaks after it, so the element is not kept on one line."""
    if node.kind == "tblock" or (node.kind in ("leaf", "raw") and node.open.startswith(("{%", "{#"))):
        return True
    return any(_has_template_tag(c) for c in node.children)


def _has_block_child(node: _Node) -> bool:
    return any(c.kind == "element" and c.name in _BLOCK for c in node.children)


def _render(node: _Node, depth: int, out: list[str]) -> None:
    pad = "  " * depth
    if node.kind == "ws":
        return
    if node.kind in ("leaf", "var"):
        out.append(pad + node.open)
    elif node.kind == "text":
        out.append(pad + re.sub(r"\s*\n\s*", " ", node.open.strip()))
    elif node.kind == "raw":
        out.append(pad + re.sub(r"\n[ \t]*(?=\n)", "", node.open))
    elif node.kind == "element" and not any(c.kind != "ws" for c in node.children):
        out.append(pad + node.open + node.close)
    elif node.kind == "element" and _has_inline_content(node) and not _has_block_child(node) and not _has_template_tag(node):
        out.append(pad + _flat(node))
    else:
        out.append(pad + node.open)
        mids = {}
        for idx, tag in node.mids:
            mids.setdefault(idx, []).append(tag)
        for idx, child in enumerate(node.children):
            for tag in mids.get(idx, []):
                out.append(pad + tag)
            _render(child, depth + 1, out)
        for tag in mids.get(len(node.children), []):
            out.append(pad + tag)
        out.append(pad + node.close)


def _squeeze(text: str) -> str:
    """Fallback: the original text without blank lines or trailing spaces."""
    return "\n".join(line.rstrip() for line in text.strip().splitlines() if line.strip())


def format_example(src: str) -> str:
    """Lay out a template example for reading: one element per line, indented by nesting, no blank lines."""
    try:
        root = _parse(src)
    except _Unbalanced:
        return _squeeze(src)
    out: list[str] = []
    for child in root.children:
        _render(child, 0, out)
    result = "\n".join(line for line in out if line.strip())
    # Only whitespace may differ from the original; if anything else moved, keep the original layout.
    if re.sub(r"\s+", "", result) != re.sub(r"\s+", "", src):
        return _squeeze(src)
    return result
