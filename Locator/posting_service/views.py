from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service


# Create your views here.

def ServiceCreateView(request):
  if request.method == 'POST':
    print(request.POST)
    form = ServiceForm(request.POST) 
    if form.is_valid():
      print("form is valid")
      form.save()
      return redirect('home')
    else:
      print("form is invalid")
  else:
    form = ServiceForm
  
  return render(request, 'service.html', {'form' : form})