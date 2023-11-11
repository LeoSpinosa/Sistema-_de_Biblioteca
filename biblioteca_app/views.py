from django.shortcuts import render, redirect
from .models import Books, Gender
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')

def index(request):

    books = Books.objects.all()    
    return render(request, 'pages/index.html', {'books': books})

def books_detail(request, id):
    
    books = Books.objects.get(id=id)
    return render(request, 'pages/book.detail.html', {'books' : books})