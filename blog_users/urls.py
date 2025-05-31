from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from blog_users.apps import BlogUsersConfig
from blog_users.views import BlogUserCreateView, email_verification, BlogUserUpdateView, BlogUserDeleteView

app_name = BlogUsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', BlogUserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('update/', BlogUserUpdateView.as_view(), name='update'),
    path('delete/', BlogUserDeleteView.as_view(), name='delete'),
]
