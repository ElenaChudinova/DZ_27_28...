from django.contrib import admin
from sending.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsletter_id', 'first_shipment', 'end_shipment', 'status_news_letter', 'message')
