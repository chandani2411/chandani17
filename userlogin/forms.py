from .models import Comment,Reply

from django import forms


class CommentForm(forms.ModelForm):
    type = forms.CharField()
    class Meta:
        model = Comment
        exclude = ["like", ]

class ReplyForm(forms.ModelForm):
    type=forms.CharField()
    class Meta:
        model = Reply
        exclude=["like",]


