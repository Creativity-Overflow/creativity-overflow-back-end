from django.urls import path
from .views import ArtList, ArtDetail

urlpatterns = [
    path("", ArtList.as_view(), name="art_list"),
    path("<int:pk>/", ArtDetail.as_view(), name="art_detail"),
]
