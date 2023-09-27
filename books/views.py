from rest_framework import viewsets, permissions
from .models import Book, Genre, Condition, Author
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer
from .filters import BookFilter



# Define a custom permission class to allow unauthenticated users to access the list view
class UnauthenticatedListPermission(permissions.BasePermission):
    """
    Custom permission to allow unauthenticated users to access the list view.
    """
    def has_permission(self, request, view):
        # Allow GET requests (list view) for unauthenticated users.
        return view.action == 'list' or request.user.is_authenticated


# Define a viewset for the Book model
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()       # Define the queryset for the viewset (all books)
    serializer_class = BookSerializer   # Specify the serializer to use for book objects
    permission_classes = [UnauthenticatedListPermission]  # Apply the custom permission class
    filterset_class = BookFilter        # Apply the custom filter for book objects


# Define a viewset for the Author model
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Define a viewset for the Genre model
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Define a viewset for the Condition model
class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
