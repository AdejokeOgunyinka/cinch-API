from django.urls import reverse
from db.models.user import User
from db.models.artist import Artist
from db.models.location import Location
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token


class TestValidate(APITestCase):

    def setUp(self):
        user_data = {
            "email": "there@gmail.com",
            "password": "resa1234"
        }

        self.user = User.objects.create(**user_data)

        artist_data = {
            "user_id": self.user,
            "firstname": "Resa",
            "lastname": "Obas",
            "avatar_url": "http://test.com"
        }

        self.artist = Artist.objects.create(**artist_data)

        location_data = {
            "id" : "234",
            "country_code": "+234",
            "country": "Nigeria"
        }

        self.location = Location.objects.create(**location_data)

        self.data = {
            "avatar_url": "https://url.com",
            "phone_number": "+2348123333453",
            "location_id": "234"
        }
        self.with_first_lastname = {
            "firstname": "Ree",
            "lastname": "Obasy",
            "avatar_url": "https://url.com",
            "phone_number": "+2348123333453",
            "location_id": "234"
        }
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_without_first_and_lastname(self):
        url = reverse('artists-update-profile')
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_first_and_lastname(self):
        url = reverse('artists-update-profile')
        response = self.client.put(url, self.with_first_lastname)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_data_updates_in_db(self):
        url = reverse('artists-update-profile')
        response = self.client.put(url, self.with_first_lastname)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('data')['first_name'], 'Ree')
