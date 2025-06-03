from django.contrib.auth.forms import UserCreationForm
from blog_users.models import BlogUser
from my_blog.forms import StyleFormMixin


class BlogUserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = BlogUser
        fields = ("email", "password1", "password2")

