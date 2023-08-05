from django.contrib import admin
from .models import Art , Sold , Inventory

# Register your models here.
admin.site.register(Art)
admin.site.register(Sold)
admin.site.register(Inventory)
