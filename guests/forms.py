from django import forms
from allauth.account.forms import SignupForm
from .models import Profile
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    """ Custom Signup form """
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=250)
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    postal_code = forms.CharField(max_length=10)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
        )

    def __init__(self, *args, **kwargs):
        """ Initialize the form """
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                _('Username already exists. \
                    Please choose a different username.'))
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                _('Email address already exists. \
                    Please use a different email address.'))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(
                _('Phone number already exists in our records. \
                    Please use a different phone number.'))
        return phone_number

    def save(self, request):
        """ Save the user and profile"""
        user = super(CustomSignupForm, self).save(request)
        Profile.objects.create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            city=self.cleaned_data['city'],
            country=self.cleaned_data['country'],
            postal_code=self.cleaned_data['postal_code'],
            date_of_birth=self.cleaned_data['date_of_birth']
        )
        return user


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
