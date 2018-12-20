from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import Ingredient, IngredientCategory

from .forms import IngredientForm, IngredientCategoryForm

# Create your views here.
class IngredientListView(ListView):
    model = Ingredient

class IngredientDetailView(DetailView):
    model = Ingredient

class IngredientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('home')

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True


class IngredientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy('home')

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True


class IngredientCategoryListView(ListView):
    model = IngredientCategory
    template_name = 'ingredients/category_list.html'

class IngredientCategoryDetailView(DetailView):
    model = IngredientCategory
    template_name = 'ingredients/ingredient_detail.html'

class IngredientCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = IngredientCategory
    form_class = IngredientCategoryForm
    success_url = reverse_lazy('home')
    template_name = 'ingredients/ingredient_form.html'

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True


class IngredientCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = IngredientCategory
    form_class = IngredientCategoryForm
    success_url = reverse_lazy('home')
    template_name = 'ingredients/ingredient_form.html'

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True
