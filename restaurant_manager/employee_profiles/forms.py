from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import EmployeeProfile

DESIGNATION_CHOICES = (
    ('', 'Select employee type'),
    ('TM', 'Table Manager'),
    ('KM', 'Kitchen Manager'),
    ('RM', 'Restaurant Manager'),
    ('SF', 'Shef')
)

class EmployeeProfileCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    employee_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=DESIGNATION_CHOICES)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}), required=False)
    salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    joining_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}), required=False)
    leaving_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}), required=False)
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'checkbox-primary'}), initial=True)
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta(UserCreationForm):
        model = EmployeeProfile
        # fields = ('username', 'email')
        # fields = UserCreationForm.Meta.fields + ('employee_type', 'mobile', 'address', 'photo', 'salary', 'joining_date', 'leaving_date', 'active')
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'employee_type', 'mobile', 'address', 'salary', 'joining_date', 'leaving_date', 'active', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'


class EmployeeProfileChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=False)
    employee_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=DESIGNATION_CHOICES, required=False)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    joining_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}), required=False)
    leaving_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}), required=False)
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'checkbox-primary'}), initial=True)
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model = EmployeeProfile
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'first_name', 'last_name', 'email', 'employee_type', 'mobile', 'address', 'salary', 'joining_date', 'leaving_date', 'active', 'photo', 'password')
