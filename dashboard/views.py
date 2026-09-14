from pathlib import Path
import re

from django.http import FileResponse, Http404
from django.shortcuts import render
from django.utils import timezone

from . import arabic_search as ar_search
from . import mushaf as mushaf_lib


def home(request):
    return render(
        request,
        'dashboard/home.html',
        {
            'nav': 'home',
            'now': timezone.now(),
        },
    )


def summaries(request):
    from django.contrib import messages
    from django.shortcuts import redirect

    from .models import SummaryNote

    surahs = mushaf_lib.load_surah_meta()
    flash = ''
    flash_err = False

    if request.method == 'POST':
        action = (request.POST.get('action') or '').strip()
        if action == 'delete':
            try:
                note_id = int(request.POST.get('id') or 0)
                SummaryNote.objects.filter(pk=note_id).delete()
                messages.success(request, 'Xülasə silindi.')
            except (TypeError, ValueError):
                messages.error(request, 'Silinmədi.')
            return redirect('dash-summaries')

        if action == 'save':
            scope = (request.POST.get('scope') or 'surah').strip()
            if scope not in (SummaryNote.SCOPE_SURAH, SummaryNote.SCOPE_AYAH):
                scope = SummaryNote.SCOPE_SURAH
            text = (request.POST.get('text') or '').strip()
            try:
                surah = int(request.POST.get('surah') or 0)
            except (TypeError, ValueError):
                surah = 0
            ayah = None
            if scope == SummaryNote.SCOPE_AYAH:
                try:
                    ayah = int(request.POST.get('ayah') or 0)
                except (TypeError, ValueError):
                    ayah = 0
                if not ayah or ayah < 1:
                    ayah = None

            edit_id = request.POST.get('id')
            err = None
            if surah < 1 or surah > 114:
                err = 'Surə seçin (1–114).'
            elif scope == SummaryNote.SCOPE_AYAH and not ayah:
                err = 'Ayə nömrəsini yazın.'
            elif not text:
                err = 'Mətn boş ola bilməz.'

            if err:
                messages.error(request, err)
            else:
                if edit_id:
                    try:
                        note = SummaryNote.objects.get(pk=int(edit_id))
                        note.scope = scope
                        note.surah = surah
                        note.ayah = ayah if scope == SummaryNote.SCOPE_AYAH else None
                        note.text = text
                        note.save()
                        messages.success(request, 'Xülasə yeniləndi.')
                    except (SummaryNote.DoesNotExist, TypeError, ValueError):
                        messages.error(request, 'Qeyd tapılmadı.')
                else:
                    SummaryNote.objects.create(
                        scope=scope,
                        surah=surah,
                        ayah=ayah if scope == SummaryNote.SCOPE_AYAH else None,
                        text=text,
                    )
                    messages.success(request, 'Xülasə yadda saxlanıldı.')
                return redirect('dash-summaries')

            form = {
                'scope': scope,
                'surah': surah if 1 <= surah <= 114 else '',
                'ayah': ayah or '',
                'text': text,
            }
            edit = None
            if edit_id:
                try:
                    edit = SummaryNote.objects.get(pk=int(edit_id))
                except (SummaryNote.DoesNotExist, TypeError, ValueError):
                    edit = None
            notes = list(SummaryNote.objects.all()[:100])
            return render(
                request,
                'dashboard/summaries.html',
                {
                    'nav': 'summaries',
                    'surahs': surahs,
                    'notes': notes,
                    'form': form,
                    'edit': edit,
                    'flash': err,
                    'flash_err': True,
                },
            )

    edit = None
    form = {'scope': 'surah', 'surah': '', 'ayah': '', 'text': ''}
    edit_q = request.GET.get('edit')
    if edit_q:
        try:
            edit = SummaryNote.objects.get(pk=int(edit_q))
            form = {
                'scope': edit.scope,
                'surah': edit.surah,
                'ayah': edit.ayah or '',
                'text': edit.text,
            }
        except (SummaryNote.DoesNotExist, TypeError, ValueError):
            edit = None

    # Pull django messages into template flash
    storage = messages.get_messages(request)
    for m in storage:
        flash = str(m)
        flash_err = m.level >= messages.ERROR
        break

    notes = list(SummaryNote.objects.all()[:100])
    return render(
        request,
        'dashboard/summaries.html',
        {
            'nav': 'summaries',
            'surahs': surahs,
            'notes': notes,
            'form': form,
            'edit': edit,
            'flash': flash,
            'flash_err': flash_err,
        },
    )


def quran(request):
    surah_q = request.GET.get('surah')
    page_q = request.GET.get('page')
    surah_num_q = (request.GET.get('surah_num') or '').strip()
    q_ar = (request.GET.get('q') or '').strip()
    filter_surah_q = (request.GET.get('filter_surah') or '').strip()
    verse_q = (request.GET.get('verse') or '').strip()

    filter_surah = None
    if filter_surah_q:
        try:
            fs = int(filter_surah_q)
            if 1 <= fs <= 114:
                filter_surah = fs
        except (TypeError, ValueError):
            filter_surah = None

    page_num: int | None = None
    highlight_verse: str | None = None
    explicit_nav = False  # page / surah select / surah_num / verse click

    if verse_q and re.match(r'^\d{1,3}:\d{1,3}$', verse_q):
        highlight_verse = verse_q
        page_num = ar_search.page_for_verse(verse_q)
        explicit_nav = True

    if page_num is None and surah_num_q:
        try:
            sid = int(surah_num_q)
            if 1 <= sid <= 114:
                page_num = mushaf_lib.surah_start_page(sid)
                filter_surah = filter_surah or sid
                # Surə № + axtarış → nəticənin ilk ayəsinə keçə bilək
                if not q_ar:
                    explicit_nav = True
        except (TypeError, ValueError):
            pass

    if page_num is None and page_q not in (None, ''):
        try:
            page_num = int(page_q)
            explicit_nav = True
        except (TypeError, ValueError):
            page_num = None

    if page_num is None and surah_q:
        try:
            page_num = mushaf_lib.surah_start_page(int(surah_q))
            explicit_nav = True
        except (TypeError, ValueError):
            pass

    search_hits: list[dict] = []
    if q_ar and ar_search.has_arabic_letters(q_ar):
        # If surah_num set, also scope search to that surah
        scope = filter_surah
        if scope is None and surah_num_q:
            try:
                sid = int(surah_num_q)
                if 1 <= sid <= 114:
                    scope = sid
            except (TypeError, ValueError):
                pass
        search_hits = ar_search.search_arabic_ayahs(q_ar, surah_id=scope)
        if not explicit_nav and search_hits and search_hits[0].get('page'):
            page_num = search_hits[0]['page']
            highlight_verse = search_hits[0]['verseKey']

    if page_num is None:
        page_num = 1

    page_num = max(1, min(int(page_num), mushaf_lib.PAGE_COUNT))
    page = mushaf_lib.prepare_page_view(page_num)
    surahs = mushaf_lib.load_surah_meta()
    current_surah_idx = mushaf_lib.page_to_surah_index(page_num)
    current_surah = surahs[current_surah_idx] if surahs else None

    if page and highlight_verse:
        for line in page['lines']:
            for w in line['words']:
                w['highlight'] = w.get('verse_key') == highlight_verse

    return render(
        request,
        'dashboard/quran.html',
        {
            'nav': 'quran',
            'page_num': page_num,
            'page_count': mushaf_lib.PAGE_COUNT,
            'page': page,
            'surahs': surahs,
            'current_surah': current_surah,
            'prev_page': page_num - 1 if page_num > 1 else None,
            'next_page': page_num + 1 if page_num < mushaf_lib.PAGE_COUNT else None,
            'mushaf_ready': page is not None,
            'q_ar': q_ar,
            'surah_num': surah_num_q,
            'filter_surah': filter_surah,
            'search_hits': search_hits,
            'highlight_verse': highlight_verse or '',
        },
    )


def mushaf_font(request, filename: str):
    name = Path(filename).name
    if name != filename:
        raise Http404()
    path = mushaf_lib.fonts_dir() / name
    if not path.is_file():
        raise Http404()
    return FileResponse(path.open('rb'), content_type='font/ttf')


def reciters(request):
    return render(request, 'dashboard/reciters.html', {'nav': 'reciters'})
