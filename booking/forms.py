from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Booking
from rooms.models import RoomCategory, Room


class BookingForm(forms.ModelForm):
    """
    Form for booking a room.

    Fields:
        check_in (DateField): Date picker for selecting check-in date.
        check_out (DateField): Date picker for selecting check-out date.

        room_category (ModelChoiceField):
        Dropdown list of available room categories.

        no_of_guests (IntegerField):
        Input field for specifying number of guests.

    Meta:
        model (Booking): The model class to be used for this form.
        fields (list): List of fields to include in the form.
        labels (dict): Custom labels for form fields.

    Methods:
        clean(): Custom form validation method to validate dates,
        number of guests, and calculate total price based on selected
        dates and room category.
    """
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'form-control'}),
        required=True
    )
    check_out = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date', 'class': 'form-control'}),
        required=True
    )
    room_category = forms.ModelChoiceField(
        queryset=RoomCategory.objects.all(), required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    no_of_guests = forms.IntegerField(
        min_value=1, required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = [
            'check_in', 'check_out',
            'room_category', 'no_of_guests']
        labels = {
            'check_in': 'Check in',
            'check_out': 'Check out',
            'room_category': 'Room',
            'no_of_guests': 'Number of Guests',
        }

    def clean(self):
        """Custom booking form validation."""
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        no_of_guests = cleaned_data.get('no_of_guests')
        room_category = cleaned_data.get('room_category')

        # Validate check in and check out dates
        if check_in and check_out:
            if check_in < timezone.now().date():
                raise ValidationError('Check in date cannot be in the past')
            if check_out < check_in:
                raise ValidationError(
                    'Check out date cannot be before check in date')

        # Validate number of guests
        if no_of_guests < 1:
            raise ValidationError('Number of guests must be greater than 0')

        if no_of_guests > cleaned_data['room_category'].capacity:
            raise ValidationError('Number of guests exceeds maximum allowed')

        # Calculate total price if check-in, check-out,
        # and room category are valid
        # price is stored in the RoomCategory model
        if check_in and check_out and room_category:
            total_nights = (check_out - check_in).days
            price_per_night = room_category.price.amount
            total_price = price_per_night * total_nights
            cleaned_data['total_price'] = total_price

        return cleaned_data
