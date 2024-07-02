from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    """ Create a profile form """
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'city',
            'country',
            'postal_code',
            'date_of_birth'
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_number': 'Phone Number',
            'address': 'Address',
            'city': 'City',
            'country': 'Country',
            'postal_code': 'Postal Code',
            'date_of_birth': 'Date of Birth'
        }