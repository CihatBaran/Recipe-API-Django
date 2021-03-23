from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUsersApiTest(TestCase):
    "TEST the user api (public)"

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """TEST creating user with valid payload is successfull"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpass',
            'name': 'testname'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertNotEqual(user, None)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Creating user already exists"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpass',
            'name': 'testname'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Creating user with short password (more than 5)"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'tt',
            'name': 'testname'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test the token is created for user"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'cihatbaran22',
            'name': 'testname'
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_crendtial(self):
        """Token will not be created if invalid token is given"""
        create_user(email="test@gmail.com", password="cihatbaran22")
        not_created_payload = {
            'email': 'test@gmail.com',
            'password': 'passwordiswrong',
            'name': 'testname'
        }
        res = self.client.post(TOKEN_URL, not_created_payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token if the user does not exists"""
        payload = {
            'email': 'test@gmail.com',
            'password': 'passwordiswrong',
            'name': 'testname'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_fields(self):
        """Test that email and passwords are required"""
        res = self.client.post(
            TOKEN_URL, {'email': 'test@gmail.com', 'password': ''})
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
