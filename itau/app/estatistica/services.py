from datetime import timedelta
from django.utils import timezone
from django.db.models import Count, Sum, Avg, Min, Max
from app.transacao.models import Transacao



def estatisica_service():
    agora = timezone.now()
    limite = agora - timedelta(seconds=60)
    transacoes = Transacao.objects.filter(dataHora__gte=limite, dataHora__lte=agora)
    estatisticas = transacoes.aggregate(
        count=Count("id"),
        sum=Sum("valor"),
        avg=Avg("valor"),
        min=Min("valor"),
        max=Max("valor")
    )

    return {
        "count": estatisticas["count"],
        "sum": estatisticas["sum"],
        "avg": estatisticas["avg"],
        "max": estatisticas["max"]
    }