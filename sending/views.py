from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from message.forms import MessageForm
from sending.forms import NewsletterForm
from sending.models import Newsletter

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
