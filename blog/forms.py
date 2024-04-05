# from django.forms import forms
from django import forms

from blog.models import BlogComment


class BlogCommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content', )
        labels = {
            "content": "Message",
        }
