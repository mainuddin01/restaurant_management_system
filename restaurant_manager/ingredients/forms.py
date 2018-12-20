from django import forms

from ingredients.models import Ingredient, IngredientCategory


class IngredientForm(forms.ModelForm):

    class Meta():
        model = Ingredient
        exclude = ('slug',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})


class IngredientCategoryForm(forms.ModelForm):

    class Meta():
        model = IngredientCategory
        exclude = ('slug',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['parent_category'].widget.attrs.update({'class': 'form-control'})

        self.fields['parent_category'].required = False
