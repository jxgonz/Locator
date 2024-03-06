from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service


# Create your views here.

def ServiceCreateView(request):
  if request.method == 'POST':
    print(request.POST)
    form = ServiceForm(request.POST, request.FILES) 
    if form.is_valid():
      service = form.save(commit=False)
      service.freelancer = request.user
      service.save()
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

@login_required
def ManageServicesView(request):
    services = Service.objects.filter(freelancer=request.user)
    return render(request, 'manage_services.html', {'services': services})
  