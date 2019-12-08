# _*_ conding: utf-8 _*_
from django import forms
from django.forms import ModelForm
from economiza.models import Produto, Comercio
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password',
        ]
        widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
                    'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
                    'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
                    'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255}),                    
        }

        error_messages = {
            'username': {
                'required': 'Este campo é obrigatório'
            },

            'first_name': {
                'required': 'Este campo é obrigatório'
            },

            'last_name': {
                'required': 'Este campo é obrigatório'
            },

            'email': {
                'required': 'Este campo é obrigatório'
            },

            'password': {
                'required': 'Este campo é obrigatório'
            },
        }

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

