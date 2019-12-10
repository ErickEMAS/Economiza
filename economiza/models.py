from django.db import models

# Create your models here.

class Comercio(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome + ' ' + self.bairro + ' ' + self.cidade

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)
    preco = models.DecimalField(decimal_places=2, max_digits=1000, default=50)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nome