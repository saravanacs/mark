from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import masters,stock,selling
from ERP.serializers.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from ERP.custom_views.common_functions import *
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from django.urls import reverse
from rest_framework import status

row_per_page = settings.GLOBAL_SETTINGS['row_per_page']
@api_view(['GET', 'POST'])
def jqgrid_test(request):
    return Response(template_name='ERP/research/jqgrid.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@api_view(['GET', 'POST'])
def jqgrid_data(request):
    from django.db import connection
    sendrows=[]
    with connection.cursor() as cursor:
        query="select series,id,sales_date,discount,bill_amount,item_discount,discount,bill_amount_before_tax,tax_amount,net_amount,customer_id,paid_amount,balance_amount,(select name from ERP_customer cus where cus.id=sales.customer_id) as customer_name from ERP_salesinvoice sales"
        cursor.execute(query)
        rows = dictfetchall(cursor)
        sendrows=[]
        for row in rows:
            data={
             "CustomerName":row['customer_name'],
             "BillNo":row['series'],
             "BillAmount":row['bill_amount_before_tax'],
             "TaxAmount":row['tax_amount'],
             "NetAmount":row['net_amount'],
             "PaidAmouunt":row['paid_amount'],
             "BalanceAmount":row['balance_amount'],
            }
            sendrows.append(data)
    send_data={
        "records":"830", 
        "page":1, 
        "total":42,
        "rows":sendrows,
        }
    return Response(send_data)
    