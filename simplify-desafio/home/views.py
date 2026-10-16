from django.shortcuts import render

from ToDoList.categoria.models import Categoria


# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'base.html', {'categorias': categorias})
