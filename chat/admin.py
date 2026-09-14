from django.contrib import admin

from .models import ChatGroup, ChatMessage


@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'member_count', 'updated_at')
    search_fields = ('title', 'id')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'sender_name', 'created_at', 'media_type')
    list_filter = ('media_type', 'group')
    search_fields = ('text', 'sender_name', 'id')
