from django.shortcuts import render
from my_blog.models import Post
from datetime import datetime
from datetime import datetime


def posts(request):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%x %H:%M:%S")
    if request.method == 'POST':
        post = Post.objects.create(title=f'{formatted_time}', body='This is the body of the new post')
        total = Post.objects.count()
        context = {
            'post': post,
            'total': total
                   }
        return render(request, 'responses/post_add.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'post': post
        }
        return render(request, 'components/post.html', context)
    
    elif request.method == 'DELETE':
        post.delete()
        total = Post.objects.count()
        context = {'total': total }
        return render(request, 'components/sidebar_header.html', context)
