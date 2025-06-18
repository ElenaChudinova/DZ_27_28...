from django.forms import ModelForm, BooleanField

from .models import Newsletter, MailingAttempt

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ("status_news_letter", "message", "recipients")

class MailingAttemptForm(ModelForm):
    class Meta:
        model = MailingAttempt
        fields = ("status_mailing_attempt", "mail_server_response", "news_letter")