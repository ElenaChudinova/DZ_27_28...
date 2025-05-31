import secrets

from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog_users.forms import BllogUserRegisterForm
from blog_users.models import BlogUser

from config.settings import EMAIL_HOST_USER


class BlogUserCreateView(CreateView):
    model = BlogUser
    form_class = BllogUserRegisterForm
    success_url = reverse_lazy('blog_users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(15)
        host = self.request.get_host()
        url = f'http://{host}/blog_users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f'Привет, перейди по ссылке для подтверждения почты{url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

