from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.forms import UserCreateView, email_verification
from users.views import MailingRecipientUpdateView, MailingRecipientDeleteView, MailingRecipientListView

app_name = UsersConfig.name

urlpatterns = [
    path('', MailingRecipientListView.as_view(), name='base.html'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('users/<int:pk>/update/', MailingRecipientUpdateView.as_view(), name="users_update"),
    path('users/<int:pk>/delete/', MailingRecipientDeleteView.as_view(), name="users_delete"),
]
