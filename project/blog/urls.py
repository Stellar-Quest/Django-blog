from django.urls import path

from .views import index, post, create_new_post

urlpatterns = [
    path('', index, name='index',),
    path('post/<int:post_id>/', post, name='post'),
    path('create/', create_new_post, name='create'),
]
