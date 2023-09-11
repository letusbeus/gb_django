from django.urls import path
from . import views

app_name = 'hw_2'

urlpatterns = [
    path('create_customer/', views.create_customer, name='create_customer'),
    path('get_customers/', views.get_customers, name='get_customers'),
    path('get_customer/', views.get_customer, name='get_customer'),
    path('customer_min_orders/', views.customer_min_orders, name='customer_min_orders'),
    path('customer_max_orders/', views.customer_max_orders, name='customer_max_orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('get_products/', views.get_products, name='get_products'),
    path('get_product/', views.get_product, name='get_product'),
    path('product_price_gt/', views.product_price_gt, name='product_price_gt'),
    path('product_price_lt/', views.product_price_lt, name='product_price_lt'),
    path('product_price_exact/', views.product_price_exact, name='product_price_exact'),
    path('get_orders/', views.get_orders, name='get_orders'),
    path('get_order/', views.get_order, name='get_order'),
    path('get_orders_from/', views.get_orders_from, name='get_orders_from'),
    path('get_orders_placed_at/', views.get_orders_placed_at, name='get_orders_placed_at'),
]