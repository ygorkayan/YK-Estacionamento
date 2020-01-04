from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == "POST":
        logar = authenticate(username=request.POST['nickname'], password=request.POST['senha'])
        login(request, logar)
        return redirect("login-dashboard")
    else:
        return render(request, "Login/index.html")


@login_required
def dashboard(request):
    return render(request, "login/sistema de login/dashboard.html")

@login_required
def icons(request):
    return render(request, "login/sistema de login/icons.html")

@login_required
def map(request):
    return render(request, "login/sistema de login/map.html")

@login_required
def notifications(request):
    return render(request, "login/sistema de login/notifications.html")

@login_required
def tables(request):
    return render(request, "login/sistema de login/tables.html")

@login_required
def typography(request):
    return render(request, "login/sistema de login/typography.html")

@login_required
def user(request):
    return render(request, "login/sistema de login/user.html")


