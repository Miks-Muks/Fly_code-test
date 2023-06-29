from django import template

register = template.Library()


@register.filter
def is_author(book, user):
    return book.author.filter(id=user.id).exists()
