from django.contrib.auth.models import User
from rest_framework import serializers



# Define a serializer for user creation (registration) with additional password field
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Create a write-only password field

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],   # Extract and set the user's email from validated data
            username=validated_data['username']   # Extract and set the user's username from validated data
        )
        user.set_password(validated_data['password'])   # Set the user's password (hashed)
        user.save()
        return user


 # Define a serializer for user data retrieval   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']