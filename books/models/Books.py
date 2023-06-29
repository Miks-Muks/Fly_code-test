from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill

from users.models import Author


class Books(models.Model):
    name = models.CharField(verbose_name='awda', max_length=40)
    author = models.ManyToManyField(Author, )
    description = models.TextField(verbose_name='description of book', null=True, blank=True)
    cover = models.ImageField(upload_to='book/photo')
    cover_small = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
                                  ResizeToFill(50, 50)], source='cover')
    year_of_publishing = models.DateField(verbose_name='The year of publishing')
    archived = models.BooleanField(default=False)
    number_of_page = models.IntegerField(validators=[MinValueValidator(limit_value=10), ])
    slug = models.SlugField(max_length=40, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'slug': self.slug})

    def is_author(self, user):
        return self.author.filter(id=user.id).exists()