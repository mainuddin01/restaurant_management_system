from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from ingredients.models import Ingredient

import random

from string import ascii_lowercase

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey('Unit')
    active = models.BooleanField(default=True)
    category = models.ManyToManyField('ProductCategory')
    ingredients = models.ManyToManyField(Ingredient)

    def get_price(self):
        if self.sale_price:
            return self.sale_price
        return self.price

    def get_single_image(self):
        if self.productimage_set:
            return self.productimage_set.first()
        return None

    # It will cause recursion error
    # def save(self, *args, **kwargs):
    #     super(Product, self).save(*args, **kwargs)
    #     self.slug = slugify(self.name)
    #     self.save()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

pre_save.connect(product_pre_save_receiver, sender=Product)


def image_upload_to(instance, filename):
    product_name = instance.product.name
    slug = slugify(product_name)
    special_code = [(str(random.randint(0, 10)) + random.choice(ascii_lowercase)) for i in range(2)]
    base_name, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, special_code, file_extension)
    return "product_images/%s/%s" %(slug, new_filename)

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)

    def __str__(self):
        return self.product.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name

def product_category_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

pre_save.connect(product_category_pre_save_receiver, sender=ProductCategory)

class Unit(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
