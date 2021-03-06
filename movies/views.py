from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from .forms import create_movie_form
from .models import Movie, Genre, UserMovies
from .serializer import MovieSerializer, GenreSerializer

@login_required
@csrf_exempt
def create_movie(request):
    if request.method == 'POST':
        form = create_movie_form(request.POST, request.FILES)

        if form.is_valid():
            valid_form = form.save(commit = False)
            valid_form.created_by_id = request.user.id
            valid_form.save()
            return HttpResponseRedirect('/movies/all_movies')

    genres = Genre.objects.all()

    return render(request, "movies/create_movie.html", {'genres': genres})

@login_required
def all_movies(request):
	return render(request, "movies/all_movies.html")

class GenresList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MoviesList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@login_required
def edit_movie(request, pk):
    movie = Movie.objects.get(id = pk)
    return render(request, "movies/edit_movie.html", {'movie': movie})

def recommended_movies(request):
    query = 'select * from movies_movie where id not in \
    (select movie_id from movies_usermovies where user_id = {}) \
    order by Random() Limit 5;'.format(request.user.id)

    movies = Movie.objects.raw(query)

    return render(request, "movies/recommendations.html", {'movies': movies})

@login_required
@csrf_exempt
def add_user_movie(request):
    movie = request.POST.get('movie')
    usermovies = UserMovies.objects.create(user = request.user, movie_id = movie)
    return HttpResponse('ok')
