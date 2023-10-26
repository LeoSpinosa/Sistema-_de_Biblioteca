from django.shortcuts import render, redirect
from .models import Books, Gender

def index(request):

    books = Books.objects.all()
    # for produto in produtos:
    #     print(produto.name + produto.price)
    return render(request, 'pages/index.html', {'books':books})
