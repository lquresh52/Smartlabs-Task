from django.urls import path, include
from api import views


urlpatterns = [
    path('order-by-username/<str:username>/', views.order_by_username, name='order-by-username'),
    path('tot-num-orders-per-users/', views.total_number_of_orders_per_users, name='tot-num-orders-per-users'),
    path('total-orders-per-month/', views.total_orders_per_month, name='total-orders-per-month'),
    path('total-revenue-from-orders-per-month/', views.total_revenue_from_orders_per_month, name='total-revenue-from-orders-per-month'),
]
