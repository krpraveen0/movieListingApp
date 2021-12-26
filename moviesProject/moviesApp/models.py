from django.db import models

# Create your models here.
#creating movie model
class Movie(models.Model):
    release_date = models.DateField()
    movie_name = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)
    actress = models.CharField(max_length=30)
    rating = models.IntegerField()
