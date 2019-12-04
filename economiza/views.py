from django.shortcuts import render
from economiza.forms import ProdutoForm, ComercioForm
from economiza.models import *

# Create your views here.

def mostrar_home(request):
    return render(request, 'home.html')

def mostrar_cadastre(request):
    return render(request, 'cadastre.html')

def mostrar_cadastre_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        context  = {
            'msg': 'Produto cadastrado com sucesso'
        }
        return render (request, 'cadastre_produto.html', context)
    
    context = {
        'formulario': form
    }

    return render(request, 'cadastre_produto.html', context)

def mostrar_cadastre_comercio(request):
    form = ComercioForm(request.POST or None)

    if form.is_valid():
        form.save()
        context = {
            'msg': 'Comercio cadastrado com sucesso'
        }
        return render (request, 'cadastre_comercio.html', context)
    
    context = {
        'formulario': form
    }

    return render(request, 'cadastre_comercio.html', context)

def mostrar_minha_lista(request):
    return render(request, 'minha_lista.html')

def mostrar_novo_item_lista(request):
    return render(request, 'novo_item_lista.html')

def mostrar_simulador(request):
    return render(request, 'simulador.html')

def mostrar_login(request):
    return render(request, 'login.html')

def mostrar_cadastro_usuario(request):
    return render(request, 'cadastro_usuario.html')