from rest_framework.response import Response

from rest_framework.views import APIView

from app.customer.serializers import CustomerSerializer
from app.loans.models import Loans
from app. loans.serializers import LoansSerializer


# Create your views here.

class LoansView(APIView):
    def post(self, request):
        serializer_customer = CustomerSerializer(data=request.data)
        serializer_customer.is_valid(raise_exception=True)

        loans = Loans.objects.all()
        serializer_loans = LoansSerializer(loans, many=True)

        details = {
            "name": serializer_customer.validated_data["name"],
            "loans": serializer_loans.data,
        }

        return Response(details)
