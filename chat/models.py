from django.db import models


class ChatGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    telegram_chat_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, default='')
    member_count = models.PositiveIntegerField(default=0)
    accent = models.CharField(max_length=16, default='#4A9BC7')
    icon = models.CharField(max_length=32, default='people')
    updated_at = models.BigIntegerField()

    class Meta:
        db_table = 'groups'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def to_api(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'memberCount': self.member_count,
            'accent': self.accent,
            'icon': self.icon,
            'updatedAt': self.updated_at,
        }


class ChatMessage(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    group = models.ForeignKey(
        ChatGroup,
        on_delete=models.CASCADE,
        related_name='messages',
        db_column='group_id',
    )
    telegram_message_id = models.BigIntegerField()
    sender_id = models.BigIntegerField(null=True, blank=True)
    sender_name = models.CharField(max_length=255, blank=True, default='')
    text = models.TextField(blank=True, default='')
    created_at = models.BigIntegerField()
    media_type = models.CharField(max_length=32, null=True, blank=True)
    media_file = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'messages'
        ordering = ['created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['group', 'telegram_message_id'],
                name='uniq_group_telegram_message',
            ),
        ]
        indexes = [
            models.Index(fields=['group', '-created_at'], name='idx_messages_group_created'),
        ]

    def __str__(self):
        return f'{self.group_id}:{self.telegram_message_id}'

    def to_api(self):
        return {
            'id': self.id,
            'groupId': self.group_id,
            'senderId': self.sender_id,
            'senderName': self.sender_name,
            'text': self.text,
            'createdAt': self.created_at,
            'telegramMessageId': self.telegram_message_id,
            'mediaType': self.media_type or None,
            'mediaUrl': f'/media/{self.media_file}' if self.media_file else None,
            'duration': self.duration,
        }
