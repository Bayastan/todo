from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Books

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def books(request):
    books_list = Books.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def second(request):
    return HttpResponse("Test page 2")

def third(request):
    return HttpResponse("This is page3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)


def add_book(request):
    form = request.POST 
    book=Books(
    title=form["title"],
    subtitle=form["subtitle"],
    description=form["description"],
    genre=form["genre"],
    price=form["price"],
    year=form["year"][:10],
    )
    book.save()
    return redirect(books)

def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorites = True
    book.save()
    return redirect(books)

def unmark_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorites = False
    book.save()
    return redirect(books)

def book(request, id):
    book_object = Books.objects.filter(id=id)
    return render(request, "books_detail.html", {"books_list": book_object})

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)
