from rest_framework.response import Response
from rest_framework.views import APIView

from app.customer.serializers import CustomerSerializer
from app. loans.serializers import LoansSerializer

from app.loans.services import valid_loans

# Create your views here.

class LoansView(APIView):
    def post(self, request):
        serializer_customer = CustomerSerializer(data=request.data)
        serializer_customer.is_valid(raise_exception=True)

        loans_valid = valid_loans(serializer_customer.validated_data["age"], serializer_customer.validated_data["income"], serializer_customer.validated_data["location"])
        serializer_loans = LoansSerializer(loans_valid, many=True)

        details = {
            "name": serializer_customer.validated_data["name"],
            "loans": serializer_loans.data,
        }

        return Response(details)
