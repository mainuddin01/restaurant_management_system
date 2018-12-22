from django.db import models
from django.db.models.signals import post_save

from employee_profiles.models import EmployeeProfile
from products.models import Product
# from restaurant.models import Customer

# Create your models here.
class CartItem(models.Model):
    cart = models.ForeignKey('Cart')
    item = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.item.name

    def save(self, *args, **kwargs):
        item_price = self.item.get_price()
        quantity = self.quantity
        line_total = item_price * quantity
        self.line_total = line_total
        super(CartItem, self).save(*args, **kwargs)
        return self

# def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
#     item_price = instance.item.get_price()
#     line_total = item_price * instance.quantity
#     instance.line_total = line_total
#     instance.save()
#
# post_save.connect(cart_item_post_save_receiver, sender=CartItem)


class Cart(models.Model):
    table_manager = models.ForeignKey(EmployeeProfile)
    item = models.ManyToManyField(Product, through='CartItem')
    customer = models.ForeignKey('restaurant.Customer', related_name='cart')
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)
