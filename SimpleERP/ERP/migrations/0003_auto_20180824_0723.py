# Generated by Django 2.0.6 on 2018-08-24 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ERP', '0002_auto_20180824_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_tracking',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projecttracking_Created_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='date',
            field=models.DateField(auto_now=True, default=None),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projecttracking_Modified_By_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERP.Project'),
        ),
        migrations.AddField(
            model_name='project_tracking',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]