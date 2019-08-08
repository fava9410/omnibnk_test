from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .forms import create_movie_form
from .models import Movie, Genre
from .serializer import MovieSerializer

@login_required
@csrf_exempt
def create_movie(request):
    if request.method == 'POST':
        form = create_movie_form(request.POST)
        if form.is_valid():
            valid_form = form.save(commit = False)
            valid_form.created_by_id = request.user.id
            valid_form.save()

    genres = Genre.objects.all()

    return render(request, "movies/create_movie.html", {'genres': genres})

@login_required
def all_movies(request):
	return render(request, "movies/all_movies.html")

class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.filter(deleted = False)
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(deleted = False)
    serializer_class = MovieSerializer
