from django.urls import path

from sending.apps import SendingConfig
from sending.views import NewsletterListView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView, \
    NewsletterDetailView

app_name = SendingConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name="newsletter_create"),
    path('newsletter/<int:pk>/update/', NewsletterUpdateView.as_view(), name="newsletter_update"),
    path('newsletter/<int:pk>/delete/', NewsletterDeleteView.as_view(), name="newsletter_delete"),
]
