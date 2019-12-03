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