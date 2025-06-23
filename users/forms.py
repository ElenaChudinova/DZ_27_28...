from django.contrib.auth.forms import UserCreationForm

from sending.forms import StyleFormMixin
from users.models import Clients


class ClientsRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = Clients
        fields = ("email", "password1", "password2")







