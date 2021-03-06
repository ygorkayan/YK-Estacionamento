from django.db import models


class Suporte(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=80)
    sobrenome = models.CharField(max_length=80)
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    texto = models.TextField(max_length=700)

    class Meta:
        verbose_name_plural = 'Suporte'

    def __str__(self):
        return self.nickname


class Carrinho(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=80)
    sobrenome = models.CharField(max_length=80)
    nickname = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    valor = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = 'Carrinho'

    def __str__(self):
        return self.nome
