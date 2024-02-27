from django.db import models
from login.service import Service
from django.conf import settings

# Create your models here.
class Review(models.Model):
  service_to_review = models.ForeignKey(Service, on_delete=models.CASCADE)
  # appointment_verification = models.ForeignKey()
  buyer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField()
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)