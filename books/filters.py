import django_filters
from .models import Book


# Define a custom filter class for the Book model
class BookFilter(django_filters.FilterSet):
    # Define filter fields and their lookup expressions
    title = django_filters.CharFilter(lookup_expr='icontains')  # Filter for case-insensitive partial title match


    class Meta:
        model = Book
        fields = ['author', 'title', 'genre', 'location']   # Specify the fields to filter on