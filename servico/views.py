from django.shortcuts import render, redirect, get_object_or_404
import pdb;


from .models import Servico
from .forms import CadastroForm

def criar_servico(request):
  form=CadastroForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('buscar_servico')
  return render(request, 'servico/form_cadastro.html', {'form':form})

def buscar_servico(request):
  data = Servico.objects.all()
  return render(request, 'servico/listagem.html', {'data':data})

def editar_servico(request, pk):
  servico = get_object_or_404(Servico, pk=pk)
  form=CadastroForm(request.POST or None, instance=servico)
  if form.is_valid():
    form.save()
    return redirect('buscar_servico')
  return render(request, 'servico/form_cadastro.html', {'form':form})

def deletar_servico(request, pk):
  servico = get_object_or_404(Servico, pk=pk)
  if request.method=='POST':
    servico.delete()
    return redirect('buscar_servico')
  return render(request, 'deletar_confirmar.html', {'object':servico})