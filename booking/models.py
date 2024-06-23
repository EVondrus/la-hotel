from django.db import models
from djmoney.models.fields import MoneyField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import date
from rooms.models import Room
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    """
    Define the booking information
    """
    booking_Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    check_in = models.DateField()
    check_out = models.DateField()
    no_of_guests = models.PositiveIntegerField()
    total_price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user} - {self.room} - {self.check_in} - {self.check_out} - {self.total_price}'


    class Meta:
        ordering = ['-check_in']


    def save(self, *args, **kwargs):
        """
        Overrides the default save method to calculate the total price of the booking based on
        the room category prices and the number of nights. The total price is calculated as 
        the sum of the price for each room category multiplied by the number of nights.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        nights = (self.check_out - self.check_in).days
        total_price = sum(room.category.price * nights for room in self.rooms.all())
        self.total_price = total_price
        super().save(*args, **kwargs)

@receiver(pre_save, sender=Booking)
def pre_save_booking(sender, instance, **kwargs):
    """
    Signal to calculate and set the total price of the booking before saving it.
    The total price is calculated based on the room category prices and the number
    of nights. This ensures that the total price is always up-to-date before the
    booking instance is saved.

    Args:
        sender: The model class that sent the signal.
        instance: The actual instance being saved.
        **kwargs: Arbitrary keyword arguments.
    """
    if instance.rooms.exists():
        nights = (instance.check_out - instance.check_in).days
        total_price = sum(room.category.price * nights for room in instance.rooms.all())
        instance.total_price = total_price


