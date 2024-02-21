from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics
from .serializer import LoginSerializer
from .models import User
from .forms import RegisterForm

# Create your views here.
class LoginView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = LoginSerializer
  
def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
    
    # return(redirect(""))
  else:
    form = RegisterForm()
      
  return render(response, "signup.html", {"form":form})