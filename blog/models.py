from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class UserBlog(models.Model):
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    owner = models.ForeignKey(User, related_name='owner',  on_delete=models.CASCADE)
    feed = models.ManyToManyField(User, related_name='feed', blank=True)
    read = models.ManyToManyField(Post, related_name='read', blank=True)
    subscribers = models.ManyToManyField(User, related_name='blog_subs', blank=True)

    def add_read(self, post):
        self.read.add(post)
        self.save()

    def add_feed(self, user):
        self.feed.add(user)
        self.save()

    def add_sub(self, user):
        self.subscribers.add(user)
        self.save()

    def delete_feed(self, user):
        self.feed.remove(user)
        for i in self.read.filter(author=user):
            self.read.remove(i)
        self.save()

    def delete_sub(self, user):
        self.subscribers.remove(user)
        self.save()

    def __str__(self):
        return self.owner.username
