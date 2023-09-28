from rest_framework import viewsets, permissions
from .models import Book, Genre, Condition, Author
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer, AvailableBookSerializer
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
    serializer_class = BookSerializer   # Specify the serializer to use for book objects
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users only
    filterset_class = BookFilter   # Apply the custom filter for book objects

    def get_queryset(self):
        # Filter the queryset to show only books owned by the currently logged-in user
        return Book.objects.filter(owner=self.request.user)


# Define a viewset for available books
class AvailableBookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.filter(available=True)  # Filter books that are available
    serializer_class = AvailableBookSerializer  # Use the custom serializer
    permission_classes = [UnauthenticatedListPermission]  # Allow unauthenticated users to access



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
