from django.db import models
from django.contrib.auth.models import User
import string
import random


def generate_unique_code():
    length = 6

    while True:
        ServiceID = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Service.objects.filter(ServiceID=ServiceID).count() == 0:
            break

    return ServiceID

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.User.username}/{filename}'
  
# Create your models here.
class Service(models.Model):
  ServiceID = models.CharField(max_length=8, default=generate_unique_code, unique=True)
  freelancer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  serviceName = models.CharField(max_length=250)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2) 
  credentials = models.FileField(upload_to='documents/', null=True, blank=True)
#   category = models.CharField(max_length=40, choices=[('EDUCATION', 'Education'), ('LIFESTYLE AND WELLNESS', 'Lifestyle and Wellness'), ('CONSTRUCTION AND RENOVATION', 'Construction and Renovation'), ('LANDSCAPING AND GARDENING', 'Landscaping and Gardening')], null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
class Photo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    service_img = models.ImageField(upload_to='images/', null=True, blank=True)
    
      