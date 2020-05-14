from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, './generator/home.html', {'password':'hui43g6iu3o4'})


def password(request):
    return render(request, 'generator/password.html')