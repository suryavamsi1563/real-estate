# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-31 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20190131_1145'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Property',
            new_name='PropertyTable',
        ),
    ]