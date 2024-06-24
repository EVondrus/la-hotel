from django.contrib import admin

# Register your models here.
from .models import Room, RoomCategory

admin.site.register(Room)
admin.site.register(RoomCategory)
