from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello(request):
    movie_details ={'movies':
    [
    {
        'title':"Godfather",
        'year':"1994",
        'summary':"story of an underworld king",
        'sucsess':True
    },
    {
        'title':"Titanic",
        'year':"1990",
        'summary':"story of an ship",
        'sucsess':False
    },
    {
        'title':"underworld",
        'year':"2000",
        'summary':"story of an underworld dog",
        'sucsess':True
    },
    {
        'title':"Home alone",
        'year':"1994",
        'summary':"story of a kid",
        'sucsess':False
    }
    ]
    }
    return render(request,'hello.html',movie_details)
def welcome(request):
    return HttpResponse("welcome")