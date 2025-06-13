from django.shortcuts import render
from .models import MovieInfo
# Create your views here.
def create(request):
    if request.POST:
        title = request.POST.get("title")
        year = request.POST.get("year")
        desc =request.POST.get("summary")
        movie_obj = MovieInfo(title=title,year=year,description=desc)
        movie_obj.save()

    return render(request, 'create.html')

def list(request):
    return render(request, 'list.html')

def edit(request):
    return render(request, 'edit.html')

def movie(request):
    movie_list = {
        'movies': [
            {
                'title': "Godfather",
                'year': "1994",
                'summary': "story of an underworld king",
                'image': 'godfather.png'
            },
            {
                'title': "batman",
                'year': "2000",
                'summary': "I am vengence",
                'image': 'batman.jpg'
            }
        ]
    }
    return render(request, 'movie.html', movie_list)

def cred(request):
    movie_set = MovieInfo.objects.all()
    print(movie_set)
    return render(request, 'cred.html',{'movies':movie_set})
