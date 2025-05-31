import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from blog_users.forms import BlogUserRegisterForm
from blog_users.models import BlogUser

from config.settings import EMAIL_HOST_USER


class BlogUserCreateView(LoginRequiredMixin, CreateView):
    model = BlogUser
    form_class = BlogUserRegisterForm
    template_name = 'bloguser_form.html'
    success_url = reverse_lazy('blog_users:login')

    def form_valid(self, form):
        form.instaance.user = self.request.user
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(15)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/blog_users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(BlogUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("blog_users:login"))

class BlogUserUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogUser
    form_class = BlogUserRegisterForm
    template_name = 'bloguser_form.html'
    success_url = reverse_lazy('blog_users:login')

    def form_valid(self, form):
        form.instaance.user = self.request.user
        return super().form_valid(form)

class BlogUserDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogUser
    form_class = BlogUserRegisterForm
    template_name = 'bloguser_form.html'
    success_url = reverse_lazy('blog_users:login')

    def form_valid(self, form):
        form.instaance.user = self.request.user
        return super().form_valid(form)