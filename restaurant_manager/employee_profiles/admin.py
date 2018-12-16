from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EmployeeProfileCreationForm, EmployeeProfileChangeForm
from .models import EmployeeProfile

# Register your models here.
class EmployeeProfileAdmin(UserAdmin):
    model = EmployeeProfile
    add_form = EmployeeProfileCreationForm
    form = EmployeeProfileChangeForm

admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
