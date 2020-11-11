from .payment_interface import PaymentInterface
from app.action import Action


class BankList(Action):
    def perform(self):
        try:
            res = PaymentInterface.get_without_header('https://api.paystack.co/bank')
            banks = res.get('data')
            bank_data = [{'name' : bank.get('name'), 'code': bank.get('code')} for bank in banks]
            return bank_data
        except:
            return self.fail(dict(paystack_error='Having problems connecting to paystack'))
