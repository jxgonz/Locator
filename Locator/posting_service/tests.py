from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User



# Create your tests here.


class PostingServiceTestCase(TestCase):
    def test_post_service(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        self.client.post(reverse('register'), form_data)

        service_data = {
            "serviceName": "Cleaning",
            "description": "Clean your house",
            "price": "20",
            "credentials": SimpleUploadedFile(name='test_image.png', content=b'file_content', content_type='image/png')

        }
        response = self.client.post(reverse('posting_service:create-service'), service_data)

        self.assertEqual(response.status_code, 302)

    def test_post_service_missing(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        self.client.post(reverse('register'), form_data)

        service_data = {
            "serviceName": "Cleaning",
            "price": "20",
            "credentials": SimpleUploadedFile(name='test_image.png', content=b'file_content',
                                              content_type='image/png')

        }
        response = self.client.post(reverse('posting_service:create-service'), service_data)

        self.assertEqual(response.status_code, 200)


