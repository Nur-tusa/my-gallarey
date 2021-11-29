from django.contrib import admin
from .models import  gallery_category, photos, Location

# Register your models here.

admin.site.register(gallery_category)
admin.site.register(photos)
admin.site.register(Location)