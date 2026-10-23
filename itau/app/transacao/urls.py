from django.urls import path
from .views import TransacaoView

urlpatterns = [
    path('transacao/', TransacaoView.as_view(), name="transacao"),

]