from django import forms
from allauth.account.forms import SignupForm
from .models import Profile
from django.contrib import messages


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

    def save(self, request):
        """ Save the user and profile"""
        print("Saving user")
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
