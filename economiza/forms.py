from django import forms
from economiza.models import Produto, Comercio

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

