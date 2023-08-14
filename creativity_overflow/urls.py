# creativity_overflow/urls.py

from django.urls import path

from .views import (
    ArtList,
    ArtDetail,
    ArtistArtList,
    ArtistArtDetail,
    SoldArt,
    Inventory_list,
    Inventory_update,
    Customer_bidds,
    Winned_bidds,
    Delete_art,
    Sold_artist_art,
    photography,
    digitalArts,
    physicalArts,
    MoveRowView,
)

urlpatterns = [
    path("", ArtList.as_view(), name="art-list"),
    path("<int:pk>/", ArtDetail.as_view(), name="art-detail"),
    path("artist-art/", ArtistArtList.as_view(), name="artist-art-list"),
    path("artist-art/<int:pk>/", ArtistArtDetail.as_view(), name="artist-art-detail"),
    path("sold-art/", SoldArt.as_view(), name="sold-art"),
    path("inventory/", Inventory_list.as_view(), name="inventory-list"),
    path("inventory/<int:pk>/", Inventory_update.as_view(), name="inventory-update"), #ma bdo front_slash belakhr
    path("customer-bidds/", Customer_bidds.as_view(), name="customer-bidds"),
    path("won-bids/", Winned_bidds.as_view(), name="won-bids"),
    path("delete-art/<int:pk>/", Delete_art.as_view(), name="delete-art"),
    path("sold-artist-art/", Sold_artist_art.as_view(), name="sold-artist-art"),
    path("physical/",physicalArts.as_view(),name="physical"),
    path("digital/",digitalArts.as_view(),name="digital"),
    path("photos/",photography.as_view(),name="photos"),
    path("move_row/<int:source_id>/",MoveRowView.as_view(),name="auto_move"),
]
