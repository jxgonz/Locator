from django.db import models

# Create your models here.
class User(models.Model):
  userID = models.CharField(max_length=8, default="", unique=True)
  username = models.CharField(max_length=10, unique=True)
  firstname = models.CharField(max_length=254)
  lastname = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)
  is_freelancer = models.BooleanField(null=False, default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  
