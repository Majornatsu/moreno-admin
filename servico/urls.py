from django.urls import path
from .views import criar_servico, buscar_servico

urlpatterns = [
    path('criar/', criar_servico, name='criar_servico'),
    path('', buscar_servico, name='buscar_servico'),
]
