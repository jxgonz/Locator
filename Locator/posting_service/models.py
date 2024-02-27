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
# class Freelancer(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   FreelancerID = models.CharField(max_length=8, default=generate_unique_code, unique=True)
#   # services_offered = models.JSONField(default=list)  # Storing services offered as a JSON list

class Service(models.Model):
  ServiceID = models.CharField(max_length=8, default=generate_unique_code, unique=True)
  # freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
  serviceName = models.CharField(max_length=250)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2) 
  # portfolio = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
  # credentials = models.FileField(upload_to=user_directory_path, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  