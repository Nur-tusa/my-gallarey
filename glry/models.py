from django.db import models

from cloudinary.models import CloudinaryField
# Create your models here.
class gallery_category(models.Model):
  
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_type(self):
        self.save()

    def delete_type(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
