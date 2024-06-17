from django.shortcuts import render


def login(reqest):
    context = {"title": "Home - Авторизация"}
    return render(reqest, 'users/login.html', context)


def registration(reqest):
    context = {"title": "Home - Регистрация"}
    return render(reqest, 'users/registration.html', context)


def profile(reqest):
    context = {"title": "Home - Кабинет"}
    return render(reqest, 'users/profile.html', context)


def logout(reqest):
    ...