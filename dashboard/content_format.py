"""Tətbiq mətni — sadə markdown (##, ###, >, paraqraf)."""

from __future__ import annotations

import html
import re


def body_to_html(body: str) -> str:
    raw = (body or '').strip()
    if not raw:
        return ''
    chunks = re.split(r'\n\n+', raw)
    out: list[str] = []
    for block in chunks:
        block = block.strip()
        if not block:
            continue
        if block.startswith('## '):
            out.append(f'<h2>{html.escape(block[3:].strip())}</h2>')
            continue
        if block.startswith('### '):
            out.append(f'<h3>{html.escape(block[4:].strip())}</h3>')
            continue
        if block.startswith('> '):
            lines = block.split('\n')
            inner = '<br>'.join(
                html.escape(ln[2:].strip() if ln.startswith('> ') else ln.strip())
                for ln in lines
                if ln.strip()
            )
            out.append(f'<blockquote>{inner}</blockquote>')
            continue
        inner = '<br>'.join(html.escape(ln) for ln in block.split('\n'))
        out.append(f'<p>{inner}</p>')
    return '\n'.join(out)
