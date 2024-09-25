from django.urls import path


from core.erp.views.client.views import ClientView
from core.erp.views.sale.views import SaleCreateView, SaleListView, SaleDeleteView, SaleUpdateView, SaleInvoicePdfView
from core.erp.views.tests.views import TestView
from core.erp.views.category.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.product.views import *

app_name = 'erp'

urlpatterns = [
   path('category/list/', CategoryListView.as_view(), name='category_list'),
   path('category/list2/', category_list, name='category_list2'),
   path('category/create/', CategoryCreateView.as_view(), name='category_create'),
   path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
   path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
   path('category/form/', CategoryFormView.as_view(), name='category_form'),

   # Product
   path('product/list/', ProductListView.as_view(), name='product_list'),
   path('product/create/', ProductCreateView.as_view(), name='product_create'),
   path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
   path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

   # Client
   path('client/', ClientView.as_view(), name='client'),

   # home
   path('dashboard/', DashBoardView.as_view(), name='dashboard'),

   #Test
   path('test/', TestView.as_view(), name='test'),

   # Sale
   path('sale/list/', SaleListView.as_view(), name='sale_list'),
   path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
   path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
   path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
   path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),


]