from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking
from rooms.models import RoomCategory, Room


class BookingForm(forms.ModelForm):
    """Form for booking a room."""
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
        widget=forms.Select(attrs={'class': 'form-control'}))
    no_of_guests = forms.IntegerField(
        min_value=1, required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    total_price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = Booking
        fields = [
            'check_in', 'check_out',
            'room_category', 'no_of_guests', 'total_price']
        labels = {
            'check_in': 'Check in',
            'check_out': 'Check out',
            'room_category': 'Room',
            'no_of_guests': 'Number of Guests',
            'total_price': 'Total Price'
        }

    def clean(self):
        """Custom booking form validation."""
        data = super().clean()
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        no_of_guests = data.get('no_of_guests')
        # Validate check in and check out dates
        if check_in and check_out:
            if check_in < timezone.now().date():
                raise ValidationError('Check in date cannot be in the past')
            if check_out < check_in:
                raise ValidationError(
                    'Check out date cannot be before check in date')

        if no_of_guests < 1:
            raise ValidationError('Number of guests must be greater than 0')
