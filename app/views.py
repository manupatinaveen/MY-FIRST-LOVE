from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This is our first view function')

def propose(request):
    return HttpResponse('<marquee>Yes I Love U Too</marquee>')

def rejection(request):
    return HttpResponse('<h1>Frnd dailogue: Akka Chellellu Lera ra neeku</h1>')