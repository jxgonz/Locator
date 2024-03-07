from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from posting_service.models import Service
from django.core.files.uploadedfile import SimpleUploadedFile


class BookingServiceTestCase(TestCase):
    def test_booking_service(self):
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

        booking_url = f"/book/{self.service.ServiceID}/"
        booking_data = {
            'date_time': '2024-03-10T14:00'
        }

        response = self.client.post(booking_url, booking_data)

        self.assertEqual(response.status_code, 302)

    def test_booking_service_conflict(self):
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

        booking_url = f"/book/{self.service.ServiceID}/"
        booking_data = {
            'date_time': '2024-03-10T14:00'
        }

        response = self.client.post(booking_url, booking_data)

        self.assertEqual(response.status_code, 302)

        self.service2 = Service.objects.create(
            serviceName='Test Service2',
            description='Test Description2',
            price=100,
            credentials=SimpleUploadedFile(name='test_image.png', content=b'file_content', content_type='image/png')
        )

        booking_url2 = f"/book/{self.service2.ServiceID}/"

        response = self.client.post(booking_url2, booking_data)

        self.assertEqual(response.status_code, 302)








