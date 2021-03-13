from django.urls import path
from .views import (criar_bicicleta, buscar_bicicleta, editar_bicicleta, deletar_bicicleta)

urlpatterns = [
    path('criar/', criar_bicicleta, name='criar_bicicleta'),
    path('', buscar_bicicleta, name='buscar_bicicleta'),
    path('<int:pk>/editar', editar_bicicleta, name='editar_bicicleta'),
    path('<int:pk>/deletar', deletar_bicicleta, name='deletar_bicicleta'),
]