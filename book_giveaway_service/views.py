from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserSerializer


# Define an API view for creating user accounts
class UserCreateView(APIView):
    permission_classes = [AllowAny]  # Allow any user (unauthenticated) to access this view

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)  # Create a user serializer instance
        if serializer.is_valid():
            user = serializer.save()  # Save the user data if it's valid
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)  # Return a success response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   # Return validation errors if data is invalid



# Define an API view for retrieving the current authenticated user
class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)  # Require authentication to access this view

    def get(self, request):
        serializer = UserSerializer(request.user)  # Serialize the current user's data
        return Response(serializer.data)  # Return the serialized user data