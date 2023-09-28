from rest_framework import serializers
from .models import Author, Genre, Condition, Book


# Define a serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model that this serializer is associated with
        fields = '__all__'  # Include all fields from the model in the serialized representation

class AvailableBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Define a serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


# Define a serializer for the Genre model
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


# Define a serializer for the Condition model
class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

