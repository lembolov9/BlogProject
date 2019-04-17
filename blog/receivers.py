from django.contrib.auth.models import User
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver

from blog.models import UserBlog


@receiver(post_save, sender=User)
def create_blog_for_user(sender, instance, created,  **kwargs):
    if created:
        UserBlog(owner=instance).save()


