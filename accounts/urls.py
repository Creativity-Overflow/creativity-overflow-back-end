from django.urls import path

from .views import signup_artist , signup , update_credits

urlpatterns = [
    path("signup/", signup , name="signup"),
    path("artist_signup/", signup_artist , name="artist_signup"),
    path("update_credits/<int:pk>/", update_credits , name="credits"),
    
]
