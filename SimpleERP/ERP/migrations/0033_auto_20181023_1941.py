# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 19:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0032_auto_20181023_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 41, 52, 37455)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 41, 52, 37474)),
        ),
        migrations.AlterField(
            model_name='leadcs',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 41, 52, 36769)),
        ),
        migrations.AlterField(
            model_name='leadcs',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 41, 52, 36791)),
        ),
    ]