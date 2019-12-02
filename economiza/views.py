from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, 'home.html')

def mostrar_cadastre(request):
    return render(request, 'cadastre.html')