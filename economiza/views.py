from economiza.models import Comercio, Produto, Usuario
from django.shortcuts import render, redirect
from django.http import HttpResponse
from economiza.forms import ProdutoForm, ComercioForm, UsuarioForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required


# Create your views here.

def cadastre_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        context = {
            'msg': 'Usuario cadastrado com sucesso'
        }
        return render(request, 'user/cadastro_usuario.html', context)
    
    context = {
        'formulario': form
    }

    return render(request, 'user/cadastro_usuario.html', context)

def mostrar_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
    return render (request, 'user/login.html')

def submit_logout(request):
    logout(request)
    return redirect('/login')

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
        return render(request, 'cadastre_produto.html', context)
    
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
        return render(request, 'cadastre_comercio.html', context)
    
    context = {
        'formulario': form
    }

    return render(request, 'cadastre_comercio.html', context)

def mostrar_minha_lista(request):
    return render(request, 'minha_lista.html')

def mostrar_novo_item_lista(request):
    return render(request, 'novo_item_lista.html')

