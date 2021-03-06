from django.db import models
from cliente.models import Cliente
from servico.models import Servico

class Bicicleta(models.Model):
  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  servicos = models.ManyToManyField(Servico)
  def __str__(self):
    text ='{} - {}'.format(self.marca,self.modelo)
    return text