from django.urls import path
from .views import (add_to_cart_ajax,
                    BookListView,
                    BookDetailView,
                    AllBookListView,)
                    #books_list_view,
                    #books_detail_view,
                    #all_books_list_view,
urlpatterns = [
     path('', BookListView.as_view(), name='home'),
    #path('', books_list_view, name='home'),
     path('add-to-cart/', add_to_cart_ajax, name='add_to_cart_ajax'),
     path('all_books/', AllBookListView.as_view(), name='all_books'),
    #path('all_books/', all_books_list_view, name='all_books'),
     path('book_detail/<int:pk>/', BookDetailView.as_view(), name='books-detail'),
     #path('book_detail/<int:pk>/', books_detail_view, name='books-detail'),
 ]