from django.contrib import admin
from blog_users.models import BlogUser


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

