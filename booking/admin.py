from django.contrib import admin
from .models import Booking
from django.contrib.auth.models import User
from rooms.models import Room, RoomCategory

# Register your models here.
class RoomInline(admin.TabularInline):
    model = Booking.rooms.through
    extra = 1
    fields = ['room']

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'total_price', 'created', 'updated')
    list_filter = ('check_in', 'check_out', 'created', 'updated')
    search_fields = ('booking_Id', 'user__username', 'user__email') 
    inlines = [RoomInline]
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'check_in'
    autocomplete_fields = ['user']
    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'check_in', 'check_out', 'no_of_guests')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Booking, BookingAdmin)

