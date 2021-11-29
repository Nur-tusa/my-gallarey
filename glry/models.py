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

        
