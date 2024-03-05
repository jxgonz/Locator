from django.urls import path
from .views import ServiceCreateView, UpdateServiceView, DeleteServiceView

app_name='posting_service'

urlpatterns = [
    path('create-service/', ServiceCreateView, name="create-service"),
    path('service/<str:service_id>/edit/', UpdateServiceView, name="edit_service"),
    path('service/<str:service_id>/delete/', DeleteServiceView, name='delete_service'),
]