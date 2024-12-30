#!/usr/bin/env python


from django.shortcuts import render

def main_view(request):
    return render(request, 'third_task/main.html')

def shop_view(request):
    items = {
        'item1': 'какой-то товар',
        'item2': 'какой-нибудь товар',
        'item3': 'ещё какой-нибудь товар',
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart_view(request):
    return render(request, 'third_task/cart.html')

