from django.urls import path
from .views import register

urlpatterns = [
    # path('', LoginView.as_view()),
    path('register/', register, name="register"),
]