from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from .models import EmployeeProfile

from .forms import EmployeeProfileCreationForm, EmployeeProfileChangeForm

# Create your views here.
class CreateEmployee(CreateView):
    form_class = EmployeeProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'employee_profiles/create_employee.html'

class EmployeeList(ListView):
    model = EmployeeProfile
    template_name = 'employee_profiles/employee_list.html'

class EmployeeDetail(DetailView):
    model = EmployeeProfile
    template_name = 'employee_profiles/employee_detail.html'

class UpdateEmployee(UpdateView):
    model = EmployeeProfile
    form_class = EmployeeProfileChangeForm
    success_url = reverse_lazy('login')
    template_name = 'employee_profiles/create_employee.html'
