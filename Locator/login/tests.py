# Create your tests here.

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .views import register


class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        response = self.client.post(reverse('register'), form_data)

        self.assertEqual(response.status_code, 302)

        user_exists = User.objects.filter(username='johndoe').exists()
        self.assertTrue(user_exists)

    def test_user_registration_missing(self):
        form_data = {
            'first_name': 'John2',
            'last_name': 'Doe',
            'username': 'john2doe',
            'email': 'johnd2oe@example.com',
        }
        response = self.client.post(reverse('register'), form_data)

        self.assertEqual(response.status_code, 200)
        user_exists = User.objects.filter(username='johndoe').exists()
        self.assertFalse(user_exists)

    def test_user_registration_dup_username(self):
        form_data1 = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }

        form_data2 = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'john3doe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        response = self.client.post(reverse('register'), form_data1)

        self.assertEqual(response.status_code, 302)

        response2 = self.client.post(reverse('register'), form_data2)

        self.assertEqual(response2.status_code, 200)

    def test_user_registration_dup_email(self):
        form_data1 = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        form_data2 = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'john2doe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        response = self.client.post(reverse('register'), form_data1)

        self.assertEqual(response.status_code, 302)

        response2 = self.client.post(reverse('register'), form_data2)

        self.assertEqual(response2.status_code, 302)

        user_exists = User.objects.filter(username='johndoe').exists()
        self.assertTrue(user_exists)

        user_exists = User.objects.filter(username='john2doe').exists()
        self.assertTrue(user_exists)
