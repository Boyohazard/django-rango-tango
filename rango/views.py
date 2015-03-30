from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says, 'Hey there world!'\n<br /><a href=\"about\">About</a>")
    
def about(request):
    return HttpResponse("Rango says, 'Here is the about page'\n<br /><a href=\"/rango/\">Index</a>")