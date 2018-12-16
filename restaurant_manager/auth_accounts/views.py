from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .forms import RestaurantUserCreationForm

# Create your views here.
class SignUp(CreateView):
    form_class = RestaurantUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth_accounts/signup.html'
