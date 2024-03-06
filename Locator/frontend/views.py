from django.shortcuts import render
from posting_service.models import Service

# Create your views here.
def ViewServices(request):
  services = Service.objects.all()
  return render(request, 'explore.html', {'services': services})

def home(response):
  return render(response, "test.html")