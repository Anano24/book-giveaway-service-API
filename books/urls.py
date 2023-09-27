from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, GenreViewSet, ConditionViewSet


# Create a default router instance for generating URL patterns
router = routers.DefaultRouter()

# Register viewsets for different models with the router, specifying URL prefixes
router.register(r'books', BookViewSet, 'book')
router.register(r'authors', AuthorViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'condition', ConditionViewSet)


# Define the urlpatterns list for routing URLs to views
urlpatterns = [
    path('', include(router.urls)),  # Include the URLs generated by the router
]