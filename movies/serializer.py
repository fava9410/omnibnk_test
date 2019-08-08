from .models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name', read_only=True)

    class Meta:
        model = Movie
        fields = ('name', 'director', 'released_date', 'genre')
