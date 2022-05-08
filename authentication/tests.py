from rest_framework import status
#from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class AuthTestCase(APITestCase):

    def test_signup(self):
        data = {"username":"khalid","email": "khalid@email.com","phone_number":"+212656845962",
                "password": "password123","gender":0}
        response = self.client.post("/auth/signup/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        data = {"email": "tarik@email.com",
                "password": "password123"}
        response = self.client.post("/auth/login", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_unauthenticated(self):
        data = {"email": "unknown@email.com",
                "password": "password123"}
        response = self.client.post("/auth/login", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)