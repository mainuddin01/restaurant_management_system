from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse

from .models import Product, ProductCategory, ProductImage

from .forms import ProductForm, ProductCategoryForm, ProductImageForm

# Create your views here.
class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    # success_url = reverse_lazy('home')

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True

class ProductImageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ProductImage
    form_class = ProductImageForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:list')

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True


class ProductCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    # success_url = reverse_lazy('home')
    template_name = 'products/product_form.html'

    def test_func(self):
        if self.request.user.employee_type in ['RM', 'KM'] or self.request.user.is_superuser:
            return True
