from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Art
from .permissions import IsOwnerOrReadOnly
from .serializers import ArtSerializer


class ArtList(ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer


class ArtDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
