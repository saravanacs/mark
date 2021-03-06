# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 19:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0031_auto_20181023_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 37, 54, 273448)),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 37, 54, 273466)),
        ),
        migrations.AddField(
            model_name='leadcs',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 37, 54, 272732)),
        ),
        migrations.AddField(
            model_name='leadcs',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leadcs',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 19, 37, 54, 272755)),
        ),
    ]
