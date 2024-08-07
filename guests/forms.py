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
        """
        Validate that the username is unique.

        Returns:
            str: The cleaned username.

        Raises:
            ValidationError: If the username already exists.
        """
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                _('Username already exists. \
                    Please choose a different username.'))
        return username

    def clean_email(self):
        """
        Validate that the email is unique.

        Returns:
            str: The cleaned email.

        Raises:
            ValidationError: If the email already exists.
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                _('Email address already exists. \
                    Please use a different email address.'))
        return email

    def clean_phone_number(self):
        """
        Validate that the phone number is unique.

        Returns:
            str: The cleaned phone number.

        Raises:
            ValidationError: If the phone number already exists in the Profile model.
        """
        phone_number = self.cleaned_data['phone_number']
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(
                _('Phone number already exists in our records. \
                    Please use a different phone number.'))
        return phone_number

    def clean(self):
        """
        Check that all required fields are filled out.

        Raises:
            ValidationError: If any required field is missing.
        """
        cleaned_data = super().clean()
        
        # List of required fields
        required_fields = [
            'first_name', 'last_name', 'phone_number', 
            'address', 'city', 'country', 'postal_code', 
            'date_of_birth'
        ]
        
        missing_fields = []
        for field in required_fields:
            if field not in cleaned_data or not cleaned_data[field]:
                missing_fields.append(field.capitalize())

        if missing_fields:
            error_message = _("The following fields are required: ") + ", ".join(missing_fields)
            raise ValidationError(error_message)

        return cleaned_data

    def save(self, request):
        """
        Save the user and create a related profile.

        Args:
            request: The HTTP request object.

        Returns:
            User: The created user instance.
        """
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
    """ Form for creating and updating user profiles."""
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
