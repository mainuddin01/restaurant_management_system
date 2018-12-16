from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from ingredients.models import Ingredient

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

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.slug = slugify(self.name)
        self.save()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


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
    parent_category = models.ForeignKey('ProductCategory', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(ProductCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.name)
        self.save()

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
