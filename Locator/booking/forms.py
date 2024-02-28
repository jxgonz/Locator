from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = ['service', 'date_time', 'client']
    widgets = {
      'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }