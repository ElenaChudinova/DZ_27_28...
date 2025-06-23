import secrets
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from users.models import Clients
from users.forms import ClientsRegisterForm

class ClientsListView(ListView):
    model = Clients

class ClientsDetailView(DetailView, LoginRequiredMixin):
    model = Clients

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Clients
    form_class = ClientsRegisterForm
    template_name = 'users/client_form.html'
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
    user = get_object_or_404(Clients, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))

class ClientsUpdateView(UpdateView, LoginRequiredMixin):
    model = Clients
    success_url = reverse_lazy('users:client_list')

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:client_detail', args=[self.kwargs.get('pk')])


class ClientsDeleteView(DeleteView, LoginRequiredMixin):
    model = Clients
    success_url = reverse_lazy('users:client_list')