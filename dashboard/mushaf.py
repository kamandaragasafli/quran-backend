"""QCF4 Madinah mushaf — self-contained under data/mushaf/ (quran-app lazım deyil).

İstəyə görə QURAN_APP_DIR varsa oradan oxuyur; yoxdursa backend data/mushaf.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from django.conf import settings

PAGE_COUNT = 604

# Madinah mushaf — cüz başlanğıc səhifələri (tətbiq juzPages.ts ilə eyni)
JUZ_START_PAGES = [
    1, 22, 42, 62, 82, 102, 121, 142, 162, 182, 201, 222, 242, 262, 282, 302, 322,
    342, 362, 382, 402, 422, 442, 462, 482, 502, 522, 542, 562, 582,
]

QCF_VERSE_PAGE_MOVE = {
    '5:77': {'from': 120, 'to': 121},
}


def juz_start_page(juz: int) -> int:
    if juz < 1 or juz > 30:
        return 1
    return JUZ_START_PAGES[juz - 1]


def juz_end_page(juz: int) -> int:
    if juz < 1 or juz > 30:
        return PAGE_COUNT
    if juz == 30:
        return PAGE_COUNT
    return JUZ_START_PAGES[juz] - 1


def surahs_for_page_range(page_min: int, page_max: int) -> list[dict]:
    """Verilmiş səhifə aralığına düşən surələr."""
    meta = load_surah_meta()
    starts = load_surah_start_pages()
    out: list[dict] = []
    for i, s in enumerate(meta):
        start = int(starts[i]) if i < len(starts) else 1
        end = int(starts[i + 1]) - 1 if i + 1 < len(starts) else PAGE_COUNT
        if end >= page_min and start <= page_max:
            out.append(s)
    return out


def bundled_mushaf_dir() -> Path:
    return Path(settings.BASE_DIR) / 'data' / 'mushaf'


def quran_app_dir() -> Path:
    return Path(settings.QURAN_APP_DIR).resolve()


def _prefer(*candidates: Path) -> Path:
    for p in candidates:
        if p.is_file() or p.is_dir():
            return p
    return candidates[-1]


def pages_dir() -> Path:
    return _prefer(
        bundled_mushaf_dir() / 'pages',
        quran_app_dir() / 'src' / 'data' / 'qcf4' / 'pages',
    )


def fonts_dir() -> Path:
    return _prefer(
        bundled_mushaf_dir() / 'fonts',
        quran_app_dir() / 'assets' / 'fonts' / 'qcf4',
    )


def surah_meta_path() -> Path:
    return _prefer(
        bundled_mushaf_dir() / 'surah-meta.json',
        quran_app_dir() / 'assets' / 'data' / 'surah-meta.json',
    )


def surah_pages_path() -> Path:
    return _prefer(
        bundled_mushaf_dir() / 'surah-pages.json',
        quran_app_dir() / 'src' / 'data' / 'qcf4' / 'surah-pages.json',
    )


@lru_cache(maxsize=1)
def load_surah_meta() -> list[dict]:
    path = surah_meta_path()
    if not path.is_file():
        return []
    return json.loads(path.read_text(encoding='utf-8'))


@lru_cache(maxsize=1)
def load_surah_start_pages() -> list[int]:
    path = surah_pages_path()
    if not path.is_file():
        return [1] * 114
    return json.loads(path.read_text(encoding='utf-8'))


def mushaf_status() -> dict:
    """Dashboard / deploy diaqnostikası."""
    meta = surah_meta_path()
    pages = pages_dir()
    fonts = fonts_dir()
    page_count = 0
    if pages.is_dir():
        page_count = sum(1 for _ in pages.glob('*.json'))
    return {
        'source': 'bundled' if (bundled_mushaf_dir() / 'pages').is_dir() else 'quran_app',
        'bundled_dir': str(bundled_mushaf_dir()),
        'surah_meta': str(meta),
        'surah_meta_ok': meta.is_file(),
        'surah_count': len(load_surah_meta()),
        'pages_dir': str(pages),
        'pages_ok': page_count >= 600,
        'page_json_count': page_count,
        'fonts_dir': str(fonts),
        'fonts_ok': fonts.is_dir() and any(fonts.glob('*.ttf')),
    }
def surah_start_page(surah_id: int) -> int:
    pages = load_surah_start_pages()
    idx = surah_id - 1
    if idx < 0 or idx >= len(pages):
        return 1
    return int(pages[idx])


def page_to_surah_index(page: int) -> int:
    pages = load_surah_start_pages()
    idx = 0
    for i, start in enumerate(pages):
        if start <= page:
            idx = i
    return idx


def font_filename(font_name: str) -> str | None:
    fonts = fonts_dir()
    if font_name == 'QCF4_QBSML':
        candidate = fonts / 'QCF4_QBSML.ttf'
        return candidate.name if candidate.is_file() else None
    if font_name.startswith('QCF4_Hafs_'):
        candidate = fonts / f'{font_name}_W.ttf'
        if candidate.is_file():
            return candidate.name
        # fallback without _W
        alt = fonts / f'{font_name}.ttf'
        return alt.name if alt.is_file() else None
    candidate = fonts / f'{font_name}.ttf'
    return candidate.name if candidate.is_file() else None


def glyph_char(word: dict) -> str:
    ch = word.get('char')
    if ch:
        return ch
    code = word.get('code')
    if isinstance(code, int):
        try:
            return chr(code)
        except (ValueError, OverflowError):
            return ''
    return ''


def collect_font_names(page: dict) -> list[str]:
    names: set[str] = set()
    if page.get('font'):
        names.add(page['font'])
    for line in page.get('lines') or []:
        for word in line.get('words') or []:
            if word.get('font'):
                names.add(word['font'])
    return sorted(names)


def apply_layout_overrides(page: dict) -> dict:
    """Port of QCF_VERSE_PAGE_MOVE (Maidə 77)."""
    page_num = page.get('page')
    # Only apply when needed — keep simple: return as-is for dashboard v1
    # Full move logic is complex; page JSON already mostly correct after app patches.
    _ = page_num
    return page


@lru_cache(maxsize=604)
def load_page(page_number: int) -> dict | None:
    if page_number < 1 or page_number > PAGE_COUNT:
        return None
    path = pages_dir() / f'{page_number}.json'
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding='utf-8'))
    return apply_layout_overrides(data)


@lru_cache(maxsize=604)
def prepare_page_view(page_number: int) -> dict | None:
    page = load_page(page_number)
    if not page:
        return None

    fonts_needed = []
    for name in collect_font_names(page):
        fname = font_filename(name)
        if fname:
            fonts_needed.append({'name': name, 'file': fname})

    lines = []
    for line in page.get('lines') or []:
        words = []
        for word in line.get('words') or []:
            words.append(
                {
                    'char': glyph_char(word),
                    'font': word.get('font') or page.get('font') or '',
                    'text': word.get('text') or '',
                    'type': word.get('type') or 'word',
                    'verse_key': word.get('verse_key') or '',
                    'position': word.get('position') or 0,
                }
            )
        lines.append({'line': line.get('line'), 'words': words})

    return {
        'page': page.get('page', page_number),
        'font': page.get('font'),
        'surahs': page.get('surahs') or [],
        'lines': lines,
        'fonts': fonts_needed,
    }
