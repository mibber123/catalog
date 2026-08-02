from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

class HealthView(APIView):
    """Simple endpoint used by Kubernetes health probes."""
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok"
        })


#
# /api/books - All methods (GET, POST)
#
class BookView(APIView):
    """ List all books, or create a new book """

    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


#
# /api/books/<pk> - All methods (GET, PUT, DELETE)
#
class BookDetailView(APIView):
    """Retrieve, update or delete a single book."""

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk, *args, **kwargs):
        book = self.get_object(pk)

        serializer = BookSerializer(book)

        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        book = self.get_object(pk)

        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        book = self.get_object(pk)

        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

def patch(self, request, pk, *args, **kwargs):
    book = self.get_object(pk)

    serializer = BookSerializer(
        book,
        data=request.data,
        partial=True,
    )

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)

health_view = HealthView.as_view()
book_view = BookView.as_view()
book_detail_view = BookDetailView.as_view()
