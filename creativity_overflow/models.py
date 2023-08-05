from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser , Artist
from django.db.models import JSONField

class Art(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="created_artworks")
    bidders = JSONField(default=dict)
    highest_bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bidded_on_artworks',blank=True)
    current_price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    category = models.CharField(max_length=30)
    image = models.ImageField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('art_detail', args=[str(self.id)])

class Sold(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="sold_artworks")
    bidders = JSONField(default=dict)
    highest_bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bidded_on_sold_artworks')
    current_price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    category = models.CharField(max_length=30)
    image = models.ImageField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.TextField(default="", null=True, blank=True)
    category = models.CharField(max_length=30)
    image = models.ImageField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name