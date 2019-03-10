# Create your views here.
# Front end

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


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Book


class IndexView(ListView):
    model = Book
    template_name = 'books/index.html'
    ordering = ['-id']


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['name', 'author', 'price']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class BookUpdate(LoginRequiredMixin,  UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['name', 'author', 'price']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.creator:
            return True
        return False


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/details.html'


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/delete-book.html'
    success_url = '/books'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False
