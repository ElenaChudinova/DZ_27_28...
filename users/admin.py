from django.contrib import admin
from users.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'phone', 'country', )
