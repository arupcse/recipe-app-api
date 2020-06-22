from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new use is normalized"""
        email = 'arup@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Pass123')

        self.assertEqual(user.email, email.lower())

    def test_create_superuser(self):
        """ Test create super user """
        user = get_user_model().objects.create_superuser(
            'hello@gamiil.com',
            'Pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_stuff)
