from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Hello, world! This is my Django app.")
def welcome(request):
    return HttpResponse("welcome")