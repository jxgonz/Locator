from django.urls import path
from .views import postReview

app_name = 'reviews'

urlpatterns = [
    path('review/<str:service_id>/', postReview, name="review")
]