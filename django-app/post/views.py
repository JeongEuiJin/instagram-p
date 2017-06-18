from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Post

User = get_user_model()


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
            'post': post
        }

    except Post.DoesNotExist as e:
        # return HttpResponseNotFound('Post not found, detail:{}'.format(e))
        return redirect('post:post_list')

    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        user = User.objects.first()
        post = Post.objects.create(
            author=user,
            photo=request.FILES['file'],
        )
        comment_string = request.Post.get('comment', '')

        if comment_string:
            post.comment_set.create(
                author=user,
                content=comment_string,
            )

        return redirect('post:post_detail', post_pk=post.pk)
    else:
        return render(request, 'post/post_create.html')


def post_anyway(request):
    return redirect('post:post_list')
