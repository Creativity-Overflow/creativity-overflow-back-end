from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
)
from rest_framework.views import APIView
from .models import Art, Inventory
from .permissions import IsOwnerOrReadOnly , IsArtistOrReadOnly , IsOwnerArtist,IsAdminUsers
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from .serializers import ArtSerializer, Artist_art, InventorySerializer , PriceSerializer , ArtCreateSerializer
from accounts.models import CustomUser
from django.urls import reverse
from django.http import JsonResponse

# all art work
class ArtList(ListCreateAPIView):
    queryset = Art.objects.filter(status = 'available')
    serializer_class = ArtSerializer
    permission_classes = [IsArtistOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArtCreateSerializer
        else:
            return ArtSerializer

# create Art
# class CreateArt(CreateAPIView):
#     queryset = Art.objects.all()
#     serializer_class = ArtSerializer
#     permission_classes=[IsArtistOrReadOnly]

# specific paint
class ArtDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    def perform_update(self, serializer):
        serializer.save(highest_bidder=self.request.user,bidders={self.request.user.id:"1"})
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return PriceSerializer
        else:
            return ArtSerializer

# all artist art
class ArtistArtList(ListCreateAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        print(self.request.user)
        return Art.objects.filter(artist=self.request.user)
    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArtCreateSerializer
        else:
            return ArtSerializer

# specific artist art
class ArtistArtDetail(RetrieveUpdateAPIView):
    serializer_class = Artist_art

    def get_queryset(self):
        return Art.objects.filter(artist=self.request.user)

# all sold artworks
class SoldArt(ListAPIView):
    queryset = Art.objects.filter(status = 'sold')
    serializer_class = ArtSerializer

# all artworks in inventory regarding specific user
class Inventory_list(ListCreateAPIView):
    serializer_class = InventorySerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user_id = self.request.user.id
        return Inventory.objects.filter(artist_id = user_id)

# updating specific artwork in inventory
class Inventory_update(RetrieveUpdateDestroyAPIView):
    queryset=Inventory.objects.all()
    permission_classes = [IsOwnerArtist]
    serializer_class = InventorySerializer

    # def get_queryset(self):
    #     return Inventory.objects.filter(artist=self.request.user)

# all artworks that specific customer bidden on
class Customer_bidds(ListAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Art.objects.filter(bidders__has_key=str(user_id))

# all won bids regarding specific customer
class Winned_bidds(ListAPIView):
    serializer_class = ArtSerializer

    def get_queryset(self):
        return Art.objects.filter(highest_bidder=self.request.user.id , status = 'sold' )

# delete from art model
class Delete_art(RetrieveDestroyAPIView):
    queryset = Art.objects.all()

    serializer_class = ArtSerializer
    permission_class = [IsAdminUsers]
    def get_absolute_url(self):
        return reverse('art-list')

# artist sell
class Sold_artist_art(ListAPIView):
    serializer_class = ArtSerializer
    def get_queryset(self):

        return Art.objects.filter(artist=self.request.user.id, status = 'sold')
    

class physicalArts(ListAPIView):
    serializer_class = ArtSerializer
    queryset = Art.objects.filter(category = "physical_art")

class digitalArts(ListAPIView):
    serializer_class = ArtSerializer
    queryset = Art.objects.filter(category = "digital_art")

class photography(ListAPIView):
    serializer_class = ArtSerializer
    queryset = Art.objects.filter(category = "photography")

class MoveRowView(APIView):
    def post(self, request, source_id):
        try:
            art_row = Art.objects.get(id=source_id)
            if art_row.current_price > 0 :
                art_row.status = "sold"
                art_row.save()
            else:
                inventory_instance = Inventory.objects.create(name=art_row.name,artist=art_row.artist,description=art_row.description,category=art_row.category,image=art_row.image)
                inventory_instance.save()
                art_row.delete()
            return JsonResponse({'status': 'success'})
        except Art.DoesNotExist:
            return JsonResponse({'error': 'Source row not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
