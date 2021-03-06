# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-24 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0037_auto_20181024_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiryform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.Item')),
                ('leadid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.Leadcs')),
            ],
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='itemid',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='leadid',
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
    ]
