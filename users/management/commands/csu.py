from django.core.management import BaseCommand
from users.models import MailingRecipient


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = MailingRecipient.objects.create(email="ovetganna_admin@example.com")
        user.set_password("123asd")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
