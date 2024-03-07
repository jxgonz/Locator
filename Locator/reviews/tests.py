from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from posting_service.models import Service
from django.core.files.uploadedfile import SimpleUploadedFile


class BookingServiceTestCase(TestCase):
    def test_reviewing_service(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        self.client.post(reverse('register'), form_data)

        self.service = Service.objects.create(
            serviceName='Test Service',
            description='Test Description',
            price=100,
            credentials=SimpleUploadedFile(name='test_image.png', content=b'file_content', content_type='image/png')
        )

        comment_url = f"/serviceview/{self.service.ServiceID}/"
        comment_data = {
            'rating': '5',
            'comment': 'Excellent'
        }

        response = self.client.post(comment_url, comment_data)

        self.assertEqual(response.status_code, 302)

    def test_reviewing_service_no_comment(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        self.client.post(reverse('register'), form_data)

        self.service = Service.objects.create(
            serviceName='Test Service',
            description='Test Description',
            price=100,
            credentials=SimpleUploadedFile(name='test_image.png', content=b'file_content', content_type='image/png')
        )

        comment_url = f"/serviceview/{self.service.ServiceID}/"
        comment_data = {
            'rating': '5',
        }

        response = self.client.post(comment_url, comment_data)

        self.assertEqual(response.status_code, 200)

    def test_reviewing_service_no_rating(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'Television1234@',
            'password2': 'Television1234@',
        }
        self.client.post(reverse('register'), form_data)

        self.service = Service.objects.create(
            serviceName='Test Service',
            description='Test Description',
            price=100,
            credentials=SimpleUploadedFile(name='test_image.png', content=b'file_content', content_type='image/png')
        )

        comment_url = f"/serviceview/{self.service.ServiceID}/"
        comment_data = {
            'comment': 'Excellent'
        }

        response = self.client.post(comment_url, comment_data)

        self.assertEqual(response.status_code, 200)
