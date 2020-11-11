import requests
from django.conf import settings


class PaymentInterface:
    @classmethod
    def get_without_header(cls, url):
        res = requests.get(url)
        return res.json()

    @classmethod
    def get_with_header(cls, url):
        header = {'Content-Type': 'application/json',
                  'Authorization': settings.BEARER_KEY}
        res = requests.get(url, headers=header)
        return res.json()
