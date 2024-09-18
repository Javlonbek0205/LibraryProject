

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from yaml import serialize

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
# Create your views here.

##############################################################################
class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned{len(books)} books",
            "books": serializer_data
        }
        return Response(data)

#class BookListApi(generics.ListAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
##############################################################################
class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status": "Succesfull",
                "data": serializer_data
            }
            return Response(data, status = status.HTTP_200_OK )
        except Exception:
            return Response(
            {"status": "Does not exists",
                  "massage": "Book is not found"}, status = status.HTTP_404_NOT_FOUND
            )
#class BookDetailView(generics.RetrieveAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
##############################################################################
class BookDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    "status": True,
                    "Massage": "Successfully deleted"
                }, status= status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {
                    "status": False,
                    "Massage": "Book is not found"
                },status = status.HTTP_400_BAD_REQUEST
            )

#class BookDeleteView(generics.DestroyAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

###############################################################################
class BookUpdateView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id = pk)
        data = request.data
        serializer_data = BookSerializer(instance=book, data = data, partial=True)
        if serializer_data.is_valid(raise_exception=True):
            book_saved = serializer_data.save()

        return Response(
            {
                "status": True,
                "massage": f"Book {book_saved} updated successfully"
            }
        )

#class BookUpdateView(generics.UpdateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

###############################################################################
class BookCreateView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"status": "All books saved",
                    "books": data
            }
            return Response(data)
#class BookCreateView(generics.CreateAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
#################################################################################

#kop tarmaoqli viewlar

#bu GET va POST uchun ochiq
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#bu DELETE va (PUT, PATCH) methodlari uchun ochiq
class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#@api_view(['GET'])
#def book_list_view(self, *args, **kwargs):
#    books = Book.objects.all()
#    serializer = BookSerializer(books, many = True)
#    return Response(serializer.data)
#############################################################################

#viewset va routerlar  orqali endpoint va view yaratish

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    #cdrf.co saytida viewsetlar va barcha viewlarni o'rgansa bo'ladi