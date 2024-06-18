from django.shortcuts import render

from users.forms import UsersLoginForm


def login(request):
    if request.method == 'POST':
        form = UsersLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UsersLoginForm   


    context = {"title": "Home - Авторизация", "form": form}
    return render(request, "users/login.html", context)


def registration(request):
    context = {"title": "Home - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "Home - Кабинет"}
    return render(request, "users/profile.html", context)


def logout(request): ...
