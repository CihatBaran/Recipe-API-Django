from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Creating new user with an email successfull..."""
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', password='foo')

        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.check_password('foo'))
        self.assertTrue(user.is_active)

    def test_new_user_email_normalized(self):
        """Test the email for new user if it is normalized or not!"""
        email = "cihatbaran@GMAIL.COM"
        User = get_user_model()
        user = User.objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="cihatbarann@gmail.com", password='foo', is_active=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="cihatbarann@gmail.com", password='foo', is_staff=False)
