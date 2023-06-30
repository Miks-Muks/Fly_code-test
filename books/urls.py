from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('list', views.BookListView.as_view(), name='list'),
    path('authors', views.AuthorListView.as_view(), name='authors'),
    path('', views.IndexView.as_view(), name='home'),
    path('detail/<slug:slug>', views.BookDetailView.as_view(), name='detail'),
    path('authors/books/<int:author_id>', views.AuthorBooks.as_view(), name='author_books'),
    path('book/create', views.CreateBook.as_view(), name='create_book'),
    path('book/update/<int:book_id>', views.UpdateBook.as_view(), name='update_book'),
    path('book/comment_create/<slug:slug>/<int:pk_book>', views.CommentCreate.as_view(), name='comment_create'),
    path('book/comment_delete/<slug:slug>/<int:comment_pk>', views.DeleteCommentView.as_view(), name='comment_delete'),
]
