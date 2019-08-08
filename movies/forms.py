from django.forms import ModelForm
from .models import Movie

class create_movie_form(ModelForm):
    class Meta:
        model = Movie
        fields = ('name','released_date','genre','director',)
