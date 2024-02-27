from django.urls import path
from .views import ServiceCreateView

app_name='posting_service'

urlpatterns = [
    path('create-service/', ServiceCreateView, name="create-service"),
]