from django.shortcuts import render
from rest_framework import status
from django.contrib.auth.models import User
from .models import Order, Item
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer, ItemSerializer


# Create your views here.

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

@api_view(['GET'])
def order_by_username(request, username):

    if request.method != 'GET':
        return Response({},status=status.HTTP_404_NOT_FOUND)
    try:
        user = User.objects.get(username=username)
        order = Order.objects.filter(user=user)[0]
        items = Item.objects.all().filter(order=order)
        item_bought = []
        sub_total = []
        for item in items:
            item_dict = {
                "name" : item.name,
                "price": item.price,
                "quantity": item.quantity,
                "total": item.price * item.quantity
            }
            sub_total.append(item.price * item.quantity)
            item_bought.append(item_dict)

        data = {
            "user": {
                "username": user.username,
                "email": user.email
            },
            "items" : item_bought,
            "sub_total" : sum(sub_total),
            "total" : sum(sub_total) - order.discount,
            "discount" : order.discount
        }
        return Response(data)
    except Exception: 
        return Response({"Error":f"User not found having username as '{username}'"},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def total_number_of_orders_per_users(request):
    orders = Order.objects.all()
    tot_num_order_per_user = []
    for order in orders:
        item = Item.objects.filter(order=order)
        tot_num_order_per_user.append({"user_id": order.user.id, "count" : len(item)})
    return Response(tot_num_order_per_user)


@api_view(['GET'])
def total_orders_per_month(request):
    tot_orders_per_month = []
    for i in range(1, 13):
        items = Item.objects.filter(date__month=i)
        tot_orders_per_month.append({"month":months[i-1], "count":len(items)})
    return Response(tot_orders_per_month)


@api_view(['GET'])
def total_revenue_from_orders_per_month(request):
    tot_revenue_per_month = []
    for i in range(1, 13):
        items = Item.objects.filter(date__month=i)
        revenue = sum(item.price for item in items)
        tot_revenue_per_month.append({"month":months[i-1], "revenue":revenue})
    return Response(tot_revenue_per_month)