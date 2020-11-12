from payment.payment_interface import PaymentInterface
from rest_framework.test import APITestCase
from rest_framework import status
import json


class TestPaymentInterface(APITestCase):

    def test_get(self):
        res = PaymentInterface.get('https://api.paystack.co/bank')
        self.assertEquals(res.get('status'), True)

    def test_get_header(self):
        res = PaymentInterface.get_header(
            'https://api.paystack.co/bank/resolve?account_number=3104841829&bank_code=011')
        self.assertEquals(res.get('status'), True)

    def test_post(self):
        data = json.dumps({"customer": "CUS_d78op1enq5cftcd", "risk_action": "allow"})
        res = PaymentInterface.post('https://api.paystack.co/customer/set_risk_action', data)
        self.assertEquals(res.get('status'), None)
