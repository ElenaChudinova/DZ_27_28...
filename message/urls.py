from django.urls import path
from django.views.decorators.cache import cache_page

from message.apps import MessageConfig
from message.views import MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MessageConfig.name

urlpatterns = [
    # path('', MessageListView.as_view(), name='message_list'),
    # path('message/<int:pk>/', cache_page(60)(MessageDetailView.as_view()), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name="blog_create"),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name="message_update"),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name="message_delete"),
]
