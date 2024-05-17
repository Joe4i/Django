# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello World! I'm a home page")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("I'm about page")
    return render(request, 'about.html')