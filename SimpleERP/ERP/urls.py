from django.conf.urls import url,include
from ERP.custom_views.master import company,currency,state,warehouse,unit,itemgroup,customergroup,taxgroup,tax,suppliergroup,supplier,customer,itemsize,itemcolor,itembrand,item
from ERP.custom_views.stock import stockentry,purchase
from ERP.custom_views.account import paymententry
from ERP.custom_views.project import project,project_item
from ERP.custom_views.expense import expense,expensecategory
from ERP.custom_views.selling import price,sales
from ERP.custom_views.stock import stock
from ERP.custom_views.research import research
from ERP.custom_views import autocompletes
from ERP.custom_views.project import project,project_item
from ERP.custom_views.expense import expense,expensecategory
from ERP.custom_views import default
from django.conf import settings
from django.contrib.auth.decorators import login_required
from ERP.custom_views.crm import crm
from ERP.custom_views.crm import item_entry
    
app_name = 'ERP'
urlpatterns = [	
    url(r'^$', default.login_user, name='login'),
    url(r'^user/create', default.signup_user, name='signup_user'),
    url(r'^user/list', default.user_list, name='user_list'),
    url(r'^user/update/(?P<id>[^/]*)/$', default.user_update),
    url(r'^user/view/(?P<id>[^/]*)/$', default.user_view),
    url(r'^home/$', default.index, name='default'),
    url(r'^stock/list', stock.stock_list, name='stock_list'),
    url(r'^project/create', project.project_create, name='project_create'),
    url(r'^project/item_create', project.project_items_create, name='project_items_create'),
    url(r'^project/project_items', project.project_items, name='project_items'),
    url(r'^project/view/(?P<id>[^/]*)/$', project.project_view),
    url(r'^project/update/(?P<id>[^/]*)/$', project.project_update),
    url(r'^project/list', project.list_project, name='project_list'),
    url(r'^project/delete/(?P<id>[^/]*)/$', project.delete_project),
    url(r'^project/projectitems_delete/', project.projectitems_delete),
    url(r'^project/project_tracking/',login_required(project.project_tracking),name="project_tracking"),
    url(r'^project/project_tracking_add/',login_required(project.project_tracking_add),name="project_tracking_add"),
    url(r'^project/project_tracking_delete/(?P<id>[^/]*)/$', project.project_tracking_delete),

    

#     url(r'^projectprojectitems_delete/item/create',project_item.project_item_create, name='project_item_create'),
#     url(r'^project/item/list', project_item.project_item_list, name='project_item_list'),
#     url(r'^project/item/view/(?P<id>[^/]*)/$', project_item.project_item_view),
#     url(r'^project/item/update/(?P<id>[^/]*)/$', project_item.project_item_update),
#     url(r'^project/item/delete/(?P<id>[^/]*)/$', project_item.project_item_delete),
    

    url(r'^expense/create', expense.expense_create,name='expense_create'),
    url(r'^expense/update/(?P<id>[^/]*)/$', expense.expense_update),
    url(r'^expense/view/(?P<id>[^/]*)/$', expense.expense_view),
    url(r'^expense/list', expense.list_expense,name='list_expense'),
    url(r'^expense/delete/(?P<id>[^/]*)/$', expense.delete_expense),
    url(r'^expense/category/create', expensecategory.expensecategory_create,name='expensecategory_create'),
    url(r'^expense/category/list', expensecategory.expensecategory_list,name='expensecategory_list'),
    url(r'^expense/category/view/(?P<id>[^/]*)/$', expensecategory.expensecategory_view),
    url(r'^expense/category/update/(?P<id>[^/]*)/$', expensecategory.expensecategory_update),
    url(r'^expense/category/delete/(?P<id>[^/]*)/$', expensecategory.expensecategory_delete),
    url(r'^company/create/', company.company_create,name='company_create'),
    url(r'^company/update/(?P<id>[^/]*)/$', company.company_update),
    url(r'^company/view/(?P<id>[^/]*)/$', company.company_view),
    url(r'^company/list/', company.list_company, name='list_company'),
    url(r'^company/delete/(?P<id>[^/]*)/$', company.delete_company),

    url(r'^currency/create/', currency.currency_create,name='currency_create'),
    url(r'^currency/update/(?P<id>[^/]*)/$', currency.currency_update),
    url(r'^currency/view/(?P<id>[^/]*)/$', currency.currency_view),
    url(r'^currency/list/', currency.list_currency, name='list_currency'),
    url(r'^currency/delete/(?P<id>[^/]*)/$', currency.delete_currency),

    url(r'^state/create/', state.state_create,name='state_create'),
    url(r'^state/update/(?P<id>[^/]*)/$', state.state_update),
    url(r'^state/view/(?P<id>[^/]*)/$', state.state_view),
    url(r'^state/list/', state.list_state, name='list_state'),
    url(r'^state/delete/(?P<id>[^/]*)/$', state.delete_state),

    url(r'^warehouse/create/', warehouse.warehouse_create,name='warehouse_create'),
    url(r'^warehouse/update/(?P<id>[^/]*)/$', warehouse.warehouse_update),
    url(r'^warehouse/view/(?P<id>[^/]*)/$', warehouse.warehouse_view),
    url(r'^warehouse/list/', warehouse.list_warehouse, name='list_warehouse'),
    url(r'^warehouse/delete/(?P<id>[^/]*)/$', warehouse.delete_warehouse),

    url(r'^unit/create/', unit.unit_create,name='unit_create'),
    url(r'^unit/update/(?P<id>[^/]*)/$', unit.unit_update),
    url(r'^unit/view/(?P<id>[^/]*)/$', unit.unit_view),
    url(r'^unit/list/', unit.list_unit, name='list_unit'),
    url(r'^unit/delete/(?P<id>[^/]*)/$', unit.delete_unit),

    url(r'^itemgroup/create/', itemgroup.itemgroup_create,name='itemgroup_create'),
    url(r'^itemgroup/update/(?P<id>[^/]*)/$', itemgroup.itemgroup_update),
    url(r'^itemgroup/view/(?P<id>[^/]*)/$', itemgroup.itemgroup_view),
    url(r'^itemgroup/list/', itemgroup.itemgroup_list, name='itemgroup_list'),
    url(r'^itemgroup/delete/(?P<id>[^/]*)/$', itemgroup.itemgroup_delete),


    url(r'^customergroup/create/', customergroup.customergroup_create,name='customergroup_create'),
    url(r'^customergroup/update/(?P<id>[^/]*)/$', customergroup.customergroup_update),
    url(r'^customergroup/view/(?P<id>[^/]*)/$', customergroup.customergroup_view),
    url(r'^customergroup/list/', customergroup.customergroup_list, name='customergroup_list'),
    url(r'^customergroup/delete/(?P<id>[^/]*)/$', customergroup.customergroup_delete),

    url(r'^taxgroup/create/', taxgroup.taxgroup_create,name='taxgroup_create'),
    url(r'^taxgroup/update/(?P<id>[^/]*)/$', taxgroup.taxgroup_update),
    url(r'^taxgroup/view/(?P<id>[^/]*)/$', taxgroup.taxgroup_view),
    url(r'^taxgroup/list/', taxgroup.taxgroup_list, name='taxgroup_list'),
    url(r'^taxgroup/delete/(?P<id>[^/]*)/$', taxgroup.taxgroup_delete),

    url(r'^tax/create/', tax.tax_create,name='tax_create'),
    url(r'^tax/update/(?P<id>[^/]*)/$', tax.tax_update),
    url(r'^tax/view/(?P<id>[^/]*)/$', tax.tax_view),
    url(r'^tax/list/', tax.tax_list, name='tax_list'),
    url(r'^tax/delete/(?P<id>[^/]*)/$', tax.tax_delete),

    url(r'^suppliergroup/create/', suppliergroup.suppliergroup_create,name='suppliergroup_create'),
    url(r'^suppliergroup/update/(?P<id>[^/]*)/$', suppliergroup.suppliergroup_update),
    url(r'^suppliergroup/view/(?P<id>[^/]*)/$', suppliergroup.suppliergroup_view),
    url(r'^suppliergroup/list/', suppliergroup.suppliergroup_list, name='suppliergroup_list'),
    url(r'^suppliergroup/delete/(?P<id>[^/]*)/$', suppliergroup.suppliergroup_delete),

    url(r'^supplier/create/', supplier.supplier_create,name='supplier_create'),
    url(r'^supplier/update/(?P<id>[^/]*)/$', supplier.supplier_update),
    url(r'^supplier/view/(?P<id>[^/]*)/$', supplier.supplier_view),
    url(r'^supplier/list/', supplier.supplier_list, name='supplier_list'),
    url(r'^supplier/delete/(?P<id>[^/]*)/$', supplier.supplier_delete),

    url(r'^customer/create/', customer.customer_create,name='customer_create'),
    url(r'^customer/update/(?P<id>[^/]*)/$', customer.customer_update),
    url(r'^customer/view/(?P<id>[^/]*)/$', customer.customer_view),
    url(r'^customer/list/', customer.customer_list, name='customer_list'),
    url(r'^customer/delete/(?P<id>[^/]*)/$', customer.customer_delete),

    url(r'^itemcolor/create/', itemcolor.itemcolor_create,name='itemcolor_create'),
    url(r'^itemcolor/update/(?P<id>[^/]*)/$', itemcolor.itemcolor_update),
    url(r'^itemcolor/view/(?P<id>[^/]*)/$', itemcolor.itemcolor_view),
    url(r'^itemcolor/list/', itemcolor.itemcolor_list, name='itemcolor_list'),
    url(r'^itemcolor/delete/(?P<id>[^/]*)/$', itemcolor.itemcolor_delete),


    url(r'^itemsize/create/', itemsize.itemsize_create,name='itemsize_create'),
    url(r'^itemsize/update/(?P<id>[^/]*)/$', itemsize.itemsize_update),
    url(r'^itemsize/view/(?P<id>[^/]*)/$', itemsize.itemsize_view),
    url(r'^itemsize/list/', itemsize.itemsize_list, name='itemsize_list'),
    url(r'^itemsize/delete/(?P<id>[^/]*)/$', itemsize.itemsize_delete),

    url(r'^itembrand/create/', login_required(itembrand.itembrand_create),name='itembrand_create'),
    url(r'^itembrand/update/(?P<id>[^/]*)/$', login_required(itembrand.itembrand_update)),
    url(r'^itembrand/view/(?P<id>[^/]*)/$', login_required(itembrand.itembrand_view)),
    url(r'^itembrand/list/', login_required(itembrand.itembrand_list), name='itembrand_list'),
    url(r'^itembrand/delete/(?P<id>[^/]*)/$', login_required(itembrand.itembrand_delete)),

    url(r'^item/create/', login_required(item.item_create),name='item_create'),
    url(r'^item/update/(?P<id>[^/]*)/$', login_required(item.item_update)),
    url(r'^item/view/(?P<id>[^/]*)/$', login_required(item.item_view)),
    url(r'^item/list/', login_required(item.item_list), name='item_list'),
    url(r'^item/delete/(?P<id>[^/]*)/$', login_required(item.item_delete)),
    url(r'^item/delete/(?P<id>[^/]*)/$', login_required(item.item_delete)),
    url(r'^item/item_list_autocomplete/', login_required(item.item_list_autocomplete)),
    
    
    url(r'^stockentry/items_create/', login_required(stockentry.stockentry_items_create),name='stockentry_items_create'),
    url(r'^stockentry/stockentry_items/', login_required(stockentry.stockentry_items),name='stockentry_items'),
    url(r'^stockentry/stockentryitems_delete/', login_required(stockentry.stockentryitems_delete)),
    url(r'^stockentry/update/items_create/', login_required(stockentry.stockentry_items_create),name='stockentry_items_create'),
    url(r'^stockentry/update/stockentry_items/', login_required(stockentry.stockentry_items),name='stockentry_items'),
    url(r'^stockentry/update/stockentryitems_delete/', login_required(stockentry.stockentryitems_delete)),
    url(r'^stockentry/view/stockentry_items/', login_required(stockentry.stockentry_items),name='stockentry_items'),
    url(r'^stockentry/create/', login_required(stockentry.stockentry_create),name='stockentry_create'),
    url(r'^stockentry/update/(?P<id>[^/]*)/$', login_required(stockentry.stockentry_update)),
    url(r'^stockentry/list/', login_required(stockentry.stockentry_list), name='stockentry_list'),
    url(r'^stockentry/view/(?P<id>[^/]*)/$', login_required(stockentry.stockentry_view), name='stockentry_view'),
    url(r'^stockentry/delete/(?P<id>[^/]*)/$', login_required(stockentry.stockentry_delete)),
    
    
    url(r'^price/create/', login_required(price.price_create),name='price_create'),
    url(r'^price/update/(?P<id>[^/]*)/$', login_required(price.price_update)),
    url(r'^price/view/(?P<id>[^/]*)/$', login_required(price.price_view)),
    url(r'^price/list/', login_required(price.price_list), name='price_list'),
    url(r'^price/delete/(?P<id>[^/]*)/$', login_required(price.price_delete)),
    
    
    
    
    
    url(r'^purchase/create/', login_required(purchase.purchase_create),name='purchase_create'),
    url(r'^purchase/items_create/', login_required(purchase.purchase_items_create),name='purchase_items_create'),
    url(r'^purchase/purchase_items/', login_required(purchase.purchase_items),name='purchase_items'),
    url(r'^purchase/purchaseitems_delete/', login_required(purchase.purchaseitems_delete)),
    url(r'^purchase/list/', login_required(purchase.purchase_list), name='purchase_list'),
    url(r'^purchase/update/(?P<id>[^/]*)/$', login_required(purchase.purchase_update)),
    url(r'^purchase/view/(?P<id>[^/]*)/$', login_required(purchase.purchase_view), name='purchase_view'),
    url(r'^purchase/serial_nos/', login_required(purchase.serial_nos), name='serial_nos'),
   
   
    url(r'^sales/create/', login_required(sales.sales_create),name='sales_create'),
    url(r'^sales/items_create/', login_required(sales.items_create),name='items_create'),
    url(r'^sales/sales_items/', login_required(sales.sales_items),name='sales_items'),
    url(r'^sales/discount_apply/', login_required(sales.discount_apply),name='discount_apply'),
    url(r'^sales/salesitems_delete/', login_required(sales.salesitems_delete)),
    url(r'^sales/salesinvocie_submit/',login_required(sales.salesinvocie_submit),name="salesinvocie_submit"),
    url(r'^sales/sales_item_detail/',login_required(sales.sales_item_detail),name="sales_item_detail"),
    url(r'^sales/item_edit_apply/',login_required(sales.item_edit_apply),name="item_edit_apply"),
    url(r'^sales/bill_print/(?P<id>[^/]*)/$',login_required(sales.bill_print),name="bill_print"),
    url(r'^sales/list/', login_required(sales.sales_list), name='sales_list'),
    url(r'^sales/service_items/', login_required(sales.service_items),name='services_items'),
    url(r'^sales/service_items_add/', login_required(sales.service_items_add),name='service_items_add'),
    url(r'^sales/service_items_show/', login_required(sales.service_items_show),name='service_items_show'),
    url(r'^sales/service_items_delete',login_required(sales.service_items_delete)),
    
    url(r'^paymententry/create/', login_required(paymententry.paymententry_create),name='paymententry_create'),
    
    #autocompletes
    url(r'^autocompletes/item_list_autocomplete/', autocompletes.item_list_autocomplete),
    url(r'^autocompletes/supplier_list_autocomplete/', autocompletes.supplier_list_autocomplete),
    url(r'^autocompletes/customer_list_autocomplete/', autocompletes.customer_list_autocomplete),
    url(r'^autocompletes/salesitem_list_autocomplete/', autocompletes.salesitem_list_autocomplete),
    #url(r'^barcode/create/', barcode.barcode_create),
    url(r'^research/jqgrid/', research.jqgrid_test),
    url(r'^research/jqgrid_data/', research.jqgrid_data),


    
    #url(r'^crm/items_create/', login_required(crm.leadentry_items_create),name='leadentry_items_create'),
    #url(r'^crm/crmentry_items/', login_required(crm.crmentry_items),name='crmentry_items'),
    #url(r'^crm/update/items_create/', login_required(crm.leadentry_items_create),name='leadentry_items_create'),
    #url(r'^crm/update/crmentry_items/', login_required(crm.crmentry_items), name='crmentry_items'),    
    #url(r'^crm/update/crmentry_items_delete/', login_required(crm.crmentry_items_delete)),
    #url(r'^crm/view/crmentry_items/', login_required(crm.crmentry_items), name='crmentry_items'),

    url(r'^crm/create/', login_required(crm.create_lead),name='lead_create'),
    url(r'^crm/update/(?P<id>[^/]*)/$', login_required(crm.update_lead)),
    url(r'^crm/list/', login_required(crm.list_lead),name='lead_list'),
    url(r'^crm/view/(?P<id>[^/]*)/$', login_required(crm.lead_view), name='lead_view'),
    url(r'^crm/delete/(?P<id>[^/]*)/$', login_required(crm.lead_delete)),
    url(r'^crm/items_create/', login_required(crm.items_create),name='items_create'),

    
    #url(r'^stockentry/update/(?P<id>[^/]*)/$', stockentry.stockentry_update),
    #url(r'^stockentry/view/(?P<id>[^/]*)/$', stockentry.stockentry_view),
    #url(r'^stockentry/list/', stockentry.stockentry_list, name='stockentry_list'),
    #url(r'^stockentry/delete/(?P<id>[^/]*)/$', stockentry.stockentry_delete),
    

]

