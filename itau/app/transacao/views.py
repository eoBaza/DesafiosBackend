from .serializers import TransacaoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from .models import Transacao

class TransacaoView(APIView):
    def post(self, request):
        transacao_serializer = TransacaoSerializer(data=request.data)
        try:
            transacao_serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response(
                transacao_serializer.errors,
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        Transacao.objects.create(
            **transacao_serializer.validated_data
        )

        return Response(
            status=status.HTTP_201_CREATED
        )