import pytest
from tests.factories import UserFactory, BookFactory, ReviewFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def test_user():
    yield UserFactory()


@pytest.fixture()
def test_book():
    yield BookFactory(title="Test Book")


@pytest.fixture()
def test_five_books():
    for _ in range(5):
        BookFactory()

    yield


@pytest.fixture
def test_five_reviews(test_book):
    for _ in range(5):
        ReviewFactory(book=test_book)

    yield
