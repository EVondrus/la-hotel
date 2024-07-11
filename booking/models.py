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
    Represents a booking made by a user for one or more rooms.

    Methods:
        __str__(): Returns a string representation of the booking.
        calculate_total_price(check_in, check_out, room_category): 
        Calculates the total price based on check-in, check-out dates,
        and room category.

        get_available_rooms(room_category, check_in, check_out): 
        Retrieves rooms available for booking within a given category
        and timeframe.
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
        return f"Booking from {self.check_in} to {self.check_out} \
            - Total: {self.total_price}"

    class Meta:
        ordering = ['-check_in']

    @staticmethod
    def calculate_total_price(check_in, check_out, room_category):
        """
        Calculates the total price of a booking based on the check-in,
        check-out dates, and room category price.

        Returns:
            float: Total price of the booking.
        """
        if check_out <= check_in:
            raise ValueError("Check-out date must be after check-in date")
        total_nights = (check_out - check_in).days
        price_per_night = room_category.price.amount
        return price_per_night * total_nights

    @staticmethod
    def get_available_rooms(room_category, check_in, check_out):
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

        def save(self, *args, **kwargs):

            if self.check_out <= self.check_in:
                raise ValueError("Check-out date must be after check-in date")

            # All rooms in the same category have the same price
            room_category = self.rooms.first().category

            # Calculate total price using the static method
            self.total_price = self.calculate_total_price(
                self.check_in, self.check_out, room_category
            )

            super().save(*args, **kwargs)

    @receiver(post_save, sender='booking.Booking')
    def update_room_availability_on_save(sender, instance, created, **kwargs):
        """Mark rooms as unavailable upon booking creation."""
        if created:
            for room in instance.rooms.all():
                room.avaliable = False
                room.save()
