from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dashboard.models import SummaryNote, WordMarkNote

from .models import ChatGroup, ChatMessage


@api_view(['GET'])
def health(_request):
    from dashboard.mushaf import mushaf_status

    return Response({'ok': True, 'mushaf': mushaf_status()})


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
    about_by_verse: dict[str, dict] = {}
    latest = None
    rows = list(WordMarkNote.objects.all().order_by('id'))
    for note in rows:
        if note.updated_at and (latest is None or note.updated_at > latest):
            latest = note.updated_at
        for mark in note.to_ink_marks():
            key = f"{mark['verseKey']}:{mark['position']}"
            ink_by_key[key] = mark
        for about in note.to_about_notes():
            about_by_verse[about['verseKey']] = about
    return {
        'ink_marks': list(ink_by_key.values()),
        'about_notes': list(about_by_verse.values()),
        'updated_at': latest.isoformat() if latest else None,
    }


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
    if kind not in (WordMarkNote.KIND_WAQF_ISTINAF, WordMarkNote.KIND_QIRAAT):
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

    touch_keys = {f"{w['verseKey']}:{w['position']}" for w in words}
    for note in list(WordMarkNote.objects.all()):
        remaining = []
        for w in note._word_items():
            key = f"{w['verseKey']}:{w['position']}"
            if key not in touch_keys:
                remaining.append(w)
        if not remaining:
            note.delete()
        elif len(remaining) != len(note._word_items()):
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
