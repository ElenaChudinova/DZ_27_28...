from django.contrib import admin
from users.models import MailingRecipient


@admin.register(MailingRecipient)
class MailingRecipientAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'comment')
