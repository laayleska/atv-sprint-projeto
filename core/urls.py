from django.urls import path
from . import views

urlpatterns = [
    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
]