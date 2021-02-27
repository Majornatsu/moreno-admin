from django.db import models
from servico.models import Servico

class Bicicleta(models.Model):
  marca = models.CharField(max_length=200)
  modelo = models.CharField(max_length=200)
  servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
  def __str__(self):
    text ='{} - {}'.format(self.marca,self.modelo)
    return text