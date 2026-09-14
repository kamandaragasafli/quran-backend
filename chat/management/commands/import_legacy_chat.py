"""Import groups/messages from the old Node SQLite chat.db."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from chat.models import ChatGroup, ChatMessage


class Command(BaseCommand):
    help = 'Import legacy Node chat.db into Django models'

    def add_arguments(self, parser):
        parser.add_argument(
            'db_path',
            nargs='?',
            default=str(Path(settings.BASE_DIR).parent / 'quran-app' / 'backend' / 'data' / 'chat.db'),
            help='Path to legacy chat.db',
        )

    def handle(self, *args, **options):
        db_path = Path(options['db_path'])
        if not db_path.is_file():
            raise CommandError(f'DB tapılmadı: {db_path}')

        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        groups = cur.execute('SELECT * FROM groups').fetchall()
        messages = cur.execute('SELECT * FROM messages').fetchall()
        conn.close()

        created_g = updated_g = created_m = skipped_m = 0

        with transaction.atomic():
            for row in groups:
                defaults = {
                    'telegram_chat_id': row['telegram_chat_id'],
                    'title': row['title'],
                    'subtitle': row['subtitle'] or '',
                    'member_count': row['member_count'] or 0,
                    'accent': row['accent'] or '#4A9BC7',
                    'icon': row['icon'] or 'people',
                    'updated_at': row['updated_at'],
                }
                obj, created = ChatGroup.objects.update_or_create(
                    id=row['id'],
                    defaults=defaults,
                )
                if created:
                    created_g += 1
                else:
                    updated_g += 1

            for row in messages:
                if ChatMessage.objects.filter(pk=row['id']).exists():
                    skipped_m += 1
                    continue
                if not ChatGroup.objects.filter(pk=row['group_id']).exists():
                    skipped_m += 1
                    continue
                ChatMessage.objects.create(
                    id=row['id'],
                    group_id=row['group_id'],
                    telegram_message_id=row['telegram_message_id'],
                    sender_id=row['sender_id'],
                    sender_name=row['sender_name'] or '',
                    text=row['text'] or '',
                    created_at=row['created_at'],
                    media_type=row['media_type'] if 'media_type' in row.keys() else None,
                    media_file=row['media_file'] if 'media_file' in row.keys() else None,
                    duration=row['duration'] if 'duration' in row.keys() else None,
                )
                created_m += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Groups +{created_g}/~{updated_g}, messages +{created_m} (skip {skipped_m})'
            )
        )
