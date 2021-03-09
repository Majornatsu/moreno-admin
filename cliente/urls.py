from django.urls import path
from .views import criar_cliente, buscar_cliente

urlpatterns = [
    path('criar/', criar_cliente, name='criar_cliente'),
    path('', buscar_cliente, name='buscar_cliente'),
]