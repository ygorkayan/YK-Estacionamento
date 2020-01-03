from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def index(request):
    if request.method == "POST":
        print("Entrou")
        logar = authenticate(username=request.POST['nickname'], password=request.POST['senha'])
        login(request, logar)
        return redirect("login-dashboard")

    return render(request, "Login/index.html")


def dashboard(request):
    return render(request, "login/sistema de login/dashboard.html")


def icons(request):
    return render(request, "login/sistema de login/icons.html")


def map(request):
    return render(request, "login/sistema de login/map.html")


def notifications(request):
    return render(request, "login/sistema de login/notifications.html")


def tables(request):
    return render(request, "login/sistema de login/tables.html")


def typography(request):
    return render(request, "login/sistema de login/typography.html")


def user(request):
    return render(request, "login/sistema de login/user.html")


