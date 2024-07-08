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
from datetime import timedelta
import datetime

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
        else:
            booking = form.save(commit=False)
            booking.user = self.request.user
            first_available_room = available_rooms.first()
            booking.save()
            booking.rooms.add(first_available_room)

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


# class BookingSuccess(TemplateView):
#     template_name = 'booking/booking_success.html'

#     def get(self, request, *args, **kwargs):
#         booking_id = request.session.get('booking_id')
#         if booking_id:
#             # booking_id is cleared from the session after retrieving it
#             del request.session['booking_id']
#             return super().get(request, *args, **kwargs)
#         else:
#             messages.error(request, 'Booking details not found. Please try again or contact support.')
#             return redirect('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         booking_id = self.request.session.get('booking_id', None)
#         if booking_id:
#             context['booking'] = get_object_or_404(Booking, id=booking_id)
#         return context

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

        # Calculate the deadline for editing (15:00 on the day before check-in)
        check_in_deadline = check_in.replace(
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
        else:
            booking = form.save(commit=False)
            old_room = booking.rooms.first()  # Get the previously booked room
            first_available_room = available_rooms.first()
            booking.rooms.clear()  # Clear current rooms
            booking.rooms.add(first_available_room)  # Add new available room
            booking.save()  # Save the booking with the new room

            # logic to make the old room available for others
            if old_room:
                old_room.booking_set.remove(booking)  # Remove booking from the old room

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

        # Calculate the deadline for deletion (15:00 on the day before check-in)
        check_in_deadline = booking.check_in.replace(
            hour=15, minute=0, second=0) - timedelta(days=1)

        # Check if the current time is beyond the deletion deadline
        if timezone.now() > check_in_deadline:
            messages.error(
                self.request,
                'Bookings cannot be deleted within 24 hours before check-in. \
                    Please contact us for assistance.'
            )
            return HttpResponseRedirect(self.success_url)

        # Proceed with deletion if within the allowed time
        return super().delete(request, *args, **kwargs)


