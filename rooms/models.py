from django.db import models
from djmoney.models.fields import MoneyField

class RoomCategory(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    """
    Model representing a room in the hotel.
    """
    ROOM_CATEGORIES =(
        ('STA', 'Standard'),
        ('DEL', 'Deluxe'),
        ('SUI', 'Suite')
        )

    BED_SIZE = (
        ('DUB', 'Doubble'),
        ('QUE', 'Queen'),
        ('KIN', 'King')
        )

    room_number = models.IntegerField(unique=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.SET_NULL, null=True)
    beds = models.CharField(choices=BED_SIZE)
    max_guests = models.IntegerField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    description = models.TextField(max_length=2000, help_text="Enter a brief description of the room", blank=True, null=True)
    image = models.ImageField(upload_to='room_images', default='room_images/default-room.webp')

    def __str__(self):
        return f"{self.room_number}  {self.category} || Bed: {self.beds} - Guests: {self.max_guests} || {self.price}"