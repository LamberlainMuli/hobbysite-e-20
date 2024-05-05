from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["author"]

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["article"]