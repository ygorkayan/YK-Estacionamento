from django.shortcuts import render
from django.contrib.auth import login, authenticate


def index(request):
    if request.method == "POST":
        # Codigo Funcionando, agora so implementar oque usuarios logado ver :/
        # logar = authenticate(username=request.POST['nickname'], password=request.POST['senha'])
        # login(request, logar)
        print("logado")
    else:
        print("nao logado")
    return render(request, "Login/index.html")


