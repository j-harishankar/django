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
       frm = MovieForm(request.POST,request.FILES)
       if frm.is_valid():
           frm.save()
    else:
        frm = MovieForm()    
    return render(request, 'create.html',{'frm':frm})

def list(request):
    print(request.COOKIES)
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
    recent_movies = request.session.get('recent_visits',[])
    visits = int(request.COOKIES.get('visits',0))# here you get the number of visits stored in cookies if its empty then return 0 thats what ,0 represents 
    visits = visits+1
    movie_set = MovieInfo.objects.all()
    recent_movies = MovieInfo.objects.filter(pk__in=recent_movies)
    response = render(request, 'cred.html',{
        'recent':recent_movies,
        'movies':movie_set,
        'visit':visits
        })
    response.set_cookie('visits',str(visits))
    return response


def edit(request,pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.POST:
        # title = request.POST.get('title')
        # year = request.POST.get('year')
        # description = request.POST.get('description')
        # instance_to_be_edited.title = title
        # instance_to_be_edited.year = year
        # instance_to_be_edited.description =description
        # instance_to_be_edited.save()
        frm = MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            frm.save()
    else:
        key = f'edit_visits_{pk}'
        visit_count = request.session.get(key, 0) + 1        
        request.session[key] = visit_count
        frm = MovieForm(instance=instance_to_be_edited)
    return render(request, 'create.html',{'frm':frm,'visit_count': visit_count})

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request, 'cred.html',{'movies':movie_set})