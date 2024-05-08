from django import forms

from .models import ArticleCategory,Article,Comment


class WikiForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author']
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WikiEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled = True

        # author = getattr(self.instance, 'author', None)
        # Set the disabled attribute for the author field
        # self.fields['author'].disabled = True
        # Set the initial value for the author field

class WikiTitleFilterForm(forms.Form):
    title = forms.CharField()
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
