from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.core.exceptions import NON_FIELD_ERRORS
from .masters import *

class Project(models.Model):
    project_name = models.CharField(max_length=500)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    estimated_amount = models.FloatField(max_length=100)
    estimated_start_date = models.DateField(auto_now_add=True)
    estimated_end_date = models.DateField(blank=True, null=True)
    project_net_amt = models.FloatField(max_length=100, default=None)
    status = models.IntegerField(default=0)
    submit_status = models.IntegerField(default=0)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company',blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='project_Created_By_User', default=1)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='project_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)
#     class Meta:
#         unique_together = [
#             ("project_name", "deleted"),
#         ]

class Project_Item(models.Model):
    item= models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name='project_item_name')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.FloatField(default=0)
    rate = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    net_amount = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    
class Project_Tracking(models.Model):
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.IntegerField(default=0) # 1 -salary 2-other Expense
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    
    amount = models.FloatField(default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projecttracking_Created_By_User', default=1)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projecttracking_Modified_By_User', default=1)
    deleted = models.BooleanField(default=False)

    
    