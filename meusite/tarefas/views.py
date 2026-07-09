from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def tarefas_nome(request):
    nome = {
        'nome': 'Vitor'

    }
    return render(request, 'pagetarefas/home.html', nome)

def tarefas_adicionar(request):
    adicionar = {
        'nome': 'à Página de Adicionar Tarefas'
    }
    return render(request, 'pagetarefas/adicionar.html', adicionar)

def tarefas_editar(request):
    editar = {
        'nome': 'à Página de Editar Tarefas'
    }
    return render(request, 'pagetarefas/editar.html', editar)


def tarefas_excluir(request):
    excluir = {
        'nome': 'à Página de Excluir Tarefas'
    }
    return render(request, 'pagetarefas/excluir.html', excluir)
