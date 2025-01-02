from django.shortcuts import render

from my_blog.models import Post

def index(request):
    posts= Post.objects.all()
    total= Post.objects.count()
    context = {
            'posts': posts,
            'total': total
            }
    return render(request, './index.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    posts = Post.objects.all()
    context = {'post':post,
               'posts':posts
               }
    return render(request, 'index.html', context)

# 1:38:56