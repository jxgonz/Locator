from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service, Photo
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Avg


# Create your views here.

def ServiceCreateView(request):
  if request.method == 'POST':
    form = ServiceForm(request.POST, request.FILES) 
    images = request.FILES.getlist('images')
    if form.is_valid():
      service = form.save(commit=False)
      service.freelancer = request.user
      service.save()
      for image in images:
        photo = Photo.objects.create(service=service, service_img=image)
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

def ServicePageView(request, service_id):
  service = Service.objects.get(ServiceID=service_id)
  reviews = Review.objects.filter(service=service)
  photos = Photo.objects.filter(service=service)
  average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
  average_rating_rounded = round(average_rating, 2)
  if request.method == "POST":
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.client = request.user
      review.service = service
      review.rating = form.cleaned_data['rating']
      review.comment = form.cleaned_data['comment']
      review.save()
      return redirect('home')
  else:
    form = ReviewForm()
  
  return render(request, 'service_page.html', {'form' : form, 'service' : service, 'reviews' : reviews, 'photos':photos,'average_rating': average_rating_rounded})

@login_required
def ManageServicesView(request):
    services = Service.objects.filter(freelancer=request.user)
    return render(request, 'manage_services.html', {'services': services})
  
  
  