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


def sanitize_for_uthmanic(text: str) -> str:
    """App sanitizeArabicForMadinah — UthmanicHafs üçün."""
    if not text:
        return text
    t = text
    t = re.sub(r'[\u200E\u200F\u200B\u200C\u200D\uFEFF]', '', t)
    t = t.replace('\u060C', ',').replace('\u061B', ';').replace('\u061F', '?')
    t = (
        t.replace('\u08F0', '\u064B')
        .replace('\u08F1', '\u064C')
        .replace('\u08F2', '\u064D')
        .replace('\u08F3', '\u064F')
    )
    t = re.sub(r'[\u08A0-\u08FF]', '', t)
    t = t.replace('\u06E1', '\u0652')
    t = re.sub(r'[\u06D6-\u06ED]', '', t)
    t = t.replace('\u0640', '')
    t = t.replace('\u0670', '\u0627')
    t = t.replace('\u0653', '')
    t = re.sub(r'\u0627{2,}', '\u0627', t)
    t = re.sub(r' {2,}', ' ', t)
    return t.strip()


def searchable_ayah_text(surah: int, ayah: int, raw: str) -> str | None:
    text = (raw or '').replace('\ufeff', '').strip()
    if not text:
        return None
    if ayah == 1 and surah != 9:
        text = strip_leading_bismillah(text)
        if not text:
            return None
    return text


def strip_harakat_display(text: str) -> str:
    """QCF söz mətnini hərəkəsiz göstərmək üçün."""
    t = sanitize_for_uthmanic(text or '')
    t = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640]', '', t)
    return re.sub(r' {2,}', ' ', t).strip()


def _page_has_verse(page: dict | None, verse_key: str) -> bool:
    if not page or not verse_key:
        return False
    for line in page.get('lines') or []:
        for w in line.get('words') or []:
            if w.get('verse_key') == verse_key:
                return True
    return False


def prepare_plain_page(page_number: int) -> dict | None:
    """QCF səhifəsi — hərəkəsiz sözlər (position saxlanır → ma_inkar API)."""
    from . import mushaf as mushaf_lib

    if page_number < 1 or page_number > mushaf_lib.PAGE_COUNT:
        return None
    page = mushaf_lib.prepare_page_view(page_number)
    if not page:
        return None

    next_page = (
        mushaf_lib.prepare_page_view(page_number + 1)
        if page_number < mushaf_lib.PAGE_COUNT
        else None
    )

    blocks: list[dict] = []
    flow: list[dict] = []
    primary_surah = 1
    for s in page.get('surahs') or []:
        try:
            primary_surah = int(s.get('id') or primary_surah)
            break
        except (TypeError, ValueError):
            pass

    def flush_flow() -> None:
        nonlocal flow
        if not flow:
            return
        # Son ayə növbəti səhifədə davam edirsə end işarəsini gizlə
        last_vk = ''
        for tok in reversed(flow):
            if tok.get('kind') == 'word':
                last_vk = tok.get('verse_key') or ''
                break
        if last_vk and _page_has_verse(next_page, last_vk):
            for tok in reversed(flow):
                if tok.get('kind') == 'end' and tok.get('verse_key') == last_vk:
                    tok['hidden'] = True
                    break
        blocks.append({'kind': 'flow', 'tokens': flow})
        flow = []

    for line in page.get('lines') or []:
        for word in line.get('words') or []:
            wtype = word.get('type') or 'word'
            if wtype == 'surah_header':
                sid = word.get('sura')
                if not sid:
                    for s in page.get('surahs') or []:
                        if int(s.get('verse_start') or 0) == 1:
                            sid = s.get('id')
                            break
                    if not sid and page.get('surahs'):
                        sid = page['surahs'][0].get('id')
                try:
                    sid_i = int(sid)
                except (TypeError, ValueError):
                    continue
                flush_flow()
                blocks.append({'kind': 'header', 'surah_id': sid_i})
                primary_surah = sid_i
                continue

            if wtype == 'bismillah':
                flush_flow()
                blocks.append(
                    {
                        'kind': 'bismillah',
                        'text': strip_harakat_display(_bismillah_plain()),
                    }
                )
                continue

            key = word.get('verse_key') or ''
            if wtype == 'end':
                if not key:
                    continue
                try:
                    ayah = int(key.split(':', 1)[1])
                except (ValueError, IndexError):
                    continue
                flow.append(
                    {
                        'kind': 'end',
                        'verse_key': key,
                        'ayah': ayah,
                        'hidden': False,
                    }
                )
                continue

            if wtype != 'word' or not key:
                continue
            try:
                pos = int(word.get('position') or 0)
            except (TypeError, ValueError):
                pos = 0
            if pos < 1:
                continue
            raw = (word.get('text') or '').strip()
            display = strip_harakat_display(raw) or raw
            if not display:
                continue
            try:
                primary_surah = int(key.split(':', 1)[0])
            except (ValueError, IndexError):
                pass
            flow.append(
                {
                    'kind': 'word',
                    'verse_key': key,
                    'position': pos,
                    'text': raw,
                    'display': display,
                }
            )

    flush_flow()

    catchword = None
    if next_page:
        for line in next_page.get('lines') or []:
            for word in line.get('words') or []:
                if (word.get('type') or 'word') != 'word':
                    continue
                raw = (word.get('text') or '').strip()
                first = strip_harakat_display(raw)
                if first:
                    catchword = first.split()[0] if first.split() else first
                break
            if catchword:
                break

    has_words = any(
        t.get('kind') == 'word'
        for b in blocks
        if b.get('kind') == 'flow'
        for t in (b.get('tokens') or [])
    )

    return {
        'page': page_number,
        'primary_surah': primary_surah,
        'surahs': page.get('surahs') or [],
        'blocks': blocks,
        'catchword': catchword,
        'has_words': has_words,
    }


def tanzil_ayah_plain(surah: int, ayah: int) -> str | None:
    """Hərəkəsiz ayə mətni (app plainAyahText ilə eyni qaydalar)."""
    pack = load_tanzil()
    arr = pack.get(str(surah)) or []
    if ayah < 1 or ayah > len(arr):
        return None
    text = (arr[ayah - 1] or '').replace('\ufeff', '').strip()
    if not text:
        return None
    if ayah == 1 and surah not in (1, 9):
        text = strip_leading_bismillah(text)
    if not text:
        return None
    return sanitize_for_uthmanic(text) or None


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
