from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, 'home.html')

def mostrar_cadastre(request):
    return render(request, 'cadastre.html')

def mostrar_cadastre_produto(request):
    return render(request, 'cadastre_produto.html')

def mostrar_cadastre_comercio(request):
    return render(request, 'cadastre_comercio.html')

def mostrar_minha_lista(request):
    return render(request, 'minha_lista.html')

def mostrar_novo_item_lista(request):
    return render(request, 'novo_item_lista.html')

def mostrar_simulador(request):
    return render(request, 'simulador.html')

def mostrar_login(request):
    return render(request, 'login.html')