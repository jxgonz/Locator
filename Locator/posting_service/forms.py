from django import forms
from django.contrib.auth.models import User
from .models import Service


class ServiceForm(forms.ModelForm):
  class Meta:
    model = Service
    fields = ["id", "serviceName", "description", "price"]