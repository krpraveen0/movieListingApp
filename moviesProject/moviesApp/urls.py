from django.urls import path
from moviesApp import views

urlpatterns = [
    path('',views.home_view),
    path('add-movie/',views.add_movie_view,name="add_movie"),
    path('list-movies/',views.list_movie_view,name="list_movies"),
]
