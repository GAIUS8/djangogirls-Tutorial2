from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')

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
    return render(request,'blog/post_detail.html', context=context)