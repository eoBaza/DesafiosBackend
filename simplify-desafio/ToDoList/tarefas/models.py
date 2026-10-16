from django.db import models

from ToDoList.categoria.models import Categoria


# Create your models here.
class Tarefas(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    prioridade = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    realizado = models.BooleanField(default=False)


    class Meta:
        db_table = 'tarefas'
        verbose_name = 'Tarefa'

    def __str__(self):
        return self.nome