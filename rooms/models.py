from django.db import models
from djmoney.models.fields import MoneyField
from django_resized import ResizedImageField



# Create your models here.
class RoomCategory(models.Model):
    """
    Model representing a category of rooms in the hotel.
    """
    ROOM_CATEGORIES = (
        ('STANDARD', 'Standard'),
        ('DELUXE', 'Deluxe'),
        ('SUITE', 'Suite')
        )

    BED_SIZE = (
        ('DOUBLE', 'Double'),
        ('QUEEN', 'Queen'),
        ('KING', 'King')
        )

    category = models.CharField(
        max_length=10, choices=ROOM_CATEGORIES, blank=False, null=False)
    beds = models.CharField(
        max_length=10, choices=BED_SIZE, blank=False, null=False)
    capacity = models.PositiveIntegerField(blank=False, null=False)
    price = MoneyField(
        max_digits=10, decimal_places=2, default_currency='EUR',
        blank=False, null=False)
    description = models.TextField(
        max_length=10000, help_text="Enter a description of the room",
        blank=True, null=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="room-categories/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(
        max_length=100, help_text="Enter a breif description of the image",
        default="placeholder default room image",
        blank=False, null=False
    )

    def __str__(self):
        return f"{self.category} || Bed: {self.beds} - Guests: {self.capacity}\
        || Price: {self.price}"


class Room(models.Model):
    """
    Model representing a room in the hotel.
    """
    room_number = models.CharField(
        max_length=10, unique=True, blank=False, null=False)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    avaliable = models.BooleanField(
        default=True, help_text="Check if the room is avaliable")

    class Meta:
        unique_together = (('room_number', 'category'),)

    def __str__(self):
        return f"{self.room_number} - {self.category} - {self.avaliable}"
