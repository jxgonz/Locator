from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service


# Create your views here.

def ServiceCreateView(request):
  if request.method == 'POST':
    print(request.POST)
    form = ServiceForm(request.POST, request.FILES) 
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = ServiceForm()
  
  return render(request, 'service.html', {'form' : form})

def UpdateServiceView(request, service_id):
  service = Service.objects.get(ServiceID=service_id)
  if request.method == "POST":
    form = ServiceForm(request.POST, request.FILES, instance=service)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = ServiceForm(instance=service)
    
  return render(request, 'edit_service.html', {'form' : form})

def DeleteServiceView(request, service_id):
  service = Service.objects.get(ServiceID=service_id)
  service.delete()
  return redirect('home')