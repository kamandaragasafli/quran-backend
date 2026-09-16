from django.db import models
from django.utils import timezone


# Tətbiqdəki eyni rəng sistemi (wordInkMarks / wordAboutNotes)
COLOR_WAQF = '#E53935'
COLOR_ISTINAF = '#43A047'
COLOR_QIRAAT = '#1E88E5'
COLOR_GRAD_MID = 'rgba(0, 0, 0, 0)'


class AppContent(models.Model):
    """Tətbiq mətnləri — Haqqında, Məal giriş, Qarilər (admin ↔ API)."""

    KEY_ABOUT = 'about'
    KEY_MEAL_INTRO = 'meal_intro'
    KEY_RECITERS = 'reciters'
    KEY_CHOICES = [
        (KEY_ABOUT, 'Haqqında'),
        (KEY_MEAL_INTRO, 'Məal giriş'),
        (KEY_RECITERS, 'Qarilər'),
    ]

    key = models.SlugField(max_length=40, unique=True, choices=KEY_CHOICES)
    data = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['key']
        verbose_name = 'Tətbiq mətnı'
        verbose_name_plural = 'Tətbiq mətnləri'

    def __str__(self):
        return dict(self.KEY_CHOICES).get(self.key, self.key)

    @classmethod
    def get_or_seed(cls, key: str) -> 'AppContent':
        from .content_defaults import default_for

        obj, created = cls.objects.get_or_create(key=key, defaults={'data': default_for(key)})
        if created or not obj.data:
            obj.data = default_for(key)
            obj.save(update_fields=['data', 'updated_at'])
        return obj

    def to_api(self) -> dict:
        return {
            'key': self.key,
            'data': self.data or {},
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class SummaryNote(models.Model):
    SCOPE_SURAH = 'surah'
    SCOPE_AYAH = 'ayah'
    SCOPE_CHOICES = [
        (SCOPE_SURAH, 'Surə'),
        (SCOPE_AYAH, 'Ayə'),
    ]

    scope = models.CharField(max_length=8, choices=SCOPE_CHOICES, default=SCOPE_SURAH)
    surah = models.PositiveSmallIntegerField()
    ayah = models.PositiveSmallIntegerField(null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        indexes = [
            models.Index(fields=['surah', 'ayah']),
        ]

    def __str__(self):
        if self.scope == self.SCOPE_AYAH and self.ayah:
            return f'{self.surah}:{self.ayah}'
        return f'Surə {self.surah}'

    @property
    def label(self) -> str:
        if self.scope == self.SCOPE_AYAH and self.ayah:
            return f'{self.surah}:{self.ayah}'
        return f'Surə {self.surah}'


class WordMarkNote(models.Model):
    """
    Mushaf söz seçimi — vəqf / istinaf və ya qiraət qeydi.
    Tətbiqdə: ink rəngi + AyahInfoSheet «Haqqında».
    """

    KIND_WAQF_ISTINAF = 'waqf_istinaf'
    KIND_QIRAAT = 'qiraat'
    KIND_CHOICES = [
        (KIND_WAQF_ISTINAF, 'Vəqf / İstinaf'),
        (KIND_QIRAAT, 'Qiraət Qeydi'),
    ]

    DIR_ISTINAF_FIRST = 'istinaf_first'  # yaşıl → … → qırmızı
    DIR_WAQF_FIRST = 'waqf_first'        # qırmızı → … → yaşıl
    DIR_CHOICES = [
        (DIR_ISTINAF_FIRST, 'İstinaf → Vəqf'),
        (DIR_WAQF_FIRST, 'Vəqf → İstinaf'),
    ]

    words = models.JSONField(
        default=list,
        help_text='[{"verseKey":"1:5","position":2,"text":"..."}]',
    )
    kind = models.CharField(
        max_length=20,
        choices=KIND_CHOICES,
        default=KIND_WAQF_ISTINAF,
    )
    direction = models.CharField(
        max_length=20,
        choices=DIR_CHOICES,
        default=DIR_ISTINAF_FIRST,
    )
    waqf_note = models.TextField(blank=True, default='')
    istinaf_note = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        keys = []
        for w in self.words or []:
            vk = w.get('verseKey') or ''
            pos = w.get('position')
            if vk and pos:
                keys.append(f'{vk}#{pos}')
        return ' '.join(keys[:4]) or f'WordMark#{self.pk}'

    def _word_items(self) -> list[dict]:
        out = []
        for raw in self.words or []:
            if not isinstance(raw, dict):
                continue
            vk = str(raw.get('verseKey') or '').strip()
            try:
                pos = int(raw.get('position'))
            except (TypeError, ValueError):
                continue
            text = str(raw.get('text') or '').strip()
            if not vk or pos < 1:
                continue
            out.append({'verseKey': vk, 'position': pos, 'text': text})
        return out

    def to_ink_marks(self) -> list[dict]:
        items = self._word_items()
        if not items:
            return []

        if self.kind == self.KIND_QIRAAT:
            # Həmişə yalnız ilk və son söz mavi (tək sözdə həmin söz)
            n = len(items)
            targets = items if n == 1 else [items[0], items[-1]]
            return [
                {
                    'verseKey': w['verseKey'],
                    'position': w['position'],
                    'color': COLOR_QIRAAT,
                    'noteId': self.pk,
                }
                for w in targets
            ]

        has_w = bool((self.waqf_note or '').strip())
        has_i = bool((self.istinaf_note or '').strip())
        # Qeyd istəyə bağlı — boş olsa da işarələ
        if not has_w and not has_i:
            has_w = True
            has_i = True

        marks: list[dict] = []
        n = len(items)

        # İki+ söz + hər iki tərəf
        if n >= 2 and has_w and has_i:
            first = items[0]
            last = items[-1]
            if self.direction == self.DIR_WAQF_FIRST:
                first_color, last_color = COLOR_WAQF, COLOR_ISTINAF
            else:
                first_color, last_color = COLOR_ISTINAF, COLOR_WAQF
            marks.append(
                {
                    'verseKey': first['verseKey'],
                    'position': first['position'],
                    'color': first_color,
                    'noteId': self.pk,
                }
            )
            marks.append(
                {
                    'verseKey': last['verseKey'],
                    'position': last['position'],
                    'color': last_color,
                    'noteId': self.pk,
                }
            )
            return marks

        for i, w in enumerate(items):
            mark: dict = {
                'verseKey': w['verseKey'],
                'position': w['position'],
                'noteId': self.pk,
            }
            if has_w and has_i:
                # Tək söz — gradient (istiqamətə görə)
                if self.direction == self.DIR_WAQF_FIRST:
                    mark['textGradient'] = [COLOR_WAQF, COLOR_GRAD_MID, COLOR_ISTINAF]
                else:
                    mark['textGradient'] = [COLOR_ISTINAF, COLOR_GRAD_MID, COLOR_WAQF]
            elif has_w:
                mark['color'] = COLOR_WAQF
            else:
                mark['color'] = COLOR_ISTINAF
            marks.append(mark)
        return marks

    def to_about_notes(self) -> list[dict]:
        items = self._word_items()
        if not items:
            return []

        if self.kind == self.KIND_QIRAAT:
            body = (self.waqf_note or '').strip()
            lemma = ' '.join(w['text'] for w in items if w['text']) or items[0]['verseKey']
            n = len(items)
            # Tam seçim — ilk/son mavi, ortadakılar normal (etiket yox)
            examples = []
            for i, w in enumerate(items):
                text = (w.get('text') or '').strip()
                if not text:
                    continue
                is_edge = n == 1 or i == 0 or i == n - 1
                examples.append(
                    {
                        'label': '',
                        'arabic': text,
                        'color': COLOR_QIRAAT if is_edge else '',
                    }
                )
            # Haqqında — seçimin əhatə etdiyi hər ayə üçün eyni tam ifadə
            by_verse: dict[str, list[dict]] = {}
            for w in items:
                by_verse.setdefault(w['verseKey'], []).append(w)
            notes = []
            for vk, words in by_verse.items():
                verse_lemma = ' '.join(w['text'] for w in words if w['text']) or vk
                notes.append(
                    {
                        'verseKey': vk,
                        'lemma': lemma or verse_lemma,
                        'body': body,
                        'examples': examples,
                        'positions': [w['position'] for w in words],
                    }
                )
            return notes

        waqf = (self.waqf_note or '').strip()
        istinaf = (self.istinaf_note or '').strip()
        has_w = bool(waqf)
        has_i = bool(istinaf)
        # Qeyd istəyə bağlı — boş olsa da Haqqında göstərilsin
        if not has_w and not has_i:
            has_w = True
            has_i = True

        body_parts = []
        if waqf:
            body_parts.append(waqf)
        if istinaf:
            body_parts.append(istinaf)
        body = '\n\n'.join(body_parts)

        by_verse: dict[str, list[dict]] = {}
        for w in items:
            by_verse.setdefault(w['verseKey'], []).append(w)

        notes = []
        for vk, words in by_verse.items():
            lemma = ' '.join(w['text'] for w in words if w['text']) or vk
            n = len(words)
            examples = []
            if n >= 2 and has_w and has_i:
                first = words[0]['text'] or lemma
                last = words[-1]['text'] or lemma
                examples.append(
                    {
                        'label': 'İstināf',
                        'arabic': first,
                        'color': COLOR_ISTINAF,
                        'icon': 'play-back',
                    }
                )
                examples.append(
                    {
                        'label': 'Vəqf',
                        'arabic': last,
                        'color': COLOR_WAQF,
                        'icon': 'stop',
                    }
                )
            elif has_w and has_i:
                examples.append(
                    {
                        'label': 'Vəqf halında',
                        'arabic': lemma,
                        'color': COLOR_WAQF,
                        'icon': 'stop',
                    }
                )
                examples.append(
                    {
                        'label': 'İstināf halında',
                        'arabic': lemma,
                        'color': COLOR_ISTINAF,
                        'icon': 'play-back',
                    }
                )
            elif has_w:
                examples.append(
                    {
                        'label': 'Vəqf',
                        'arabic': lemma,
                        'color': COLOR_WAQF,
                        'icon': 'stop',
                    }
                )
            else:
                examples.append(
                    {
                        'label': 'İstināf',
                        'arabic': lemma,
                        'color': COLOR_ISTINAF,
                        'icon': 'play-back',
                    }
                )

            notes.append(
                {
                    'verseKey': vk,
                    'lemma': lemma,
                    'body': body,
                    'examples': examples,
                    'positions': [w['position'] for w in words],
                }
            )
        return notes
