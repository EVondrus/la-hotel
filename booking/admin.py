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

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user','check_in', 'check_out', 'total_price')
    list_filter = ('check_in', 'check_out', 'user__email')
    search_fields = ('booking_id', 'user__username', 'user__email') 
    inlines = [RoomInline]
    date_hierarchy = 'check_in'
    autocomplete_fields = ['user']
    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'check_in', 'check_out', 'no_of_guests', 'total_price')
        }),
    )
    ordering = ('-check_in',)

    def save_model(self, request, obj, form, change):
        """
        Overrides the default save_model method to set the total price of the booking
        before saving it to the database. This ensures that the total price is always
        up-to-date before the booking instance is saved.

        Args:
            request: The request object.
            obj: The booking instance being saved.
            form: The form instance.
            change: A boolean flag indicating whether the object is being changed or created.
        """
        nights = (obj.check_out - obj.check_in).days
        total_price = sum(room.category.price * nights for room in obj.rooms.all())
        obj.total_price = total_price
        super().save_model(request, obj, form, change)


