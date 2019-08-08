from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class AuditLog(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null = False, blank = False, related_name = 'creater')
    updated_at = models.DateTimeField(auto_now = True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name = 'updater')

    class Meta:
        abstract = True

class Genre(models.Model):
    name = models.CharField(max_length = 100)

class Movie(AuditLog):
    name = models.CharField(max_length = 100, null=False, blank = False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null = False, blank = False)
    released_date = models.DateField()
    director = models.CharField(max_length = 100, null=False, blank = False)
    imagefile = models.FileField(upload_to='movies_pictures/%Y/%m/%d/', null = True)

class UserMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = False, blank = False, related_name = 'user_movie')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null = False, blank = False, related_name = 'favorite_movie')
