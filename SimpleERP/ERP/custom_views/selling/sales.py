from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from ERP.models import masters, stock, selling
from ERP.serializers.serializers import *
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from ERP.custom_views.common_functions import *
from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import  settings
from django.urls import reverse
from rest_framework import status
from django.db.models import Sum
from django.template.loader import render_to_string
from ERP.custom_views.stock.stock import *
from ERP.custom_views.stock.stockentry import *
from django.contrib import messages

row_per_page = settings.GLOBAL_SETTINGS['row_per_page']
@api_view(['GET', 'POST'])
def sales_create(request):
    if request.method == 'GET':
        return Response({'data':'', 'module':'Sales Create'}, template_name='ERP/selling/sales/create_update.html')

@api_view(['GET', 'POST'])
def sales_items(request):
    html = None
    model_obj = []
    model_obj_invoice = None;
    model_obj = None;
    if request.is_ajax() and request.GET['id']:
        id = request.GET['id']
        data = []
        custom_filter = {}
        custom_filter['deleted'] = 0
        custom_filter['sales_invoice_id'] = id
        model_obj = SalesInvoice_Items.objects.filter(**custom_filter).order_by('-id')
        model_obj_invoice = Salesinvoice.objects.get(pk=id)
    html = render_to_string('ERP/selling/sales/sales_items.html', {'data': model_obj, "basic_data":model_obj_invoice})
    return HttpResponse(html)

@api_view(['GET', 'POST'])
def service_items(request):
    html = None
    model_obj = []
    model_obj_invoice = None;
    model_obj = None;
    if request.is_ajax() and request.POST['sales_invoice_id']:
        id = request.POST['sales_invoice_id']
        data = []
        custom_filter = {}
        custom_filter['deleted'] = 0
        custom_filter['sales_invoice_id'] = id
        model_obj = SalesInvoice_Items.objects.filter(**custom_filter).order_by('-id')
        model_obj_invoice = Salesinvoice.objects.get(pk=id)
    html = render_to_string('ERP/selling/sales/service_items_create.html', {'data': model_obj, "basic_data":model_obj_invoice})
    return HttpResponse(html)

@api_view(['GET', 'POST'])
def service_items_add(request):
    service_items = {
                "sales_invoice":request.POST['sales_invoice_id'],
                "service_item":request.POST['service_item'],
                "service_item_for":request.POST['service_item_for'],
                "service_item_rate":request.POST['service_item_rate'],
                "warehouse":request.POST['warehouse'],
                "service_item_amount":request.POST['service_item_amount'],
                "service_item_qty":request.POST['service_item_qty'],
                'deleted':0
                }
    serializer = ServiceBilling_ItemsSerializer(data=service_items)
    if serializer.is_valid():
        company_id = session_user_company(request);
        salesinvoice_item = serializer.save(company=company_id)
        return Response({"status":True})
    else:
        error_details=[]
        for key in serializer.errors.keys():
            error_details.append({"field": key, "message": serializer.errors[key][0]})
        error_data = {
            "Error": {
            "status": 400,
            "message": "Your submitted data was not valid - please correct the below errors",
            "error_details": error_details
        }
        }
        return Response({"status":error_details})
    
@api_view(['GET', 'POST'])
def service_items_show(request):
    custom_filter = {}
    model_data=[]
    if request.is_ajax() and request.POST['sales_invoice_id']:
        id = request.POST['sales_invoice_id']
        custom_filter['sales_invoice'] = id
        custom_filter['deleted'] = 0
        model_obj = ServiceBilling_Items.objects.filter(**custom_filter).order_by('-id')
        model_data = ServiceBilling_ItemsSerializer(model_obj, many=True).data
    html = render_to_string('ERP/selling/sales/service_items_list.html', {'data': model_data})
    return HttpResponse(html)

@api_view(['GET', 'POST'])
def sales_list(request):
    custom_filter = {}
    custom_filter['deleted'] = 0
    model_obj = Salesinvoice.objects.filter(**custom_filter).order_by('-id')
    model_data = SalesInvoiceSerializer(model_obj, many=True).data
    page = request.GET.get('page', 1)
    paginator = Paginator(model_data, row_per_page)
    try:
        model_data = paginator.page(page)
    except PageNotAnInteger:
        model_data = paginator.page(1)
    except EmptyPage:
        model_data = paginator.page(paginator.num_pages)
    if request.accepted_renderer.format == 'html':
        return Response({"data": model_data, 'module':'Sales Invoice', "custom_filter":custom_filter}, template_name='ERP/selling/sales/list.html')
    return Response({"data": model_data, "custom_filter":custom_filter}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def items_create(request):
    item_id = request.data['item']
    serial_no = request.data['serial_no']
    sales_invoice_id = request.data['sales_invoice_id']
    error_details = []
    company_id = session_user_company(request);
    error_mode = 0
    error_data = None
    if not sales_invoice_id:
        if request.POST['bill_type'] == 3:
            mode="SER"
        elif request.POST['bill_type'] == 2:
            mode = "EST"
        else:
            mode = "SIN"
        series = serires_values(company_id, mode)
        sales_date = db_store_date(request.POST['sales_date'])
        
        data = {
                "series":series,
                "sales_date":sales_date,
                "customer":request.POST['customer'],
                "bill_type":request.POST['bill_type'],
                "bill_mode":request.POST['bill_mode'],
            }
        serializer = SalesInvoiceSerializer(data=data)
        if serializer.is_valid():
            user_id = session_user_id(request)
            date_modified = store_date_time()
            sales_invoice = serializer.save(created_by=user_id, created_date=date_modified)
            sales_invoice_id = sales_invoice.id
        else:
            sales_invoice_id = ""
            for key in serializer.errors.keys():
                error_details.append({"field": key, "message": serializer.errors[key][0]})
            error_data = {
                "Error": {
                "status": 400,
                "message": "Your submitted data was not valid - please correct the below errors",
                "error_details": error_details
            }
            }
            error_mode = 1
            return_data = {"sales_invoice_id":sales_invoice_id, "error_details":error_data, "error_mode":error_mode}
            return Response(return_data)
    if sales_invoice_id:
       if sales_invoice_id:
            discount = 0;
            item = request.POST['item'];
            qty = request.POST['qty']
            old_qty = 0;
            # return Response(item)
            invoice_mat = None;   
            try:
                invoice_mat = SalesInvoice_Items.objects.get(sales_invoice_id=sales_invoice_id, item=item, deleted=0)
                if invoice_mat:
                    # invoice_mat=SalesInvoice_Items.objects.get(sales_invoice=sales_invoice_id,item=item,deleted=0)
                    if invoice_mat:
                        old_qty = invoice_mat.qty
                        discount = invoice_mat.discount
            except:
                pass
            qty = float(qty) + float(old_qty)
            try:
                item_price = Price.objects.get(item=item, company=company_id, deleted=0)
            except:
                error_details = []
                error_data = {
                "Error": {
                "status": 400,
                "message": "Item Rate not set",
                "error_details":"",
                }
                }
                error_mode = 1
                return_data = {"sales_invoice_id":sales_invoice_id, "error_details":error_data, "error_mode":error_mode}
                return Response(return_data)
            rate = item_price.selling_price
            tax_group = item_price.selling_tax_group_id
            tax_per = item_price.selling_tax_group.tax_per
            bill_amount = float(qty) * float(rate)
            tax_amount = (float(bill_amount) * float(tax_per / 100))
            net_amount = float(tax_amount) + bill_amount;
            bill_amount_before_tax = bill_amount
            warehouse = request.POST['warehouse']
            data_salesinvoice_items = {
                "sales_invoice":sales_invoice_id,
                "item":item,
                "qty":qty,
                "rate":rate,
                "warehouse":warehouse,
                "bill_amount":bill_amount,
                "discount":discount,
                "bill_amount_before_tax":bill_amount_before_tax,
                "tax_per":tax_per,
                "tax_amount":tax_amount,
                "net_amount":net_amount,
                "taxgroup" :tax_group,
                'deleted':0
                }
            if not invoice_mat:
                serializer = SalesInvoice_ItemsSerializer(data=data_salesinvoice_items)
            else:
                if invoice_mat:
                    serializer = SalesInvoice_ItemsSerializer(invoice_mat, data=data_salesinvoice_items)
            if serializer.is_valid():
                user_id = session_user_id(request)
                date_modified = store_date_time()
                company_id = session_user_company(request);
                salesinvoice_item = serializer.save(company=company_id, created_by=user_id, created_date=date_modified)
                salesinvoice_item_id = salesinvoice_item.id
                item_id = request.POST['item']
                item_details = Item.objects.get(pk=item_id)
                #
                if serial_no:
                    serial_no_checking=serial_batch_add(request,salesinvoice_item_id,item_id,serial_no,1)
                sales_invoice_rate_update(sales_invoice_id)    
            else:
                # purchaseinvoice_id=""
                error_details = []
                for key in serializer.errors.keys():
                    error_details.append({"field": key, "message": serializer.errors[key][0]})
                error_data = {
                    "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
                }
                error_mode = 1
            return_data = {"sales_invoice_id":sales_invoice_id, "error_details":error_data, "error_mode":error_mode}
    return Response(return_data)

    # return Response({'data':"tesst"})


@api_view(['GET', 'POST'])
def discount_apply(request):
    item_discount_per = request.POST['item_discount_per'];
    item_discount_total = request.POST['item_discount_total']
    item_discount_val = request.POST['item_discount_val']
    sales_invoice_id = request.POST['sales_invoice_id']
    salesinvoice_item_id = request.POST['salesinvoice_item_id']
    salesinvoice_item = SalesInvoice_Items.objects.get(pk=salesinvoice_item_id)
    bill_amount = salesinvoice_item.bill_amount;
    tax_per = salesinvoice_item.tax_per
    before_tax = float(bill_amount) - float(item_discount_total)
    tax_amount = float(before_tax) * float(tax_per) / 100
    net_amount = before_tax + tax_amount
    salesinvoice_item.net_amount = float(net_amount);
    salesinvoice_item.tax_amount = float(tax_amount);
    salesinvoice_item.discount = float(item_discount_total);
    salesinvoice_item.discount_val = float(item_discount_val);
    salesinvoice_item.discount_per = float(item_discount_per);
    salesinvoice_item.save();
    sales_invoice_rate_update(sales_invoice_id)
    return Response({"sales_invoice_id":sales_invoice_id})


def sales_invoice_rate_update(salesinvoice_id):
    # Rate Updatation
    bill_amount = SalesInvoice_Items.objects.filter(sales_invoice=salesinvoice_id, deleted=0).aggregate(Sum('bill_amount'))
    tax_amount = SalesInvoice_Items.objects.filter(sales_invoice=salesinvoice_id, deleted=0).aggregate(Sum('tax_amount'))
    net_amount = SalesInvoice_Items.objects.filter(sales_invoice=salesinvoice_id, deleted=0).aggregate(Sum('net_amount'))
    item_discount = SalesInvoice_Items.objects.filter(sales_invoice=salesinvoice_id, deleted=0).aggregate(Sum('discount'))
    salesinvoice = Salesinvoice.objects.get(id=salesinvoice_id)
    if salesinvoice:
        # return_data={"purchaseinvoice_id":purchaseinvoice_id,"otherdata1":bill_amount,"otherdata2":tax_amount,"otherdata3":item_discount}
        # return Response(return_data)
        if SalesInvoice_Items.objects.filter(sales_invoice=salesinvoice_id, deleted=0):
            salesinvoice.bill_amount = bill_amount['bill_amount__sum']
            salesinvoice.tax_amount = tax_amount['tax_amount__sum']
            salesinvoice.net_amount = net_amount['net_amount__sum']
            salesinvoice.item_discount = item_discount['discount__sum']
            salesinvoice.bill_amount_before_tax = float(bill_amount['bill_amount__sum']) - float(item_discount['discount__sum']);
        else:
            salesinvoice.bill_amount = 0
            salesinvoice.tax_amount = 0
            salesinvoice.net_amount = 0
            salesinvoice.item_discount = 0
            salesinvoice.bill_amount_before_tax = 0            
        salesinvoice.save()


@api_view(['GET'])
def salesitems_delete(request):
    if request.is_ajax() and request.GET['id']:
        id = request.GET['id']
        selected_values = SalesInvoice_Items.objects.get(pk=request.GET['id'])
        user_id = session_user_id(request)
        date_modified = store_date_time()
        selected_values.modified_date = date_modified
        selected_values.modified_by = user_id
        selected_values.deleted = 1
        selected_values.save();
        sales_invoice_rate_update(selected_values.sales_invoice_id)
        return Response({"sales_invoice_id":selected_values.sales_invoice_id})

@api_view(['GET'])
def service_items_delete(request):
    if request.is_ajax() and request.GET['id']:
        id = request.GET['id']
        selected_values = ServiceBilling_Items.objects.get(pk=request.GET['id'])
        user_id = session_user_id(request)
        selected_values.deleted = 1
        selected_values.save();
        sales_invoice_rate_update(selected_values.sales_invoice_id)
        return Response({"sales_invoice_id":selected_values.sales_invoice_id})



@api_view(['GET', 'POST'])
def sales_item_detail(request):
    # sales_invoice_id=request.POST['salesinvoice_item_id']
    if request.is_ajax() and request.POST['salesinvoice_item_id']:
        id = request.POST['salesinvoice_item_id']
        data = []
        # return Response(request.GET['id'])
        custom_filter = {}
        custom_filter['deleted'] = 0
        custom_filter['id'] = id
        model_obj = SalesInvoice_Items.objects.get(**custom_filter)
        
    html = render_to_string('ERP/selling/sales/sales_item_detail.html', {'data':model_obj})
    # html = render_to_string('ERP/stock/test.html', {'data': request})
    return HttpResponse(html)
    # return Response({"sales_invoice_id":sales_invoice_id})

    
@api_view(['GET', 'POST'])
def item_edit_apply(request):
    sales_invoice_id0 = request.POST['salesinvoice_item_id0']
    sales_invoice_items = SalesInvoice_Items.objects.get(pk=sales_invoice_id0)
    sales_invoice_items.rate = request.POST['rate0']
    sales_invoice_items.bill_amount = request.POST['item_bill_amount0']
    sales_invoice_items.net_amount = request.POST['net_amount0']
    sales_invoice_items.tax_amount = request.POST['tax_amount0']
    sales_invoice_items.rate = request.POST['rate0']
    sales_invoice_items.qty = request.POST['qty0']
    sales_invoice_items.discount = request.POST['item_discount_total0']
    sales_invoice_items.discount_val = request.POST['item_discount_val0']
    sales_invoice_items.discount_per = request.POST['item_discount_per0']
    sales_invoice_items.save();
    sales_invoice_rate_update(sales_invoice_items.sales_invoice_id)
    return Response({"sales_invoice_id":sales_invoice_items.sales_invoice_id})


@api_view(['GET', 'POST'])
def salesinvocie_submit(request):
    sales_invoice_id = request.POST['sales_invoice_id']
    sales_invoice = Salesinvoice.objects.get(id=sales_invoice_id)
    error_details,error_mode=serail_no_stock_validation(request,sales_invoice_id);
    if error_mode==1:
        return Response({"sales_invoice_id":sales_invoice_id, "error_details":error_details,"error_mode":error_mode})
    paid_staus = "0"
    if sales_invoice:
        invoice_discount = request.POST['invoice_discount'];
        if float(invoice_discount) > 0:
            # return Response({'data':request.POST['new_net_amount'], 'module':'Purchase'}, template_name='ERP/stock/test.html')
            sales_invoice.discount = float(request.POST['invoice_discount'])
            sales_invoice.net_amount = float(request.POST['new_net_amount'])
            sales_invoice.tax_amount = float(request.POST['new_tax_amount']);
        sales_invoice.status = 1
        sales_invoice.bill_payment_type = request.POST['payment_mode']
        sales_invoice.save()
        sales_invoice = Salesinvoice.objects.get(id=sales_invoice_id)
        if request.POST['payment_mode'] == "1":
            paid_staus = ""
            sales_invoice.paid_amount = sales_invoice.net_amount
            sales_invoice.balance_amount = 0
        if request.POST['payment_mode'] == "2":
            sales_invoice.paid_amount = 0
            sales_invoice.balance_amount = sales_invoice.net_amount
        if request.POST['payment_mode'] == "3":
            sales_invoice.paid_amount = 0
            sales_invoice.status = 0
            sales_invoice.balance_amount = sales_invoice.net_amount
        sales_invoice.save();
        
        bill_amount_before_tax = sales_invoice.bill_amount_before_tax;
        salesitem_list = SalesInvoice_Items.objects.all().filter(sales_invoice=sales_invoice_id, deleted=0)
        for salesitem_list_val in salesitem_list:
            ref_type = 1
            ref_id = salesitem_list_val.id
            qty = salesitem_list_val.qty
            item = salesitem_list_val.item
            warehouse = salesitem_list_val.warehouse
            company = salesitem_list_val.company
            bill_amount = salesitem_list_val.bill_amount
            discount = salesitem_list_val.discount
            tax_per = salesitem_list_val.tax_per
            tax_amount = salesitem_list_val.tax_amount
            if float(invoice_discount) > 0:
                salesinvoice_items = SalesInvoice_Items.objects.get(pk=ref_id)
                item_bill_amount_before_tax = salesinvoice_items.bill_amount_before_tax
                new_discount = float(invoice_discount) / float(bill_amount_before_tax) * float(item_bill_amount_before_tax)
                new_disccount_plus_old = new_discount + discount
                new_bill_amount_before_tax = bill_amount - new_disccount_plus_old
                new_tax = tax_amount;
                if float(tax_amount) > 0:
                    new_tax = float(new_bill_amount_before_tax) * float(tax_per) / float(100)
                salesinvoice_items.discount = new_disccount_plus_old
                salesinvoice_items.bill_amount_before_tax = new_bill_amount_before_tax
                salesinvoice_items.net_amount = new_bill_amount_before_tax + new_tax
                salesinvoice_items.tax_amount = new_tax
                salesinvoice_items.save();
            ref_name = "Sales Create"
            mode = 2
            ref_type = 3
            if item.maintain_stock:
                custom_filter={}
                custom_filter['deleted']=0
                custom_filter['item']=item.id
                custom_filter['warehouse']=warehouse.id
                custom_filter['company']=company.id
                stock=Stock.objects.filter(**custom_filter)
                data = stock_create_update(item, qty, warehouse, company, mode, ref_id, ref_type, ref_name, request)
                
        service_list = ServiceBilling_Items.objects.all().filter(sales_invoice=sales_invoice_id, deleted=0)
        for service_list_val in service_list:
            data = stock_create_update(service_list_val.service_item, service_list_val.service_item_qty, service_list_val.warehouse,
                                       service_list_val.company, mode, service_list_val.id, ref_type, 'Service Bill',request)

            pass
                #return Response({"sales_invoice_id":sales_invoice_id, "tax_error_details":data})
        tax_error_details = tax_splitup(1, sales_invoice_id, 1, request)
        return Response({"sales_invoice_id":sales_invoice_id, "tax_error_details":tax_error_details})



def serail_no_stock_validation(request,sales_invoice_id):
    salesitem_list = SalesInvoice_Items.objects.all().filter(sales_invoice=sales_invoice_id, deleted=0)
    error_details=[]
    error_mode=0
    for salesitem_list_val in salesitem_list:
        item=salesitem_list_val.item
        warehouse=salesitem_list_val.warehouse
        company = salesitem_list_val.company
        qty=salesitem_list_val.qty
        if item.maintain_stock:
                custom_filter={}
                custom_filter['deleted']=0
                custom_filter['item']=item.id
                custom_filter['warehouse']=warehouse.id
                custom_filter['company']=company.id
                stock=Stock.objects.filter(**custom_filter)
                if not stock:
                    error_mode=1
                    error_details.append({"field": item.name, "message":" Stock not available"})
                elif stock[0].current_stock<qty:
                    error_mode=1
                    error_details.append({"field": item.name, "message": "Stock not available"})
        if item.serial:
            pass
    data = {
        "Error": {
        "status": 400,
        "message": "Your submitted data was not valid - please correct the below errors",
        "error_details": error_details
        }   
    }    
    return data,error_mode

@api_view(['GET', 'POST'])
def bill_print(request, id):
    html = None
    model_obj = []
    # return Response("Hai")
    data = []
    # return Response(request.GET['id'])
    custom_filter = {}
    custom_filter['deleted'] = 0
    custom_filter['sales_invoice_id'] = id
    model_obj = SalesInvoice_Items.objects.filter(**custom_filter).order_by('-id')
    model_obj_invoice = Salesinvoice.objects.get(pk=id)
        
    # data = Stockentry_itemsSerializer(model_obj, many=True).data
    html = render_to_string('ERP/selling/sales/print.html', {'data': model_obj, "basic_data":model_obj_invoice})
    # html = render_to_string('ERP/stock/test.html', {'data': request})
    return HttpResponse(html)



def serial_batch_add(request,salesinvoice_id,item,serial_no,mode=1):
    pass;
#     data = {
#                 "serial_no":serial_no,
#                 "serial_no_id":sales_date,
#                 "warehouse":warehouse,
#                 "salesinvoice_id":salesinvoice_id,
#                 "bill_mode":request.POST['bill_mode'],
#             }
#     serializer = SalesInvoiceSerializer(data=data)
#     if serializer.is_valid():
#         user_id = session_user_id(request)
#         date_modified = store_date_time()
#         sales_invoice = serializer.save(created_by=user_id, created_date=date_modified)
#         sales_invoice_id = sales_invoice.id
#     else:
#         sales_invoice_id = ""
#     pass

# def serial_batch_add(salesinvoice_item_id,item_id,mode=1,serial_no):
#     pass
# #     data = {
# #                 "serial_no":serial_no,
# #                 "item_id":item_id,
# #                 "warehouse_id":warehouse_id,
# #                 
# #             }
# #     serializer = Sales_Serial_NosSerializer(data=data)
# #     if serializer.is_valid():
# #         user_id = session_user_id(request)
# #         date_modified = store_date_time()
# #         sales_invoice = serializer.save(created_by=user_id, created_date=date_modified)
# #         sales_invoice_id = sales_invoice.id
# #     else:
# #         sales_invoice_id = ""
    

def tax_splitup(ref_type, ref_id, mode, request):
    '''
    ref_type =1 sales tax
    ref_type =2 purchase tax 
    mode=1 same state
    mode=2 diffrent state
    '''
    if ref_type == 1:
        tax_items = SalesInvoice_Items.objects.filter(sales_invoice=ref_id, deleted=0)
        
    if ref_type == 2:
        tax_items = PurchaseInvoice_items.objects.filter(sales_invoice=ref_id, deleted=0)
    user_id = session_user_id(request)
    date_modified = store_date_time()
    company_id = session_user_company(request);
    error_details = []
    for tax_item in tax_items:
        amount = tax_item.bill_amount_before_tax
        item_id = tax_item.item_id
        tax_group = tax_item.taxgroup_id
        if mode == 1:
            # return tax_group
            taxes = Tax.objects.filter(tax_group_id=tax_group, deleted=0, tax_type=mode)
            # return taxes[0].id
            for tax in taxes:
                tax_id = tax.id
                tax_per = tax.tax_per
                tax_amount = amount * tax_per / 100
                data = {
                    "ref_id":ref_id,
                    "ref_type":ref_type,
                    "tax_per":tax_per,
                    "item":item_id,
                    "tax_amount":tax_amount,
                    "tax":tax_id,
                    "taxgroup":tax_group,
                    "deleted":0,
                    "company_id":company_id.id,
                    "created_date":date_modified
                    }
                
                serializer = TaxSplitupSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    for key in serializer.errors.keys():
                        error_details.append({"field": key, "message": serializer.errors[key][0]})
                        data = {
                        "Error": {
                        "status": 400,
                        "message": "Your submitted data was not valid - please correct the below errors",
                        "error_details": error_details
                        }
                        }
    return error_details
    
