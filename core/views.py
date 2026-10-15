from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/listar_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Projeto criado com sucesso!')
        return redirect('listar_projetos')
    return render(request, 'core/form_projeto.html', {'form': form, 'titulo': 'Novo Projeto'})