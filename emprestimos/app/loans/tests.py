from django.test import TestCase
from app.loans.models import Loans
from app.loans.services import valid_loans  # Ajuste a importação para a pasta correta do seu service

class ValidLoansServiceTestCase(TestCase):

    def setUp(self):
        # Cria os dados mockados no banco de dados isolado de teste
        self.loan_consignment = Loans.objects.create(
            type="CONSIGNMENT",
            interest_rate = 2
            # Adicione outros campos obrigatórios do modelo Loans se existirem
        )
        self.loan_personal = Loans.objects.create(
            type="PERSONAL",
            interest_rate = 4
            # Adicione outros campos obrigatórios do modelo Loans se existirem
        )

    def test_income_greater_than_or_equal_to_500_returns_consignment(self):
        """Renda de 500 ou mais deve retornar empréstimo consignado."""
        resultado = valid_loans(age=30, income=600, location="SP")

        self.assertEqual(len(resultado), 1)
        self.assertIn(self.loan_consignment, resultado)
        self.assertNotIn(self.loan_personal, resultado)

    def test_income_less_than_or_equal_to_300_returns_personal(self):
        """Renda de 300 ou menos deve retornar empréstimo pessoal."""
        resultado = valid_loans(age=25, income=200, location="RJ")

        self.assertEqual(len(resultado), 1)
        self.assertIn(self.loan_personal, resultado)
        self.assertNotIn(self.loan_consignment, resultado)

    def test_income_between_301_and_499_returns_empty_list(self):
        """Renda entre 301 e 499 não deve retornar nenhum empréstimo."""
        resultado = valid_loans(age=40, income=400, location="MG")

        self.assertEqual(resultado, [])