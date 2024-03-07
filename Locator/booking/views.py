from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from posting_service.models import Service
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from .models import Appointment


# Create your views here.
@login_required
def bookAppointment(request, service_id):
  service = Service.objects.get(ServiceID=service_id)
  if request.method == 'POST':
    form = AppointmentForm(request.POST)
    if form.is_valid():
      appointment = form.save(commit=False)
      appointment.client = request.user
      appointment.service = service
      appointment.status = 'PENDING'
      appointment.save()
      return redirect('/appointments')
  else:
    form = AppointmentForm()
  return render(request, 'appointment.html', {'form': form, 'service': service})

def EditAppointmentView(request, appointment_id):
  appointment = Appointment.objects.get(AppointmentID=appointment_id)
  if request.method == "POST":
    form = AppointmentForm(request.POST, instance=appointment)
    if form.is_valid():
      form.save()
      return redirect('/appointments')
  else:
    form = AppointmentForm(instance=appointment)
    
  return render(request, 'edit_appointment.html', {'form' : form})

def CancelAppointmentView(request, appointment_id):
  appointment = Appointment.objects.get(AppointmentID=appointment_id)
  appointment.delete()
  return redirect('/appointments')

@login_required
def ManageAppointmentView(request):
  appointments = Appointment.objects.filter(client=request.user).order_by('date_time')
  return render(request, 'manage_appointments.html', {'appointments': appointments})
  