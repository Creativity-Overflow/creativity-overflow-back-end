from django.urls import path

from .views import signup_artist , signup

urlpatterns = [
    path("signup/", signup , name="signup"),
    path("artist_signup/", signup_artist , name="artist_signup"),
]
