from payment.payment_interface import PaymentInterface
from rest_framework.test import APITestCase
import json


class TestPaymentInterface(APITestCase):

    def test_get(self):
        res = PaymentInterface.get('https://api.paystack.co/bank')
        self.assertIsNotNone(res)

    def test_get_header(self):
        res = PaymentInterface.get_header(
            'https://api.paystack.co/bank/resolve?account_number=3104841829&bank_code=011')
        value = {
                    "status": True,
                    "message": "Account number resolved",
                    "data": {
                            "account_number": "3104841829",
                            "account_name": "OGUNYINKA ADEJOKE ARINOLA",
                            "bank_id": 7
                    }
        }
        self.assertEquals(res, value)

    def test_post(self):
        data = json.dumps({"customer": "CUS_d78op1enq5cftcd", "risk_action": "allow"})
        res = PaymentInterface.post('https://api.paystack.co/customer/set_risk_action', data)
        self.assertIsNotNone(res)
