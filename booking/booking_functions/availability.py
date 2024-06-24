from datetime import date
from booking.models import Booking
from rooms.models import Room, RoomCategory

def check_availability(room, check_in, check_out):
    """
    Check if the room is available for the given check-in and check-out dates
    """
    available_list = []
    bookings = Booking.objects.filter(room=room)
    for booking in bookings:
        # If the new check in date is after the check out date of the booking 
        # or the check out date is before the new check in date of the booking,
        # the room is available
        if booking.check_in > check_out or booking.check_out < check_in:
            available_list.append(True)
        else:
            available_list.append(False)
    return all(available_list)