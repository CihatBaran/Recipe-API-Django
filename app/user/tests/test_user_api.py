from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


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
