from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class RoomCategory(models.Model):
    """
    Model representing a category of rooms in the hotel.
    """
    ROOM_CATEGORIES =(
        ('STANDARD', 'Standard'),
        ('DELUXE', 'Deluxe'),
        ('SUITE', 'Suite')
        )

    BED_SIZE = (
        ('DOUBLE', 'Double'),
        ('QUEEN', 'Queen'),
        ('KING', 'King')
        )

    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)
    beds = models.CharField(max_length=10, choices=BED_SIZE)
    capacity = models.IntegerField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    description = models.TextField(max_length=2000, help_text="Enter a brief description of the room", blank=True, null=True)
    image = models.ImageField(upload_to='room_images', default='room_images/default-room.webp')

    def __str__(self):
        return f"{self.category} || Bed: {self.beds} - Guests: {self.capacity} || Price: {self.price}"

class Room(models.Model):
    """
    Model representing a room in the hotel.
    """
    ROOM_STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('MAINTENANCE', 'Under Maintenance'),
        ('BOOKED', 'Booked'),
        ('OCCUPIED', 'Occupied'),
    )

    room_number = models.CharField(max_length=10, unique=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=ROOM_STATUS_CHOICES, default='AVAILABLE')

    class Meta:
        unique_together = (('room_number', 'category'),)

    def __str__(self):
        return f"{self.room_number} - {self.category} - {self.status}"