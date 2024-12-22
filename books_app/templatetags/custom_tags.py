# your_app/templatetags/custom_filters.py
from django import template
from books_app.models import Books

register = template.Library()

@register.simple_tag
def get_item(category_name):

    return Books.objects.filter(
        availability='On sale',
        category__name=category_name # ManyToMany orqali bog'langan 'name' maydonini tekshirish
    ).order_by('-id')[:8]

@register.simple_tag
def get_item_book(category_name):
    return Books.objects.filter(
        availability='On sale',
        category__name=category_name  # ManyToMany orqali bog'langan 'name' maydonini tekshirish
    ).order_by('-id')[:100]