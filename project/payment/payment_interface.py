import requests
from django.conf import settings


class PaymentInterface:
    @classmethod
    def get(cls, url):
        res = requests.get(url)
        return res.json()

    @classmethod
    def get_with_auth(cls, url):
        header = {'Content-Type': 'application/json',
                  'Authorization': 'Bearer sk_test_e1f44a559f0a74adbcdfe63656db76d6152056a0'}
        print(header)
        res = requests.get(url, headers=header)
        return res.json()
