#!/usr/bin/env python


from django.urls import path
from .views import (
    main_view,
    shop_view,
    cart_view,
    sign_up_by_django,
    sign_up_by_html,
    news,
)


urlpatterns = [
    path('', main_view, name='task1_main'),
    path('shop/', shop_view, name='task1_shop'),
    path('cart/', cart_view, name='task1_cart'),
    path('sign_up/', sign_up_by_django, name='task1_sign_up'),
    path('django_sign_up/', sign_up_by_html, name='task1_django_sign_up'),
    path('news/', news, name='task1_news'),
]
