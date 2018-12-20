from django.contrib import admin

from .models import Product, ProductCategory, Unit, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Unit)
