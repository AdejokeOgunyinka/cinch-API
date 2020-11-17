from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse

from db.models.user import User
from db.models.artist import Artist
from db.models.account import Account
from db.models.location import Location


class TestArtistAccount(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@xyz.com',
            username='user1',
            password='endsars1'
        )
        self.location = Location.objects.create(
            country='Nigeria',
            country_code='+234'
        )
        self.artist = Artist.objects.create(
            user_id=self.user,
            location_id=self.location,
        )
        Account.objects.create(
            artist_id=self.artist,
            bank_code='011',
            bank_name='First Bank of Nigeria',
            account_number='3104841829'
        )

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_artist_account(self):
        url = reverse('accounts-get-artist-account')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
