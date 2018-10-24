from datetime import datetime
from django import template
from random import choice
register = template.Library()
from ERP.models.masters import *
from django.db import connection
from ERP.custom_views.common_functions import *
