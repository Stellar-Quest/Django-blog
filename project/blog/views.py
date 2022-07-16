from django.shortcuts import render, redirect

from blog.forms import PostForm
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


def post(request, post_id):
    blog_service = BlogService()
    post = blog_service.get_post_by_id(post_id)
    return render(
        request,
        'blog/post.html',
        {
            'post': post,
        }
    )


def create_new_post(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        username = request.user
        if post_form.is_valid():
            blog_service = BlogService()
            blog_service.save_new_post(post_form, username)

            return redirect('index')
    else:
        post_form = PostForm()
    return render(
        request,
        'blog/create.html',
        {
            'post_form': post_form,
        }
    )
