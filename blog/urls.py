from django.urls import path

from blog.views import FeedView, BlogPostsView, BlogsView, AddRead, AddFeed, DelFeed
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', FeedView.as_view(), name='main'),
    path('my-blog/', BlogPostsView.as_view(), name='my_blog'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('add-read/<int:post_pk>/', AddRead.as_view(), name='add-read'),
    path('add-feed/<int:user_pk>/', AddFeed.as_view(), name='add-feed'),
    path('del-feed/<int:user_pk>/', DelFeed.as_view(), name='del-feed')
]