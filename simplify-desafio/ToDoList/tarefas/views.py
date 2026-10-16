from django.shortcuts import render
from .models import Tarefas
from ToDoList.categoria.models import Categoria

# Create your views here.

def create_tarefas(request):
    tarefas = Tarefas.objects.create()
    return tarefas

def update_tarefas(request, dados):
    ...

def delete_tarefas(id_tarefas):
    tarefas = Tarefas.objects.delete(id=id_tarefas)
    tarefas.save()
    return tarefas

