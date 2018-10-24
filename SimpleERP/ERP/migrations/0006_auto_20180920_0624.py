# Generated by Django 2.0.6 on 2018-09-20 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0005_auto_20180824_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Purchase_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Purchase_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice_items',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice_items',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PurchaseInvoice_items_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice_items',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PurchaseInvoice_items_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sales_serial_nos',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.WareHouse'),
        ),
        migrations.AlterField(
            model_name='serial_no',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='serial_no',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Serial_no_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serial_no',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Serial_no_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serial_no',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.WareHouse'),
        ),
        migrations.AlterField(
            model_name='serial_no_tracking',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='serial_no_tracking',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Serial_no_tracking_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serial_no_tracking',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Serial_no_tracking_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='serial_no_tracking',
            name='serial_no_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.Serial_no'),
        ),
        migrations.AlterField(
            model_name='serial_no_tracking',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.WareHouse'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.WareHouse'),
        ),
        migrations.AlterField(
            model_name='stock_tracking',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='stock_tracking',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stock_Tracking_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock_tracking',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stock_Tracking_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stock_tracking',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.WareHouse'),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='StockEntry_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='StockEntry_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stockentry_items',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='stockentry_items',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stockentry_items_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stockentry_items',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stockentry_items_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taxsplitup',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Company'),
        ),
        migrations.AlterField(
            model_name='taxsplitup',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TaxSplitup_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taxsplitup',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TaxSplitup_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
    ]
