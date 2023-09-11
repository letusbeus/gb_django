from django.urls import path
from . import views

app_name = 'hw_2'

urlpatterns = [
    path('read_all_customers/', views.read_all_customers, name='read_all_customers'),
    path('read_customer/', views.read_customer, name='read_customer'),
    path('customer_min_orders/', views.customer_min_orders, name='customer_min_orders'),
    path('customer_max_orders/', views.customer_max_orders, name='customer_max_orders'),
    path('read_all_products/', views.read_all_products, name='read_all_products'),
    path('read_product/', views.read_product, name='read_product'),
    path('product_price_gt/', views.product_price_gt, name='product_price_gt'),
    path('product_price_lt/', views.product_price_lt, name='product_price_lt'),
    path('product_price_exact/', views.product_price_exact, name='product_price_exact'),
    path('read_all_orders/', views.read_all_orders, name='read_all_orders'),
    path('read_order/', views.read_order, name='read_order'),
    path('read_orders_from/', views.read_orders_from, name='read_orders_from'),
    path('read_orders_placed_at/', views.read_orders_placed_at, name='read_orders_placed_at'),
]