from django.contrib import admin
from .models import Blog, Category

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    idlelib = ('id',)
    list_display = ('id', 'blog_name', 'created_at', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('blog_name', 'description',)

@admin.register(Category)
class BlogAdmin(admin.ModelAdmin):
    idlelib = ('id',)
    list_display = ('id', 'category_name', 'description')
    list_filter = ('category_name',)
