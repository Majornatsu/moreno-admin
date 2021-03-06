from django import forms
from django.forms import ModelForm 
from .models import Servico

class CadastroForm(forms.ModelForm):
  class Meta:
    model = Servico
    fields = [
      'nome', 'preco'
    ]