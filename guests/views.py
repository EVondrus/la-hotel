from django.views.generic import (
    TemplateView,
    UpdateView,
    DeleteView
)
from allauth.account.views import SignupView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import logout

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Profile
from .forms import ProfileForm
from .forms import CustomSignupForm


# Create your views here.
class CustomSignup(SignupView):
    """ Custom Signup view that handles user registration. """
    template_name = 'allauth/account/signup.html'
    form_class = CustomSignupForm
    success_url = reverse_lazy('account_login')

    def form_valid(self, form):
        """
        Handle successful form submission.

        Args:
            form (CustomSignupForm): The valid form instance.

        Returns:
            HttpResponse: The response after form is validated.
        """
        messages.success(
            self.request, 'Your account has been created.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form submission.

        Args:
            form (CustomSignupForm): The invalid form instance.

        Returns:
            HttpResponse: The response after form is invalid.
        """
        messages.error(
            self.request,
            'There was an error with your submission. Please try again.'
        )
        return super().form_invalid(form)


class Profiles(TemplateView):
    """
    Displays guest profile information
    """
    template_name = 'guests/profiles.html'

    def get_context_data(self, **kwargs):
        """
        Get the profile information.

        Args:
            **kwargs: Additional context data.

        Returns:
            dict: The context data including profile and form.
        """
        user_id = self.kwargs.get('pk')
        profile = get_object_or_404(Profile, user=user_id)
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile)
        }

        return context


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit user profile information """
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        """
        Handle successful form submission.

        Args:
            form (ProfileForm): The valid form instance.

        Returns:
            HttpResponse: The response after form is validated.
        """
        self.success_url = f'/profiles/profile/{self.kwargs["pk"]}/'
        messages.success(
            self.request, 'Your profile was successfully updated.'
        )
        return super().form_valid(form)

    def get_object(self):
        """
        Retrieve the Profile object based on the user
        primary key (pk) from the URL.

        Returns:
            Profile: The Profile object associated
            with the given user primary key.
        
        Raises:
            Profile.DoesNotExist: If no Profile is found
            for the given user primary key.
    """
        return Profile.objects.get(user__pk=self.kwargs["pk"])

    def test_func(self):
        """
        Test if the user is authorized to edit the profile.

        Returns:
            bool: True if the user is authorized, otherwise False.
        """
        return self.request.user == self.get_object().user


class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes the user's profile and related bookings
    and logs them out of the system.
    """
    model = Profile
    template_name = 'allauth/account/delete_profile.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        """
        Ensure user can only delete their own profile.

        Returns:
            bool: True if the user is authorized, otherwise False.
        """
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        """
        Handle successful deletion.

        Args:
            form (ModelForm): The form instance.

        Returns:
            HttpResponseRedirect: The response redirecting to home.
        """
        messages.success(self.request, 'Your account has been permanently \
        deleted, including all related bookings. Welcome back anytime!')

        self.request.user.delete()

        logout(self.request)

        return HttpResponseRedirect(reverse('home'))
