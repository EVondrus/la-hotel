from django.views.generic import(
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from django.contrib import messages

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import timedelta, datetime

from .models import Booking
from rooms.models import Room, RoomCategory
from .forms import BookingForm


# Create your views here.
class AddBooking(LoginRequiredMixin, CreateView):
    """ View for adding a booking """
    template_name = 'booking/add_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('booking:booking_success')

    def form_valid(self, form):
        """ Process the form data """
        form.instance.user = self.request.user
        room_category = form.cleaned_data['room_category']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']

        # Check if the selected room is available for the selected dates
        available_rooms = Booking.get_available_rooms(
            room_category,
            check_in, check_out
        )
        if not available_rooms:
            messages.error(
                self.request, 'This room is not available for the selected \
                    dates. Please select another room or date.'
            )
            return self.form_invalid(form)
        
        # Save the booking
        booking = form.save()
        booking.rooms.add(available_rooms.first())  # adding the first available room
        self.request.session['booking_id'] = booking.id
        messages.success(
            self.request, 'Your reservation has been confirmed. \
                Thank you for booking with us!'
        )
            
        return super().form_valid(form)

    def form_invalid(self, form):
        """Handle invalid form submissions"""
        messages.error(
            self.request, 'Your booking could not be processed. \
                Please try again or contact us for support.'
        )
        return super().form_invalid(form)


class BookingSuccess(TemplateView):
    """ View for displaying a success message after booking """
    template_name = 'booking/booking_success.html'


class BookingList(LoginRequiredMixin, ListView):
    """ View for listing all bookings made by the user. """
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'
    model = Booking


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View for editing a booking """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/edit_booking.html'
    success_url = reverse_lazy('booking:booking_list')

    def form_valid(self, form):
        """ Process the form data """
        room_category = form.cleaned_data['room_category']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']

        # check_in is a datetime.date object from form.cleaned_data
        check_in_datetime = timezone.make_aware(datetime.combine(check_in, datetime.min.time()))
        # Calculate the deadline for editing (15:00 on the day before check-in)
        check_in_deadline = check_in_datetime.replace(
            hour=15, minute=0, second=0) - timedelta(days=1)

        # Check if the current time is beyond the edit deadline
        if timezone.now() > check_in_deadline:
            messages.error(
                self.request,
                'Bookings can only be edited up to 24 hours before check-in. \
                    Please contact us for assistance.'
            )
            return self.form_invalid(form)
        
        # Proceed with room booking logic if within the allowed edit time
        available_rooms = Booking.get_available_rooms(
            room_category, check_in, check_out
        )
        if not available_rooms:
            messages.error(
                self.request, 'This room is not available for the selected \
                    dates. Please select another room or date.')
            return self.form_invalid(form)
        
        # Update booking details and room assignment
        booking = form.save(commit=False)
        old_room = booking.rooms.first() if booking.rooms.exists() else None  # Get the previously booked room, if any

        #adding the first available room
        first_available_room = available_rooms.first()
        booking.rooms.clear()  # Clear current rooms
        booking.rooms.add(first_available_room)  # Add new available room

        # Recalculate total price based on updated booking details
        total_nights = (check_out - check_in).days
        price_per_night = room_category.price.amount  # Adjust if necessary
        total_price = price_per_night * total_nights
        booking.total_price = total_price
        booking.save()  # Save the booking with the new room and total price

        # Make the old room available for others
        if old_room:
            old_room.avaliable = True
            old_room.save()

        messages.success(self.request, 'Your booking has been updated.')
        return super().form_valid(form)

    def test_func(self):
        """ Check if the user is the owner of the booking """
        return self.request.user == self.get_object().user

    def form_invalid(self, form):
        """ Handle invalid form submissions """
        messages.error(
            self.request, 'Your booking could not be updated. \
                Please try again or contact us for support.'
        )
        return super().form_invalid(form)


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ View for deleting a booking """
    model = Booking
    success_url = reverse_lazy('booking:booking_list')

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        """ Perform delete operation """
        booking = self.get_object()
        success_url = 'home'

        check_in_datetime = timezone.make_aware(datetime.combine(check_in, datetime.min.time()))
        # Calculate the deadline for editing (15:00 on the day before check-in)
        check_in_deadline = check_in_datetime.replace(
            hour=15, minute=0, second=0) - timedelta(days=1)

        # Check if the current time is beyond the edit deadline
        if timezone.now() > check_in_deadline:
            messages.error(
                self.request,
                'Bookings can only be edited up to 24 hours before check-in. \
                    Please contact us for assistance.'
            )
            return HttpResponseRedirect(self.success_url)

        # Proceed with deletion if within the allowed time
        return super().delete(request, *args, **kwargs)


