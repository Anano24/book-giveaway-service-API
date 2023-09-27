from django.contrib import admin
from .models import Author, Genre, Condition, Book


# Register the (Author, Genre, Condition, and Book) models with the admin site

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Condition)
admin.site.register(Book)
