from django.db import models
from django.contrib.auth.models import User
from posting_service.models import Service
from django.utils import timezone
import string
import random

def generate_unique_code():
    length = 6

    while True:
        AppointmentID = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Appointment.objects.filter(AppointmentID=AppointmentID).count() == 0:
            break

    return AppointmentID

# Create your models here.
class Appointment(models.Model):
  AppointmentID = models.CharField(max_length=8, default=generate_unique_code, unique=True)
  client = models.ForeignKey(User, on_delete=models.CASCADE)
  service = models.ForeignKey(Service, on_delete=models.CASCADE)
  status = models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('COMPLETED', 'Completed'), ('CANCELLED', 'Cancelled')], blank=True)
  date_time = models.DateTimeField(default=timezone.now)
  created_at = models.DateTimeField(auto_now_add=True, null=True)