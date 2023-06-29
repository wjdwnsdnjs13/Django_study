from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.shortcuts import render, redirect

nextId = 4
topics = [
    {'id': 1, 'title': 'routing', 'body': 'Routing is ...'},
    {'id': 2, 'title': 'view', 'body': 'View is ...'},
    {'id': 3, 'title': 'Model', 'body': 'Model is ...'}
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        print("hi")
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <h1><a href="/">Django</a></h1>
    <ol>
        {ol}
    </ol>
    {articleTag}
    <ul>
        <li><a href="/create/">create</a></li>
        {contextUI}
    </ul>
    '''


# Create your views here.
def index(request):
    article = '''<h2>Welcome</h2>
    Hello, Django'''
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def update(request, id):
    global topics
    if request.method == "GET":
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic["title"],
                    "body": topic["body"]
                }
        article = f'''
                <form action="/update/{id}/" method="POST">
                    <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                    <p><textarea name="body" placeholder="body">{selectedTopic["title"]}</textarea></p>
                    <p><input type="submit"></p>
                </form>
                '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')


@csrf_exempt #from django.views.decorators.csrf import csrf_exempt 후 사용하려는 함수에 달아주면 됨.
def create(request):
    global nextId
    print("request. : ", request.method)
    if request.method == "GET":
        article = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        print(request.POST["title"])
        title = request.POST["title"]
        body = request.POST["body"]
        newTopic = {"id": nextId, "title": title, "body": body}
        topics.append(newTopic)
        url = "/read/" + str(nextId)
        nextId += 1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))
