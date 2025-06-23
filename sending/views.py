from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from sending.forms import NewsletterForm, MessageForm, MailingRecipientForm
from sending.models import Newsletter, Message, MailingRecipient


class HomeListView(ListView):
    model = MailingRecipient
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'newsletter_all': Newsletter.objects.all(),
            'newsletter': Newsletter.objects.filter(status_news_letter=self.request.LAUNCHED),
            'mailings': MailingRecipient.objects.upcoming(),
        })
        return ctx

class MailingRecipientCreateView(CreateView, LoginRequiredMixin):
    model = MailingRecipient
    form_class = MailingRecipientForm

    def get_queryset(self):
        return MailingRecipient.objects.filter(pk=self.request.user.pk)

class MailingRecipientUpdateView(UpdateView, LoginRequiredMixin):
    model = MailingRecipient
    form_class = MailingRecipientForm
    success_url = reverse_lazy('sending:mailing_recipient_list')

class MailingRecipientDeleteView(DeleteView, LoginRequiredMixin):
    model = MailingRecipient
    success_url = reverse_lazy('sending:mailing_recipient_list')


class MessageListView(ListView):
    model = Message

class MessageDetailView(DetailView, LoginRequiredMixin):
    model = Message

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied

class MessageCreateView(CreateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('sending:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)

class MessageUpdateView(UpdateView, LoginRequiredMixin):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('sending:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageDeleteView(DeleteView, LoginRequiredMixin):
    model = Message
    success_url = reverse_lazy('sending:message_list')


class NewsletterListView(ListView):
    model = Newsletter

    def get_queryset(self):
        all = Newsletter.objects.all()
        launched = Newsletter.objects.filter(STATUS_MAILING='LAUNCHED')
        return all, launched

class NewsletterDetailView(DetailView, LoginRequiredMixin):
    model = Newsletter

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied

class NewsletterCreateView(CreateView, LoginRequiredMixin):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('sending:newsletter_list')

    def form_valid(self, form):
        sending = form.save()
        user = self.request.user
        sending.owner = user
        sending.save()
        return super().form_valid(form)

class NewsletterUpdateView(UpdateView, LoginRequiredMixin):
    model = Newsletter
    form_class = MessageForm
    success_url = reverse_lazy('sending:newsletter_list')

    def form_valid(self, form):
        sending = form.save()
        user = self.request.user
        sending.owner = user
        sending.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('message:middleware_detail', args=[self.kwargs.get('pk')])


class NewsletterDeleteView(DeleteView, LoginRequiredMixin):
    model = Newsletter
    success_url = reverse_lazy('sending:newsletter_list')
