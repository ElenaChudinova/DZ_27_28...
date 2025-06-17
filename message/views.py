from django.contrib.auth.mixins import LoginRequiredMixin

from message.forms import MessageForm
from sending.models import Message
from django.core.exceptions import PermissionDenied
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class MessageListView(ListView):
    model = Message

class MessageCreateView(CreateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('message:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)

class MessageUpdateView(UpdateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('message:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)



class MessageDeleteView(DeleteView, LoginRequiredMixin):
    model = Message
    success_url = reverse_lazy('message:message_list')


