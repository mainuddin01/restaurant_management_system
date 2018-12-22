from django.db import models
from django.core.urlresolvers import reverse

from carts.models import Cart

# Create your models here.
class Table(models.Model):
    LEFT = 'L'
    RIGHT = 'R'
    TABLE_ALIGNMENT_CHOICES = (
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    )
    name = models.CharField(max_length=50, unique=True)
    seats = models.PositiveSmallIntegerField()
    alignment = models.CharField(max_length=1, choices=TABLE_ALIGNMENT_CHOICES, default=LEFT)
    available = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def get_absolute_url(self):
        return reverse('restaurant:table_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Customer(models.Model):
    REGULARCUSTOMER = 'RC'
    WALKINGCUSTOMER = 'WC'
    CUSTOMER_TYPE_CHOICES = (
        (REGULARCUSTOMER, 'Regular Customer'),
        (WALKINGCUSTOMER, 'Walking Customer'),
    )
    table = models.ForeignKey('Table')
    type = models.CharField(max_length=2, choices=CUSTOMER_TYPE_CHOICES, default=REGULARCUSTOMER)
    name = models.CharField(max_length=50, default='Anonymous')
    members = models.PositiveSmallIntegerField(default=1)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)

    def get_cart(self):
        return Cart.objects.filter(customer=self.id).first()

    def get_absolute_url(self):
        return reverse('restaurant:customer_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
