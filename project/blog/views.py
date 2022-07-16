from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import PostSerializer
from blog.services import BlogService


class IndexView(APIView):

    def get(self, request):
        blog_service = BlogService()
        posts = blog_service.get_posts()
        serialized_posts = PostSerializer(posts, many=True)

        return Response(serialized_posts.data, status=status.HTTP_200_OK)


class PostView(APIView):
    def get(self, request, post_id):
        blog_service = BlogService()
        post = blog_service.get_post_by_id(post_id)
        serialized_post = PostSerializer(post)

        return Response(serialized_post.data, status=status.HTTP_200_OK)


class NewPost(APIView):

    def post(self, request):
        username = request.user
        post = PostSerializer(data=request.data)
        if post.is_valid():
            blog_service = BlogService()
            blog_service.save_new_post_api(post, username)
            return Response(post.data, status=status.HTTP_201_CREATED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

