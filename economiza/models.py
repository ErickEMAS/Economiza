from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=1000, default=50)

    def __str__(self):
        return self.nome

class Comercio(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    numero = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome