# _*_ conding: utf-8 _*_
from django import forms
from django.forms import ModelForm
from economiza.models import Produto, Comercio, Usuario
from django.contrib.auth.models import User

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
                    'nome',
                    'marca',
                    'comercio',
                    'preco'
        ]

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = [
                    'nome',
                    'rua',
                    'bairro',
                    'cidade',
                    'numero'
        ]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
                    'nome',
                    'senha',
                    'email'
        ]
        widgets = {
                    'senha': forms.PasswordInput(),
        }
