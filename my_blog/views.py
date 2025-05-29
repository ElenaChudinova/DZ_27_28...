from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from my_blog.models import Blog


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

class BlogCreateView(CreateView):
    model = Blog
    fields = ("blog_name", "description", "image", "category_name", "publication")
    success_url = reverse_lazy('my_blog:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("blog_name", "description", "image", "category_name", "publication")
    success_url = reverse_lazy('my_blog:blog_list')

    def get_success_url(self):
        return reverse('my_blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('my_blog:blog_list')
