from payment.payment_interface import PaymentInterface
from rest_framework.test import APITestCase


class TestPaymentInterface(APITestCase):

    def test_get(self):
        res = PaymentInterface.get('https://api.paystack.co/bank')
        self.assertEquals(res.get('status'), True)

    def test_get_header(self):
        res = PaymentInterface.get_header(
            'https://api.paystack.co/bank/resolve?account_number=3104841829&bank_code=011')
        self.assertEquals(res.get('status'), True)
