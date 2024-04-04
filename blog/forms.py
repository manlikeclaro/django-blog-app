# from django.forms import forms
from django import forms

from blog.models import BlogComment


class BlogCommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('author_name', 'author_email', 'comment_content')
        labels = {
            "author_name": "Name",
            "author_email": "Email",
            "comment_content": "Message",
        }
