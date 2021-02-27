from django.db import models

class Servico(models.Model):
  nome = models.CharField(max_length=200, unique=True)
  preco= models.FloatField(default=0.0)
  def __str__(self):
      return self.nome
  