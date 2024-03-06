# Create your tests here.

from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from views import register


class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 's3cret_password',
            'confirm_password': 's3cret_password',
        }
        response = self.client.post(reverse('register'), form_data)

        self.assertEqual(response.status_code, 302)

        user_exists = User.objects.filter(username='johndoe').exists()
        self.assertTrue(user_exists)

