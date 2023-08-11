from rest_framework import serializers
from .models import Art , Inventory


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = "__all__"

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
