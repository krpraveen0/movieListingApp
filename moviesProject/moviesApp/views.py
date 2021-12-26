from django.shortcuts import render
from moviesApp.forms import MovieForm
from moviesApp.models import Movie
# Create your views here.
#home view
def home_view(request):
    return render(request,'moviesApp/index.html')

#movie adding view
def add_movie_view(request):
    #empty form object
    form = MovieForm()
    #checking for post method request
    if request.method =='POST':
        #form object with POST object
        form=MovieForm(request.POST)
        #checking if form is valid
        if form.is_valid():
            #save it to db
            form.save()
        #return to home page
        return home_view(request)
    #returning response addmovie.html with form object
    return render(request,'moviesApp/addmovie.html',{'form':form})

#function for movie list view
def list_movie_view(request):
    #storing all the Movie objects ordered in descending order
    movies_list = Movie.objects.all().order_by('-rating')
    return render(request,'moviesApp/listmovie.html',{'movies_list':movies_list})
