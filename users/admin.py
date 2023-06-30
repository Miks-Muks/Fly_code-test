from django.contrib import admin

from .models import Author, CustomUser
from books.models import Books


class CounterBook:
    def get_book_count(self, obj):
        return Books.objects.filter(author=obj).count()

    get_book_count.short_description = 'Books'


# Register your models here.
@admin.register(Author)
class AuthorAdmin(CounterBook, admin.ModelAdmin):
    list_display = ('user', 'get_book_count',)


admin.site.register(CustomUser)