from django.db import models

# Create your models here.
class gallery_type(models.Model):
  
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_type(self):
        self.save()

    def delete_type(self):
        self.delete()


class addres(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = addres.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_address(cls, id, value):
        cls.objects.filter(id=id).update(picture=value)

    def save_address(self):
        self.save()

    def delete_address(self):
        self.delete()

