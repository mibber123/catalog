from django.urls import re_path
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('books/', views.book_view, name='book_view'),
    #re_path(r'books/$', views.book_view, name='books'),
    #re_path(r'^books/(?P<id>\d+)/$', views.book_detail, name='book_detail'),
]