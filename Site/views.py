import threading

from django.core.mail import send_mail
from django.shortcuts import render

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

            nome = request.POST["nome"]
            email = request.POST["email"]

            email = threading.Thread(target=Mandar_Email, args=(nome, email, 2))
            email.start()
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

            nome = request.POST["nome"]
            valor = request.POST["valor"]
            email = request.POST["email"]
            nickname = request.POST["nickname"]
            outros = {
                "valor": valor,
                "nickname": nickname,
                "senha": "abc123"
            }

            email = threading.Thread(target=Mandar_Email, args=(nome, email, 1, outros))
            email.start()
    return render(request, "Site/index.html")


def Mandar_Email(nome, email, tipo, outros=""):
    # Tipo
    # 1 Compra / Carrinho
    # 2 Suporte

    assunto = "YK Estacionamento"
    if tipo == 1:
        msg = f"Obrigado por comprar sua mensalidade {nome}, ela foi no valor de ${outros['valor']}\n" \
              f"login: {outros['nickname']}\n" \
              f"senha: {outros['senha']}\n" \
              f"Faça login e aproveite a melhor empresa de estacionamento"
    else:
        msg = "Sua mensagem foi recebida, logo entraremos em contato."

    send_mail(assunto, msg, 'myemail@gmail.com', [email])
