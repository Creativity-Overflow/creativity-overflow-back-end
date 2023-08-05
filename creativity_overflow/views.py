from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
)
from .models import Art, Sold, Inventory
from .permissions import IsOwnerOrReadOnly 
from rest_framework.permissions import IsAuthenticated
from .serializers import ArtSerializer, CustomerSerializer, Artist_art, InventorySerializer , SoldSerializer
from accounts.models import CustomUser, Artist
from django.urls import reverse

# all art work
class ArtList(ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

# specific paint
class ArtDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Art.objects.all()
    serializer_class = CustomerSerializer

# all artist art
class ArtistArtList(ListCreateAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        return Art.objects.filter(artist=self.request.user)

# specific artist art
class ArtistArtDetail(RetrieveUpdateAPIView):
    serializer_class = Artist_art

    def get_queryset(self):
        return Art.objects.filter(artist=self.request.user)

# all sold artworks
class SoldArt(ListCreateAPIView):
    queryset = Sold.objects.all()
    serializer_class = SoldSerializer

# all artworks in inventory regarding specific user
class Inventory_list(ListCreateAPIView):
    queryset=Inventory.objects.all()
    serializer_class = InventorySerializer
    # def get_queryset(self):
    #     return Inventory.objects.all()

# updating specific artwork in inventory
class Inventory_update(RetrieveUpdateDestroyAPIView):
    queryset=Inventory.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = InventorySerializer

    # def get_queryset(self):
    #     return Inventory.objects.filter(artist=self.request.user)

# all artworks that specific customer bidded on
class Customer_bidds(ListAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Art.objects.filter(bidders__has_key=str(user_id))

# all won bids regarding specific customer 
class Winned_bidds(ListAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        return Sold.objects.filter(highest_bidder=self.request.user.id)

# delete from art model
class Delete_art(RetrieveDestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

    def get_absolute_url(self):
        return reverse('home')

# artist sell        
class Sold_artist_art(ListAPIView):
    serializer_class = SoldSerializer

    def get_queryset(self):
        return Sold.objects.filter(artist=self.request.user.id)
    
