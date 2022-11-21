from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import render, get_object_or_404

POSTS_PER_PAGE = 10

def index(request):
    posts = Post.objects.order_by('-pub_date')[:POSTS_PER_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': 'Группаы проекта Yatube',
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
