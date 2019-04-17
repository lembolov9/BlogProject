from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, FormView, ListView

from blog.forms import GuiPostForm
from blog.models import Post, UserBlog


class LogMixin(LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.pk
        return context

class PostDetailView(LogMixin, DetailView):
    model = Post

class PostsView(LogMixin, ListView):
    model = Post
    ordering = ['-created']

class BlogPostsView(PostsView):
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        posts = super().get_queryset().filter(author=self.request.user)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.kwargs['pk']
        return context


class FeedView(PostsView):
    template_name = 'blog/feed_list.html'

    def get_queryset(self):
        feed = UserBlog.objects.get(owner=self.request.user).feed.all()
        posts = super().get_queryset().filter(author__in=feed)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['read'] = UserBlog.objects.get(owner=self.request.user).read.all()
        return context


class BlogsView(LogMixin, ListView):
    model = UserBlog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed'] = UserBlog.objects.get(owner=self.request.user).feed.all()
        return context


class AddRead(LogMixin, View):
    def get(self, request,  post_pk):
        blog = UserBlog.objects.get(owner=request.user)
        post = Post.objects.get(pk=post_pk)
        blog.add_read(post)
        return redirect('main')

class AddFeed(LogMixin, View):
    def get(self, request, user_pk):
        feed_blog = UserBlog.objects.get(owner=request.user)
        sub_blog = UserBlog.objects.get(owner__id=user_pk)
        sub_user = User.objects.get(pk=user_pk)
        feed_blog.add_feed(sub_user)
        sub_blog.add_sub(request.user)
        return redirect('main')

class DelFeed(LogMixin, View):
    def get(self, request, user_pk):
        feed_blog = UserBlog.objects.get(owner=request.user)
        sub_blog = UserBlog.objects.get(owner__id=user_pk)
        sub_user = User.objects.get(pk=user_pk)
        feed_blog.delete_feed(sub_user)
        sub_blog.delete_sub(request.user)
        return redirect('main')

class AddPost(LogMixin, FormView):
    template_name = 'blog/add_post.html'
    form_class = GuiPostForm

    def post(self, request, *args, **kwargs):
        post = Post(title=request.POST['title'], text=request.POST['text'], author=request.user)
        post.save()
        return redirect('post-detail', post.pk)
