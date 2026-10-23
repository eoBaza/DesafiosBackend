from rest_framework import serializers


class LoansSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50)
    interest_rate = serializers.IntegerField()