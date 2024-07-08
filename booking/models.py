from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from djmoney.models.fields import MoneyField
from datetime import date

from django.contrib.auth.models import User
from rooms.models import Room, RoomCategory

# Create your models here.


class Booking(models.Model):
    """
    Define the booking information
    """
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    check_in = models.DateField(blank=False, null=False)
    check_out = models.DateField(blank=False, null=False)
    no_of_guests = models.PositiveIntegerField(blank=False, null=False)
    total_price = MoneyField(
        max_digits=10, decimal_places=2, default_currency='EUR',
        blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.rooms} -\
            {self.check_in} - {self.check_out} - {self.total_price}'

    class Meta:
        ordering = ['-check_in']

    def save(self, *args, **kwargs):
        # Ensure check-out date is after check-in date
        if self.check_out <= self.check_in:
            raise ValueError("Check-out date must be after check-in date")

        # Calculate total nights
        total_nights = (self.check_out - self.check_in).days

        # All rooms in the same category have the same price
        room_category = self.rooms.first().category

        # Calculate total price
        # price is stored in the RoomCategory model
        price_per_night = room_category.price.amount 
        self.total_price = price_per_night * total_nights

        super(Booking, self).save(*args, **kwargs)


    @staticmethod
    def get_available_rooms(room_category, check_in, check_out):
        print(f"Checking availability for: Category={room_category}, Check-in={check_in}, Check-out={check_out}")
        available_rooms = []
        rooms_in_category = Room.objects.filter(
            category=room_category, avaliable=True
        )

        for room in rooms_in_category:
            overlapping_bookings = Booking.objects.filter(
                rooms=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exists()

            if not overlapping_bookings:
                available_rooms.append(room)

        return available_rooms


@receiver(post_save, sender=Booking)
def update_room_availability_on_save(sender, instance, created, **kwargs):
    """Mark rooms as unavailable upon booking creation."""
    if created:
        for room in instance.rooms.all():
            room.avaliable = False
            room.save()
