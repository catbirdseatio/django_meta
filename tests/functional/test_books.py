import pytest
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains
from tests.factories import BookFactory


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

    def test_multiple_books(self, client, test_five_books):
        response = client.get(reverse("books:list"))
        assertContains(response, '<h2 class="title">', 5)


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
        assertContains(response, 'There are no reviews.')


class TestSearchResultsListView:
    base_url = reverse("books:search_results")

    @pytest.fixture(scope="function")
    def test_search_books_title(self):
        for i in range(5): BookFactory(title=f"Book {i}")

        yield
    
    @pytest.fixture(scope="function")
    def test_search_books_author(self):
        for i in range(5): BookFactory(author=f"Edmund Welles")

        yield

    def test_search_form_title(self, test_search_books_title, client):
        response = client.get(f"{self.base_url}?q=book")
        assertContains(response, '<h2 class="title">',5)
    
    def test_search_form_title(self, test_search_books_author, client):
        response = client.get(f"{self.base_url}?q=Edmund Welles")
        assertContains(response, '<h2 class="title">',5)
