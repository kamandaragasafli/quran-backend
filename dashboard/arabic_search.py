"""Arabic ayah/word search — mirrors quran-app arabicAyahSearch.ts."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from django.conf import settings

MAX_HITS = 80

BISMILLAH_RE = re.compile(
    r'^بسم\s+ٱ?لل[هه]\s+ٱ?لرحمن\s+ٱ?لرحيم\s*',
    re.UNICODE,
)


def quran_app_dir() -> Path:
    return Path(settings.QURAN_APP_DIR).resolve()


def bundled_mushaf_dir() -> Path:
    return Path(settings.BASE_DIR) / 'data' / 'mushaf'


def _prefer_file(*candidates: Path) -> Path:
    for p in candidates:
        if p.is_file():
            return p
    return candidates[-1]


@lru_cache(maxsize=1)
def load_tanzil() -> dict[str, list[str]]:
    path = _prefer_file(
        bundled_mushaf_dir() / 'tanzil-simple-clean.json',
        quran_app_dir() / 'assets' / 'data' / 'tanzil-simple-clean.json',
    )
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    return data.get('surahs') or {}


@lru_cache(maxsize=1)
def load_verse_to_page() -> dict[str, int]:
    path = _prefer_file(
        bundled_mushaf_dir() / 'verse-to-page.json',
        quran_app_dir() / 'src' / 'data' / 'qcf4' / 'verse-to-page.json',
    )
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding='utf-8'))


QCF_VERSE_PAGE_MOVE = {
    '5:77': 121,
}


def page_for_verse(verse_key: str) -> int | None:
    moved = QCF_VERSE_PAGE_MOVE.get(verse_key)
    if moved:
        return moved
    page = load_verse_to_page().get(verse_key)
    return int(page) if isinstance(page, int) else None


def has_arabic_letters(s: str) -> bool:
    return bool(re.search(r'[\u0600-\u06FF]', s or ''))


def fold_arabic_char(ch: str) -> str:
    code = ord(ch)
    if (
        (0x064B <= code <= 0x065F)
        or code == 0x0670
        or (0x06D6 <= code <= 0x06ED)
        or (0x08F0 <= code <= 0x08FF)
    ):
        return ''
    if code == 0x0640 or (0x200B <= code <= 0x200F) or code == 0xFEFF:
        return ''
    if ch in 'أإآٱٲٳ':
        return 'ا'
    if ch == 'ؤ':
        return 'و'
    if ch in 'ئى':
        return 'ي'
    if ch.isspace():
        return ' '
    return ch


def normalize_arabic(input_text: str) -> str:
    out: list[str] = []
    for ch in input_text or '':
        folded = fold_arabic_char(ch)
        if not folded:
            continue
        if folded == ' ' and out and out[-1] == ' ':
            continue
        out.append(folded)
    return ''.join(out).strip()


@lru_cache(maxsize=1)
def _bismillah_plain() -> str:
    pack = load_tanzil()
    raw = (pack.get('1') or [''])[0] or 'بسم ٱلله ٱلرحمن ٱلرحيم'
    return raw.replace('\ufeff', '').strip()


def strip_leading_bismillah(text: str) -> str:
    t = text.strip()
    plain = _bismillah_plain()
    if t.startswith(plain):
        return t[len(plain) :].strip()
    return BISMILLAH_RE.sub('', t).strip() or t


def searchable_ayah_text(surah: int, ayah: int, raw: str) -> str | None:
    text = (raw or '').replace('\ufeff', '').strip()
    if not text:
        return None
    if ayah == 1 and surah != 9:
        text = strip_leading_bismillah(text)
        if not text:
            return None
    return text


def search_arabic_ayahs(
    query: str,
    *,
    surah_id: int | None = None,
    limit: int = MAX_HITS,
) -> list[dict]:
    q = normalize_arabic(query)
    if not q or len(q) < 2:
        return []

    pack = load_tanzil()
    if not pack:
        return []

    from .mushaf import load_surah_meta

    surahs_meta = {s['id']: s for s in load_surah_meta()}
    hits: list[dict] = []

    surah_range = range(surah_id, surah_id + 1) if surah_id else range(1, 115)
    for surah in surah_range:
        ayahs = pack.get(str(surah))
        if not ayahs:
            continue
        meta = surahs_meta.get(surah) or {}
        for i, raw in enumerate(ayahs):
            ayah_number = i + 1
            text = searchable_ayah_text(surah, ayah_number, raw)
            if not text:
                continue
            if q not in normalize_arabic(text):
                continue
            verse_key = f'{surah}:{ayah_number}'
            hits.append(
                {
                    'surahId': surah,
                    'ayahNumber': ayah_number,
                    'verseKey': verse_key,
                    'text': text,
                    'page': page_for_verse(verse_key),
                    'nameAz': meta.get('nameAz') or f'Surə {surah}',
                }
            )
            if len(hits) >= limit:
                return hits
    return hits
