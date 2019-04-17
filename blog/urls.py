import django.contrib.auth.views as auth_views
from django.urls import path

from blog.views import (AddFeed, AddPost, AddRead, BlogPostsView, BlogsView,
                        DelFeed, FeedView, PostDetailView)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('feed/', FeedView.as_view(), name='main'),
    path('blog/<int:pk>', BlogPostsView.as_view(), name='blog-posts'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('add-read/<int:post_pk>/', AddRead.as_view(), name='add-read'),
    path('add-feed/<int:user_pk>/', AddFeed.as_view(), name='add-feed'),
    path('del-feed/<int:user_pk>/', DelFeed.as_view(), name='del-feed'),
    path('add-post', AddPost.as_view(), name='add-post'),
]
