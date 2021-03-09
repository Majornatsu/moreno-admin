from django.shortcuts import render, redirect
import pdb;

from .models import Cliente
from .forms import DadosForm

def criar_cliente(request):
  form=DadosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('buscar_cliente')
  return render(request, 'cliente/form_cadastro.html', {'form':form})

def buscar_cliente(request):
  data = Cliente.objects.all()
  return render(request, 'cliente/listagem.html', {'data':data})