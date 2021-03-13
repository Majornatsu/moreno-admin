from django.shortcuts import render, redirect, get_object_or_404
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

def editar_bicicleta(request, pk):
  bicicleta = get_object_or_404(Bicicleta, pk=pk)
  form=BikeForm(request.POST or None, instance=bicicleta)
  if form.is_valid():
    form.save()
    return redirect('buscar_bicicleta')
  return render(request, 'bicicleta/form_cadastro.html', {'form':form})

def deletar_bicicleta(request, pk):
  bicicleta = get_object_or_404(Bicicleta, pk=pk)
  if request.method=='POST':
    bicicleta.delete()
    return redirect('buscar_bicicleta')
  return render(request, 'deletar_confirmar.html', {'object':bicicleta})
