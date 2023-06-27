from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcom!</h1>')

def create(request):
    return HttpResponse('<h1>Create!</h1>')

def read(request, id):
    return HttpResponse('<h1>Read!'+id+'</h1>')
