from django.urls import path
from .views import BookListView, BookDetailView, home, about

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail')
]