from payment.payment_interface import PaymentInterface
from rest_framework.test import APITestCase


class TestPaymentInterface(APITestCase):

    def test_get_without_header(self):
        res = PaymentInterface.get_without_header('https://api.paystack.co/bank')
        self.assertIsNotNone(res)

    def test_get_with_header(self):
        res = PaymentInterface.get_with_header(
            'https://api.paystack.co/bank/resolve?account_number=3104841829&bank_code=011')
        self.assertIsNotNone(res)
