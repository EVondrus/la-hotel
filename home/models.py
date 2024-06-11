from django.db import models

# Create your models here.

class Hotel(models.Model):
    """
    Define the hotel information
    """
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    avaliable_rooms = models.IntegerField()

    def __str__(self):
        return f'Hotel name: {self.name}'
        
