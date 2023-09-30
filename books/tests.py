from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Genre, Condition, Book
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ConditionSerializer
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Test Genre')
        self.condition = Condition.objects.create(name='New')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            location='Library',
            condition=self.condition,
            owner=self.user,
            cover_image='media/book_cover/image.jpg'  # Specify the path to your cover image
        )
        # self.book.genre.add(self.genre)
        self.book.genre.set([self.genre])

    def test_author_model(self):
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(str(author), 'Test Author')

    def test_genre_model(self):
        genre = Genre.objects.get(id=self.genre.id)
        self.assertEqual(str(genre), 'Test Genre')

    def test_condition_model(self):
        condition = Condition.objects.get(id=self.condition.id)
        self.assertEqual(str(condition), 'New')

    def test_book_model(self):
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(str(book), 'Test Book')



class SerializerTestCase(TestCase):
    def test_book_serializer(self):
        # Create Author, Genre, and Condition objects with valid primary keys
        author = Author.objects.create(name='Test Author')
        genre = Genre.objects.create(name='Test Genre')
        condition = Condition.objects.create(name='New')

        book_data = {
            'title': 'Serializer Test Book',
            'author': author.pk,  # Assign the primary key of the Author object
            'genre': [genre.pk],  # Assign a list of primary keys for Genre objects
            'location': 'Library',
            'condition': condition.pk,  # Assign the primary key of the Condition object
            'owner': None,
            'available': True,
            'cover_image': None
        }

        serializer = BookSerializer(data=book_data)

        if not serializer.is_valid():
            print(serializer.errors)

        self.assertTrue(serializer.is_valid())



    def test_author_serializer(self):
        author_data = {
            'name': 'Test Author',
        }

        serializer = AuthorSerializer(data=author_data)

        if not serializer.is_valid():
            print(serializer.errors)

        self.assertTrue(serializer.is_valid())



    def test_genre_serializer(self):
        genre_data = {
            'name': 'Test Genre',
        }

        serializer = GenreSerializer(data=genre_data)
        if not serializer.is_valid():
            print(serializer.errors)
        
        self.assertTrue(serializer.is_valid())



    def test_condition_serializer(self):
        condition_data = {
            'name': 'Test Condition',
        }

        serializer = ConditionSerializer(data=condition_data)
        if not serializer.is_valid():
            print(serializer.errors)
        
        self.assertTrue(serializer.is_valid())



class AvailableBookTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.author = Author.objects.create(name='Test Author')
        self.genre = Genre.objects.create(name='Test Genre')
        self.condition = Condition.objects.create(name='New')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            location='Library',
            condition=self.condition,
            owner=self.user,
            cover_image='media/book_cover/image.jpg' 
        )
        self.book.genre.set([self.genre])

    def test_book_list_view(self):
        response = self.client.get('/available-books/')  
        self.assertEqual(response.status_code, 200)


    

class AuthorViewSetTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword') # Create a user
        self.client.force_authenticate(user=user)
        self.author = Author.objects.create(name='Test Author')
        self.url = reverse('author-list')  

    def test_list_authors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class GenreViewSetTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword') # Create a user
        self.client.force_authenticate(user=user)
        self.author = Genre.objects.create(name='Test Genre')
        self.url = reverse('genre-list')  

    def test_list_Genre(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class ConditionViewSetTestCase(APITestCase):
    def setUp(self):
        self.condition = Condition.objects.create(name='Test Condition')
        self.url = reverse('condition-list')

    def test_list_conditions(self): 
        user = User.objects.create_user(username='testuser', password='testpassword') # Create a user
        self.client.force_authenticate(user=user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_condition(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)
        data = {'name': 'New Condition'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_create_condition(self):
        data = {'name': 'New Condition'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_update_condition(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)
        data = {'name': 'Updated Condition'}
        response = self.client.put(reverse('condition-detail', args=[self.condition.pk]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_condition(self):
        data = {'name': 'Updated Condition'}
        response = self.client.put(reverse('condition-detail', args=[self.condition.pk]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


