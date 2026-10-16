from django.shortcuts import render

from ToDoList.categoria.models import Categoria
from ToDoList.tarefas.models import Tarefas

def create_tarefas(request):
    nome = request.get('nome')
    descricao = request.get('descricao')
    tarefas = Tarefas.objects.create(nome = nome, descricao = descricao)
    return tarefas

def update_tarefas(request):
    ...

def delete_tarefas(id_tarefas):
    tarefas = Tarefas.objects.delete(id=id_tarefas)
    return tarefas

def tarefas_list():
    tarefas = Tarefas.objects.select_related("prioridade").all()
    return tarefas

# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    tarefas = tarefas_list()
    return render(request, 'base.html', {'categorias': categorias, 'tarefas': tarefas})
