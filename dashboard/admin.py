from django.contrib import admin

from .models import AppContent, Juz30Segment, PageNote, SummaryNote, WordMarkNote


@admin.register(WordMarkNote)
class WordMarkNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'direction', 'words_preview', 'updated_at')
    list_filter = ('kind', 'direction')
    search_fields = ('waqf_note', 'istinaf_note')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-updated_at',)

    @admin.display(description='Sözlər')
    def words_preview(self, obj: WordMarkNote) -> str:
        parts = []
        for w in (obj.words or [])[:6]:
            if not isinstance(w, dict):
                continue
            vk = w.get('verseKey') or ''
            text = (w.get('text') or '').strip()
            pos = w.get('position')
            if vk and pos:
                parts.append(f'{vk}#{pos}' + (f' {text}' if text else ''))
        more = len(obj.words or []) - 6
        s = ' · '.join(parts) if parts else '—'
        if more > 0:
            s += f' (+{more})'
        return s


@admin.register(PageNote)
class PageNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'page', 'body_preview', 'updated_at')
    search_fields = ('body',)
    ordering = ('page',)
    readonly_fields = ('created_at', 'updated_at')

    @admin.display(description='Qeyd')
    def body_preview(self, obj: PageNote) -> str:
        t = (obj.body or '').strip().replace('\n', ' ')
        return t[:80] + ('…' if len(t) > 80 else '')


@admin.register(SummaryNote)
class SummaryNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'scope', 'surah', 'ayah', 'text_preview', 'updated_at')
    list_filter = ('scope',)
    search_fields = ('text',)
    ordering = ('surah', 'ayah', 'id')

    @admin.display(description='Mətn')
    def text_preview(self, obj: SummaryNote) -> str:
        t = (obj.text or '').strip().replace('\n', ' ')
        return t[:80] + ('…' if len(t) > 80 else '')


@admin.register(AppContent)
class AppContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Juz30Segment)
class Juz30SegmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'words_preview', 'updated_at')
    search_fields = ('summary_note', 'azbar_note')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-updated_at',)

    @admin.display(description='Sözlər')
    def words_preview(self, obj: Juz30Segment) -> str:
        parts = []
        for w in (obj.words or [])[:6]:
            if not isinstance(w, dict):
                continue
            vk = w.get('verseKey') or ''
            text = (w.get('text') or '').strip()
            pos = w.get('position')
            if vk and pos:
                parts.append(f'{vk}#{pos}' + (f' {text}' if text else ''))
        more = len(obj.words or []) - 6
        s = ' · '.join(parts) if parts else '—'
        if more > 0:
            s += f' (+{more})'
        return s
