from django.shortcuts import render
from books.models import Book
from users.models import User


def index(request):
    books = Book.objects.all() #Queries will go to 'books_db'
    users = User.objects.all() #Queries will go to 'users_db'
    return render(
        request,
        'index.html',
        {
            'books': books,
            'users': users
        }
    )