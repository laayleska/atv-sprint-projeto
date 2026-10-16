from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

# Listar Tarefas
def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'core/listar_tarefas.html', {'tarefas': tarefas})

# Criar Tarefa
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'core/form_tarefa.html', {'form': form, 'titulo_pagina': 'Nova Tarefa'})

# Editar Tarefa
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'core/form_tarefa.html', {'form': form, 'titulo_pagina': 'Editar Tarefa'})

# Eliminar Tarefa
def eliminar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')
    return render(request, 'core/confirmar_eliminar_tarefa.html', {'tarefa': tarefa})