from django.urls import path
from .views import bookAppointment, EditAppointmentView, CancelAppointmentView, ManageAppointmentView

app_name = 'appointments'

urlpatterns = [
    path('book/<str:service_id>/', bookAppointment, name="book"),
    path('appointments', ManageAppointmentView, name="manage_appointments"),
    path('appointment/<str:appointment_id>/edit/', EditAppointmentView, name="edit_appointment"),
    path('appointment/<str:appointment_id>/cancel/', CancelAppointmentView, name="cancel_appointment"),
]