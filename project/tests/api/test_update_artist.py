from django.urls import reverse
from db.models.user import User
from db.models.artist import Artist
from rest_framework.test import APITestCase
from rest_framework import status


class TestValidate(APITestCase):

    def setUp(self):
        user_data = {
            "username": "ResB",
            "email": "there@gmail.com",
            "phone_number": "+2348151107708",
            "password": "resa1234"
        }

        self.user = User.objects.create(**user_data)
        artist_data = {
            "user_id":self.user,
            "firstname": "Resa",
            "lastname": "Obas",
            "avatar_url": "http://test.com"
        }

        self.artist = Artist.objects.create(**artist_data)

        self.data = {
            "username": "CoderGirl",
            "firstname": "Reeds",
            "lastname": "Obasy",
            "avatar_url": "https://url.com",
            "phone_number": "+2348123333453"
        }
        self.wrong_firstname = {
            "username": "CoderGirl",
            "firstname": "R76",
            "lastname": "Obasy",
            "avatar_url": "https://url.com",
            "phone_number": "+2348123333453"
        }

        self.update_username = {
            "username": "CodeBeast",
            "firstname": "Resa",
            "lastname": "Obasy",
            "avatar_url": "https://url.com",
            "phone_number": "+2348123333453"
        }

    def test_correct_data_validation(self):
        url = reverse('artists-update-profile', kwargs={"artist_id": self.artist.id})
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_incorrect_firstname_data_validation(self):
        url = reverse('artists-update-profile', kwargs={"artist_id": self.artist.id})
        response = self.client.put(url, self.wrong_firstname)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_data_updates_in_db(self):
        url = reverse('artists-update-profile', kwargs={"artist_id": self.artist.id})
        response = self.client.put(url, self.update_username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'].get('data').get('username'), 'CodeBeast')
