from django.urls import path
from . import views


app_name = 'tarefas'
urlpatterns = [
    path('', views.tarefas_nome, name='home'),
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('editar/', views.tarefas_editar, name='editar'),
    path('excluir/', views.tarefas_excluir, name='excluir'),
]