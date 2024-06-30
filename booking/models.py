from django.db import models
from djmoney.models.fields import MoneyField
from datetime import date
from rooms.models import Room
from django.contrib.auth.models import User

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

