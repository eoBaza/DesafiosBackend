from django.urls import path
from .views import EstatisticasView

urlpatterns = [
    path('estatisticas/', EstatisticasView.as_view(), name='estatistica'),
]