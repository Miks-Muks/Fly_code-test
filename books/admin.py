from django.contrib import admin

from .models import Books, Comment


# Register your models here.
class CounterComments:
    def get_comments_count(self, obj):
        return Comment.objects.filter(author__in=obj.author.all()).count()

    get_comments_count.short_description = 'Comments'


class StatisticForBooks:

    def get_author_names(self, obj):
        return ", ".join([author.user.username for author in obj.author.all()])

    get_author_names.short_description = 'Authors'


@admin.register(Books)
class BooksAdmin(StatisticForBooks, CounterComments, admin.ModelAdmin):
    """Настройки для категорий"""
    list_display = ['slug', 'name', 'get_author_names', 'get_comments_count']
    list_editable = ['name']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author',)
