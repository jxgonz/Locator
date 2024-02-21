from django.urls import path, include
from .views import LoginView
from .views import register

urlpatterns = [
    # path('', LoginView.as_view()),
    path('register/', register, name="register"),
    path('', include("django.contrib.auth.urls")),
]