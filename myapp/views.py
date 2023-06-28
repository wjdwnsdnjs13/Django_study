from django.http import HttpResponse
import random
from django.shortcuts import render

topics = [
    {'id' : 1, 'title' : 'routing', 'body' : 'Routing is ...'},
    {'id' : 2, 'title' : 'view', 'body' : 'View is ...'},
    {'id' : 3, 'title' : 'Model', 'body' : 'Model is ...'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <h1><a href="/">Django</a></h1>
    <ol>
        {ol}
    </ol>
    {articleTag}
    '''


# Create your views here.
def index(request):
    article = '''<h2>Welcome</h2>
    Hello, Django'''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('<h1>Create!</h1>')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
