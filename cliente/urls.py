from django.urls import path
from .views import criar_cliente, buscar_cliente, editar_cliente, deletar_cliente

urlpatterns = [
    path('criar/', criar_cliente, name='criar_cliente'),
    path('', buscar_cliente, name='buscar_cliente'),
    path('<int:pk>/editar', editar_cliente, name='editar_cliente'),
    path('<int:pk>/excluir', deletar_cliente, name='deletar_cliente'),
]