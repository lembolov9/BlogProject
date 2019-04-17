from django.forms import ModelForm

from blog.models import Post


class GuiPostForm(ModelForm):
    class Meta:
        model=Post
        fields = ['title', 'text']
