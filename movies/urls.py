from django.urls import path
from . import views

urlpatterns = [
    path('create_movie', views.create_movie, name='create_movie'),
    path('all_movies', views.all_movies, name='all_movies'),
    path('list_all_movies', views.MoviesList.as_view(), name='list_all_movies'),
    path('movie_detail/<int:pk>/', views.MovieDetail.as_view()),
    path('edit_movie/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('manage_genres', views.GenresList.as_view(), name='manage_genres'),
    path('recommended_movies', views.recommended_movies, name='recommended_movies'),
    path('add_user_movie', views.add_user_movie, name='add_user_movie'),
]
