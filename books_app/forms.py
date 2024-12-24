from django.forms import ModelForm
from django import forms

from .models import Books, Category, Reviews, OrderItem


class ReviewCreateForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('rating', 'text')

class OrderForm(ModelForm):
    class Meta:
        model= OrderItem
        fields = ['quantity']

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ('title',
            'author',
            'price',
            'category',
            'format',
            'availability',
            'book_image',
            'description',
            'publisher',
            'isbn',
            'quantity',
        )