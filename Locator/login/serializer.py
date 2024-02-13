from rest_framework import serializers
from .models import User

class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('userID', 'username', 'firstname', 'lastname', 'email', 'is_freelancer', 'created_at')