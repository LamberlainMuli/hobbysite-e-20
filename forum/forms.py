from django import forms

from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        exclude = ["author"]


class ThreadUpdateForm(forms.ModelForm):
    class Meta:
        model = Thread
        exclude = ["thread", "author"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']