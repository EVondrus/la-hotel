from django.contrib import admin
from .models import Booking
from django.contrib.auth.models import User
from rooms.models import Room, RoomCategory

# Register your models here.
# Inline class for the rooms field in the BookingAdmin


class RoomInline(admin.TabularInline):
    model = Booking.rooms.through
    extra = 1
    fields = ['room']


class BookingAdmin(admin.ModelAdmin): 
    list_display = (
        'booking_id',
        'user',
        'check_in',
        'check_out',
        'total_price'
    )
    list_filter = (
        'check_in',
        'check_out',
        'user__email'
    )
    inlines = [RoomInline]
    date_hierarchy = 'check_in'
    ordering = ('-check_in',)
    search_fields = (
        'user__email',
        'user__last_name',
        'check_in'
    )


admin.site.register(Booking, BookingAdmin)