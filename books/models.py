# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User



# Define a model for authors
class Author(models.Model):
    name = models.CharField(max_length=100) # Define a character field for author names
    
    def __str__(self):
        return self.name # Define a human-readable string representation for author objects


# Define a model for book genres
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


# Define a model for book conditions
class Condition(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


# Define a model for books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books_written', on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')
    condition = models.ForeignKey(Condition, related_name='books_condition', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='books_owned', on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
