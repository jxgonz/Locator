from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from posting_service.models import Service
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def bookAppointment(request, service_id):
  service = get_object_or_404(Service, id=service_id)
  if request.method == 'POST':
    form = AppointmentForm(request.POST)
    if form.is_valid():
      appointment = form.save()
      appointment.client = request.user
      appointment.service = service
      appointment.status = 'PENDING'
      appointment.save()
      return redirect('home')
  else:
    form = AppointmentForm()
  return render(request, 'appointment.html', {'form': form, 'service': service})