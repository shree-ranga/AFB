import re
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class TestSetup(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

        self.user_data = {"username": "username", "password": "strong-password"}

        return super().setUp()


class UserTest(TestSetup):
    def test_user_registration(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        token = Token.objects.get(user=User.objects.get())
        self.assertEqual(User.objects.get().auth_token, token)
        self.assertEqual(res.status_code, 201)

    def test_user_login(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_user_logout(self):
        # force authentication
        user = User.objects.create_user(username="username", password="password")
        token = Token.objects.create(user=user)
        client = APIClient()
        client.force_authenticate(user=user)
        res = client.delete(self.logout_url)
        self.assertEqual(res.status_code, 204)
