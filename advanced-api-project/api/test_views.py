from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some books
        self.book1 = Book.objects.create(title='Python 101', author='Mark')
        self.book2 = Book.objects.create(title='Clean Code', author='Robert')

        # Set API client
        self.client = APIClient()

        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
    
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_unauthenticated(self):
        data = {'title': 'New Book', 'author': 'Alice'}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'New Book', 'author': 'Alice'}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {'title': 'Python 102', 'author': 'Mark'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Python 102')

    def test_update_book_unauthenticated(self):
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {'title': 'Python 102', 'author': 'Mark'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_filter_books(self):
        response = self.client.get(self.list_url, {'title': 'Python 101'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python 101')

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Robert'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Robert')

    def test_order_books(self):
        response = self.client.get(self.list_url, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Python 101')  
