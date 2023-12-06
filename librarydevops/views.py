from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book

def helloView(request):
    books = Book.objects.all()
    return render(request, "viewbook.html", {"books": books})

def addBookView(request):
    return render(request, "addbook.html")

def addBook(request):
    if request.method == "POST":
        t = request.POST["title"]
        a = request.POST["author"]
        q = request.POST["quantity"]  
        
        book = Book()
        book.title = t
        book.author = a
        book.quantity = q  
        book.save()
        return HttpResponseRedirect('/')

def editBook(request):
    if request.method == "POST":
        t = request.POST["title"]
        q = request.POST["quantity"]  
        
        book = Book.objects.get(id=request.POST['bid'])
        book.title = t
        book.quantity = q  
        book.save()
        return HttpResponseRedirect('/')

def editBookView(request):
    book = Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request, "edit-book.html", {"book": book})

def deleteBookView(request):
    book = Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')