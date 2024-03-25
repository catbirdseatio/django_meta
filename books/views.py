from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/detail.html"
    context_object_name = "book"


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")

        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
