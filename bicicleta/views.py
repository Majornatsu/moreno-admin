from django.shortcuts import render, redirect
import pdb;


from .models import Bicicleta
from .forms import BikeForm

def criar_bicicleta(request):
  form=BikeForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('buscar_bicicleta')
  return render(request, 'bicicleta/form_cadastro.html', {'form':form})

def buscar_bicicleta(request):
  data = Bicicleta.objects.all()
  return render(request, 'bicicleta/listagem.html', {'data':data})