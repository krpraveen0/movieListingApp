from django import forms
from moviesApp.models import Movie

#creating a movie form
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields = '__all__'
