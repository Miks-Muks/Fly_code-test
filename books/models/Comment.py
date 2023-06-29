from django.db import models

from users.models import Author

from .Books import Books


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author}'
