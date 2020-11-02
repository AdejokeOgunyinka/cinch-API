from rest_framework.test import APITestCase, APIClient
# from db.models.artist import Artist
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from db.models.user import User
import json


class OtpViewSetTest(APITestCase):

    def SetUp(self):
        self.client = APIClient
        self.otp = '123456'
        self.user = User.objects.create(
            email="remiadewale2809@gmail.com",
            username="remi2828",
            phone_number="+2349062215897",
            password="remi2828",
            otp_code=self.otp
        )


        self.artist = Artist.objects.create(
            user_id=self.user,
            firstname="Remi",
            lastname="Adewale",
        )


    def test_invalid_response_verify_otp(self):

        url = reverse('otps-verify')  # confirm if this url path will work
        req_data = {
            "email": "",
            "otp_code": ""
        }

        response = self.client.post(url,req_data)

        self.assertEqual(response.status_code, 200)
        exp_data = {
                "message": "failure",
        }
        self.assertEqual(exp_data["message"], response.data["message"])


    def test_invalid_response_verify_otp_with_incorrect_otp(self):


        url = reverse('otps-verify')
        req_data = {
            "email": self.user["email"],
            "otp_code": "1234567"
        }
        response = self.client.post(url, req_data)
        self.assertEqual(response.status_code, 200)
        exp_data = {
                "message": "failure",
        }
        self.assertEqual(exp_data["message"], response.data["message"])


    def test_invalid_response_verify_otp_with_incorrect_email(self):


        url = reverse('otps-verify')
        req_data = {
            "email": "remiawale2809@gmail.com",
            "otp_code": self.user["otp_code"]
        }
        response = self.client.post(url, req_data)
        self.assertEqual(response.status_code, 200)
        exp_data = {
            "message": "failure",

        }

        self.assertEqual(exp_data["message"], response.data["message"])


    def test_valid_email_valid_otp(self):
        url = reverse('otps-verify')
        req_data = {
            "email": self.user["email"],
            "otp_code": self.user["otp_code"]
        }
        response = self.client.post(url, req_data)
        self.assertEqual(response.status_code, 200)
        exp_data = {
            "message": "success",

        }
        self.assertEqual(exp_data["message"], response.data["message"])

