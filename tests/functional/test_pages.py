import pytest
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed

from pages.views import HomePageView, AboutPageView


pytestmark = pytest.mark.django_db


class TestHomepage:
    @pytest.fixture(scope="function")
    def response(self, client):
        yield client.get(reverse("index"))

    @pytest.fixture(scope="function")
    def authenticated_response(self, client, test_user):
        client.force_login(test_user)
        yield client.get(reverse("index"))

    def test_homepage_status_code(self, response):
        assert response.status_code == 200

    def test_homepage_template(self, response):
        assertTemplateUsed(response, "pages/index.html")

    def test_username_on_page(self, authenticated_response, test_user):
        assert f"{test_user.email}" in str(authenticated_response.content)

    def test_username_not_on_page(self, test_user, response):
        assert f"{test_user.email}" not in str(response.content)
        assert f"You are not logged in." in str(response.content)

    def test_incorrect_html(self, response):
        assert f"Hello! This should not be on the page." not in str(response.content)

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        assert view.func.__name__ == HomePageView.as_view().__name__


class TestAboutPage:
    @pytest.fixture(scope="function")
    def response(self, client):
        yield client.get(reverse("about"))

    def test_homepage_status_code(self, response):
        assert response.status_code == 200

    def test_homepage_template(self, response):
        assertTemplateUsed(response, "pages/about.html")
    
    def test_correct_html(self, response):
        assert f"About Page" in str(response.content)

    def test_incorrect_html(self, response):
        assert f"Hello! This should not be on the page." not in str(response.content)

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/about")
        assert view.func.__name__ == AboutPageView.as_view().__name__