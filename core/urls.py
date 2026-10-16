from django.urls import path
from . import views

urlpatterns = [
    # URLs de Projetos já existentes...
    
    # URLs de Tarefas
    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/eliminar/', views.eliminar_tarefa, name='eliminar_tarefa'),
]