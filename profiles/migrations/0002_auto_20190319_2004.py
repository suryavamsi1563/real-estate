# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='contacted_properties',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='listed_properties',
        ),
    ]