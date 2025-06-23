from django.urls import path
from django.views.decorators.cache import cache_page

from sending.apps import SendingConfig, MessageConfig, MailingRecipientConfig
from sending.views import NewsletterListView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView, \
    NewsletterDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MessageDetailView, MessageListView, \
    HomeListView

app_name = SendingConfig.name, MessageConfig.name, MailingRecipientConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name="newsletter_create"),
    path('newsletter_update/<int:pk>/', NewsletterUpdateView.as_view(), name="newsletter_update"),
    path('newsletter_delete/<int:pk>/', NewsletterDeleteView.as_view(), name="newsletter_delete"),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name="blog_create"),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name="message_update"),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name="message_delete"),
]
