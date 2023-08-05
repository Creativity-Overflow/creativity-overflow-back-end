from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    credits=models.DecimalField(default=10000.00,decimal_places=2,max_digits=18)
    # add additional fields in here

    def __str__(self):
        return self.username

class Artist(CustomUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

