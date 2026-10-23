from rest_framework import serializers
from django.utils import timezone



class TransacaoSerializer(serializers.Serializer):
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)
    dataHora= serializers.DateTimeField()

    def validate_valor(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "O valor não pode ser negativo!"
            )
        return value

    def validate_dataHora(self, value):
        if value > timezone.now():
            raise serializers.ValidationError(
                "A data não pode ser futura!"
            )
        return value