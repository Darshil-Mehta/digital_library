from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/books.html'
    context_object_name = 'books'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

def home(request):
    return render(request, 'books/home.html')

def about(request):
    return render(request, 'books/about.html')