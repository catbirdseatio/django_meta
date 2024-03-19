from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/detail.html"
    context_object_name = "book"
