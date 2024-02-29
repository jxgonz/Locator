from django.db import models
from login.service import Service
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
  service = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
  # appointment_verification = models.ForeignKey()
  client = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  rating = models.PositiveIntegerField()
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)