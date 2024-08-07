from django.db import models
from djmoney.models.fields import MoneyField
from django_resized import ResizedImageField


# Create your models here.
class RoomCategory(models.Model):
    """
    Model representing a category of rooms in the hotel.

    Attributes:
        category (str): The category of the room (Standard, Deluxe, Suite).
        beds (str): The size of the beds in the room (Double, Queen, King).
        capacity (int): The maximum number of guests the room can accommodate.
        price (MoneyField): The price of the room.
        description (str): A description of the room.
        image (ResizedImageField): An image of the room,
        resized to 400x400 and saved in WEBP format.
        image_alt (str): An alternative text for the room image,
        used for accessibility and SEO.
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
        size=[400, 400],
        crop=['middle', 'center'],
        quality=75,
        upload_to="room-categories/",
        force_format="WEBP",
        blank=False,
        null=False,
        max_length=1000
    )
    image_alt = models.CharField(
        max_length=100, help_text="Enter a breif description of the image",
        default="Default room image",
        blank=False, null=False
    )

    def __str__(self):
        return f"{self.category} || Bed: {self.beds} - Guests: {self.capacity}\
        || Price: {self.price}"


class Room(models.Model):
    """
    Model representing a room in the hotel.

    Attributes:
        room_number (str): The unique identifier for the room.
        category (ForeignKey): The category the room belongs to.
        available (bool): Whether the room is available for booking.
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
