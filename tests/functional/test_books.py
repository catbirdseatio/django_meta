import pytest
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains, assertNotContains
from tests.factories import BookFactory, ReviewFactory


pytestmark = pytest.mark.django_db


class TestBookListView:
    @pytest.fixture(scope="function")
    def response(self, client, test_book, test_user):
        client.force_login(test_user)
        yield client.get(reverse("books:list"))

    def test_get_success(self, response):
        assert response.status_code == 200

    def test_get_books_in_template(self, response, test_book):
        assert test_book.title in str(response.content)

    def test_assert_template_used(self, response):
        assertTemplateUsed(response, "books/list.html")

    def test_multiple_books(self, test_five_books, client, test_user):
        client.force_login(test_user)
        response = client.get(reverse("books:list"))
        assertContains(response, 'class="title"', 5)


class TestBookDetailView:
    @pytest.fixture(scope="function")
    def response(self, client, test_book, test_user):
        client.force_login(test_user)
        yield client.get(reverse("books:detail", args=[str(test_book.id)]))

    def test_get_success(self, response):
        assert response.status_code == 200
        assert response.status_code != 404

    def test_get_book_in_template(self, response, test_book):
        assertContains(response, test_book.price)
        assertContains(response, test_book.author)
        assertContains(response, test_book.title)

    def test_assert_template_used(self, response):
        assertTemplateUsed(response, "books/detail.html")

    def test_assert_reviews_in_template(self, test_book, test_five_reviews, response):
        assertContains(response, "<article", 5)

    def test_assert_no_reviews_in_template(self, test_book, response):
        assertContains(response, "There are no reviews.")
