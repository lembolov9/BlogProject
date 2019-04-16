from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User)

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
