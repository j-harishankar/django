from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get("title")) 
        print(request.POST.get("year")) 
        print(request.POST.get("summary")) 

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
    movie_list = {
        'movies': [
            {
                'title': "Godfather",
                'year': "1994",
                'summary': "story of an underworld king",
                'sucsess': True
            },
            {
                'title': "Titanic",
                'year': "1990",
                'summary': "story of an ship",
                'sucsess': False
            },
            {
                'title': "underworld",
                'year': "2000",
                'summary': "story of an underworld dog",
                'sucsess': True
            },
            {
                'title': "Home alone",
                'year': "1994",
                'summary': "story of a kid",
                'sucsess': False
            }
        ]
    }
    return render(request, 'cred.html', movie_list)
