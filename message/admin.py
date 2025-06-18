from django.contrib import admin
from message.models import Message


@admin.register(Message)
class MailingRecipientAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'subject_letter', 'letter', 'owner')