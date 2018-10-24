from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import *
from ERP.serializers.serializers import *
from django.contrib.auth import authenticate, login, logout
from ERP.custom_views.common_functions import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.response import Response
from ERP.custom_views.common_functions import store_date_time,\
    db_store_date
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from django.urls import reverse

row_per_page=settings.GLOBAL_SETTINGS['row_per_page']


def paymententry_create(request):
    #return HttpResponse(request.session['_auth_user_id'])
    return render(request, template_name='ERP/accounts/paymententry/create_update.html')