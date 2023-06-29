from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, TemplateView

from .models import Books, Comment
from .services import get_books, BookService, AuthorService
from .forms import BookForm, CommentForm

from users.models import Author


# Create your views here.


class IndexView(TemplateView):
    template_name = 'books/index.html'


class BookListView(ListView):
    template_name = 'books/list.html'
    queryset = get_books(model=Books)
    context_object_name = 'books'


class AuthorListView(ListView):
    template_name = 'books/authors.html'
    queryset = Author.objects.select_related('user').all()
    context_object_name = 'authors'


class AuthorBooks(View):
    template_name = 'books/list.html'

    def get(self, request, author_id: int):
        author_service = BookService()
        books = author_service.get_books_by_author(author_id)
        return render(request, self.template_name, {'books': books})


class BookDetailView(DetailView):
    model = Books
    context_object_name = 'book'
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(book__slug=self.kwargs['slug'])
        context['form'] = CommentForm()
        return context


class CreateBook(LoginRequiredMixin, View):
    form_class = BookForm
    template_name = 'books/books_create.html'
    login_url = 'users/login'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.slug = form.cleaned_data.get('name')
            form.author = request.user.id
            form.save()
            return redirect('books:list')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


class UpdateBook(UpdateView):
    model = Books
    template_name = 'books/books_update.html'
    pk_url_kwarg = 'book_id'
    fields = '__all__'
    success_url = '/list'


class CommentCreate(LoginRequiredMixin, View):
    login_url = '/users/login'

    def post(self, request, pk_book):
        author_service = AuthorService()
        author_service.set_comment(request, pk_book)
        return redirect('books:list', )
