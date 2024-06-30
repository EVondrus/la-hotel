from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Hotel(models.Model):
    """
    Define the hotel information
    """
    name = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    adress = models.CharField(
        max_length=100, blank=False, null=False)
    zip_code = models.CharField(
        max_length=20, blank=False, null=False)
    city = models.CharField(
        max_length=100, blank=False, null=False)
    email = models.EmailField(
        max_length=100, unique=True, blank=False, null=False)
    phone = models.CharField(
        max_length=20, unique=True, blank=False, null=False)
    image = ResizedImageField(
        size=[550, None], quality=75, upload_to="hotel",
        force_format="WEBP", blank=False, null=False
    )
    image_alt = models.CharField(
        max_length=100, help_text="Enter a breif description of the image",
        default="placeholder default hotel image",
        blank=False, null=False
    )
    description = models.TextField(
        help_text="Enter a description of the hotel", blank=False, null=False)
    avaliable_rooms = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Hotel name: {self.name}'
        
