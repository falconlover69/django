from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
    # return HttpResponse('HELLO FROM POSTS')
    # def deletePost: 
    #         # Posts.objects.filter(id=id).delete()
    #         print('Hello from delete function')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
        # 'delete': deletePost
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)

# def deletePost(id):
#     Posts.objects.filter(id=id).delete()

    # posts = Posts.objects.all()[:10]

    # context = {
    #     'title': 'Latest Posts',
    #     'posts': posts
    # }

    # return render(request, 'posts/index.html', context)
