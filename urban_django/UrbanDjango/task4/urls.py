#!/usr/bin/env python


from django.urls import path
from .views import main_view, shop_view, cart_view


urlpatterns = [
    path('', main_view, name='main'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]

