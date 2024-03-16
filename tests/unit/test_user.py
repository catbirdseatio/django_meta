import pytest
from django.contrib.auth import get_user_model


pytestmark = pytest.mark.django_db
User = get_user_model()


class TestUser:
    def test_create_user(self, test_user):
        assert test_user.email is not None
        assert test_user.is_active
        assert not test_user.is_staff
        assert not test_user.is_superuser

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            email="clark@dailyplanet.com",
            password="testpass321",
            username="clarke_kent",
        )
        assert admin_user.email == "clark@dailyplanet.com"
        assert admin_user.username == "clarke_kent"
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser
