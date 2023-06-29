from abc import ABC, abstractmethod

from django.shortcuts import redirect
from django.utils import timezone

from users.models import Author
from .models import Books
from .forms import CommentForm


def get_books(model: object, **kwargs) -> tuple:
    return model.objects.filter(archived=False).only('name')


class BaseBookService(ABC):
    @abstractmethod
    def get_books_by_author(self, author: str):
        pass


class BookService(BaseBookService):
    def get_books_by_author(self, author_id: int):
        books = Books.objects.filter(author=author_id, archived=False)
        return books


class BaseAuthorService(ABC):
    @abstractmethod
    def set_comment(self):
        ...

    def delete_comment(self):
        ...


class AuthorService(BaseAuthorService):

    def set_comment(self, request, pk_book: int):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment = form.cleaned_data['text']
            comment.author = Author.objects.get(pk=request.user.id)
            comment.date = timezone.now()
            comment.book = Books.objects.get(pk=pk_book)
            comment.save()


    def delete_comment(self):
        pass
