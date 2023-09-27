from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Book  # Import the Book model

class TakeBookView(APIView):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if book.available:
            book.owner = request.user
            book.available = False
            book.save()
            return Response({"message": "Book taken successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)

class ReturnBookView(APIView):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id, owner=request.user)
        if not book.available:
            book.owner = None
            book.available = True
            book.save()
            return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Book is already available"}, status=status.HTTP_400_BAD_REQUEST)
