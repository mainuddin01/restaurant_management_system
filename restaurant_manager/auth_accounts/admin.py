from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RestaurantUserCreationForm, RestaurantUserChangeForm
from .models import RestaurantUser

# Register your models here.
class RestaurantUserAdmin(UserAdmin):
    model = RestaurantUser
    add_form = RestaurantUserCreationForm
    form = RestaurantUserChangeForm

admin.site.register(RestaurantUser, RestaurantUserAdmin)
