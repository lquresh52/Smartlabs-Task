from django.urls import path, include
from tasks import views


urlpatterns = [
    path('', views.currency_convertor, name='currency-convertor'),
    path('converted-currency/<str:from_currency>/<str:to_currency>/<str:converted_amount>/<str:amount>/<str:conversion_rate>/', views.converted_currency, name='converted-currency'),
]
