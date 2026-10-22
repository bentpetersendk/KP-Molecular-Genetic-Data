"""MkDocs hook: open external links in a new browser tab.

Every link in a page body whose address starts with http:// or https:// gets
target="_blank" rel="noopener noreferrer", so students keep the tutorial open
while they work in Galaxy or read an external page. Links to pages of this
course site (relative links, anchors, and addresses under site_url) are not
changed. The destination is never changed. Teacher and Student repositories
carry identical copies of this file.
"""
from __future__ import annotations

import re

_A = re.compile(r"<a\s([^>]*?)>", re.I)
_HREF = re.compile(r'href="(https?://[^"]*)"', re.I)


def _external(html: str, site_url: str) -> str:
    def fix(m):
        attrs = m.group(1)
        h = _HREF.search(attrs)
        if not h or (site_url and h.group(1).startswith(site_url)) or re.search(r"\btarget=", attrs, re.I):
            return m.group(0)
        attrs = re.sub(r"\brel=\"[^\"]*\"", "", attrs).rstrip()
        return f'<a {attrs} target="_blank" rel="noopener noreferrer">'
    return _A.sub(fix, html)


def on_page_content(html, page, config, files):
    return _external(html, (config.get("site_url") or "").rstrip("/") + "/")
