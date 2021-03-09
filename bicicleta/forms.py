from django import forms
from django.forms import ModelForm 
from .models import Bicicleta

class BikeForm(forms.ModelForm):
  class Meta:
    model = Bicicleta
    fields = [
      'marca', 'modelo', 'cliente', 'servicos',
    ]