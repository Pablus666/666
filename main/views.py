from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }


    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'Вся правда о Руслане',
        'text_on_page': 'РУСИФИКАТОР НАТУРАЛ!!!!'
    }

    return render(request, 'main/about.html', context)


def delivery(request):
    context = {
        'title': 'Home - Доставка',
        'content': 'Доставка и оплата',
    }


    return render(request, 'main/delivery.html', context)


def info(request):
    context = {
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
    }


    return render(request, 'main/info.html', context)
