from django.shortcuts import render
from .models import MovieInfo
from . forms import MovieForm
# Create your views here.
def create(request):
    frm = MovieForm()
    if request.POST:
       # title = request.POST.get("title")
       # year = request.POST.get("year")
       # desc =request.POST.get("description")
       # movie_obj = MovieInfo(title=title,year=year,description=desc)
       # movie_obj.save()
       # or
       frm = MovieForm(request.POST)
       if frm.is_valid:
           frm.save()
    else:
        frm = MovieForm()    
    return render(request, 'create.html',{'frm':frm})

def list(request):
    return render(request, 'list.html')



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
    return render(request, 'cred.html',{'movies':movie_set})


def edit(request,pk):
    return render(request, 'edit.html')

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request, 'cred.html',{'movies':movie_set})