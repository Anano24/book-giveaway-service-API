from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from books.models import Author, Genre, Condition, Book
from rest_framework.test import APITestCase

class BookHubAPITest(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an author, genre, condition, and a book
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Fiction')
        self.condition = Condition.objects.create(name='New')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            condition=self.condition,
            location='Library',
            cover_image='media/book_cover/image.jpg'  # Specify the path to your cover image
        )
        self.book.genre.add(self.genre)
        self.book.owner = self.user
        self.book.save()

        # Create a client for making API requests and authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_take_book(self):
        response = self.client.post(f'/books/{self.book.id}/take/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Book taken successfully')
        self.book.refresh_from_db()
        self.assertFalse(self.book.available)
        self.assertEqual(self.book.owner, self.user)

    def test_take_unavailable_book(self):
        # Make the book unavailable
        self.book.available = False
        self.book.save()

        response = self.client.post(f'/books/{self.book.id}/take/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Book is not available')

    def test_return_book(self):
        # Take the book first
        self.client.post(f'/books/{self.book.id}/take/')

        response = self.client.post(f'/books/{self.book.id}/return/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Book returned successfully')
        self.book.refresh_from_db()
        self.assertTrue(self.book.available)
        self.assertIsNone(self.book.owner)

    def test_return_already_available_book(self):
        response = self.client.post(f'/books/{self.book.id}/return/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Book is already available')



