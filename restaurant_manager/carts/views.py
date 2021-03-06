from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse

from products.models import Product, ProductCategory

from restaurant.models import Customer

from .models import Cart, CartItem

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

        cart_id = request.GET.get('cart_id')
        item_id = request.GET.get('item_id')
        item_added_to_cart = False
        cart_item_data = None

        if cart_id and item_id:
            cart = get_object_or_404(Cart, id=cart_id)
            item = get_object_or_404(Product, id=item_id)
            try:
                cart_item, item_added_to_cart = CartItem.objects.get_or_create(cart=cart, item=item)
                cart_item_data = {'cart_item': cart_item.id, 'cart_item_name': cart_item.item.name, 'cart_item_quantity': cart_item.quantity, 'cart_item_line_total': cart_item.line_total}
            except:
                raise Http404

        cart_item_id = request.GET.get('item')
        item_qty = request.GET.get('qty')

        updated = False
        deleted = False
        item_line_total = 0.00

        if cart_item_id:
            cart_item = get_object_or_404(CartItem, id=cart_item_id)
            item_qty = int(item_qty)
            if item_qty > 0:
                cart_item.quantity = item_qty
                updated_item = cart_item.save()
                item_line_total = updated_item.line_total
            else:
                cart_item.delete()
                deleted = True

        if request.is_ajax():
                return JsonResponse({'updated': updated, 'deleted': deleted, 'item_line_total': item_line_total, 'item_added_to_cart': item_added_to_cart, 'cart_item_data': cart_item_data})

        context = {
            'mininavbar': True,
            'table_id': table_id,
            'active_customers': active_customers,
            'customer_form': CustomerForm(),
            'product_filter': product_filter,
        }
        return render(request, 'carts/users_carts.html', context)
