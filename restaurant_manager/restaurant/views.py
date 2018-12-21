from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy

from .models import Table, Customer
from .forms import TableForm, CustomerForm

# Create your views here.
class TableCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Table
    form_class = TableForm


    def test_func(self):
        if self.request.user.employee_type == 'RM' or self.request.user.is_superuser:
            return True

class TableListView(LoginRequiredMixin, ListView):
    model = Table

class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table

class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    form_class = TableForm


    def test_func(self):
        if self.request.user.employee_type == 'RM' or self.request.user.is_superuser:
            return True

class TableDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Table
    success_url = reverse_lazy('restaurant:table_list')


    def test_func(self):
        if self.request.user.employee_type == 'RM' or self.request.user.is_superuser:
            return True
