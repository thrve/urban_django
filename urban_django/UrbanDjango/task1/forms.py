#!/usr/bin/env python


from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='введите логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='введите пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='повторите пароль')
    age = forms.IntegerField(
        max_value=120,
        min_value=1,
        label='введите свой возраст',
        widget=forms.NumberInput(
            attrs={
                'class': 'age-input',
            }
        ),
    )
