from django import forms

from ingredients.models import Ingredient

from .models import Product, ProductCategory, ProductImage, Unit


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sale_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    unit = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Unit.objects.all(),)
    category = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-control'}), queryset=ProductCategory.objects.all(), required=False)
    ingredients = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-control'}), queryset=Ingredient.objects.all(), required=False)
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'checkbox-primary'}), initial=True)

    class Meta():
        model = Product
        exclude = ('slug',)
