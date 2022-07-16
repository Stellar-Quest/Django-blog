from django.contrib.auth.models import User

from blog.models import Post


class BlogService:

    def create_post(self):
        pass

    def get_posts(self):
        posts = Post.objects.all().order_by('-id')
        return posts

    def get_post_by_id(self, post_id):
        post = Post.objects.get(id=post_id)
        return post

    def save_new_post(self, post_form, username):
        user = User.objects.get(username=username)
        new_post = post_form.save(commit=False)
        new_post.author = user
        new_post.save()
