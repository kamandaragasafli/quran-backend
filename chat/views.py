from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dashboard.models import (
    AppContent,
    Juz30Segment,
    JUZ30_COLORS,
    PageNote,
    SummaryNote,
    WordMarkNote,
)

from .models import ChatGroup, ChatMessage


@api_view(['GET'])
def health(_request):
    from dashboard.mushaf import mushaf_status

    return Response({'ok': True, 'mushaf': mushaf_status()})


@api_view(['GET'])
def app_content_pack(_request):
    """Haqqında + Məal giriş + Qarilər + Telegram — tətbiq üçün pack."""
    keys = [
        AppContent.KEY_ABOUT,
        AppContent.KEY_MEAL_INTRO,
        AppContent.KEY_RECITERS,
        AppContent.KEY_TELEGRAM,
    ]
    pages = {}
    latest = None
    for key in keys:
        obj = AppContent.get_or_seed(key)
        pages[key] = obj.data or {}
        if obj.updated_at and (latest is None or obj.updated_at > latest):
            latest = obj.updated_at
    return Response(
        {
            'pages': pages,
            'updated_at': latest.isoformat() if latest else None,
        }
    )


@api_view(['GET'])
def app_content_detail(_request, key: str):
    key = (key or '').strip().replace('-', '_')
    allowed = {
        AppContent.KEY_ABOUT,
        AppContent.KEY_MEAL_INTRO,
        AppContent.KEY_RECITERS,
        AppContent.KEY_TELEGRAM,
    }
    if key not in allowed:
        return Response({'error': 'Naməlum mətn'}, status=status.HTTP_404_NOT_FOUND)
    obj = AppContent.get_or_seed(key)
    return Response(obj.to_api())


@api_view(['GET'])
def meal_summaries(_request):
    """Dashboard /xulaseler/ qeydləri — məal oxuyucu üçün pack formatı."""
    surahs: dict = {}
    ayahs: dict = {}
    latest = None

    notes = SummaryNote.objects.all().order_by('surah', 'ayah', 'id')
    for note in notes:
        text = (note.text or '').strip()
        if not text:
            continue
        if note.updated_at and (latest is None or note.updated_at > latest):
            latest = note.updated_at

        if note.scope == SummaryNote.SCOPE_AYAH and note.ayah:
            ayahs[f'{note.surah}:{note.ayah}'] = {'intro': text}
            entry = surahs.setdefault(str(note.surah), {})
            summaries = entry.setdefault('summaries', [])
            summaries.append({'from': note.ayah, 'to': note.ayah, 'text': text})
            continue

        entry = surahs.setdefault(str(note.surah), {})
        if 'intro' not in entry:
            entry['intro'] = text
        else:
            entry.setdefault('paragraphs', []).append(text)

    for entry in surahs.values():
        summaries = entry.get('summaries')
        if isinstance(summaries, list):
            summaries.sort(key=lambda s: (s.get('from', 0), s.get('to', 0)))

    return Response(
        {
            'surahs': surahs,
            'ayahs': ayahs,
            'updated_at': latest.isoformat() if latest else None,
        }
    )


def _build_word_marks_pack():
    ink_by_key: dict[str, dict] = {}
    about_notes: list[dict] = []
    latest = None
    rows = list(WordMarkNote.objects.all().order_by('id'))
    for note in rows:
        if note.updated_at and (latest is None or note.updated_at > latest):
            latest = note.updated_at
        for mark in note.to_ink_marks():
            key = f"{mark['verseKey']}:{mark['position']}"
            ink_by_key[key] = mark
        for about in note.to_about_notes():
            about_notes.append({**about, 'noteId': note.pk})

    page_notes = []
    for pn in PageNote.objects.all().order_by('page'):
        if pn.updated_at and (latest is None or pn.updated_at > latest):
            latest = pn.updated_at
        page_notes.append(pn.to_api())

    juz30_pack = _build_juz30_pack(include_ink=True)
    stamps = [s for s in [latest.isoformat() if latest else None, juz30_pack.get('updated_at')] if s]
    # 30 cüz ink — eyni pack-də (tətbiq rəng + qeyd)
    for mark in juz30_pack.get('ink_marks') or []:
        key = f"{mark['verseKey']}:{mark['position']}"
        ink_by_key[key] = mark
    return {
        'ink_marks': list(ink_by_key.values()),
        'about_notes': about_notes,
        'page_notes': page_notes,
        'juz30_segments': juz30_pack['segments'],
        'updated_at': max(stamps) if stamps else None,
    }


def _build_juz30_pack(*, include_ink: bool = True) -> dict:
    segments = []
    ink_by_key: dict[str, dict] = {}
    latest = None
    for seg in Juz30Segment.objects.all().order_by('id'):
        if seg.updated_at and (latest is None or seg.updated_at > latest):
            latest = seg.updated_at
        segments.append(seg.to_api())
        if include_ink:
            for mark in seg.to_ink_marks():
                key = f"{mark['verseKey']}:{mark['position']}"
                ink_by_key[key] = mark
    out = {
        'segments': segments,
        'updated_at': latest.isoformat() if latest else None,
    }
    if include_ink:
        out['ink_marks'] = list(ink_by_key.values())
    return out


def _normalize_juz30_color(raw) -> str:
    c = str(raw or '').strip()
    if c.upper() in {x.upper() for x in JUZ30_COLORS}:
        # preserve canonical casing from palette
        for p in JUZ30_COLORS:
            if p.upper() == c.upper():
                return p
    if c.startswith('#') and len(c) in (4, 7):
        return c
    return JUZ30_COLORS[0]


def _parse_words_payload(raw) -> list[dict]:
    if not isinstance(raw, list):
        return []
    out = []
    seen = set()
    for item in raw:
        if not isinstance(item, dict):
            continue
        vk = str(item.get('verseKey') or item.get('verse_key') or '').strip()
        try:
            pos = int(item.get('position'))
        except (TypeError, ValueError):
            continue
        text = str(item.get('text') or '').strip()
        if not vk or pos < 1:
            continue
        key = f'{vk}:{pos}'
        if key in seen:
            continue
        seen.add(key)
        out.append({'verseKey': vk, 'position': pos, 'text': text})
    return out


def _unique_verse_keys(words: list[dict]) -> list[str]:
    keys: list[str] = []
    for w in words:
        vk = w['verseKey']
        if vk not in keys:
            keys.append(vk)
    return keys


def _validate_qiraat_selection(words: list[dict]) -> str | None:
    """1–3 ayə (istənilən söz sayı) və ya >3 ayə + 3–6 söz."""
    ayah_count = len(_unique_verse_keys(words))
    n = len(words)
    if ayah_count <= 3:
        return None
    if 3 <= n <= 6:
        return None
    return (
        'Qiraət qeydi: 1–3 ayə seçin, '
        'və ya 3-dən çox ayədə 3–6 söz seçin (ilk və son söz mavi).'
    )


@api_view(['GET', 'POST'])
def word_marks(request):
    """Söz rəngləri + Haqqında qeydləri (admin ↔ tətbiq)."""
    if request.method == 'GET':
        return Response(_build_word_marks_pack())

    words = _parse_words_payload(request.data.get('words'))
    waqf_note = str(request.data.get('waqf_note') or request.data.get('waqfNote') or '').strip()
    istinaf_note = str(
        request.data.get('istinaf_note') or request.data.get('istinafNote') or ''
    ).strip()
    # Qiraət qeydi — tək `note` sahəsi
    note_text = str(request.data.get('note') or '').strip()
    kind = str(request.data.get('kind') or WordMarkNote.KIND_WAQF_ISTINAF).strip()
    if kind not in (
        WordMarkNote.KIND_WAQF_ISTINAF,
        WordMarkNote.KIND_QIRAAT,
        WordMarkNote.KIND_MA_INKAR,
    ):
        kind = WordMarkNote.KIND_WAQF_ISTINAF
    direction = str(
        request.data.get('direction') or WordMarkNote.DIR_ISTINAF_FIRST
    ).strip()
    if direction not in (
        WordMarkNote.DIR_ISTINAF_FIRST,
        WordMarkNote.DIR_WAQF_FIRST,
    ):
        direction = WordMarkNote.DIR_ISTINAF_FIRST

    if not words:
        return Response({'error': 'Söz seçin'}, status=status.HTTP_400_BAD_REQUEST)

    if kind == WordMarkNote.KIND_QIRAAT:
        err = _validate_qiraat_selection(words)
        if err:
            return Response({'error': err}, status=status.HTTP_400_BAD_REQUEST)
        waqf_note = note_text or waqf_note
        istinaf_note = ''
        direction = WordMarkNote.DIR_ISTINAF_FIRST
    elif kind == WordMarkNote.KIND_MA_INKAR:
        waqf_note = note_text or waqf_note
        istinaf_note = ''
        direction = WordMarkNote.DIR_ISTINAF_FIRST
    # Vəqf / İstinaf — rəng istiqaməti; qeyd mətnı məcburi deyil (səhifə qeydindən ayrı)
    touch_keys = {f"{w['verseKey']}:{w['position']}" for w in words}
    for note in list(WordMarkNote.objects.all()):
        current = note._word_items()  # artıq position-a görə sıralanmış
        remaining = [
            w for w in current
            if f"{w['verseKey']}:{w['position']}" not in touch_keys
        ]
        if not remaining:
            note.delete()
        elif len(remaining) != len(current):
            # Sıralı halda saxla — gələcəkdə first/last dəyişməsin
            note.words = remaining
            note.save(update_fields=['words', 'updated_at'])

    created = WordMarkNote.objects.create(
        words=words,
        kind=kind,
        direction=direction,
        waqf_note=waqf_note,
        istinaf_note=istinaf_note,
    )
    pack = _build_word_marks_pack()
    pack['id'] = created.id
    pack['ok'] = True
    return Response(pack, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def word_mark_detail(_request, note_id: int):
    deleted, _ = WordMarkNote.objects.filter(pk=note_id).delete()
    if not deleted:
        return Response({'error': 'Tapılmadı'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'ok': True, **_build_word_marks_pack()})


@api_view(['GET', 'POST'])
def page_notes(request):
    """Səhifə qeydləri — admin ↔ tətbiq Duracaq."""
    if request.method == 'GET':
        return Response(_build_word_marks_pack())

    try:
        page = int(request.data.get('page'))
    except (TypeError, ValueError):
        return Response({'error': 'Səhifə nömrəsi lazımdır'}, status=status.HTTP_400_BAD_REQUEST)
    if page < 1 or page > 604:
        return Response({'error': 'Səhifə 1–604 olmalıdır'}, status=status.HTTP_400_BAD_REQUEST)

    body = str(request.data.get('body') or request.data.get('note') or '').strip()
    if not body:
        return Response({'error': 'Qeyd yazın'}, status=status.HTTP_400_BAD_REQUEST)

    obj, created = PageNote.objects.update_or_create(
        page=page,
        defaults={'body': body},
    )
    pack = _build_word_marks_pack()
    pack['id'] = obj.id
    pack['ok'] = True
    pack['created'] = created
    return Response(pack, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


@api_view(['DELETE'])
def page_note_detail(_request, note_id: int):
    deleted, _ = PageNote.objects.filter(pk=note_id).delete()
    if not deleted:
        return Response({'error': 'Tapılmadı'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'ok': True, **_build_word_marks_pack()})


@api_view(['GET', 'POST'])
def juz30_segments(request):
    """30 cüz — rəngli söz seçimi + xülasə / əzbər qeydi."""
    if request.method == 'GET':
        return Response(_build_juz30_pack())

    words = _parse_words_payload(request.data.get('words'))
    if not words:
        return Response({'error': 'Söz seçin'}, status=status.HTTP_400_BAD_REQUEST)

    color = _normalize_juz30_color(
        request.data.get('color') or request.data.get('ink_color')
    )
    summary_note = str(
        request.data.get('summary_note')
        or request.data.get('summaryNote')
        or request.data.get('xulase')
        or ''
    )
    azbar_note = str(
        request.data.get('azbar_note')
        or request.data.get('azbarNote')
        or request.data.get('ezber')
        or ''
    )

    touch_keys = {f"{w['verseKey']}:{w['position']}" for w in words}
    keep_id = None
    raw_id = request.data.get('id') or request.data.get('noteId') or request.data.get('note_id')
    if raw_id not in (None, ''):
        try:
            keep_id = int(raw_id)
        except (TypeError, ValueError):
            keep_id = None

    for seg in list(Juz30Segment.objects.all()):
        if keep_id and seg.pk == keep_id:
            continue
        current = seg._word_items()
        remaining = [
            w for w in current
            if f"{w['verseKey']}:{w['position']}" not in touch_keys
        ]
        if not remaining:
            seg.delete()
        elif len(remaining) != len(current):
            seg.words = remaining
            seg.save(update_fields=['words', 'updated_at'])

    if keep_id:
        try:
            obj = Juz30Segment.objects.get(pk=keep_id)
        except Juz30Segment.DoesNotExist:
            obj = None
        if obj is not None:
            obj.words = words
            obj.color = color
            obj.summary_note = summary_note
            obj.azbar_note = azbar_note
            obj.save()
            pack = _build_juz30_pack()
            pack['id'] = obj.id
            pack['ok'] = True
            pack['created'] = False
            return Response(pack)

    created = Juz30Segment.objects.create(
        words=words,
        color=color,
        summary_note=summary_note,
        azbar_note=azbar_note,
    )
    pack = _build_juz30_pack()
    pack['id'] = created.id
    pack['ok'] = True
    pack['created'] = True
    return Response(pack, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def juz30_segment_detail(_request, note_id: int):
    deleted, _ = Juz30Segment.objects.filter(pk=note_id).delete()
    if not deleted:
        return Response({'error': 'Tapılmadı'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'ok': True, **_build_juz30_pack()})


@api_view(['GET'])
def list_groups(_request):
    groups = [g.to_api() for g in ChatGroup.objects.all()]
    return Response({'groups': groups})


@api_view(['GET'])
def get_group(_request, group_id: str):
    try:
        group = ChatGroup.objects.get(pk=group_id)
    except ChatGroup.DoesNotExist:
        return Response({'error': 'Qrup tapılmadı'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'group': group.to_api()})


@api_view(['GET', 'POST'])
def group_messages(request, group_id: str):
    try:
        group = ChatGroup.objects.get(pk=group_id)
    except ChatGroup.DoesNotExist:
        return Response({'error': 'Qrup tapılmadı'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        return Response(
            {'error': 'Appdən mesaj göndərmək bağlıdır'},
            status=status.HTTP_403_FORBIDDEN,
        )

    try:
        limit = int(request.query_params.get('limit') or 50)
    except (TypeError, ValueError):
        limit = 50
    limit = max(1, min(limit, 200))

    qs = ChatMessage.objects.filter(group=group)
    before = request.query_params.get('before')
    if before:
        try:
            qs = qs.filter(created_at__lt=int(before))
        except (TypeError, ValueError):
            pass

    rows = list(qs.order_by('-created_at')[:limit])
    rows.reverse()
    return Response({'group': group.to_api(), 'messages': [m.to_api() for m in rows]})
