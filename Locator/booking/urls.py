from django.urls import path, include
from .views import bookAppointment

app_name = 'appointments'

urlpatterns = [
    path('book/<int:service_id>/', bookAppointment, name="book")
]