from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'all_books' : Book.objects.all().order_by('title'),
    }


    return render(request, "index.html", context)

def add_book(request):
    if request.POST:
        print("whast good")
        Book.objects.create(title=request.POST['title'], description=request.POST['description'])
    else:
        print("not good")
    return redirect('/')

def delete_book(request, number):
    book = Book.objects.get(id=int(number))
    book.delete()
    return redirect('/')


def book_info(request, number):
    this_book = Book.objects.get(id=int(number))
    this_book_authors = this_book.publishers.all()
    all_authors = Author.objects.all().order_by('f_name').order_by('f_name')
    selectable_authors = Author.objects.exclude(id__in=this_book_authors).order_by('f_name')

    context = {
        "book": this_book,
        "book_authors": this_book_authors,
        "all_authors": all_authors,
        "selectable_authors" : selectable_authors
    }
    return render(request, 'book_info.html', context)

def authors(request):
    authors = Author.objects.all()
    context = {
        'all_authors' : authors
    }
    return render(request, 'authors.html', context)

def add_author_to_book(request, number):
    if request.POST:
        book_id = int(number)

        to_add_author_id = int(request.POST["author"]) #id vlue of author to be added
        book_displayed = Book.objects.get(id=book_id) #the currently diplayed book
        author_to_add = Author.objects.get(id=to_add_author_id) #the author object to add to the book
        book_displayed.publishers.add(author_to_add) # adding the author to the book
    else:
        print("not good")
    return redirect(f'/books/{int(number)}')
    

def add_author(request):
    if request.POST:
        Author.objects.create(f_name=request.POST['first_name'], l_name=request.POST['last_name'], notes=request.POST['author_notes'])
    else:
        print("not good")
    return redirect('/authors')

def author_info(request, number):
    author = Author.objects.get(id=int(number))
    author_books = author.books.all()
    all_books = Book.objects.all().order_by('title')
    selectable_books = Book.objects.exclude(id__in=author_books).order_by('title')

    context = {
        "author": author,
        "author_books": author_books,
        "all_books": all_books,
        "selectable_books" : selectable_books
    }
    return render(request, 'author_info.html', context)

def add_book_to_author(request, number):
        if request.POST:
            author_id = int(number)

            to_add_book_id = int(request.POST["author"]) #id vlue of author to be added
            author_displayed = Author.objects.get(id=author_id) #the currently diplayed book
            book_to_add = Book.objects.get(id=to_add_book_id) #the author object to add to the book
            author_displayed.books.add(book_to_add) # adding the author to the book
        else:
            print("not good")
        return redirect(f'/authors/{int(number)}')