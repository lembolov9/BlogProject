from django.contrib import admin

# Register your models here.
from blog.models import Post, UserBlog

admin.site.register(Post)
admin.site.register(UserBlog)