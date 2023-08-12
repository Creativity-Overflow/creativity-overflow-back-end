from rest_framework import serializers
from .models import Art , Inventory


class ArtSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.username', read_only=True)
    highest_bidder_name = serializers.CharField(source='highest_bidder.username', read_only=True)

    class Meta:
        model = Art
        fields = [
            'id', 'name', 'artist', 'artist_name', 'bidders', 'highest_bidder',
            'highest_bidder_name', 'current_price', 'description', 'category',
            'image', 'status', 'start_date', 'end_date'
        ]

class ArtCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        exclude = ['artist','bidders','highest_bidder','status','current_price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ['current_price','highest_bidder']

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Art
        fields = ['current_price']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields="__all__"

class Artist_art(serializers.ModelSerializer):
    class Meta:
        model=Art
        fields= ['name','description','category',]
