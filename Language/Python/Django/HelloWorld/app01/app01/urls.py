from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
]