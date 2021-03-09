from django.db import models

class Cliente(models.Model):
    nomes = models.CharField(max_length=200, unique=True)
    cep = models.CharField(max_length=10)
    complemento = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    telefone = models.CharField(max_length=19)
    def __str__(self):
        text = '{}'.format(self.nomes)
        return text

    
