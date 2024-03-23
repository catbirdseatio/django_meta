from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/list.html"
    context_object_name = "books"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/detail.html"
    context_object_name = "book"
    login_url = "account_login"
