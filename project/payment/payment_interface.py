import requests
from django.conf import settings


class PaymentInterface:
    @classmethod
    def get(cls, url):
        res = requests.get(url)
        return res.json()

    @classmethod
    def get_header(cls, url):
        header = {'Content-Type': 'application/json',
                  'Authorization': settings.PAYSTACK_PUBLIC_KEY}
        res = requests.get(url, headers=header)
        return res.json()

    @classmethod
    def post(cls, url, data):
        header = {'Content-Type': 'application/json',
                  'Authorization': settings.PAYSTACK_PUBLIC_KEY}
        res = requests.post(url, data, headers=header)
        return res.json()
