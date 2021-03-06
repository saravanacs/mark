# Generated by Django 2.0.6 on 2018-08-24 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ERP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='bill',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expense',
            name='bill_no',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expense_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
        ),
        migrations.AddField(
            model_name='expense',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.expensecategory'),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expense_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=None),
        ),
        migrations.AddField(
            model_name='expense',
            name='net_total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='expense',
            name='supplier',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.TaxGroup'),
        ),
        migrations.AddField(
            model_name='expense',
            name='tax_per',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='expense',
            name='taxamount',
            field=models.FloatField(default=0),
        ),
    ]
