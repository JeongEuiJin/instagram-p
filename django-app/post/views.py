from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
        context = {
            'post':post
        }

    except Post.DoesNotExist as e:
        # return HttpResponseNotFound('Post not found, detail:{}'.format(e))
        return redirect('post:post_list')

    return render(request, 'post/post_detail.html', context)

