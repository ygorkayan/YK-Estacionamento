from django.shortcuts import render, redirect
from .forms import FormSuporte, FormCarrinho


def index(request):
    return render(request, "Site/index.html")


def sobre(request):
    return render(request, "Site/sobre.html")


def suporte(request):
    if request.method == "POST":
        formulario = FormSuporte(request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, "Site/suporte.html")


def preco(request):
    if request.method == "POST":
        valor = request.POST["valor"].split(",")
        preço = valor[0]
        info = valor[1]
        context = {"preco": preço, "info": info}
        return render(request,"Site/carrinho.html", context)
    return render(request, "Site/preco.html")


def carrinho(request):
    if request.method == "POST":
        formulario = FormCarrinho(request.POST)
        print(formulario.is_valid())
        if formulario.is_valid():
            formulario.save()

    return render(request, "Site/index.html")
