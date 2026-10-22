from app.customer.models import Customer
from app.loans.models import Loans

def valid_loans(age, income, location):
    #emprestimo consignado
    if income >= 500:
        loas = Loans.objects.filter(type="CONSIGNMENT").first()
