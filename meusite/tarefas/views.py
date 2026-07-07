from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def tarefas_nome(request):
    return HttpResponse("<h1>Aqui estão suas tarefas!</h1>")

def tarefas_adicionar(request):
    return HttpResponse('<h1>Adicionar tarefas</h1><button>Adicionar tarefas</button>')
