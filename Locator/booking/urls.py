from django.urls import path
from .views import bookAppointment

app_name = 'appointments'

urlpatterns = [
    path('book/<str:service_id>/', bookAppointment, name="book")
]