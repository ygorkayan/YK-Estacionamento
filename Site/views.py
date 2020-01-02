import threading
from django.core.mail import send_mail
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

            nome = request.POST["nome"]    #Pega o nome enviado pelo formulario
            email = request.POST["email"]  #Pega o email enviado pelo formulario

            # o email do django é bloqueante, para que a pagina nao fique esperando
            # manda o email para o render renderizar a pag suporte eu jogo isso para
            # uma threading com o nome, o email e o modo que é 2 para suporte
            email = threading.Thread(target=Mandar_Email, args=(nome, email, 2))
            email.start()
            return redirect("site-index")
    return render(request, "Site/suporte.html")


def preco(request):
    # Na pagina de preço foi colocando 2 formulario, um para o valor de 15 dias e outro para o de 30
    # usei o type hidden com value="120,Mensalista 15 Dias" onde voce pode ver, [0] == 120 e [1] == Mensa....
    if request.method == "POST":
        valor = request.POST["valor"].split(",")
        preço = valor[0]
        info = valor[1]
        context = {"preco": preço, "info": info}
        return render(request,"Site/carrinho.html", context)  # joga os valors para a pagina de carrinho
                                                              # para que os valores corretos apareca para o cliente ver
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
            senha = request.POST["senha"]
            outros = {
                "valor": valor,
                "nickname": nickname,
                "senha": senha
            }

            # o email do django é bloqueante, para que a pagina nao fique esperando
            # manda o email para o render renderizar a pag suporte eu jogo isso para
            # uma threading com o nome, o email e o modo que é 2 para suporte
            email = threading.Thread(target=Mandar_Email, args=(nome, email, 1, outros))
            email.start()
    return render(request, "Site/index.html")


def Mandar_Email(nome, email, tipo, outros=""):
    # sei que é melhor tratar threading aqui, porem ainda nao o fiz, mas vou fazer !!!

    # Como sao so 2 metodos que mandam email, preferir deixa tudo aqui
    # pois seria mais simples de dar manutençao e de entender
    # o argumentos outros, é para usar com a msg tipo 1, que com ela coloco
    # informaçoes do tipo valor, nickname e senha, ja o suporte tipo 2 nao faz uso dela

    # Tipo
    # 1 Compra / Carrinho
    # 2 Suporte

    assunto = "YK Estacionamento" # O assunto do email

    if tipo == 1:
        msg = f"Obrigado por comprar sua mensalidade {nome}, ela foi no valor de ${outros['valor']}\n" \
              f"login: {outros['nickname']}\n" \
              f"senha: {outros['senha']}\n" \
              f"Faça login e aproveite a melhor empresa de estacionamento"
    else:
        msg = "Sua mensagem foi recebida, logo entraremos em contato."

    send_mail(assunto, msg, 'myemail@gmail.com', [email]) # Manda o email
