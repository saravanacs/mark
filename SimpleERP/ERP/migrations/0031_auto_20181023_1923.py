# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0030_auto_20181023_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadcs',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='leadcs',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='leadcs',
            name='modified_date',
        ),
    ]
