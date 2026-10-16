from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'core/form_projeto.html', {'form': form, 'titulo_pagina': 'Novo Projeto'})

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'core/form_projeto.html', {'form': form, 'titulo_pagina': 'Editar Projeto'})

def eliminar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('listar_projetos')
    return render(request, 'core/confirmar_eliminar_projeto.html', {'projeto': projeto})


def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'core/listar_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'core/form_tarefa.html', {'form': form, 'titulo_pagina': 'Nova Tarefa'})

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

def eliminar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')
    return render(request, 'core/confirmar_eliminar_tarefa.html', {'tarefa': tarefa})