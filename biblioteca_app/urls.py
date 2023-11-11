from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books-detail/<int:id>/', views.books_detail, name='books-detail')
]