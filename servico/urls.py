from django.urls import path
from .views import criar_servico, buscar_servico, editar_servico, deletar_servico

urlpatterns = [
    path('criar/', criar_servico, name='criar_servico'),
    path('', buscar_servico, name='buscar_servico'),
    path('<int:pk>/editar', editar_servico, name='editar_servico'),
    path('<int:pk>/deletar', deletar_servico, name='deletar_servico'),
]
