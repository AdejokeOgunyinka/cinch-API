from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from db.models.user import User
from db.models.artist import Artist
from db.models.account import Account


class TestCreateAccount(APITestCase):
    def setUp(self):
        user_data = {
            "email": "there@gmail.com",
            "password": "resa1234",
            "otp_code":"978299"
        }

        self.user = User.objects.create(**user_data)

        artist_data = {
            "user_id": self.user,
            "firstname": "Resa",
            "lastname": "Obas",
            "avatar_url": "http://test.com"
        }

        self.artist = Artist.objects.create(**artist_data)

        account_data = {
            "account_number": "0221618652",
            "bank_code": "058",
            "bank_name": "GTB Bank",
            "artist_id": self.artist
        }

        Account.objects.create(**account_data)

        self.data = {
            "account_number": "0142651862",
            "bank_code": "058",
            "bank_name": "GTB Bank"
        }

        self.wrong_data = {
            "account_number": "02216652",
            "bank_code": "058",
            "bank_name": "GTB Bank"
        }
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_update_valid_account(self):
        url = reverse('accounts-update-account')
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_account(self):
        url = reverse('accounts-update-account')
        response = self.client.put(url, self.wrong_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_that_account_db_updates(self):
        url = reverse('accounts-update-account')
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('data')['account_number'], '0142651862')


