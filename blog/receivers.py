from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Post, UserBlog
from BlogProject.settings import EMAIL_HOST_USER, SITE_URL


@receiver(post_save, sender=User)
def create_blog_for_user(sender, instance, created,  **kwargs):
    if created:
        UserBlog(owner=instance).save()


@receiver(post_save, sender=Post)
def send_messages(sender, instance, created, **kwargs):
    if created:
        blog = UserBlog.objects.get(owner=instance.author)
        for user in blog.subscribers.all():
            if user.email == '' or user.email == instance.author.email:
                continue
            msg = f'Привет, у тебя в ленте новый пост! {SITE_URL+"post/"+str(instance.pk)}'
            send_mail('Новый пост', msg, EMAIL_HOST_USER,
                      (user.email,), fail_silently=False)
