from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse


def user_logout(request):
    logout(request)
    return HttpResponse('logout success!')


def user_login(request):
    message = ''
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            message = 'Login successful!'
        else:
            message = 'Invalid username or password!'
    return render(request,'login.html',{'message':message})


def profile(request):
    username = ''
    message = ''
    if request.user.is_authenticated:
        username = request.user.username
    else:
        message = 'not authenticated yet!'
    return render(request,'profile.html',{'username':username,'message':message})



def register(request):
    message = ''
    registered = False
    if request.method=="POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if User.objects.filter(username=username).exists():
            message = 'Username already exists!'
        else:
            user=User.objects.create_user(
                username=username,
                password=password
            )
            registered = True
    elif request.method=='GET':
        username = ''
    return render(request,'register.html',{'username':username,'message':message,'registered':registered})