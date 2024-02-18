from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('customer_orders/<int:customer_id>/', views.customer_orders, name='customer_orders'),
    path('order/<int:order_id>/', views.order_full, name='order_full'),
    path('customer_products/<int:customer_id>/', views.customer_products, name='customer_orders'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    ]
