# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0022_auto_20181023_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
    ]
