from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book

class BookViewTest(APITestCase):

    def test_response_is_correct(self):
        book = Book.objects.create(
            title="Demo",
            description="Description",
            author="Author",
            isbn="1234567890",
            published_date="2025-01-01"
        )

        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]
        assert returned_book["title"] == book.title
        assert returned_book["description"] == book.description
        assert returned_book["author"] == book.author


class HealthViewTest(APITestCase):

    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'

class BookCreateTest(APITestCase):

    def test_create_book(self):
        url = reverse("api:books")

        payload = {
            "title": "The Hobbit",
            "description": "Fantasy novel",
            "author": "J.R.R. Tolkien",
            "isbn": "9780261103344",
            "published_date": "1937-09-21"
        }

        response = self.client.post(url, payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.count() == 1

        book = Book.objects.first()
        assert book.title == payload["title"]
        assert book.author == payload["author"]

class BookDetailTest(APITestCase):

    def test_get_single_book(self):
        book = Book.objects.create(
            title="Demo",
            description="Description",
            author="Author",
            isbn="1234567890",
            published_date="2025-01-01"
        )

        url = reverse("api:book-detail", kwargs={"pk": book.pk})

        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK

        body = response.json()

        assert body["title"] == book.title
        assert body["author"] == book.author

class BookUpdateTest(APITestCase):

    def test_update_book(self):
        book = Book.objects.create(
            title="Old",
            description="Old Description",
            author="Old Author",
            isbn="1111111111",
            published_date="2020-01-01"
        )

        url = reverse("api:book-detail", kwargs={"pk": book.pk})

        payload = {
            "title": "New Title",
            "description": "Updated",
            "author": "New Author",
            "isbn": "1111111111",
            "published_date": "2020-01-01"
        }

        response = self.client.put(url, payload, format="json")

        assert response.status_code == status.HTTP_200_OK

        book.refresh_from_db()

        assert book.title == "New Title"
        assert book.author == "New Author"

class BookDeleteTest(APITestCase):

    def test_delete_book(self):
        book = Book.objects.create(
            title="Delete Me",
            description="Description",
            author="Author",
            isbn="9999999999",
            published_date="2020-01-01"
        )

        url = reverse("api:book-detail", kwargs={"pk": book.pk})

        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Book.objects.count() == 0

class BookNotFoundTest(APITestCase):

    def test_book_not_found(self):
        url = reverse("api:book-detail", kwargs={"pk": 999})

        response = self.client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
