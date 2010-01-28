from .models import Book
from django.shortcuts import get_object_or_404, render_to_response

def book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render_to_response(
                'books/book.html',
                {
                    'book' : book,
                })
