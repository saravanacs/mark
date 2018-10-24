from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import masters,stock,project
from ERP.serializers.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from ERP.custom_views.common_functions import *
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from django.urls import reverse
from django.template.loader import render_to_string  
from django.db.models import Sum

row_per_page=settings.GLOBAL_SETTINGS['row_per_page']

@api_view(['GET', 'POST'])
def project_items_create(request):
    if request.method == 'GET':
        return Response({'data':'', 'module':'Project'}, template_name='ERP/project/create_update.html')
    else:
        mutable = request.POST._mutable
        request.POST._mutable = True
        error_details = []
        if not request.POST["project_id"]:
            company_id=session_user_company(request);
            data={
                "project_name":request.POST['project_name'],
                "estimated_start_date":db_store_date_only(request.POST['estimated_start_date']),
                "estimated_end_date":db_store_date_only(request.POST['estimated_end_date']),
                "status":request.POST['status'],
                "customer":request.POST['customer'],
                "description":request.POST['description'],
                'company':session_user_company(request),
                'project_net_amt':request.POST['estimated_amount'],
                'estimated_amount':request.POST['estimated_amount'],
                }
            serializer = ProjectSerializer(data=data)
            serializer.is_valid()
            if serializer.is_valid():
                user_id= session_user_id(request)
                date_modified=store_date_time()
                project=serializer.save()
                project_id=project.id
            else:
                project_id=""
                for key in serializer.errors.keys():
                    error_details.append({"field": key, "message": serializer.errors[key][0]})
                    data = {
                    "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                    }
        else:
            project_id=request.POST["project_id"]
        if project_id:
            if not request.POST['discount']:
                discount=0
            else:
                discount=request.POST['discount'];
            data_project_items={
                "project":project_id,
                "item":request.POST['item'],
                "qty":request.POST['qty'],
                "rate":request.POST['rate'], 
                "amount":request.POST['amount'],
                "discount":discount,
                "net_amount":request.POST['net_amount'],
                'deleted':0
               
                }
            serializer = ProjectItemSerializer(data=data_project_items)
            serializer.is_valid()
            if serializer.is_valid():
                user_id= session_user_id(request)
                date_modified=store_date_time()
                serializer.save()
                net_amount = Project_Item.objects.filter(project=project_id,deleted=0).aggregate(Sum('net_amount'))
                project_details=Project.objects.get(pk=project_id);
                project_details.project_net_amt=net_amount['net_amount__sum'];
                project_details.save();       
            else:
                error_details= []
                for key in serializer.errors.keys():
                    error_details.append({"field": key, "message": serializer.errors[key][0]})
                    data = {
                    "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                    }
        return_data={"project_id":project_id,"error_details":error_details}
        return Response(return_data)
    
    

@api_view(['GET'])
def project_items(request):
    html=None
    model_obj=[]
    #return Response("Hai")
    if request.is_ajax() and request.GET['id']:
        id=request.GET['id']
        data = []
        #return Response(request.GET['id'])
        custom_filter={}
        custom_filter['deleted']=0
        custom_filter['project_id']=id
        
        model_obj = Project_Item.objects.filter(**custom_filter)
        model_obj_invoice = Project.objects.get(pk=id)
            
        #data = Stockentry_itemsSerializer(model_obj, many=True).data
    html = render_to_string('ERP/project/project_items.html', {'data': model_obj,"basic_data":model_obj_invoice})
    #html = render_to_string('ERP/stock/test.html', {'data': request})
    return HttpResponse(html)

@api_view(['GET', 'POST'])
def project_create(request):
    if request.method == 'GET':
        return Response({'data': '', 'module': 'Project'}, template_name='ERP/project/create_update.html')
    else:
        if request.POST['project_id']:
            project_id=request.POST['project_id']
            project_details=Project.objects.get(pk=project_id);
            project_details.submit_status=1;
            project_details.save();
    if request.accepted_renderer.format == 'html':
                return Response({"error_data": ""}, template_name='ERP/project/create_update.html')
    return Response(data, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def project_update(request, id):
    data_obj = Project.objects.get(id=id)
    if request.method == "GET":
        ser_data = ProjectSerializer(data_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({"data": ser_data}, template_name='ERP/project/create_update.html')
        return Response({"data": ser_data}, status=status.HTTP_200_OK)
    else:
        serializer = ProjectSerializer(data_obj, data=request.data, partial=True)
        if serializer.is_valid():
            user_id= session_user_id(request)
            date_modified=store_date_time()
            serializer.save(modified_date=date_modified,modified_by=user_id)
            if request.accepted_renderer.format == 'html':
                return HttpResponseRedirect(reverse('ERP:project_list'))
            return Response({"data": "Updated successfully"}, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key in serializer.errors.keys():
                error_details.append({"field": key, "message": serializer.errors[key][0]})
            data = {
                    "Error": {
                        "status": 400,
                        "message": "Your submitted data was not valid - please correct the below errors",
                        "error_details": error_details
                        }
                    }
            if request.accepted_renderer.format == 'html':
                return Response({"error_data": data}, template_name='ERP/project/project_create.html')
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST','Delete'])
#@permission_classes((IsAuthenticated, ))
def project_view(request, id):
    data_obj = Project.objects.get(id=id)
    if request.method == "GET":
        ser_data = ProjectSerializer(data_obj).data
        if request.accepted_renderer.format == 'html':
            return Response({"data": ser_data,"view_mode":1}, template_name='ERP/project/create_update.html')
        return Response({"data": ser_data,"view_mode":1}, status=status.HTTP_200_OK)

def delete_project(request,id):
    selected_values=Project.objects.get(pk=id)
    user_id= session_user_id(request)
    modified_date=store_date_time()
    selected_values.modified_date=modified_date
    selected_values.deleted=1
    selected_values.save();
    return HttpResponseRedirect(reverse('ERP:project_list'))

def project_tracking_delete(request,id):
    selected_values=Project_Tracking.objects.get(pk=id)
    user_id= session_user_id(request)
    modified_date=store_date_time()
    selected_values.modified_date=modified_date
    selected_values.deleted=1
    selected_values.save();
    return HttpResponseRedirect(reverse('ERP:project_list'))

@api_view(['GET', 'POST'])
def projectitems_delete(request):
    if request.is_ajax() and request.GET['id']:
        id=request.GET['id']
        selected_values=Project_Item.objects.get(pk=request.GET['id'])
        user_id= session_user_id(request)
        date_modified=store_date_time()
        selected_values.modified_date=date_modified
        selected_values.modified_by=user_id
        selected_values.deleted=1
        selected_values.save();
        net_amount = Project_Item.objects.filter(project=selected_values.project.id,deleted=0).aggregate(Sum('net_amount'))
        project_details=Project.objects.get(pk=selected_values.project.id);
        project_details.project_net_amt=net_amount['net_amount__sum'];
        project_details.save(); 
    return HttpResponse("1")

@api_view(['GET','POST'])
def project_tracking(request):
     # sales_invoice_id=request.POST['salesinvoice_item_id']
    if request.is_ajax() and request.POST['project_id']:
        id = request.POST['project_id']
        data = []
        # return Response(request.GET['id'])
        custom_filter = {}
        custom_filter['deleted'] = 0
        custom_filter['project'] = id
        model_obj=None;
        model_obj = Project_Tracking.objects.filter(**custom_filter)
    model_data = ProjectTrackingSerializer(model_obj, many=True).data
    html = render_to_string('ERP/project/project_tracking.html', {'data':model_data})
    # html = render_to_string('ERP/stock/test.html', {'data': request})
    return HttpResponse(html)
    # return Response({"sales_invoice_id":sales_invoice_id})

@api_view(['GET','POST'])
def project_tracking_add(request):
    project_id = request.POST['project_id'];
    description = request.POST['description'];
    date = request.POST['date'];
    amount = request.POST['amount'];
    data_project_tracking={
                "project":project_id,
                "description":description,
                "date":db_store_date_only(date),
                "amount":amount, 
                "status":1,
                }
    serializer = ProjectTrackingSerializer(data=data_project_tracking)
    serializer.is_valid()
    if serializer.is_valid():
        user_id= session_user_id(request)
        date_modified=store_date_time()
        serializer.save(created_by=user_id,created_date=date_modified)
    return Response({"project_id":project_id})

@api_view(['GET', 'POST'])
def list_project(request):
    custom_filter = {}
    custom_filter['deleted'] = 0
    try:
        if request.data['project_name']:
            custom_filter['project_name'] = request.data['project_name']
        if request.data['id']:
            custom_filter['id'] = request.data['id']
    except:
        pass
    model_obj = Project.objects.filter(**custom_filter)
    model_data = ProjectSerializer(model_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(model_data, row_per_page)
    try:
        model_data = paginator.page(page)
    except PageNotAnInteger:
        model_data = paginator.page(1)
    except EmptyPage:
        model_data = paginator.page(paginator.num_pages)
    if request.accepted_renderer.format == 'html':
        return Response({"data": model_data, 'module': 'Project', "custom_filter": custom_filter},
                        template_name='ERP/project/list.html')
    return Response({"data": model_data, "custom_filter": custom_filter}, status=status.HTTP_200_OK)