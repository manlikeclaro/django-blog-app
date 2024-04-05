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

    def __init__(self, *args, **kwargs):
        super(BlogCommentModelForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'id': 'comment-message',
            'placeholder': 'Enter your comment',  # Add placeholder attribute
            'rows': '10',  # Set rows attribute
            'cols': '8'
        })

        # Add labels to form fields
        # self.fields['content'].label = 'Enter Comment'
