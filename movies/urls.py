from django.urls import path
from . import views

urlpatterns = [
    path('create_movie', views.create_movie, name='create_movie'),
    path('all_movies', views.all_movies, name='all_movies'),
    path('list_all_movies', views.MoviesList.as_view(), name='list_all_movies'),
    path('movie_detail/<int:pk>/', views.MovieDetail.as_view()),
]
