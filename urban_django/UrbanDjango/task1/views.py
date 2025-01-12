#!/usr/bin/env python


from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import UserRegister
from .models import Buyer, Game, News


def main_view(request):
    return render(request, 'first_task/main.html')


def shop_view(request):
    items = Game.objects.all()
    return render(request, 'first_task/shop.html', {'items': items})


def cart_view(request):
    return render(request, 'first_task/cart.html')


def sign_up_by_django(request):
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'пароли не совпадают'
            elif age < 18:
                info['error'] = 'вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                form = UserRegister()
                return render(
                    request,
                    'first_task/registration_page.html',
                    {'message': f'приветствуем, {username}!', 'form': form},
                )

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_html(request):
    return sign_up_by_django(request)


def news(request):
    news_list = News.objects.all().order_by('date')
    for item in news_list:
        item.date = timezone.localtime(item.date).strftime('%d %b %Y, %I:%M')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'first_task/news.html', {'news': page_obj})
