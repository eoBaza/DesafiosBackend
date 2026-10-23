from django.db import models
from django.utils import timezone


class Transacao(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dataHora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transação {self.id} - R$ {self.valor}"

    class Meta:
        db_table = 'transacao'
        verbose_name='Transacao'
