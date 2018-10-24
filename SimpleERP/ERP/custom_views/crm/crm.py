from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import *
from ERP.serializers.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from ERP.custom_views.common_functions import *
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from django.urls import reverse


row_per_page = settings.GLOBAL_SETTINGS['row_per_page']


@api_view(['GET','POST'])
def create_lead(request):
	#return render(request, template_name='unit_create_update.html')
	if request.method == 'GET':
		return Response({'data':'', 'module':'Lead Entry'}, template_name='ERP/crm/create_update.html')
	else:
		serializer = LeadcsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save();
			if request.accepted_renderer.format == 'html':
				return Response({'data':'success'},template_name = 'ERP/crm/create_update.html')
			return Response({'data':'success'})
		else:
			if request.accepted_renderer.format == 'html':
				return Response({'data':serializer.errors},template_name = 'ERP/crm/create_update.html')
			return Response({'data':'error'})


@api_view(['GET'])
def list_lead(request):
	model_obj = Leadcs.objects.all()
	model_data = LeadcsSerializer(model_obj, many=True).data
	if request.accepted_renderer.format == 'html':
		return Response({"data": model_data},template_name='ERP/crm/lead_list.html')
	return Response({"data": model_data})


@api_view(['GET','PUT','POST'])
def update_lead(request, id):
 #return render(request, template_name='unit_create_update.html')
 data_obj = Leadcs.objects.get(id=id)
 if request.method == 'GET':
  data = LeadcsSerializer(data_obj).data
  return Response({'data':data},template_name='ERP/crm/create_update.html')
 else:
  serializer = LeadcsSerializer(data_obj, request.data, partial=True)
  if serializer.is_valid():
   serializer.save();
   if request.accepted_renderer.format == 'html':
    return Response({'data':'success'},template_name='ERP/crm/create_update.html')
   return Response({'data':'success'})
  else:
   if request.accepted_renderer.format == 'html':
    return Response({'data':serializer.errors},template_name='ERP/crm/create_update.html')
   return Response({'data':'success'})


@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def lead_view(request, id):
    if request.method == 'GET':
        data=Leadcs.objects.get(id=id)
        return Response({'data':data, 'module':'Lead Entry'}, template_name='ERP/crm/create_update.html')


@api_view(['GET', 'POST','Delete'])
def lead_delete(request,id):
	selected_values=Leadcs.objects.get(pk=id)
	selected_values.deleted=1;
	selected_values.save();
	return HttpResponseRedirect(reverse('ERP:lead_list'))





@api_view(['GET', 'POST','Delete'])
def items_create(request):
	#return render(request, template_name='unit_create_update.html')
	if request.method == 'GET':
		return Response({'data':''}, template_name='ERP/crm/create_update.html')
	else:
		serializer = EnquirySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save();
			if request.accepted_renderer.format == 'html':
				return Response({'data':'success'},template_name = 'ERP/crm/create_update.html')
			return Response({'data':'success'})
		else:
			if request.accepted_renderer.format == 'html':
				return Response({'data':serializer.errors},template_name = 'ERP/crm/create_update.html')
			return Response({'data':'error'})