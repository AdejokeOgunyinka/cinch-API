# from django.contrib.auth import get_user_model
# from django.urls import reverse
#
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
# from db.models.user import User
# from db.serializers.password_serializer import PasswordSerializer
#
#
# class PasswordUpdateApiTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = get_user_model().objects.create_user(
#             'user@xyz.com',
#             'user1',
#             'endsar1'
#         )
#         self.client.force_authenticate(self.user)
#         #
#         self.data = {
#             'username': 'user1',
#             'password': 'endsars1'
#         }
#         #
#         # self.update = {
#         #     'old_password': 'endsars1',
#         #     "password": "endsars2",
#         #     "confirm_password": "endsars2"
#         # }
#         # self.user = User.objects.create_user(**self.data)
#
#
#     def test_update_pass(self):
#         response1 = self.client.post('/api/user/login/', self.data, follow=True)
#         print(response1.status_code)
#         # self.client.force_authenticate(self.user)
#         # # self.client.login(username="user1", password="endsars1")
#         # response = self.client.put('/api/v1/passwords/change/', self.update)
#
#         self.assertEqual(response1.status_code, status.HTTP_200_OK)
#
#     def test_sample(self):
#         self.assertIsInstance('API Test', str)
#         pass
#
#     def test_sample(self):
#         self.assertIsInstance('API Test', str)
#         pass
#
#     def tearDown(self):
#         pass

import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from db.models.user import User
from db.serializers.password_serializer import PasswordSerializer


class PasswordUpdateApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@xyz.com',
            username='user1',
            password='endsars1'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_update_pass(self):
        response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars1", "password": "endsars2",
                                                                "confirm_password": "endsars2"})
        response.render()
        self.assertEqual(json.loads(response.content), {'message': 'success', 'data': {'data': None}, 'errors': None})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_update_pass_response(self):
    #     response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars1", "password": "endsars2",
    #                                                             "confirm_password": "endsars2"})
    #     response.render()
    #     self.assertEqual(json.loads(response.content), {'message': 'success', 'data': {'data': None}, 'errors': None})

    def test_update_fail_old_password(self):
        response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars3", "password": "endsars2",
                                                                "confirm_password": "endsars2"})
        response.render()
        self.assertEqual(json.loads(response.content), {'message': 'failure', 'data': None,
                                                        'errors': {'old_password': [
                                                            'Old password is incorrect. Please enter it again.'],
                                                            '_others': []}}
                         )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_update_fail_old_password_response(self):
    #     response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars3", "password": "endsars2",
    #                                                             "confirm_password": "endsars2"})
    #     response.render()
    #     self.assertEqual(json.loads(response.content), {'message': 'failure', 'data': None,
    #                                                     'errors': {'old_password': [
    #                                                         'Old password is incorrect. Please enter it again.'],
    #                                                                '_others': []}}
    #                      )

    def test_new_passwords_no_match(self):
        response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars1", "password": "endsars2",
                                                                "confirm_password": "endsars3"})
        response.render()
        self.assertEqual(json.loads(response.content), {'message': 'failure', 'data': None,
                                                        'errors': {'non_field_errors': [
                                                            "The two password fields don't match."],
                                                            '_others': []}}
                         )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_new_passwords_no_match_response(self):
    #     response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars1", "password": "endsars2",
    #                                                             "confirm_password": "endsars3"})
    #     response.render()
    #     self.assertEqual(json.loads(response.content), {'message': 'failure', 'data': None,
    #                                                     'errors': {'non_field_errors': [
    #                                                         "The two password fields don't match."],
    #                                                         '_others': []}}
    #                      )
