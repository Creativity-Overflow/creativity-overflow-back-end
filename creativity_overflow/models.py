from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from django.db.models import JSONField

class Art(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
    )
    CATEGORY_CHOICES = (
        ('physical_art', 'Physical Art'),
        ('digital_art', 'Digital Art'),
        ('photography', 'Photography'),
    )

    name = models.CharField(max_length=256)
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_artworks")
    bidders = JSONField(default=dict,blank=True)
    highest_bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bidded_on_artworks',null=True,blank=True)
    current_price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES ,default='physical_art' )
    image = models.CharField(max_length=1500 ,null=True , blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    # def save(self, *args, **kwargs):
    #     # Check if image field is updated
    #     if self._state.adding and self.image:
    #         container_client = blob_service_client.get_container_client('media')
    #         blob_client = container_client.get_blob_client(f'images/{self.image.name}')

    #         # Upload the image to Azure Blob Storage
    #         with self.image.open('rb') as image_file:
    #             blob_client.upload_blob(image_file)

    #     super(Art, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('art-list', args=[str(self.id)])


class Inventory(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(default="", null=True, blank=True)
    category = models.CharField(max_length=30)
    image = models.CharField(max_length=1500 ,null=True , blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
