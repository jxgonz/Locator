from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.  
def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      user = form.save()
      login(response, user)
      return(redirect("home"))
  else:
    form = RegisterForm()
      
  return render(response, "signup.html", {"form":form})