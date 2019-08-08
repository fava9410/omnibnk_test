from .models import Movie, Genre
from rest_framework import serializers, permissions

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='genre.name', read_only = True)

    class Meta:
        model = Movie
        fields = ('name', 'director', 'released_date', 'genre', 'id')

    def update(self, instance, validated_data):
        self.context['request'].user
        instance.name = validated_data.get('name', instance.name)
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.director = validated_data.get('director', instance.director)
        instance.updated_by = self.context['request'].user
        instance.save()
        return instance
