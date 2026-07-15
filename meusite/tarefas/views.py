from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel

# Create your views here.


def tarefas_nome(request):
    nome = {
        'nome': 'Vitor',
        "tarefas": TarefaModel.objects.all(),

    }
    return render(request, 'pagetarefas/home.html', nome)

def tarefas_adicionar(request):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    adicionar = {
        'form': TarefaForm()
    }
    return render(request, 'pagetarefas/adicionar.html', adicionar)

def tarefas_editar(request,id):
    tarefa = get_object_or_404(TarefaModel,id=id)
    if request.method == "POST":
        formulario = TarefaForm(request.POST,instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    else:
        editar = {
            'form':TarefaForm(instance=tarefa)
        }

    return render(request, "pagetarefas/editar.html", editar)


def tarefas_excluir(request,id):
    tarefa = get_object_or_404(TarefaModel,id=id)
    tarefa.delete()
    return redirect("tarefas:home")

