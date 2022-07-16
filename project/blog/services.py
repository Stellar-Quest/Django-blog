from blog.models import Post


class BlogService:

    def get_posts(self):
        posts = Post.objects.all().order_by('-id')
        return posts
