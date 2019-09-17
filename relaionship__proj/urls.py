
from django.urls import path
from multi_to_multi_app import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:number>', views.book_info),
    path('books/<int:number>/add_author', views.add_author_to_book),
    path('delete_book/<int:number>', views.delete_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:number>', views.author_info),
    path('authors/<int:number>/add_book', views.add_book_to_author)
]
