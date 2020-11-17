from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse

from db.models.user import User
from db.models.artist import Artist
from db.models.location import Location


class TestGetArtist(APITestCase):
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
        Artist.objects.create(
            user_id=self.user,
            location_id=self.location,
        )

        # self.token = Token.objects.create(user=self.user)
        # self.api_authentication()

    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_artist(self):
        url = reverse('artists-get-artist')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
