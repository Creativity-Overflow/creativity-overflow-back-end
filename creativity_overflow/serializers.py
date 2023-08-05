from rest_framework import serializers
from .models import Art , Inventory , Sold


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = ['current_price','highest_bidder','bidders']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields="__all__"

class Artist_art(serializers.ModelSerializer):
    class Meta:
        model=Art
        fields= ['name','description','category',]

class SoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sold
        fields = "__all__"
class Artist_inventory(serializers.ModelSerializer):
    pass        