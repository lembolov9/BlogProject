from django.contrib import admin

from blog.models import Post, UserBlog

admin.site.register(Post)
admin.site.register(UserBlog)
