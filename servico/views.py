from django.shortcuts import render, redirect
import pdb;
#C->criar o cadastro 
#R->fazer a busca e listar td q foi cadastrado
#U->atualiza algo q foi cadastrado 
#D->remove algo cadastrado

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
