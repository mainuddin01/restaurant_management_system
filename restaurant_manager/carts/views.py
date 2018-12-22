from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product, ProductCategory

from restaurant.models import Customer

from restaurant.forms import CustomerForm

import django_filters

# Create your views here.
class ProductFilter(django_filters.FilterSet):
    # name, price, category,

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', distinct=True)
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', distinct=True)
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', distinct=True)
    category = django_filters.ModelChoiceFilter(queryset=ProductCategory.objects.all(), distinct=True)

    class Meta:
        model = Product
        fields = [
            'name',
        ]

class TableUserView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        table_id = self.kwargs.get('pk')
        active_customers = Customer.objects.filter(table=table_id, active=True)
        product_list = Product.objects.all()
        product_filter = ProductFilter(request.GET, queryset=product_list)

        context = {
            'mininavbar': True,
            'table_id': table_id,
            'active_customers': active_customers,
            'customer_form': CustomerForm(),
            'product_filter': product_filter,
        }
        return render(request, 'carts/users_carts.html', context)
