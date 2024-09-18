from django.urls import path
from .views import BookListApi, BookDetailView, BookUpdateView, \
    BookDeleteView, BookCreateView, BookListCreateView, BookUpdateDeleteView, BookViewSet
#book_list_view,
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('booklistcreate/', BookListCreateView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view()),
    # path('books/', BookListApi.as_view()),
    # path('books/create/', BookCreateView.as_view()),
    # path('books/<int:pk>/', BookDetailView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateView.as_view()),
    #path('books/', book_list_view),
   # ctrl + /
]

urlpatterns += router.urls