#!/usr/bin/env python


from django.shortcuts import render
from .forms import UserRegister

users = ['user1', 'user2', 'user3']


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

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                return render(
                    request,
                    'fifth_task/registration_page.html',
                    {'message': f'Приветствуем, {username}!', 'form': form},
                )

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    return sign_up_by_django(request)
