from django.shortcuts import render
from django.shortcuts import render, redirect
from posting_service.models import Service
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def postReview(request, service_id):
  service = Service.objects.get(ServiceID=service_id)
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.client = request.user
      review.service = service
      review.save()
      return redirect('home')
  else:
    form = ReviewForm()
  return render(request, 'review.html', {'form' : form, 'service' : service})