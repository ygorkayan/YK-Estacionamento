from django import forms
from .models import Suporte, Carrinho


class FormSuporte(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = ["nome", "sobrenome", "nickname", "email", "texto"]


class FormCarrinho(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ["nome", "sobrenome", "nickname", "email", "endereco", "pais", "estado", "cep", "valor"]