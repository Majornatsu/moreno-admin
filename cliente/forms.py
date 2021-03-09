from django import forms
from django.forms import ModelForm 
from .models import Cliente

class DadosForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = [
      'nomes', 'cep', 'complemento', 'numero', 'telefone',
    ]