import pytest
from tests.factories import UserFactory


@pytest.fixture
def test_user():
    yield UserFactory()
