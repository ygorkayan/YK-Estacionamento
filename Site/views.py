from django.shortcuts import render


def index(request):
    return render(request, "Site/index.html")


def sobre(request):
    return render(request, "Site/sobre.html")


def preco(request):
    return render(request, "Site/preco.html")


def carrinho(request):
    return render(request, "Site/carrinho.html")