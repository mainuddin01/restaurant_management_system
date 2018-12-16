from django.db import models
from django.conf import settings
from django.utils.text import slugify

# from products.models import Unit

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    unit = models.ForeignKey('products.Unit')
    category = models.ManyToManyField('IngredientCategory')

    def __str__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    parent_category = models.ForeignKey('IngredientCategory', blank=True, null=True)

    def __str__(self):
        return self.name



class InventoryItems(models.Model):
    inventory = models.ForeignKey('IngredientInventory')
    item = models.ForeignKey('Ingredient')
    quantity = models.DecimalField(max_digits=20, decimal_places=2)
    # unit = models.ForeignKey('products.Unit')

    def __str__(self):
        return self.item.name

class IngredientInventory(models.Model):
    # restaurant_manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='restaurant_manager' null=True, blank=True)
    kitchen_manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='kitchen_manager')
    ingredients = models.ManyToManyField('Ingredient', through='InventoryItems')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    approved = models.BooleanField(default=False)
    stocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
