from django import forms
from moviesApp.models import Movie
#date widget
class DateInput(forms.DateInput):
    input_type='date'
#creating a movie form
class MovieForm(forms.ModelForm):
    movie_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    release_date = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    actor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    actress= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    director_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    rating = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Movie
        fields = ['movie_name','release_date','actor','actress','director_name','rating']
