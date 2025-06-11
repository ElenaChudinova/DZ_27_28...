from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from my_blog.models import Blog, Category
from my_blog.forms import BlogForm, BlogModeratorForm
from my_blog.services import get_category_from_cache


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(publication=True)



class BlogCategoryDetailView(DetailView):
    model = Blog
    template_name =  'my_blog/categories.html'

    def get_context_data(self, **kwargs):
        categories = self.object.id
        context = super().get_context_data(**kwargs)
        context['categories'] = get_category_from_cache(categories)
        return context



class BlogDetailView(DetailView, LoginRequiredMixin):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied



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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return BlogForm
        if user.has_perm("my_blog.can_unpublish_blog") and user.has_perm(
                "my_blog.can_edit_blog_name") and user.has_perm("my_blog.can_edit_description"):
            return BlogModeratorForm
        raise PermissionDenied



class BlogDeleteView(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('my_blog:blog_list')
