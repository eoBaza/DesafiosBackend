from rest_framework import serializers
from app.customer.models import Customer
from .models import Loans


class LoansSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50)
    interest_rate = serializers.IntegerField()