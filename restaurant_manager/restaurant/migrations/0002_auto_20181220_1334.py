# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='members',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
