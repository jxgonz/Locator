from django.urls import path, include
from .views import home, ViewServices

urlpatterns = [
    path('', home, name="home"),
    path('explore/', ViewServices, name="explore")
]