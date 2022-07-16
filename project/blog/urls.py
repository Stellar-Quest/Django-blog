from django.urls import path

from blog.views import IndexView, PostView, NewPost

urlpatterns = [
    path('', IndexView.as_view(), name='index',),
    path('post/<int:post_id>/', PostView.as_view(), name='post'),
    path('create/', NewPost.as_view(), name='create'),
]
