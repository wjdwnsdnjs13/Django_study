from django.http import HttpResponse
import random
from django.shortcuts import render

topics = [
    {'id' : 1, 'title' : 'routing', 'body' : 'Routing is ...'},
    {'id' : 2, 'title' : 'view', 'body' : 'View is ...'},
    {'id' : 3, 'title' : 'Model', 'body' : 'Model is ...'}
]

# Create your views here.
def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return HttpResponse(f'''
    <h1>Django</h1>
    <ol>
        {ol}
    </ol>
    <h2>Welcome</h2>
    Hello, Django
    ''')

def create(request):
    return HttpResponse('<h1>Create!</h1>')

def read(request, id):
    return HttpResponse('<h1>Read!'+id+'</h1>')
