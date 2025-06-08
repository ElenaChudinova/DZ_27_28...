from django.core.cache import cache
from config.settings import CACHE_ENABLED
from my_blog.models import Blog


def get_category_from_cache():
    """Получает данные о блогах из категории 'экстрим' из кэша, если кэш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Blog.objects.filter(id='id')
    key = "category_list"
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Blog.objects.filter(id='id')
    cache.set(key, categories)
    return categories