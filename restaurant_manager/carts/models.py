from django.db import models

from employee_profiles.models import EmployeeProfile
from products.models import Product
# from restaurant.models import Customer

# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey('Cart')
    item = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.item.name


class Cart(models.Model):
    table_manager = models.ForeignKey(EmployeeProfile)
    item = models.ManyToManyField(Product, through='CartItem')
    customer = models.ForeignKey('restaurant.Customer', related_name='cart')
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)
