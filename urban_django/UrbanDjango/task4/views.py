#!/usr/bin/env python


from django.shortcuts import render


def main_view(request):
    return render(request, 'fourth_task/main.html')


def shop_view(request):
    items = {
        'item1': 'какой-то товар',
        'item2': 'какой-нибудь товар',
        'item3': 'ещё какой-нибудь товар',
    }
    return render(request, 'fourth_task/shop.html', {'items': list(items.values())})


def cart_view(request):
    return render(request, 'fourth_task/cart.html')
