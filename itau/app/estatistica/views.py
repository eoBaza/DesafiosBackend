from rest_framework.views import APIView
from rest_framework.response import Response
from .services import estatisica_service

class EstatisticasView(APIView):
    def get(self, request):
        dados = estatisica_service()
        return Response(dados)