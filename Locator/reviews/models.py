from django.db import models
from posting_service.models import Service
from booking.models import Appointment
from django.contrib.auth.models import User
import string, random

def generate_unique_code():
    length = 6

    while True:
        ReviewID = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Review.objects.filter(ReviewID=ReviewID).count() == 0:
            break

    return ReviewID

# Create your models here.
class Review(models.Model):
  ReviewID = models.CharField(max_length=8, default=generate_unique_code, unique=True)
  service = models.ForeignKey(Service, on_delete=models.CASCADE)
  # appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
  client = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField()
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)