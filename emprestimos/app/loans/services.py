from app.customer.models import Customer
from app.loans.models import Loans

def valid_loans(age, income, location):
    loans_list = []
    #emprestimo consignado
    if income >= 5000:
        loans = Loans.objects.filter(type="CONSIGNMENT").first()
        if loans:
            loans_list.append(loans)

    # emprestimo garantia / pessoal
    if income <= 3000:
        loans = Loans.objects.filter(type__in=["PERSONAL", "GUARANTEED"])
        if loans.exists():
            loans_list.extend(loans)

    # emprestimo garantia / pessoal
    elif income >=3000 and income <= 5000 and age >=30 and location == "SP":
        loans = Loans.objects.filter(type__in=["PERSONAL", "GUARANTEED"])
        if loans.exists():
            loans_list.extend(loans)


    return loans_list
