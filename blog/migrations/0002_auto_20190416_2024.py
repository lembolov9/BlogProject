# Generated by Django 2.0.4 on 2019-04-16 20:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='feed',
            field=models.ManyToManyField(blank=True, related_name='feed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='read', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='blog_subs', to=settings.AUTH_USER_MODEL),
        ),
    ]
