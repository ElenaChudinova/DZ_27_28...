from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from sending.models import MailingAttempt


class Command(BaseCommand):
    help = 'Send messages'

    def handle(self, *args, **kwargs):
        messages = MailingAttempt.objects.filter(is_sent=False)
        for message in messages:
            send_mail(
                message.subject,
                message.body,
                'maknali@yandex.ru',
                ['makkk@list.ru'],
            )
            message.is_sent = True
            message.save()
            self.stdout.write(self.style.SUCCESS(f'Sent: {message.subject}'))