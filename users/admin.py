from django.contrib import admin
from users.models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('сlient_id', 'email', 'сlient_name', 'phone', 'country', )
