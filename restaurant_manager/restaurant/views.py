from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .models import Table, Customer
from carts.models import Cart, CartItem
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




class CustomerCreateView(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, *args, **kwargs):
        customer_form = CustomerForm()
        table_id = self.kwargs.get('pk')
        context = {
            'form': customer_form,
            'table_id': table_id
        }
        return render(request, 'carts/users_carts.html', context)


    def post(self, request, *args, **kwargs):
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            table_id = self.kwargs.get('pk')
            table_instance = get_object_or_404(Table, id=table_id)
            customer.table = table_instance
            customer.save()
            table_manager = request.user
            customer_cart = Cart.objects.create(table_manager=table_manager, customer=customer)
            print(str(customer_cart))
            return HttpResponseRedirect(reverse('carts:table_user', kwargs={'pk': table_id}))

        context = {
            'form': customer_form,
            'table_id': table_id
        }
        return render(request, 'carts/users_carts.html', context)




    def test_func(self):
        if self.request.user.employee_type == 'TM' or self.request.user.is_superuser:
            return True

class CustomerDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Customer
    template_name = 'restaurant/table_detail.html'

    def test_func(self):
        if self.request.user.employee_type == 'TM' or self.request.user.is_superuser:
            return True
