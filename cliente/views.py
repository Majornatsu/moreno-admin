from django.shortcuts import render, redirect, get_object_or_404
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

def editar_cliente(request, pk):
  cliente = get_object_or_404(Cliente, pk=pk)
  form=DadosForm(request.POST or None, instance=cliente)
  if form.is_valid():
    form.save()
    return redirect('buscar_cliente')
  return render(request, 'cliente/form_cadastro.html', {'form':form})

def deletar_cliente(request, pk):
  cliente = get_object_or_404(Cliente, pk=pk)
  if request.method=='POST':
    cliente.delete()
    return redirect('buscar_cliente')
  return render(request, 'deletar_confirmar.html', {'object':cliente})