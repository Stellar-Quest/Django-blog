from django.shortcuts import render

from blog.services import BlogService


def index(request):

    blog_service = BlogService()
    posts = blog_service.get_posts()

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
