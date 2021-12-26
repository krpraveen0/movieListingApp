from django.contrib import admin
from moviesApp.models import Movie
# Register your models here.
#registering the movie model in admin panel

class MovieAdmin(admin.ModelAdmin):
    list_display=['release_date','movie_name','actor','actress','rating']
admin.site.register(Movie,MovieAdmin)
