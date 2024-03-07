from django.urls import path
from .views import ServiceCreateView, UpdateServiceView, DeleteServiceView, ManageServicesView, ServicePageView, ServiceAppointmentsView, ChangeStatus, ServiceCategoryView

app_name='posting_service'

urlpatterns = [
    path('create-service/', ServiceCreateView, name="create-service"),
    path('services/', ManageServicesView, name="manage_services"),
    path('service/<str:service_id>/edit/', UpdateServiceView, name="edit_service"),
    path('service/<str:service_id>/delete/', DeleteServiceView, name='delete_service'),
    path('serviceview/<str:service_id>/', ServicePageView, name="service_page"),
    path('serviceapp/<str:service_id>/', ServiceAppointmentsView, name="service_appointments"),
    path('appointmentstatus/<str:appointment_id>/', ChangeStatus, name="change_status"),
    path('category/<str:category>/', ServiceCategoryView, name="category"),
]