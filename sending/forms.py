from django.forms import ModelForm, BooleanField

from users.forms import YourForm
from .models import Newsletter, MailingAttempt

class NewsletterForm(YourForm, ModelForm):
    class Meta:
        model = Newsletter
        fields = ("status_news_letter", "message", "recipients")

class MailingAttemptForm(YourForm, ModelForm):
    class Meta:
        model = MailingAttempt
        fields = ("status_mailing_attempt", "mail_server_response", "news_letter")