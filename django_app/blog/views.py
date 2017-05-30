from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

User = get_user_model()


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')

    context = {
        'posts': posts
    }
    return render(request, 'blog/article_list.html', context=context)


# 블로그의 한개 포스트 상세 페이지를 리턴해주는 컨트롤러
def post_detail(request, pk):
    print('post_detail pk:', pk)
    # psot라는 키값으로 Post객체 중 pk 또는 id값이 매개변수로 주어진 pk변수와 같은 Post객체를 전달
    posts = Post.objects.get(
        pk=pk
    )
    context = {
        'post': posts,
    }
    return render(request, 'blog/post_detail.html', context=context)


def post_create(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_create.html', context=context)
    elif request.method == 'POST':
        data = request.POST
        title = data['title']
        text = data['text']
        user = User.objects.first()
        post = Post.objects.create(
            title=title,
            text=text,
            author=user,
        )
        return redirect('post_detail', pk=post.pk)
