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
                  'Authorization': settings.PAYSTACK_PUBLIC_KEY}
        print(header)
        res = requests.get(url, headers=header)
        return res.json()
