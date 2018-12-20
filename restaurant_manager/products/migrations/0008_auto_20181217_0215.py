# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-16 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Unit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory'),
        ),
    ]