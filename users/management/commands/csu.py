from django.core.management import BaseCommand
from users.models import Clients


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = Clients.objects.create(email="ovetganna_admin@example.com")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
