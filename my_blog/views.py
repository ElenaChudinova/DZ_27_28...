from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from my_blog.models import Blog
from my_blog.forms import BlogForm


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(publication=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class BlogCreateView(CreateView, LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('my_blog:blog_list')

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)

class BlogUpdateView(UpdateView, LoginRequiredMixin):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('my_blog:blog_list')

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my_blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('my_blog:blog_list')

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.owner = user
        blog.save()
        return super().form_valid(form)
