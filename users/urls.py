from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import ClientsCreateView, email_verification, ClientsUpdateView, ClientsDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', ClientsCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('client_update/<int:pk>/update/', ClientsUpdateView.as_view(), name="client_update"),
    path('client_delete/<int:pk>/delete/', ClientsDeleteView.as_view(), name="client_delete"),
]
