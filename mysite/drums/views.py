
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

def education(request):
    return render(request, 'drums/lessons.html')

def drummer(request):
    return render(request, 'drums/drummer.html')

def index(request):
    return render(request, 'drums/index.html')

def covers(request):
    covers = Cover.objects.all()
    return render(request, 'drums/covers.html')

def main(request):
    return render(request, 'drums/main.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Who I am?')
