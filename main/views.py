from django.shortcuts import render


def index(request):

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "Вся правда о Руслане",
        "text_on_page": "РУСИФИКАТОР НАТУРАЛ!!!!",
    }

    return render(request, "main/about.html", context)


