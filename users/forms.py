import secrets

from django import forms
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.forms import ModelForm, BooleanField
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from message.forms import StyleFormMixin
from .models import MailingRecipient


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = MailingRecipient
        fields = ("email", "password1", "password2")


class UserCreateView(CreateView):
    model = MailingRecipient
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(MailingRecipient, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class YourForm(forms.Form):
    pass

class MailingRecipientForm(YourForm, ModelForm):
    class Meta:
        model = MailingRecipient
        fields = ("email", "username", "comment")

class MailingRecipientManagerForm(YourForm, StyleFormMixin, ModelForm):
    class Meta:
        model = MailingRecipient
        fields = ("email", "username", "comment")
