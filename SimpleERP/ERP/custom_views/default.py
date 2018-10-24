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


def index(request):
	#return HttpResponse(request.session['_auth_user_id'])
	return render(request, template_name='ERP/master/index.html')

@api_view(['GET', 'POST'])
def login_user(request):
	if request.method == 'GET':
		return render(request, 'ERP/login.html')
	else:
		username = request.POST['username']
		password = request.POST['password']
		logout(request)
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				request.session['newvariable']='test'
# 				return Response({"data": "Data Added Successfully"},
#                             template_name='ERP/signup.html')
				return HttpResponseRedirect('/erp/home/')
			
		return render(request, 'ERP/login.html')

@api_view(['GET', 'POST'])
def signup_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			userobj=User.objects.get(username=user)
			userobj.email=request.POST['email']
			userobj.first_name=request.POST['first_name']
			userobj.last_name=request.POST['last_name']
			userobj.date_joined=db_store_date(request.POST['date_joined'])
			userobj.is_active=1;
			userobj.save();
			
			profile=Profile.objects.get(user=userobj.id)
			if request.POST['company']:
				profile.company=Company.objects.get(pk=request.POST['company'])
			profile.address=request.POST['address']
			profile.contact_no=request.POST['contact_no']
			if request.POST['date_of_birth']:
				profile.date_of_birth=db_store_date_only(request.POST['date_of_birth']);
			profile.save();
			return Response({"data": "Data Added Successfully"},
                            template_name='ERP/signup.html')
		else:
			return Response({"errors": form.errors},
                            template_name='ERP/signup.html')
	else:
		form = UserCreationForm()
	return render(request, 'ERP/signup.html', {'form': form})



@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def user_update(request, id):
    data_obj = User.objects.get(id=id)
    data_profile = Profile.objects.get(user=id)
    #data_obj['profile']=data_profile;
    if request.method == "GET":
        ser_data = data_obj;
        if request.accepted_renderer.format == 'html':
            return Response({"data": ser_data,"data_profile":data_profile}, template_name='ERP/signup.html')
        return Response({"data": ser_data}, status=status.HTTP_200_OK)
    else:
    	userobj=User.objects.get(id=id)
    	userobj.email=request.POST['email']
    	userobj.first_name=request.POST['first_name']
    	userobj.last_name=request.POST['last_name']
    	userobj.date_joined=db_store_date(request.POST['date_joined'])
    	userobj.is_active=1
    	userobj.save()
    	profile=Profile.objects.get(user=userobj.id)
    	if request.POST['company']:
    		profile.company=Company.objects.get(pk=request.POST['company'])
    	profile.address=request.POST['address']
    	profile.contact_no=request.POST['contact_no']
    	if request.POST['date_of_birth']:
    		profile.date_of_birth=db_store_date_only(request.POST['date_of_birth']);
    	profile.save();
    	return HttpResponseRedirect(reverse('ERP:user_list'))
#     	if request.accepted_renderer.format == 'html':
#     		return Response({"error_data": userobj}, template_name='ERP/user_list.html')
        #return Response(userobj, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def user_view(request, id):
    data_obj = User.objects.get(id=id)
    data_profile = Profile.objects.get(user=id)
    if request.method == "GET":
        
        if request.accepted_renderer.format == 'html':
            return Response({"data": data_obj,"view_mode":1,'module':'User',"data_profile":data_profile}, template_name='ERP/signup.html')
        return Response({"data": ser_data,"view_mode":1}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def user_list(request):
     custom_filter={}
     custom_filter['is_active']=1
     try:
        if request.data['name']:
            custom_filter['name']=request.data['name']
        if request.data['customergroup']:
            custom_filter['customergroup']=request.data['customergroup']

        if request.data['primary_contact_no']:
            custom_filter['primary_contact_no']=request.data['primary_contact_no']
     except:
        pass
     model_data = User.objects.filter(**custom_filter)
     #model_data = User(model_obj, many=True).data
     page = request.GET.get('page', 1)
     paginator = Paginator(model_data, row_per_page)
     try:
        model_data = paginator.page(page)
     except PageNotAnInteger:
        model_data = paginator.page(1)
     except EmptyPage:
        model_data = paginator.page(paginator.num_pages)
     if request.accepted_renderer.format == 'html':
        return Response({"data": model_data,'module':'User',"custom_filter":custom_filter}, template_name='ERP/user_list.html')
     return Response({"data": model_data,"custom_filter":custom_filter}, status=status.HTTP_200_OK)
