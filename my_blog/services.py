from django.core.cache import cache

from config.settings import CACHE_ENABLED
from my_blog.models import Blog


def get_my_blog_from_cache():
    """Получает данные об опубликованных блогах из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Blog.objects.filter(publication=True)
    key = "blogs_list"
    blogs = cache.get(key)
    if blogs is not None:
        return blogs
    blogs = Blog.objects.filter(publication=True)
    cache.set(key, blogs)
    return blogs