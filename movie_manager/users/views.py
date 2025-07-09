from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
# Create your views here.
def login_view(request):
    error_message = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('cred')
        else:
            error_message = 'Invalid-Credential'
    return render(request,'users/login.html',{'error':error_message})
def logout_view(request):
    authlogout(request)
    return redirect('login')

def signup(request):
    user = None
    error_message = None
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_message = str(e)

    return render(request,'users/create.html',{'users':user,'error':error_message})