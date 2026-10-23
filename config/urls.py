from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    username = request.GET.get('username','') or 'Guest'
    city = request.GET.get('city') or 'Earth'
    return render(request, 'home.html', {'city':city, 'username':username})

def about(request):
    return HttpResponse('this is about page!')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('accounts.urls')),
    path('',home),
    path('about/', about),
]
