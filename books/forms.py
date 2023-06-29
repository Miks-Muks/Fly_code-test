from django import forms

from .models import Books, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ('slug', 'cover_small', 'author')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'})
        }
