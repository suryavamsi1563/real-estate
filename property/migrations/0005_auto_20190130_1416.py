# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='property_images'),
        ),
    ]
