# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-10 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ingredients.IngredientCategory')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('stocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.IngredientInventory')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='ingredientinventory',
            name='ingredients',
            field=models.ManyToManyField(through='ingredients.InventoryItems', to='ingredients.Ingredient'),
        ),
        migrations.AddField(
            model_name='ingredientinventory',
            name='kitchen_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ManyToManyField(to='ingredients.IngredientCategory'),
        ),
    ]
