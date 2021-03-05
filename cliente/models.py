from django.db import models
from bicicleta.models import Bicicleta

class Pedido(models.Model):
    nomes = models.CharField(max_length=200, unique=True)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    telefone = models.CharField(max_length=12)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    def __str__(self):
        text = '{}'.format(self.nomes)
        return text

    
