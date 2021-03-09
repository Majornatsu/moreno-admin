from django.urls import path
from .views import criar_bicicleta, buscar_bicicleta

urlpatterns = [
    path('criar/', criar_bicicleta, name='criar_bicicleta'),
    path('', buscar_bicicleta, name='buscar_bicicleta'),
]