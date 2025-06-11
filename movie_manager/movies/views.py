from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request,'create.html')
def list(request):
    return render(request,'list.html')
def edit(request):
    return render(request,'edit.html')
def movie(request):
    movie_list ={'movies':
    [
    {
        'title':"Godfather",
        'year':"1994",
        'summary':"story of an underworld king",
        'image':'godfather.png'
    },
    {
        'title':"batman",
        'year':"2000",
        'summary':"I am vengence",
        'image':'batman.jpg'
    }
    ]
    }
    return render(request,'movie.html',movie_list)