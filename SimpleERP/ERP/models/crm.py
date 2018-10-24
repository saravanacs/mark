from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.core.exceptions import NON_FIELD_ERRORS
from .masters import *
import re
import os
import sys
from django.utils import timezone

class Leadcs(models.Model):
	leadno = models.CharField(max_length = 200, unique = True)
	lead_type = models.CharField(max_length = 200)
	lead_source = models.CharField(max_length = 200)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'customer')
	contact_person = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'person')
	contact_person_contact_no = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = 'contact')
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	deleted = models.BooleanField(default=False)

class Enquiryform(models.Model):
	leadid = models.ForeignKey(Leadcs, on_delete=models.CASCADE)
	itemid = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.CharField(max_length = 200)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	deleted = models.BooleanField(default=False)