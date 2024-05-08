from django import forms

from .models import Product

from user_management.models import Profile


class ProductForm(forms.ModelForm):

    owner = forms.ModelChoiceField(required=False, queryset=Profile.objects)

    class Meta:
        model = Product
        fields = "__all__"


class TransactionForm(forms.Form):
    amount = forms.IntegerField(min_value=0)