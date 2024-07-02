from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    """ Guest profile model """
    user = models.ForeignKey(
        User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(
        max_length=15, blank=False, unique=True)
    address = models.TextField(max_length=250, blank=False)
    city = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


# Signal to create a profile when a new user is created
# Code taken from: https://www.youtube.com/watch?v=dGnRsNH81Ik&t=6s
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """ Create or update a user profile """
    if created:
        Profile.objects.create(user=instance)