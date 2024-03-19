import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestBook:
    def test_book_listing(self, test_book):
        assert len(test_book.title) > 0
        assert len(test_book.author) > 0
        assert test_book.price > 0.00

    def test___str__(self, test_book):
        assert str(test_book) == test_book.title

    def test_get_absolute_url(self, test_book):
        assert test_book.get_absolute_url() == reverse(
            "books:detail", args=[str(test_book.id)]
        )
