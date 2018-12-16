from django.contrib import admin

from .models import Ingredient, IngredientCategory, InventoryItems, IngredientInventory

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(InventoryItems)
admin.site.register(IngredientInventory)
