from django.urls import path

from .views import SignUpView , signup

urlpatterns = [
    path("signup/", signup , name="signup"),
]
