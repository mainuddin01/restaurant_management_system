from django import forms

from .models import Table, Customer


class TableForm(forms.ModelForm):

    class Meta():
        model = Table
        fields = ('name', 'seats', 'alignment', 'available', 'active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['seats'].widget.attrs.update({'class': 'form-control'})
        self.fields['alignment'].widget.attrs.update({'class': 'form-control'})
        self.fields['available'].label = "Available "
        self.fields['active'].label = "Active "


class CustomerForm(forms.ModelForm):

    class Meta():
        model = Customer
        exclude = ('created_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['members'].widget.attrs.update({'class': 'form-control'})
        self.fields['mobile'].widget.attrs.update({'class': 'form-control'})
