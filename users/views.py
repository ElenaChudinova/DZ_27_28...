import secrets

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from users.forms import MailingRecipientForm, MailingRecipientManagerForm
from users.models import MailingRecipient

class MailingRecipientListView(ListView):
    model = MailingRecipient

    def get_queryset(self):
        return MailingRecipient.objects.all()


class MailingRecipientCreateView(CreateView, LoginRequiredMixin):
    model = MailingRecipient
    form_class = MailingRecipientForm
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



class MailingRecipientUpdateView(UpdateView, LoginRequiredMixin):
    model = MailingRecipient
    form_class = MailingRecipientForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingRecipientForm
        if user.has_perm("users.can_edit_subject_letter") and user.has_perm(
                "users.can_edit_letter"):
            return MailingRecipientManagerForm
        raise PermissionDenied



class MailingRecipientDeleteView(DeleteView, LoginRequiredMixin):
    model = MailingRecipient
    success_url = reverse_lazy('users:user_list')
