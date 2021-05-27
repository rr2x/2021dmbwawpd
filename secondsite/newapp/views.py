from django.shortcuts import render
from .models import Movies

def movie_list(request):
  movies = Movies.objects.all()
