from django.urls import path
from . import views


urlpatterns = [
    path('', views.tarefas_nome),
    path('adicionar/', views.tarefas_adicionar)
]