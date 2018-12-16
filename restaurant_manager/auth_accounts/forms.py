from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RestaurantUser


class RestaurantUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = RestaurantUser
        fields = ('username', 'email')


class RestaurantUserChangeForm(UserChangeForm):

    class Meta():
        model = RestaurantUser
        fields = UserChangeForm.Meta.fields
