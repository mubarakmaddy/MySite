from django.shortcuts import render

# Create your views here.
#Front end
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book

#
# def index(request):
#     all_books_list = Book.objects.all()
#     context = {'all_books_list': all_books_list}
#     return render(request, 'books/index.html', context)
#
#
# def details(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'books/details.html', {'book': book})
#
#
# def info(request, book_id):
#     return HttpResponse("<h2> This is detail info of book no %s </h2>" % str(book_id))
#
#
# def read(request, book_id):
#     return HttpResponse("<h2> Reading book no %s </h2>" % str(book_id))


from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/details.html'


class Test:
    def test(self):
        return HttpResponse("This is Test Page")
