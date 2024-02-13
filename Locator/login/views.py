from django.shortcuts import render
from rest_framework import generics
from .serializer import LoginSerializer
from .models import User

# Create your views here.
class LoginView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = LoginSerializer