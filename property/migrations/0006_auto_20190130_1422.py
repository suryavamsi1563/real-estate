# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-30 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import property.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20190130_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='tax_document',
            field=models.FileField(blank=True, null=True, upload_to=property.models.upload_property_files),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=property.models.upload_property_images),
        ),
    ]
