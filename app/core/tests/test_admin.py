from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSideTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="cihatbarann@gmail.com",
            password="Cbaran2011",
            name="Cihat"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="Cbaran2011",
            name="Cihat"
        )

    def test_users_listed(self):
        """Test the users are listed on user page"""
        url = reverse(
            'admin:core_customuser_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.admin_user.email)
        self.assertContains(res, self.admin_user.email)

    def test_user_change_page(self):
        """Test the user edit page works correctly"""
        url = reverse('admin:core_customuser_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        """Test create user page"""
        url = reverse('admin:core_customuser_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
